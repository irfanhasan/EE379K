# question 1
import random
import matplotlib.pyplot as plt

mu1, sigma1 = -10, 5
mu2, sigma2 = 10, 5

print ("1st Gaussian: mean: " + str(mu1) + ", standard deviation: " + str(sigma1))
print ("2nd Gaussian: mean: " + str(mu2) + ", standard deviation: " + str(sigma2))

gau1 = []

for i in range(0, 1000):
	gau1.append(int(random.gauss(mu1, sigma1) + random.gauss(mu2, sigma2)))

plt.hist(gau1, bins="auto")
plt.title("1000 Integers of Sum of Two Gaussians")
plt.show()