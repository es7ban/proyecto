import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def visualizar_grilla(ambiente):
    grilla = ambiente.grilla
    matriz = []
    for fila in grilla:
        fila_numerica = []
        for celda in fila:
            if celda is None:
                fila_numerica.append(0)
            elif celda.get_estado() == "muerta":
                fila_numerica.append(2)
            elif celda.is_resistente():
                fila_numerica.append(3)
            else:
                fila_numerica.append(1)
        matriz.append(fila_numerica)

    fig, ax = plt.subplots(figsize=(6, 6))
    cmap = plt.cm.get_cmap('Set1', 5)
    cax = ax.matshow(matriz, cmap=cmap)

    legend_elements = [
        Patch(facecolor=cmap(1 / 5), label='Bacteria activa'),
        Patch(facecolor=cmap(2 / 5), label='Bacteria muerta'),
        Patch(facecolor=cmap(3 / 5), label='Bacteria resistente'),
         Patch(facecolor=cmap(4/5), label='Biofilm'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.4, 1))
    ax.set_xticks(range(len(matriz[0])))
    ax.set_yticks(range(len(matriz)))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(color='gray', linestyle='-', linewidth=0.5)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            val = matriz[i][j]
            if val > 0:
                ax.text(j, i, str(val), va='center', ha='center', color='white')

    plt.title("Grilla (visualizacion)")
    plt.tight_layout()
    plt.show()
