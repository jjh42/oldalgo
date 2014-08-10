"""Calculate the minimum cut of a graph."""
from random import randint
import copy

class Graph():
    """Representation of a graph. Vertices are represented as a dictionary,
    edges as a list."""
    def __init__(self, file=None):
        self.v = {}
        self.e = []

        if file == None:
            file = open('kargerAdj.txt', 'r')

        self._fromfile(file)

    def _fromfile(self, file):
        for line in file.readlines():
            entries = [int(e) for e in line.split()]
            vertice = entries[0]
            # All other numbers on this line specify adjacent vertices
            for av in entries[1:]:
                if av > vertice: # Graph is undirect, ignore previously entered edges.
                    self.e.append((vertice, av))
                    e_index = len(self.e) - 1
                    if not self.v.has_key(av):
                        self.v[av] = []
                    if not self.v.has_key(vertice):
                        self.v[vertice] = []
                    # Append this edge to both vertices
                    self.v[av].append(e_index)
                    self.v[vertice].append(e_index)

    def mincut(self):
        n = 1000
        return min([copy.deepcopy(self).random_cut() for i in range(n)])

    def random_cut(self):
        while len(self.v) > 2:
            self._random_contraction()
        return len(self.e)

    def _random_contraction(self):
        # Randomly select an edge to contract
        edge_index = randint(0, len(self.e) -1)
        livev, deadv = self.e[edge_index]
        dead_edges = []
        # Remove one the vertices to make a super-vertice and repoint all the edges
        for edge_ptr in self.v[deadv]:
            # Re-assign edges to the live edge
            v1, v2 = self.e[edge_ptr]
            assert(v1 == deadv or v2 == deadv)
            if v2 == deadv:
                v2,v1 = v1, v2
            if v2 == livev: # Remember self loops to remove afterwards
                dead_edges.append(edge_ptr)
            else:
                self.e[edge_ptr] = (livev, v2)
                self.v[livev].append(edge_ptr)
        # Finally delete the vertice itself
        self.v.pop(deadv)
        # And cleanup self loop edges
        dead_edges.sort(reverse=True)
        for edge in dead_edges:
            self._remove_edge(edge)
    
    def _remove_edge(self,i):
        """Remove edge i from the list of edges while maintaining the references in the
        vertice list. Does not do anything else."""
        self.e.pop(i)
        for key in self.v:
            # First remove all references to the deleted edge
            try:
                self.v[key].remove(i)
            except:
                pass # Ignore if it had no reference
            for j, edge_ref in enumerate(self.v[key]):
                if edge_ref == i:
                    assert(0) # Should have been deleted above
                elif edge_ref > i:
                    self.v[key][j] -= 1
