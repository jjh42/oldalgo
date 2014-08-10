"""Label strongly-connected components of a graph."""

class Vertex():
    def __init__(self, label):
        self.outgoing = []
        self.incoming = []
        self.label = label
        self.scc = None

class Graph():
    def __init__(self, file=None):
        self.G = {}
        self.load_graph(file)

    def load_graph(self,file):
        if file==None:
            file = open('SCC.txt', 'r')
        for line in file.readlines():
            u,v = [int(n) for n in line.split()]
            self.ensure_node_exists(v)
            self.ensure_node_exists(u)
            self.G[u].outgoing.append(self.G[v])
            self.G[v].incoming.append(self.G[u])

    def ensure_node_exists(self, u):
        """Add node to to graph dictionary if it doesn't already exist."""
        if not self.G.has_key(u):
            self.G[u] = Vertex(u)

    def scc(self):
        self.finishing_order = []
        self.DFS(self.G.values(), self.mark_finishing_time, reverse=True)
        #print [n.label for n in self.finishing_order]
        # Now we can safely run DFS starting from the earliest finishing time
        # and get the connected components.
        self.scc_sizes = {}
        assert(len(self.finishing_order) == len(self.G))
        self.finishing_order.reverse()
        self.DFS(self.finishing_order, self.label_sccs)
        print 'Scc sizes'
        sizes = self.scc_sizes.values()
        sizes.sort(reverse=True)
        print sizes[0:5]
        assert(sum(sizes) == len(self.G))

    def label_sccs(self, node, topnode):
        assert(node.scc == None)
        node.scc = topnode.label
        if not self.scc_sizes.has_key(topnode.label):
            self.scc_sizes[topnode.label] = 1
        else:
            self.scc_sizes[topnode.label] += 1

    def mark_finishing_time(self, node, topnode):
        self.finishing_order.append(node)

    def DFS(self, nodes, operation, reverse=False):
        # Perform depth-first-search on iterator of nodes
        # calling "operation" with the node when it is finished.
        for n in nodes: # Set all nodes to unexplored
            n.explored = False
        for n in nodes:
            if not n.explored:
                self.DFS_inner(n, operation, n, reverse)

    def DFS_inner(self, node, operation, topnode, reverse):
        node.explored = True
        if reverse:
            connections = node.incoming
        else:
            connections = node.outgoing
        for n in connections:
            if not n.explored:
                self.DFS_inner(n, operation, topnode, reverse)
        operation(node, topnode)
