# functions go here
def string_check(question, valid_ans_list):
    """checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[0]:
                return item

        print(f"please choose an option from {valid_ans_list}")


# Main routine goes here
levels = ['easy', 'medium', 'hard']

like_coffe = string_check("Do you like coffe? ", ['yes', 'no'])
print(f"you chose {like_coffe}")
choose_level = string_check("chose a level: ", levels)
print(f"you chose {choose_level}")