'''
The RSSI simulation matrix is made, visualized, and tested here


'''



import math
import matplotlib.pyplot as plt



# Matrix size
size = 1000

# Center coordinates
center_x = size // 2
center_y = size // 2

# Standard deviation for the Gaussian distribution
sigma = size // 10

# Pre-calculate some values for the Gaussian distribution
two_sigma_squared = 2 * sigma * sigma
one_over_sqrt_two_pi_sigma = 1 / (math.sqrt(2 * math.pi) * sigma)

# Initialize matrix
matrix = [[0 for _ in range(size)] for _ in range(size)]

# Fill the matrix
max_value = float('-inf')
for x in range(size):
    for y in range(size):
        # Calculate the distance from the center
        dx = x - center_x
        dy = y - center_y
        distance_squared = dx * dx + dy * dy

        # Calculate the Gaussian function
        gaussian = one_over_sqrt_two_pi_sigma * math.exp(-distance_squared / two_sigma_squared)

        # Assign the value to the matrix
        matrix[x][y] = gaussian
        if gaussian > max_value:
            max_value = gaussian

# Normalize the matrix
for x in range(size):
    for y in range(size):
        matrix[x][y] /= max_value

# Now the maximum value in the matrix will be 1


def get_rssi(xloc,yloc): #x from left to right goes 0 to 1000, y from top to bottom goes 0 to 1000, aka we start at top left corner
    
    #multiply by negative one because we are using minimization algorithm, but we are trying to maximize
    print(xloc,yloc)
    return -1 * matrix[int(yloc)][int(xloc)]




# plt.imshow(matrix)
# plt.show()
