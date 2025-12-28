import random
import matplotlib.pyplot as plt

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 0]

red = []
black = []

trials = int(input("Enter number of spins: "))

for _ in range(trials):
    result = random.choice(numbers)
    if result == 0:
        pass
    elif result % 2 == 0:
        red.append(result)
    else:
        black.append(result)

red_probability = (len(red) / trials) * 100
black_probability = (len(black) / trials) * 100

print(f"Red numbers: {len(red)}. Probability: {red_probability:.2f}%")
print(f"Black numbers: {len(black)}. Probability: {black_probability:.2f}%")

categories = ["Red", "Black"]
values = [len(red), len(black)]

plt.bar(categories, values)
plt.ylabel("Count")
plt.title("Roulette Simulation Results")
plt.show()
