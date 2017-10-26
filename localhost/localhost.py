# -*- coding: utf-8 -*-
import geopandas as gp
import matplotlib.pyplot as plt
import pandas as pd

def apa(coord=False, sep=";"):
    """Plot da Área de Estudo
    coord = nome do arquivo csv, contendo variáveis
    nominadas 'Lat' e 'Lon'.

    sep = formato de separação dos dados.
    """
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
    if coord:
        data = pd.read_csv(coord, sep=sep)
        lat = data['Lat']
        lon = data['Lon']
        for i in range(len(lat)):
            plt.plot(lon[i], lat[i], marker='o', color='red', markersize=5)

    plt.show()

if __name__ == "__main__":
        # execute only if run as a script
        apa()
