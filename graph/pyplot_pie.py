import matplotlib.pyplot as plt

# -------------------- [1 Example]
values = [40, 10, 50]
labels = ['PHP', 'JavaScript', 'Python']

plt.figure(figsize=(10, 8))
plt.pie(values, labels=labels, autopct="%1d%%")
plt.title('Favorites languages')
plt.show()

# -------------------- [2 Example]
labels = 'Laranja', 'Banana', 'Melancia', 'Abacate'
sizes = [20, 30, 40, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Banana')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Proporção de aspecto igual garante o desenho como um círculo.
plt.show()
