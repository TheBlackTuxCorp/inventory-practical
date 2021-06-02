#! /usr/bin/env python
"""
Parse Input
"""
import csv
import os
import sys

DIRNAME = os.path.dirname(__file__)

# This is a helper function that takes the argument you call the script with, creates the filepath
# for the file in the sample-inputs directory, and then parses the lines of the files into a
# dict representing each line as an event. You can mostly ignore the code here and focus on adding
# your solution below in the main() function.
def parse_events_from_file():
    events = []

    filename = sys.argv[1]

    inputs_path = os.path.relpath('../sample-inputs', DIRNAME)
    input_filepath = os.path.join(inputs_path, filename)

    file = open(input_filepath, "r")
    file_contents = file.read()

    event_lines = file_contents.splitlines()

    for line in event_lines:
        event_day, num_small, num_medium, num_large = line.split(',')
        event = { "event_day": event_day, "num_small": num_small, "num_medium": num_medium, "num_large": num_large }
        events.append(event)

    return events

# From the /python directory, you can run `python parse.py success0.txt`.
# The `events` variable will be a list of dicts with the following keys:
# - "event_day" representing the day of the event
# - "num_small" representing the number of small suits required for the event
# - "num_medium" representing the number of medium suits required for the event
# - "num_large" representing the number of large suits required for the event
def main():
    events = parse_events_from_file()

    # Add your code here
    print(events)


if __name__ == "__main__":
    main()
