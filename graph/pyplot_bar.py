import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()

months = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun')
y_pos = np.arange(len(months))  # Eixo y
performance = [2342, 34234, 2525, 2525, 20470, 5334]

# Documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html

# plt.bar plot com barras verticais
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, months)

"""
# plt.barh plot com barras horizontais
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, months)  # define os locais e os rótulos dos xticks
"""

plt.ylabel('Receita R$')
plt.title('Receita 1º semestre')

plt.show()
