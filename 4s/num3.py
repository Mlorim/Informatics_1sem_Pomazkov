import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris_data.csv', delimiter=',', index_col=0)

species = []

for i in iris["Species"]:
    species.append(i)

species_dict = {}

for i in species:
    if i not in species_dict.keys():
        species_dict[i] = 1
    else:
        species_dict[i] += 1

plt.subplot(2, 1, 1)
plt.pie(species_dict.values(), labels=[i for i in species_dict.keys()])
plt.title('Species')


PetalLengthCm_dict = {">1.2 cm": 0, "1.2 - 1.5 cm": 0, ">1.5 cm": 0}

for i in iris["PetalLengthCm"]:
    i = float(i)
    if i >= 1.5:
        PetalLengthCm_dict[">1.5 cm"] += 1
        PetalLengthCm_dict[">1.2 cm"] += 1
    elif i >= 1.2:
        PetalLengthCm_dict["1.2 - 1.5 cm"] += 1
        PetalLengthCm_dict[">1.2 cm"] += 1


plt.subplot(2, 1, 2)
plt.pie(PetalLengthCm_dict.values(), labels=[i for i in PetalLengthCm_dict.keys()])
plt.title('Sheet sizes')

plt.show()
