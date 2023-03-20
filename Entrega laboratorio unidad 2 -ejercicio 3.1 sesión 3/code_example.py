import random
import math

# Declare the required variables
Nsize = 10000 # Number of replications (sample size)
c1 = 0.5
c2 = 0.5
r = 0.5
estimE = 0 # Auxiliary variables for estimating the area (2D volume) of the circle intersection in quadrant I
estimDesv = 0

# # Show the circle and the quadrant I
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# fig, ax = plt.subplots()
# ax.add_patch(patches.Circle((c1, c2), r, fill=False))
# ax.add_patch(patches.Rectangle((0, 0), 1, 1, fill=False))
# ax.set_xlim(-1, 1)
# ax.set_ylim(-1, 1)

# Main loop
for i in range(Nsize):
    # Generate random coordinates x1 and x2
    x1, x2 = random.random(), random.random()

    # Plot the point
    # plt.plot(x1, x2, 'ro')

    # If the distance from the point to the circle center is less than the radius of the circle
    if ((x1 - c1)**2 + (x2 - c2)**2) <= r**2:
        # Increment the number of successful trials
        estimE += 1

# plt.show()

# Normalize the estimate
estimE /= Nsize

# Calculate the standard deviation of the estimate
estimDesv = math.sqrt(estimE * (1 - estimE) / (Nsize - 1))

# Print the results
print("Estimation:", estimE, "Standard Deviation:", estimDesv)