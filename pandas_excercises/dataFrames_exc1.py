# Crea un DataFrame con columnas "Ciudad", "Habitantes", "País".
import pandas as pd

datos = {
    "Ciudad": ["Buenos Aires", "Tokio", "New York" ],
    "Habitantes": ["3.5M", "6.3M", "3.2M"],
    "País": ["Argentina", "Japón", "EEUU"]
}
df = pd.DataFrame(datos)
print(df)