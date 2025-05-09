import pandas as pd
df_malaga = pd.read_csv("./data/dataset_viajeros_procesado.csv", encoding= "latin1", sep= ";")

malaga = df_malaga.groupby(["PAIS_ORIGEN"])["TURISTAS"].sum()
top_malaga = pd.DataFrame(malaga)

temp_alta = df_malaga.TEMPORADA == "Temporada Alta"
df_verano= df_malaga[temp_alta]
verano = df_verano.groupby(["PAIS_ORIGEN"])["TURISTAS"].sum()
top_verano = pd.DataFrame(verano)
top_verano.reset_index(drop=False, inplace=True)

pre = df_malaga.TEMPORADA == "Pre-Temporada"
df_pre= df_malaga[pre]
pre = df_pre.groupby(["PAIS_ORIGEN"])["TURISTAS"].sum()
top_pre = pd.DataFrame(pre)
top_pre.reset_index(drop=False, inplace=True)


post = df_malaga.TEMPORADA == "Post-Temporada"
df_post = df_malaga[post]
post = df_post.groupby(["PAIS_ORIGEN"])["TURISTAS"].sum()
top_post = pd.DataFrame(post)
top_post.reset_index(drop=False, inplace=True)

malaga_estancia = df_malaga.groupby(["PAIS_ORIGEN"])["ESTANCIA_MEDIA"].mean()
top_malaga_estancia = pd.DataFrame(malaga_estancia)
top_malaga_estancia.reset_index(drop=False, inplace=True)

verano_estancia = df_verano.groupby(["PAIS_ORIGEN"])["ESTANCIA_MEDIA"].mean()
top_verano_estancia = pd.DataFrame(verano_estancia)
top_verano_estancia.reset_index(drop=False, inplace=True)

pre_estancia = df_pre.groupby(["PAIS_ORIGEN"])["ESTANCIA_MEDIA"].mean()
top_pre_estancia = pd.DataFrame(pre_estancia)
top_pre_estancia.reset_index(drop=False, inplace=True)

post_estancia = df_post.groupby(["PAIS_ORIGEN"])["ESTANCIA_MEDIA"].mean()
top_post_estancia = pd.DataFrame(post_estancia)
top_post_estancia.reset_index(drop=False, inplace=True)