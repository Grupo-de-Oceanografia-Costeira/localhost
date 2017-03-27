# -*- coding: utf-8 -*-
import geopandas as gp
import matplotlib.pyplot as plt

def apa():
    # Iniciar o Plot da Área de Estudo
    laguna = gp.read_file('ShapeFiles/DestaqueLaguna.shp')
    sc = gp.read_file('ShapeFiles/DestaqueSC.shp')
    lagoas = gp.read_file('ShapeFiles/LagoasComplexoLagunar.shp')
    rios = gp.read_file('ShapeFiles/RiosComplexoLagunar.shp')
    apa = gp.read_file('ShapeFiles/apa-bf/apa-bf.shp')

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.set_xlim(-48.9,-48.6)
    ax.set_ylim(-28.55,-28.2)

    sc.plot(ax=ax, color='black')
    lagoas.plot(ax=ax, alpha=1, color='white')
    rios.plot(ax=ax, color='red')
    apa.plot(ax=ax, color='green')
    #testing station inclusion point
    plt.plot(-48.85, -28.5, marker='o', color='red', markersize=5)

    plt.show()

if __name__ == "__apa__":
        # execute only if run as a script
            apa()
