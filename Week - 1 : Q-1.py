
import random
import matplotlib.pyplot as plt

list_of_sum = []

for x in range(0, 46656):
    sum = random.randint(1, 6) + random.randint(1, 6)
    list_of_sum.append(sum)

plt.hist(list_of_sum, bins = 11, density=True)
plt.xlabel('SUM')
plt.ylabel('PROBABILITY')
plt.title('ROLLING A PAIR OF DIE')
plt.grid(axis='y', color='pink', linestyle='--')
plt.show()
