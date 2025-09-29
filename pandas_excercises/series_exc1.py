# 1) Crea una Series con los nombres de tres ciudades.
# 2) Idem pero con definición de índices
import pandas as pd

ciudades = pd.Series(["Buenos Aires", "Tokio", "New York"])
print(ciudades)

cities = ["Buenos Aires", "Tokio", "New York"]
my_index = ["City 1", "City 2", "City 3"]
my_indexed_cities = pd.Series(cities, index=my_index)
print("\nCiudades con índice personalizado:")
print(my_indexed_cities)
print("Printing sin variable 'my_indexed_cities'")
print(pd.Series(cities, index=my_index))
