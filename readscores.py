"""
A program that reads a file of values separated by whitespace and puts that information
into a dictionary

file: readscores.py

author: Donovan Griego

Date: 10-24-2021

assignment: Lab 9
"""


def read_scores(lines):
    """This function takes a list of strings that represent whitespace-separated data.
    Returns a list of dictionaries.
    """
    data = []

    for line in lines:
        values = line.split()
        row = dict()
        row["state"] = values[0]
        row["act_percent_taking"] = values[1]
        row["act_average_score"] = values[2]
        row["sat_percent_taking"] = values[3]
        row["sat_average_math"] = values[4]
        row["sat_average_reading"] = values[5]
        row["sat_average_writing"] = values[6]
        data.append(row)
    return data


def main():
    try:
        with open("actsat.txt") as f:
            lines = f.readlines()
    except IsADirectoryError:
        print("Error; 'actsat.txt' is a directory!")
        exit(1)
    except FileNotFoundError:
        print("Error; File not found!")
        exit(1)
    for data_row in read_scores(lines):
        print(data_row)


if __name__ == "__main__":
    main()
