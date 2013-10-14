import rdflib

class Summarizer(object):

    def __init__(self, graph_url):
        self.graph = rdflib.Graph()
        self.graph.parse(graph_url)

    def size(self):
        return len(self.graph)
