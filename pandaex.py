import pandas as pd
import kagglehub
import os

path = kagglehub.dataset_download(
    "jessicali9530/animal-crossing-new-horizons-nookplaza-dataset"
)

print("Files in dataset:")
print(os.listdir(path))

villagers = pd.read_csv(f"{path}/villagers.csv")

print("\nFirst 5 rows:")
print(villagers.head())

print("\nInfo:")
villagers.info()

print("\nShape:")
print(villagers.shape)

print("\nColumns:")
print(villagers.columns)

print("\nMissing values:")
print(villagers.isna().sum())
