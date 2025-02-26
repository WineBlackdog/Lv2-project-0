# functions go here...
def yes_no(question):
    """checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes (y) or no (n).\n")


# Main routine goes here

# loop for testing purpose...
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"you chose {want_instructions}\n")
