from random import choice

choices = ["R", "P", "S"]

choicesDict = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

print("*****************ROCK PAPER SCISSORS****************")
print("choices: R(Rock), P(Paper), S(Scissors)")
print("press q to quit")


def program(userChoice: str, cpuChoice: str) -> str:
    if userChoice.isnumeric():
        return "Please enter a valid choice"
    elif userChoice == cpuChoice:
        return "It's a tie"
    elif userChoice == "R":
        return "You win" if cpuChoice == "S" else "You Lose"
    elif userChoice == "P":
        return "You win" if cpuChoice == "R" else "You Lose"
    elif userChoice == "S":
        return "You win" if cpuChoice == "P" else "You Lose"
    else:
        return "please enter a valid choice"


while True:
    userChoice = input("Make a choice: ")
    userChoice = userChoice.upper()
    cpuChoice = choice(choices)

    if userChoice.lower() == "q":
        break
    elif not userChoice:
        print("Please enter a value")
        continue

    print("user: {} :: cpu: {}".format(
        choicesDict[userChoice], choicesDict[cpuChoice]))
    output = program(userChoice=userChoice, cpuChoice=cpuChoice)
    print(output)

    if output == "You win" or output == "You Lose":
        break
