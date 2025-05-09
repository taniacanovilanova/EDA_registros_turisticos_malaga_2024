import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import math

def cardinalidad(dataframe, umbral_categoria = int, umbral_continua = float):

    df_resultado = pd.DataFrame([dataframe.nunique(), dataframe.nunique()/len(dataframe)*100]).T.rename(columns = {0: "Cardinalidad", 1: "%_Cardinalidad"})
    
    df_resultado["Tipo"] = "Numérica Discreta"
    df_resultado.loc[df_resultado["Cardinalidad"] < umbral_categoria, "Tipo"] = "Categórica"
    df_resultado.loc[df_resultado["Cardinalidad"] == 2.0, "Tipo"] = "Binaria"
    #df_resultado.loc["Cardinalidad" >= umbral_categoria, "Tipo"] = "Numérica Discreta" 
    df_resultado.loc[df_resultado["%_Cardinalidad"] >= umbral_continua, "Tipo"] = "Numérica Continua"

    return df_resultado

def pinta_categoricas(dataframe, columnas = []):
                     
    fig,axs = plt.subplots(nrows= math.ceil(len(columnas) / 2) , ncols=2, figsize=(18,10))    ## 1)
    axs = axs.flatten()    ## 2)
    
    for indice, variable in enumerate(columnas):
        
        sns.countplot(x= variable, data = dataframe, ax = axs[indice], hue = variable, legend = False)
        axs[indice].set_title(f"Frecuencias absolutas de '{variable}':")

    fig

        ## 1) math.ceil(len(columnas)/2) --> me piden 2 columnas y tantas filas como sean necesarias, así que el num de filas será el num de elementos en la lista columnas partido entre 2. 
        ## Este num tiene que ser entero sí o sí, para ello queremos redondear el resultado de la división a la alta con el método ceil del módulo math.

        ## 2) con axs.flatten() aplano a una dimensión el índice de acceso a mis axes, es decir, cambio el axs[0][0], axs[0][1], axs[1][0], axs[1][1] por axs[0], axs[1], axs[2], axs[3]
        # respectivamente. Es necesario para definir mi función y poder iterar mi lista columnas aplicando el mismo índice de sus elementos a mis axes. 

def pinta_histograma(dataframe, columnas = [], bins = int, kde = bool):
    
    fig,axs = plt.subplots(nrows= math.ceil(len(columnas) / 2) , ncols=2, figsize=(12,10)) 
    axs = axs.flatten()

    for indice, variable in enumerate(columnas):
            
        sns.histplot(dataframe[variable],
                    kde= kde,
                    bins= bins, ax = axs[indice])
        
        axs[indice].set_title(f"Histograma de '{variable}':")
        
    fig      

def pinta_boxplot(dataframe, columna):
    
    plt.figure(figsize = (7,7))
    plt.boxplot(dataframe[columna], whis=1.5,vert= False, patch_artist=True)
    plt.title(f"Diagrama de caja de {columna} de la provincia de Málaga")
    plt.xlabel(f"Total {columna}")



def pinta_secuencia_temporal(dataframe, columnas = []):

    fig,axs = plt.subplots(nrows= math.ceil(len(columnas) / 2) , ncols=2, figsize=(12,10)) 
    axs = axs.flatten()

    for indice, variable in enumerate(columnas):
        sns.lineplot( x = dataframe.MES, y = variable, data = dataframe, ax = axs[indice])
        axs[indice].set_title(f"Gráfica de '{variable}':")
    fig    

def pinta_boxplot(dataframe, columna):
    
    plt.figure(figsize = (8,8))
    plt.boxplot(dataframe[columna], whis=1.5,vert= False, patch_artist=True)
    plt.title(f"Diagrama de caja de {columna} de la provincia de Málaga")
    plt.xlabel(f"Total {columna}")
