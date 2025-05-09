import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from funciones_EDA import *
from variables import *

# EN EL MAIN SE MUESTRAN EL CONJUNTO DE DATOS UTILIZADOS PARA EL ANÁLISIS, TODOS ELLOS EN FUNCIÓN DEL PÁIS DE ORIGEN:

print("DATASET PROCESADO TRAS EL TRATAMIENTO DE DATOS:")
df_malaga
top_malaga.reset_index(drop=False, inplace=True)


print("TOP REGISTROS MÁLAGA 2024:")
top_malaga  

print("TOP REGISTROS TURISTAS TEMPORADA ALTA MÁLAGA 2024")
top_verano

print("TOP REGISTROS TURISTAS PRE-TEMPORADA MÁLAGA 2024")
top_pre

print("TOP REGISTROS TURISTAS POST-TEMPORADA MÁLAGA 2024")
top_post

print("TOP ESTANCIA MEDIA MÁLAGA 2024")
top_malaga_estancia

print("TOP ESTANCIA MEDIA TEMPORADA ALTA MÁLAGA 2024")
top_verano_estancia

print("TOP ESTANCIA MEDIA PRE-TEMPORADA MÁLAGA 2024")
top_pre_estancia

print("TOP ESTANCIA MEDIA POST-TEMPORADA MÁLAGA 2024")
top_post_estancia