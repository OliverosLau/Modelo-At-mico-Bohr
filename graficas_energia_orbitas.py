import matplotlib.pyplot as plt
import numpy as np
from energia_niveles import niveles_energia

def graficar_niveles_energia(n_max):
    """
    Genera una gráfica de los niveles de energía del átomo de hidrógeno.

    Args:
    n_max (int): Número cuántico máximo a graficar.
    """
    # Obtener niveles de energía
    niveles = niveles_energia(n_max)
    niveles_n = list(range(1, n_max + 1))
    
    # Crear la gráfica de los niveles de energía
    plt.figure(figsize=(8, 6))
    plt.plot(niveles_n, niveles, 'bo-', markersize=8, label='Energía del nivel n')
    plt.title('Niveles de energía del átomo de hidrógeno')
    plt.xlabel('Número cuántico (n)')
    plt.ylabel('Energía (eV)')
    plt.axhline(0, color='black',linewidth=1)  # Línea horizontal en y=0
    plt.grid(True)
    plt.legend()
    plt.show()

def graficar_orbitas(n_max):
    """
    Genera una gráfica de las órbitas electrónicas para los niveles de energía.

    Args:
    n_max (int): Número cuántico máximo a graficar.
    """
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Dibujar las órbitas electrónicas
    for n in range(1, n_max + 1):
        radio = n**2 * 0.53e-10  # Radio de Bohr ajustado por n^2
        orbita = plt.Circle((0, 0), radio, color='b', fill=False, linestyle='dashed')
        ax.add_artist(orbita)
        ax.text(radio + 1e-11, 0, f'n={n}', fontsize=12, verticalalignment='center')
    
    # Configurar los límites y las proporciones de la gráfica
    limite = n_max**2 * 0.53e-10 * 1.5
    ax.set_xlim(-limite, limite)
    ax.set_ylim(-limite, limite)
    ax.set_aspect('equal', 'box')
    plt.title('Órbitas electrónicas del átomo de hidrógeno')
    plt.grid(True)
    plt.show()

# Ejecución principal del módulo
if __name__ == "__main__":
    n_max = int(input("Introduce el número cuántico máximo para las gráficas: "))
    graficar_niveles_energia(n_max)
    graficar_orbitas(n_max)
