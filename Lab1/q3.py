# question 3 of homework 1
import random
import numpy
import math

data = []
for i in range (0, 25000):
	data.append(random.gauss(0, 5))
print("25000 data with mu=0 and std=5")

total = 0
for d in data:
	total += d
mu = total / 25000.0
print("est mu is " + str(mu))

total = 0
for d in data:
	total += (d - mu) ** 2
std = math.sqrt(total / 24999.0)
print("est std is " + str(std))
