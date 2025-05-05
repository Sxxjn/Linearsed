import numpy as np
import matplotlib.pyplot as plt

# 1. Loeme andmed failist
with open('maed.txt', 'r') as file:
    lines = file.readlines()

# 2. Salvestame mägede nimed ja kõrgused kahte eraldi nimekirja
mountain_names = []
mountain_heights = []

for line in lines:
    # Eemaldame liigsed tühikud ja jagame rea kaheks osaks
    parts = line.split()
    if len(parts) == 2:  # Kontrollime, et rida oleks õigesti jagatud
        name, height = parts
        mountain_names.append(name)
        mountain_heights.append(int(height))

# 3. Kasutame numpy-d arvutamiseks
heights_array = np.array(mountain_heights)

# Keskmine kõrgus
average_height = np.mean(heights_array)

# Kõrgeim ja madalaim mägi
max_height = np.max(heights_array)
min_height = np.min(heights_array)

# Kogusumma
total_height = np.sum(heights_array)

# 4. Kuvame tulemused terminalis
print(f"Keskmine kõrgus: {average_height:.2f} m")
print(f"Kõrgeim mägi: {mountain_names[np.argmax(heights_array)]} ({max_height} m)")
print(f"Madalaim mägi: {mountain_names[np.argmin(heights_array)]} ({min_height} m)")
print(f"Kogusumma kõrgustest: {total_height} m")

# 5. Loome tulpdiagrammi
plt.figure(figsize=(10, 6))
plt.bar(mountain_names, heights_array)
plt.xlabel('Mäed')
plt.ylabel('Kõrgus (m)')
plt.title('Mägedes kõrgused')
plt.xticks(rotation=45)
plt.tight_layout()

# 6. (Soovi korral) Sorteerime mäed kõrguse alusel kahanevalt
sorted_indices = np.argsort(heights_array)[::-1]  # Kahanev järjestus
sorted_mountain_names = np.array(mountain_names)[sorted_indices]
sorted_heights_array = heights_array[sorted_indices]

# 7. Loome sorteeritud graafiku
plt.figure(figsize=(10, 6))
plt.bar(sorted_mountain_names, sorted_heights_array)
plt.xlabel('Mäed')
plt.ylabel('Kõrgus (m)')
plt.title('Mägedes kõrgused (sorteeritud)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
