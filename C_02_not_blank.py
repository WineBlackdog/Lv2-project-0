def not_blank(question):
    """checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("sorry, this cant be blank. please try and again.\n")


# main routine starts here
who = not_blank("please enter your name: ")
print(f"hello {who}")
