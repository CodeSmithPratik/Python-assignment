import matplotlib.pyplot as plt


categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [10, 15, 7, 12]


plt.barh(categories, values, color='orange')


plt.xlabel('Quantity')
plt.ylabel('Fruits')
plt.title('Fruit Quantity (Horizontal Bar Chart)')

plt.show()

