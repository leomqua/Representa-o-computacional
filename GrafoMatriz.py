def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        return False

    vertices.append(vertice)
    for linha in matriz:
        linha.append(0)
    matriz.append([0] * len(vertices))
    return True


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    indice_origem = vertices.index(origem)
    indice_destino = vertices.index(destino)
    matriz[indice_origem][indice_destino] = 1
    if nao_direcionado:
        matriz[indice_destino][indice_origem] = 1


def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        return False

    indice = vertices.index(vertice)
    vertices.pop(indice)
    matriz.pop(indice)
    for linha in matriz:
        linha.pop(indice)
    return True

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    if origem not in vertices or destino not in vertices:
        return False

    indice_origem = vertices.index(origem)
    indice_destino = vertices.index(destino)
    if matriz[indice_origem][indice_destino] == 0:
        return False

    matriz[indice_origem][indice_destino] = 0
    if nao_direcionado:
        matriz[indice_destino][indice_origem] = 0
    return True


def existe_aresta(matriz, vertices, origem, destino):
    if origem not in vertices or destino not in vertices:
        return False

    indice_origem = vertices.index(origem)
    indice_destino = vertices.index(destino)
    return matriz[indice_origem][indice_destino] == 1


def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []

    indice = vertices.index(vertice)
    lista_vizinhos = []
    for indice_vizinho, conexao in enumerate(matriz[indice]):
        if conexao == 1:
            lista_vizinhos.append(vertices[indice_vizinho])
    return lista_vizinhos


def grau_vertices(matriz, vertices, nao_direcionado=False):
    graus = {}
    for indice, vertice in enumerate(vertices):
        if nao_direcionado:
            graus[vertice] = sum(matriz[indice])
        else:
            saida = sum(matriz[indice])
            entrada = sum(linha[indice] for linha in matriz)
            graus[vertice] = {
                "saida": saida,
                "entrada": entrada,
                "total": saida + entrada,
            }
    return graus


def percurso_valido(matriz, vertices, caminho):
    for indice in range(len(caminho) - 1):
        origem = caminho[indice]
        destino = caminho[indice + 1]
        if not existe_aresta(matriz, vertices, origem, destino):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):
    lista = vizinhos(matriz, vertices, vertice)
    print(f"Vizinhos de {vertice}: {lista}")
    return lista


def exibir_grafo(matriz, vertices):
    if not vertices:
        print("Grafo vazio.")
        return

    largura = max(len(str(vertice)) for vertice in vertices)
    print(" " * (largura + 2) + " ".join(
        str(vertice).rjust(largura) for vertice in vertices
    ))
    for vertice, linha in zip(vertices, matriz):
        valores = " ".join(str(valor).rjust(largura) for valor in linha)
        print(f"{str(vertice).rjust(largura)}: {valores}")


def main():
    matriz, vertices = criar_grafo()

    while True:
        print("\n--- Grafo (matriz de adjacência) ---")
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
            exibir_grafo(matriz, vertices)
        elif opcao == "2":
            vertice = input("Vértice: ").strip()
            if inserir_vertice(matriz, vertices, vertice):
                print(f"Vértice '{vertice}' inserido.")
            else:
                print(f"Vértice '{vertice}' já existe no grafo.")
        elif opcao in ("3", "4"):
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            nao_direcionado = input(
                "Aresta não direcionada? (s/n): "
            ).strip().lower() == "s"
            if opcao == "3":
                inserir_aresta(
                    matriz, vertices, origem, destino, nao_direcionado
                )
                print("Aresta inserida.")
            elif remover_aresta(
                matriz, vertices, origem, destino, nao_direcionado
            ):
                print("Aresta removida.")
            else:
                print("Aresta não encontrada.")
        elif opcao == "5":
            vertice = input("Vértice: ").strip()
            if remover_vertice(matriz, vertices, vertice):
                print(f"Vértice '{vertice}' e arestas associadas removidos.")
            else:
                print(f"Vértice '{vertice}' não existe no grafo.")
        elif opcao == "6":
            vertice = input("Vértice: ").strip()
            listar_vizinhos(matriz, vertices, vertice)
        elif opcao == "7":
            nao_direcionado = input(
                "O grafo é não direcionado? (s/n): "
            ).strip().lower() == "s"
            print(grau_vertices(matriz, vertices, nao_direcionado))
        elif opcao == "8":
            entrada = input(
                "Percurso (vértices separados por vírgula): "
            ).strip()
            caminho = (
                [vertice.strip() for vertice in entrada.split(",")]
                if entrada
                else []
            )
            if percurso_valido(matriz, vertices, caminho):
                print("Percurso válido.")
            else:
                print("Percurso inválido.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
