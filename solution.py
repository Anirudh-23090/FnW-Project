import numpy as np
import matplotlib.pyplot as plt

MAX_ITERATIONS = 1000

width = 3
height = 2
numOfPointsX = 31
numOfPointsY = 21

potential = np.zeros((numOfPointsY , numOfPointsX))

for i in range(numOfPointsX):
    potential[0 , i] = 0
    potential[-1 , i] = 5

for i in range(numOfPointsY):
    potential[i , 0] = 10
    potential[i , numOfPointsX - 1] = -10

for i in range(MAX_ITERATIONS):
    for j in range(1 , numOfPointsY - 1):
        for k in range(1 , numOfPointsX -  1):
            potential[j , k] = 0.25 * (potential[j + 1 , k] + potential[j - 1 , k] + potential[j , k + 1] + potential[j , k - 1])

x = np.linspace(0, width , numOfPointsX)
y = np.linspace(0 , height , numOfPointsY)
X, Y = np.meshgrid(x , y)

plt.figure()
plt.contourf(X , Y , potential , 100 , cmap = 'plasma')
plt.colorbar()
plt.title("2D Potential Plot Using FDM - Group 10")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()