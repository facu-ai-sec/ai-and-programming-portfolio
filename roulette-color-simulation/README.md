# Roulette Color Probability Simulation

This project is a Python script that simulates spins of a European roulette wheel and analyzes the probability of landing on red or black numbers based on parity. Even numbers are treated as red, odd numbers as black, and zero is excluded from the probability calculation, following standard roulette rules.

The program performs a user-defined number of spins, calculates empirical probabilities, and visualizes the results using a bar chart.


## How It Works

The script randomly selects numbers from a European roulette wheel ranging from 0 to 36.

Each spin is classified as:
- Red if the number is even
- Black if the number is odd
- Zero is ignored in the color count

After completing all spins, the program calculates the probability of red and black outcomes and displays the results both in the console and in a bar chart.

## Technologies Used

- Python
- random module
- matplotlib

## Output

The script prints:
- The total number of red results and their probability
- The total number of black results and their probability

It also generates a bar chart comparing the frequencies of red and black outcomes.  
An example output image is included in the repository.

## Purpose

This project was created as a learning exercise to practice probability simulation, conditional logic, basic statistics, and data visualization in Python. It serves as a simple but solid example of applying theoretical probability concepts through code.

## How to Run

Make sure you have Python installed along with matplotlib.

Run the script using:

python roulette_simulation.py
