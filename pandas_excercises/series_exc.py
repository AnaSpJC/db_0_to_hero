# Goal: entender cómo Pandas asocia cada valor con una etiqueta (índice) que vos definís.
# pd.Series(ages, index=names)
import pandas as pd

edades = pd.Series([30, 25, 40])
print(edades)

ages = [23,50, 69]
names = ["A", "B", "C"]
print(pd.Series(names, ages))
print("📊 Series con índice personalizado:")
print(pd.Series(ages, index=names))