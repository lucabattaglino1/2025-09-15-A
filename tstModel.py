# tstModel.py
from model.model import Model

mdl = Model()
mdl.buildGraph(2007,2008)
print(f"Nodi: {mdl.getNumNodes()}")
print(f"Archi: {mdl.getNumEdges()}")
