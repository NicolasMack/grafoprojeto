"projeto grafos transpore fluvial"
"nicolas alteia telles 42010225"


class Grafo:

  def __init__(self):
    self.vertices = {}
    self.arestas = []

  def adicionar_vertice(self, rotulo, peso):
    if rotulo not in self.vertices:
      self.vertices[rotulo] = {"peso": peso, "adjacentes": {}}

  def adicionar_aresta(self, u, v, peso):
    if u in self.vertices and v in self.vertices:
      self.vertices[u]["adjacentes"][v] = peso
      self.vertices[v]["adjacentes"][u] = peso
      self.arestas.append((u, v, peso))

  def remover_vertice(self, rotulo):
    if rotulo in self.vertices:
      del self.vertices[rotulo]
      self.arestas = [(u, v, peso) for u, v, peso in self.arestas
                      if u != rotulo and v != rotulo]

      for vertice in self.vertices.values():
        vertice["adjacentes"] = {
            v: peso
            for v, peso in vertice["adjacentes"].items() if v != rotulo
        }

  def remover_aresta(self, u, v):
    if u in self.vertices and v in self.vertices:
      if v in self.vertices[u]["adjacentes"]:
        del self.vertices[u]["adjacentes"][v]
        del self.vertices[v]["adjacentes"][u]
        self.arestas = [(u1, v1, peso) for u1, v1, peso in self.arestas
                        if (u1 != u or v1 != v) and (u1 != v or v1 != u)]

  def mostrar_conteudo(self):
    print("Tipo do Grafo: (Defina o tipo aqui)")
    print(len(self.vertices))
    for rotulo, data in self.vertices.items():
      print(f'{rotulo} "{rotulo}" "{data["peso"]:.2f}"')
    print(len(self.arestas))
    for u, v, peso in self.arestas:
      print(f'{u} {v} "{peso:.2f}"')

  def mostrar_grafo(self):
    for u, data in self.vertices.items():
      print(f'{u} - Peso: {data["peso"]:.2f}')
      for v, peso in data["adjacentes"].items():
        print(f'  -> {v} - Peso da aresta: {peso:.2f}')

  def verificar_conexidade(self):
    visitados = set()
    componentes_conexas = []

    for vertice in self.vertices.keys():
      if vertice not in visitados:
        componente = self.busca_em_profundidade(vertice, visitados)
        componentes_conexas.append(componente)

    if len(componentes_conexas) == 1:
      print("O grafo é conexo.")
    else:
      print("O grafo não é conexo.")
      for i, componente in enumerate(componentes_conexas, start=1):
        print(f"Componente {i}: {componente}")

  def busca_em_profundidade(self, vertice, visitados):
    componente = set()
    pilha = [vertice]

    while pilha:
      atual = pilha.pop()
      visitados.add(atual)
      componente.add(atual)

      for vizinho in self.vertices[atual]["adjacentes"]:
        if vizinho not in visitados:
          pilha.append(vizinho)

    return componente


def main():
  grafo = Grafo()
  filename = "grafo.txt"

  while True:
    print("\nMenu de Opções:")
    print("1. Inserir Vértice")
    print("2. Inserir Aresta")
    print("3. Remover Vértice")
    print("4. Remover Aresta")
    print("5. Mostrar Conteúdo do Arquivo")
    print("6. Mostrar Grafo")
    print("7. Verificar Conexidade")
    print("8. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
      rotulo = input("Digite o rótulo do vértice: ")
      peso = float(input("Digite o peso do vértice: "))
      grafo.adicionar_vertice(rotulo, peso)
    elif escolha == "2":
      u = input("Digite o rótulo do primeiro vértice da aresta: ")
      v = input("Digite o rótulo do segundo vértice da aresta: ")
      peso = float(input("Digite o peso da aresta: "))
      grafo.adicionar_aresta(u, v, peso)
    elif escolha == "3":
      rotulo = input("Digite o rótulo do vértice a ser removido: ")
      grafo.remover_vertice(rotulo)
    elif escolha == "4":
      u = input(
          "Digite o rótulo do primeiro vértice da aresta a ser removida: ")
      v = input(
          "Digite o rótulo do segundo vértice da aresta a ser removida: ")
      grafo.remover_aresta(u, v)
    elif escolha == "5":
      grafo.mostrar_conteudo()
    elif escolha == "6":
      grafo.mostrar_grafo()
    elif escolha == "7":
      grafo.verificar_conexidade()
    elif escolha == "8":
      break
    else:
      print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
  main()
