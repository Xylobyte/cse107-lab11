"""
A program that reads in a file of scores and creates a histogram of the scores.

file: scorehist.py

author: Donovan Griego

Date: 11-12-2021

assignment: Lab 11
"""
import matplotlib.pyplot as plt
import numpy as np
import readscores

def main():
    # Read in the scores
    with open('actsat.txt', 'r') as f:
        data = f.readlines()
        scores = [i['act_average_score'] for i in readscores.read_scores(data)]
    # Convert the scores to floats.
    scores = [float(score) for score in scores]
    # Get the average score
    average = np.mean(scores)
    # Create the histogram with outlines on the bars and y going from 0 to 20 and x groing from 18 to 24
    plt.hist(scores, edgecolor='black')
    # Add a title
    plt.title("Histogram of ACT Scores")
    # Add a label to the x axis
    plt.xlabel("Score out of 36")
    # Add a label to the y axis
    plt.ylabel("Number of States")
    # Add a legend
    plt.legend(["Average Score: " + str(average)])
    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()