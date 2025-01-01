# Analizador de Grafos Dirigidos y Circuitos Eulerianos

Este proyecto es una herramienta elaborada en Python para crear, analizar y visualizar grafos dirigidos. También permite exportar/importar archivos CSV para visualizar grafos ya definidos.

# Características

- Crear grafos manualmente o cargarlos desde un archivo CSV.
- Verficiar si un grafo contiene un circuito euleriano.
- Visualizar grafos con una representación gráfica más interactiva para el usuario. 
- Exportar grafos a archivos CSV.

# Requisitos para una correcta ejecución del programa.

- Python 3.7 o superior.
- Bibliotecas escenciales:
    * 'networkx' - Herramienta usada para trabajar con grafos y redes de forma más sencilla. 
    * 'matplotlib' - Herramienta que permite la creación de visualizaciones de gráficos.

NOTA: Ambas librerías son instalables ejecutando en el bash:

pip install networkx matplotlib.

# Ejemplo de Uso

Al iniciar el programa, se le dará al usuario la opción de ingresar de forma manual (con un formato específico) los nodos de origen y destino de no elegir esta opción, se permite el ingreso de nodos desde un formato CSV.

A la salida en consola se generará el gráfico visual de los nodos ingresados y sus conexiones entre las mismas, demostrando así si el grafo contiene un circuito euleriano.

# Contribuciones

Toda contribución para mejorar o hacer notar algún error en el proyecto es bienvenida. No dudes en abrir un problema o enviar un pull request. 

# Licencia

Este proyecto está licenciado bajo la Licencia MIT.