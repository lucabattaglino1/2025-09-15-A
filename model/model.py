import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._idMapAO = {}
        pass

    def getAnni(self):
        return DAO.getAllYears()

    def buildGraph(self, anno1, anno2):

        self._graph.clear()
        self._nodes = DAO.getAllNodes(anno1, anno2)
        self._idMap = {}

        for n in self._nodes:
            self._idMap[n.driverId] = n

        self._graph.add_nodes_from(self._nodes)
        self.addEdges(anno1, anno2)

    def getNumNodes(self):
        return len(self._graph.nodes)


    def addEdges(self, anno1, anno2):
        allEdges = DAO.getAllEdges(anno1, anno2, self._idMap)

        for t in allEdges:
            self._graph.add_edge(t[0], t[1], weight=t[2])

    def getNumEdges(self):
        return len(self._graph.edges)


    # stampare i 3 archi di peso maggiore
    def getTopArchi(self):

        archi = []
        for u, v, dati in self._graph.edges(data=True):
            archi.append((u, v, dati["weight"]))

        # Ordina per peso decrescente
        archi.sort(key=lambda x: x[2], reverse=True)
        return archi[:3]

    # stampare il numero di componenti connesse
    def getComponentiConnesse(self):
        return nx.number_connected_components(self._graph)

    # identifico la componente connessa di dimensione maggiore
    # stampare tutti i nodi ordinati per grado decrescente
    def getLargestComponent(self):
        componenti = list(nx.connected_components(self._graph))
        largest = max(componenti, key=len)

        nodi = []
        for n in largest:
            nodi.append((n, self._graph.degree(n)))

        nodi.sort(key=lambda x: x[1], reverse=True)
        return nodi


