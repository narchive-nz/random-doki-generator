import random

# ------------------------------------------------------------------------------
#array:
dokis = [
    "monika", "sayori", "natsuki", "yuri"
]

# ------------------------------------------------------------------------------
#question:
def yes_no(question):
    
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            print(random.choice(dokis), " (press enter to close)")
            input()
            break

        elif response == "no" or response == "n":
            print("what is WRONG with you? do you not like ddlc or something?  (press enter to close)")
            input()
            break

        else:
            print("you're literally stupid i said type Y")
            print()

# ------------------------------------------------------------------------------
#ask the user
yes_no("type Y to pick a doki: ")

