import polars as pl
import sqlite3
import plotly.express as px


conn = sqlite3.connect("basede.sqlite")

# Ejecutá una consulta y convertí el resultado en DataFrame de Polars
df = pl.read_database("SELECT id, nombre, apellido, puntaje FROM usuarios_dos", connection=conn)

# Mostralo
print(df)

resumen = df.select(["nombre", "puntaje"])

df_plot = resumen.to_pandas()

fig = px.bar(df_plot, x="nombre", y="puntaje", title="Puntaje por persona")

fig.show()

conn.close()