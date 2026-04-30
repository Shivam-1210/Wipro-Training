import csv
import os

def write_csv(filename):
    columnnmaes = ["name", "age"]
    with open(filename, "w", newline="\n") as file:
        writer = csv.DictWriter(file, filenames = columnnmaes)
        writer.
def read_csv(filename):
    with open{filename, "w", newline = "\n"} as file: