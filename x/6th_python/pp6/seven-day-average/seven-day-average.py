import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = dict()
    prev_cases = dict()

    for row in reader:
        state = row["state"]
        cases = int(row["cases"])

        if state not in prev_cases:
            prev_cases[state] = cases
            new_cases[state] = []
        else:
            new_case = cases - prev_cases[state]
            prev_cases[state] = cases

            if len(new_cases[state]) > 14:
                new_cases[state].pop(0)

            new_cases[state].append(new_case)

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        lw = sum(new_cases[state][0:7]) / 7
        tw = sum(new_cases[state][7:]) / 7
        try:
            diff = round(tw / lw * 100 - 100)
            print(
                f"{state} had a 7-day average of {round(tw)} and an increase of {diff}%."
            )
        except ZeroDivisionError:
            print(
                f"Last week and this weeks case averages in {state} were {round(lw)} and {round(tw)} respectively."
            )

    return


main()
