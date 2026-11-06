def criar_grafo():
    grafo = {}
    return grafo


def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
    else:
        print(f"Vértice '{vertice}' já existe no grafo.")


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):

    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)
    grafo[origem].append(destino)
    if nao_direcionado:
        grafo[destino].append(origem)

def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        return grafo.get(vertice, [])

def listar_vizinhos(grafo, vertice):
    lista = vizinhos(grafo, vertice)
    print(f"Vizinhos de {vertice}: {lista}")
    return lista

def exibir_grafo(grafo):
    for vertice, lista in grafo.items():
        print(f"{vertice} -> {lista}")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem not in grafo or destino not in grafo[origem]:
        return

    grafo[origem].remove(destino)

    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice not in grafo:
        return False

    del grafo[vertice]
    for vizinhos_do_vertice in grafo.values():
        while vertice in vizinhos_do_vertice:
            vizinhos_do_vertice.remove(vertice)
    return True


def existe_aresta(grafo, origem, destino):
    if origem in grafo:
        if destino in grafo[origem]:
            return True
    return False

def grau_vertices(grafo):
    graus = {}
    for vertice in grafo:
        graus[vertice] = {
            "entrada": 0,
            "saida": 0,
            "total": 0,
        }

    for vertice in grafo:
        graus[vertice]["saida"] = len(grafo[vertice])

        for origem in grafo:
            for vizinho in grafo[origem]:
                if vizinho == vertice:
                    graus[vertice]["entrada"] += 1

    for vertice in graus:
        graus[vertice]["total"] = (
            graus[vertice]["entrada"] + graus[vertice]["saida"]
        )

    return graus


def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False

    return True



def main():
    grafo = criar_grafo()

    while True:
        print("\n--- Grafo (lista de adjacência) ---")
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
        if opcao == "1":
            exibir_grafo(grafo)
        elif opcao == "2":
            vertice = input("Vértice: ").strip()
            inserir_vertice(grafo, vertice)
        elif opcao in ("3", "4"):
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            nao_direcionado = input(
                "Aresta não direcionada? (s/n): "
            ).strip().lower() == "s"
            if opcao == "3":
                inserir_aresta(
                    grafo, origem, destino, nao_direcionado
                )
            else:
                remover_aresta(
                    grafo, origem, destino, nao_direcionado
                )
        elif opcao == "5":
            vertice = input("Vértice: ").strip()
            if remover_vertice(grafo, vertice):
                print(f"Vértice '{vertice}' removido.")
            else:
                print(f"Vértice '{vertice}' não existe no grafo.")
        elif opcao == "6":
            vertice = input("Vértice: ").strip()
            listar_vizinhos(grafo, vertice)
        elif opcao == "7":
            print(grau_vertices(grafo))
        elif opcao == "8":
            entrada = input(
                "Percurso (vértices separados por vírgula): "
            )
            caminho = [vertice.strip() for vertice in entrada.split(",")]
            print("Percurso válido." if percurso_valido(grafo, caminho)
                  else "Percurso inválido.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
