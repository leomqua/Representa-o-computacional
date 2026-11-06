def criar_grafo():
    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):

    inserir_vertice(vertices, origem)
    inserir_vertice(vertices, destino)
    arestas.append([origem, destino])

    if nao_direcionado:
        arestas.append([destino, origem])

def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    aresta = [origem, destino]
    if aresta not in arestas:
        return False

    arestas.remove(aresta)
    if nao_direcionado:
        aresta_inversa = [destino, origem]
        if aresta_inversa in arestas:
            arestas.remove(aresta_inversa)
    return True

def remover_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        return False

    vertices.remove(vertice)
    arestas[:] = [
        aresta
        for aresta in arestas
        if aresta[0] != vertice and aresta[1] != vertice
    ]
    return True

def existe_aresta(arestas, origem, destino):
    for aresta in arestas:
        if aresta == [origem, destino]:
            return True
    return False


def vizinhos(vertices, arestas, vertice):
    vizinhos = []
    for origem, destino in arestas:
        if origem == vertice:
            vizinhos.append(destino)
    return vizinhos


def grau_vertices(vertices, arestas, nao_direcionado=False):
    graus = {}

    if nao_direcionado:
        for vertice in vertices:
            graus[vertice] = 0

        arestas_pendentes = [aresta.copy() for aresta in arestas]
        while arestas_pendentes:
            origem, destino = arestas_pendentes.pop(0)
            aresta_inversa = [destino, origem]
            if aresta_inversa in arestas_pendentes:
                arestas_pendentes.remove(aresta_inversa)

            if origem in graus:
                graus[origem] += 1
            if destino in graus:
                graus[destino] += 1
    else:
        for vertice in vertices:
            graus[vertice] = {
                "entrada": 0,
                "saida": 0,
                "total": 0,
            }

        for origem, destino in arestas:
            if origem in graus:
                graus[origem]["saida"] += 1
            if destino in graus:
                graus[destino]["entrada"] += 1

        for grau in graus.values():
            grau["total"] = grau["entrada"] + grau["saida"]

    return graus


def percurso_valido(arestas, caminho):
    for indice in range(len(caminho) - 1):
        origem = caminho[indice]
        destino = caminho[indice + 1]
        if not existe_aresta(arestas, origem, destino):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    lista = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {lista}")
    return lista


def exibir_grafo(vertices, arestas):
    print(f"Vértices: {vertices}")
    if not arestas:
        print("Arestas: nenhuma")
        return

    print("Arestas:")
    for origem, destino in arestas:
        print(f"  {origem} -> {destino}")


def main():
    vertices, arestas = criar_grafo()

    while True:
        print("\n--- Grafo (lista de arestas) ---")
        print("1 - Exibir grafo")
        print("2 - Inserir vértice")
        print("3 - Inserir aresta")
        print("4 - Remover aresta")
        print("5 - Remover vértice")
        print("6 - Listar vizinhos")
        print("7 - Exibir graus")
        print("8 - Verificar percurso")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "0":
            break
        elif opcao == "1":
            exibir_grafo(vertices, arestas)
        elif opcao == "2":
            vertice = input("Vértice: ").strip()
            inserir_vertice(vertices, vertice)
        elif opcao in ("3", "4"):
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            nao_direcionado = input(
                "Aresta não direcionada? (s/n): "
            ).strip().lower() == "s"

            if opcao == "3":
                inserir_aresta(
                    vertices, arestas, origem, destino, nao_direcionado
                )
            elif remover_aresta(
                arestas, origem, destino, nao_direcionado
            ):
                print("Aresta removida.")
            else:
                print("Aresta não encontrada.")
        elif opcao == "5":
            vertice = input("Vértice: ").strip()
            if remover_vertice(vertices, arestas, vertice):
                print(f"Vértice '{vertice}' e arestas associadas removidos.")
            else:
                print(f"Vértice '{vertice}' não existe no grafo.")
        elif opcao == "6":
            vertice = input("Vértice: ").strip()
            listar_vizinhos(vertices, arestas, vertice)
        elif opcao == "7":
            nao_direcionado = input(
                "O grafo é não direcionado? (s/n): "
            ).strip().lower() == "s"
            print(grau_vertices(vertices, arestas, nao_direcionado))
        elif opcao == "8":
            entrada = input(
                "Percurso (vértices separados por vírgula): "
            ).strip()
            caminho = (
                [vertice.strip() for vertice in entrada.split(",")]
                if entrada
                else []
            )
            if percurso_valido(arestas, caminho):
                print("Percurso válido.")
            else:
                print("Percurso inválido.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
