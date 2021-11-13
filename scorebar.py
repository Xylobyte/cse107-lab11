"""
A program that reads in the scores from the ACT and SAT data files and displays a bar chart of the average ACT and SAT scores for each state.

file: scorebar.py

author: Donovan Griego

date: 11-12-2021

assignment: Lab 11
"""
import matplotlib.pyplot as plt
import readscores

ACT_MAX = 36
SAT_MAX = 2400

def main():
    # Read in the scores
    try:
        with open('actsat.txt', 'r') as f:
            data = f.readlines()
            data = readscores.read_scores(data)
    except FileNotFoundError:
        print('File not found')
        exit(1)
    # Convert the scores to floats.
    states = [i['state'] for i in data]

    act_average = [float(i['act_average_score']) / ACT_MAX for i in data]
    act_percent_taking = [float(i['act_percent_taking']) for i in data]
    sat_percent_taking = [float(i['sat_percent_taking']) for i in data]
    sat_average_math = [float(i['sat_average_math']) for i in data]
    sat_average_reading = [float(i['sat_average_reading']) for i in data]
    sat_average_writing = [float(i['sat_average_writing']) for i in data]
    sat_average = [(i[0] + i[1] + i[2]) / -SAT_MAX for i in zip(sat_average_math, sat_average_reading, sat_average_writing)]


    # Get the SAT biased scores from sat_average where a state has less than 50% taking the ACT and more than 50% taking the SAT.
    sat_biased = [i[0] for i in zip(sat_average, act_percent_taking, sat_percent_taking) if i[1] < 50 and i[2] > 50]
    act_biased = [i[0] for i in zip(act_average, act_percent_taking, sat_percent_taking) if i[1] < 50 and i[2] > 50]
    state_biased = [i[0] for i in zip(states, act_percent_taking, sat_percent_taking) if i[1] < 50 and i[2] > 50]

    print("Which graph to diplay?")
    print("1. All states")
    print("2. States with less than 50% taking the ACT and more than 50% taking the SAT")
    graph_choice = input("Enter 1 or 2: ")
    fig, ax = plt.subplots(figsize=(12, 5))
    if graph_choice == "1":
        ax.bar(states, act_average, color='blue', label='ACT')
        ax.bar(states, sat_average, color='black', label='SAT') 
    elif graph_choice == "2":
        ax.bar(state_biased, act_biased, color='blue', label='ACT')
        ax.bar(state_biased, sat_biased, color='black', label='SAT')
    else:
        print("Invalid input")
        return

    # Get the average score
    # Make two bar charts in one figure. ACT is on top and SAT is inverse underneath. The origin should be in the middle. and the x axis should be the states.
    
    
    # Set the xticks to be rotated -45 on all plots
    plt.title('Comparison of SAT and ACT Scores')
    plt.xlabel('State')
    plt.ylabel('Score')
    plt.xticks(rotation=-45)
    plt.yticks([-1, -0.5, 0.5, 1], [2400,1200,18,36])
    plt.legend(['ACT', 'SAT'])
    plt.show()


if __name__ == "__main__":
    main()
