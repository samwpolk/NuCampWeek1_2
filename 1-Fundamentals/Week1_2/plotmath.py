import matplotlib.pyplot as plt
import numpy as np
import random

# Define the mathematical function to plot


def f(x):
    return x**2


# Generate x values for the function
x = np.linspace(-10, 10, 100)

# Calculate y values for the function
y = f(x)

# Plot the function
plt.plot(x, y)

# Generate and plot a probability distribution
mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, density=True)

# Present the user with three choices
print("Please select one of the following options:")
print("1. The mathematical function")
print("2. The probability distribution")
print("3. Both the function and the distribution")

# Get the user's choice
choice = input()

# If the user's choice is incorrect, plot their choice and move on to the next plot
if choice != "3":
    if choice == "1":
        plt.plot(x, y)
    else:
        count, bins, ignored = plt.hist(s, 30, density=True)
    plt.show()

# If the user's choice is correct, plot both the function and the distribution
if choice == "3":
    plt.plot(x, y)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.show()
