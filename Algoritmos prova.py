import heapq
import tkinter as tk
from tkinter import ttk

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}
        self.distancias = {}

    def adicionar_vertice(self, valor):
        self.vertices.add(valor)
        self.arestas[valor] = []
        self.distancias[(valor, valor)] = 0

    def adicionar_aresta(self, de_vertice, para_vertice, distancia):
        self.arestas[de_vertice].append(para_vertice)
        self.arestas[para_vertice].append(de_vertice)
        self.distancias[(de_vertice, para_vertice)] = distancia
        self.distancias[(para_vertice, de_vertice)] = distancia

    def dijkstra(self, inicio, fim):
        distancias = {vertice: float('infinity') for vertice in self.vertices}
        distancias[inicio] = 0
        fila = [(0, inicio)]

        while fila:
            distancia_atual, vertice_atual = heapq.heappop(fila)

            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho in self.arestas[vertice_atual]:
                nova_distancia = distancias[vertice_atual] + self.distancias[(vertice_atual, vizinho)]

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(fila, (nova_distancia, vizinho))

        return distancias[fim]


def calcular_caminho():
    cidade_origem = combo_origem.get()
    cidade_destino = combo_destino.get()

    custo_caminho = grafo.dijkstra(cidade_origem, cidade_destino)

    if custo_caminho == float('infinity'):
        resultado_label.config(text=f"Não há um caminho entre {cidade_origem} e {cidade_destino}.")
    else:
        resultado_label.config(text=f"O caminho mínimo entre {cidade_origem} e {cidade_destino} é {custo_caminho} km.")


def encerrar_programa():
    root.destroy()


grafo = Grafo()
cidades = ["São Paulo", "Rio de Janeiro", "Vitória", "Recife", "Salvador", "Natal"]

for cidade in cidades:
    grafo.adicionar_vertice(cidade)

grafo.adicionar_aresta("São Paulo", "Rio de Janeiro", 400)
grafo.adicionar_aresta("São Paulo", "Vitória", 600)
grafo.adicionar_aresta("Rio de Janeiro", "Vitória", 350)
grafo.adicionar_aresta("Rio de Janeiro", "Recife", 800)
grafo.adicionar_aresta("Vitória", "Recife", 550)
grafo.adicionar_aresta("Recife", "Salvador", 700)
grafo.adicionar_aresta("Salvador", "Natal", 450)


root = tk.Tk()
root.title("Calculadora de Caminho Mínimo")


label_origem = ttk.Label(root, text="Cidade de Origem:")
label_destino = ttk.Label(root, text="Cidade de Destino:")
combo_origem = ttk.Combobox(root, values=cidades)
combo_destino = ttk.Combobox(root, values=cidades)
calcular_button = ttk.Button(root, text="Calcular Caminho", command=calcular_caminho)
resultado_label = ttk.Label(root, text="")

label_origem.grid(row=0, column=0, padx=10, pady=10)
combo_origem.grid(row=0, column=1, padx=10, pady=10)
label_destino.grid(row=1, column=0, padx=10, pady=10)
combo_destino.grid(row=1, column=1, padx=10, pady=10)
calcular_button.grid(row=2, column=0, columnspan=2, pady=10)
resultado_label.grid(row=3, column=0, columnspan=2, pady=10)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
menu_programa = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Programa", menu=menu_programa)
menu_programa.add_command(label="Encerrar", command=encerrar_programa)


root.mainloop()
