# question 2
import random
import matplotlib.pyplot as plt


# function definitions
def createBernolli(n):
	x = 0
	for i in range(0, n):
		x += random.randrange(-1, 2, 2)
	return float(x) / n

# main
n = 250
data = []

for i in range(0, 1000):
	data.append(createBernolli(n))

plt.hist(data, bins="auto")
plt.title("Bernoulli Variable with n = " + str(n))
plt.show()


