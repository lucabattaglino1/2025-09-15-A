import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDAnno1(self):
        anni = self._model.getAnni()
        for a in anni:
            self._view._ddAnno1.options.append(ft.dropdown.Option(str(a)))
        self._view.update_page()

    def fillDDAnno2(self):
        anni = self._model.getAnni()
        for a in anni:
            self._view._ddAnno2.options.append(ft.dropdown.Option(str(a)))
        self._view.update_page()


    def handleCreaGrafo(self, e):

        anno1 = self._view._ddAnno1.value
        anno2 = self._view._ddAnno2.value

        if anno1 is None:
            self._view.txt_result.controls.append(ft.Text("Seleziona l'anno di inizio"))
            return

        if anno2 is None:
            self._view.txt_result.controls.append(ft.Text("Seleziona l'anno di fine"))
            return

        self._view.txt_result.controls.clear()

        self._model.buildGraph(anno1, anno2)

        # stampo le info
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi."))

        self._view.update_page()

    def handleDettagli(self, e):

        self._view.txt_result.controls.append(ft.Text("Archi di peso maggiore:"))
        for a1, a2, peso in self._model.getTopArchi():
            self._view.txt_result.controls.append(ft.Text(f"{a1.surname} -> {a2.surname} ( {peso} )"))

        self._view.txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getComponentiConnesse()} componenti connesse."))

        self._view.txt_result.controls.append(ft.Text("Componente connessa più grande:"))
        for nodo, grado in self._model.getLargestComponent():
            self._view.txt_result.controls.append(ft.Text(f"{nodo.surname} - grado: {grado}"))

        self._view.update_page()

    def handleCerca(self, e):
        pass

