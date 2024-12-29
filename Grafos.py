import networkx as nx
import matplotlib.pyplot as plt
import csv

# Función para leer un grafo desde un archivo CSV
def leer_grafo_csv(nombre_archivo):
    grafo = nx.DiGraph()  # Grafo dirigido
    try:
        with open(nombre_archivo, 'r') as archivo:
            lector = csv.reader(archivo)
            next(lector)  # Saltar encabezado
            for fila in lector:
                if len(fila) == 2:
                    origen, destino = fila
                    grafo.add_edge(origen, destino)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se encontró.")
    return grafo

# Función para entrada manual
def crear_grafo_manual():
    grafo = nx.DiGraph()
    print("Introduce las conexiones (formato: nodo_origen nodo_destino). Escribe 'fin' para terminar:")
    while True:
        entrada = input("Conexión: ")
        if entrada.lower() == "fin":
            break
        try:
            origen, destino = entrada.split()
            grafo.add_edge(origen, destino)
        except ValueError:
            print("Entrada inválida. Usa el formato: nodo_origen nodo_destino")
    return grafo

# Verificar si un grafo tiene un circuito euleriano
def verificar_circuito_euleriano(grafo):
    if nx.is_strongly_connected(grafo):  # Conexidad fuerte para grafos dirigidos
        grados_correctos = all(grafo.in_degree(n) == grafo.out_degree(n) for n in grafo.nodes)
        if grados_correctos:
            return True
    return False

# Visualizar el grafo
def visualizar_grafo(grafo, circuito=None):
    pos = nx.spring_layout(grafo)
    plt.figure(figsize=(8, 6))
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=3000, font_size=12)
    if circuito:
        nx.draw_networkx_edges(grafo, pos, edgelist=circuito, edge_color='red', width=2)
    plt.title("Grafo Dirigido")
    plt.show()

# Exportar grafo a archivo CSV
def exportar_grafo_csv(grafo, nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nodo_Origen", "Nodo_Destino"])
        for origen, destino in grafo.edges:
            escritor.writerow([origen, destino])
    print(f"Grafo exportado a {nombre_archivo}")

# Función principal
def main():
    print("Analizador de Grafos Dirigidos y Circuitos Eulerianos")
    print("1. Crear grafo manualmente")
    print("2. Cargar grafo desde archivo CSV")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        grafo = crear_grafo_manual()
    elif opcion == "2":
        nombre_archivo = input("Introduce el nombre del archivo CSV: ")
        grafo = leer_grafo_csv(nombre_archivo)
    else:
        print("Opción inválida")
        return

    if len(grafo) == 0:
        print("El grafo está vacío.")
        return

    # Verificar circuito euleriano
    es_euleriano = verificar_circuito_euleriano(grafo)
    if es_euleriano:
        print("El grafo contiene un circuito euleriano.")
        circuito = list(nx.eulerian_circuit(grafo))
        print("Circuito Euleriano:", " -> ".join(f"{u}->{v}" for u, v in circuito))
    else:
        print("El grafo no contiene un circuito euleriano.")
        circuito = None

    # Visualizar el grafo
    visualizar_grafo(grafo, circuito)

    # Exportar grafo (opcional)
    exportar = input("¿Deseas exportar el grafo a un archivo CSV? (s/n): ").lower()
    if exportar == "s":
        nombre_archivo_salida = input("Introduce el nombre del archivo de salida (incluye .csv): ")
        exportar_grafo_csv(grafo, nombre_archivo_salida)

if __name__ == "__main__":
    main()
