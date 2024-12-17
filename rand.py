import random

try:
    def randum(x, y):
        return random.randint(x, y)

    def doAgain():
        while True:
            userValue = None
            userChoice = input("Do you want to generate a new random number?(y or n) ").lower()
            if userChoice == "y":
                userValue = True
            elif userChoice == "n":
                userValue = False
            else:
                print("Invalid input. exiting")
                break
            return userValue

    def parse(user_input):
        try:
            x, y = user_input.split(":")
            x = int(x.strip())  
            y = int(y.strip()) 
            return randum(x, y)
        except ValueError:
            print("Invalid input format. Please enter in the format x : y.")
            return None

    while True:
        userRange = input("Enter the range of the random number (x : y): ")
        
        parsedrand = parse(userRange)
        print(parsedrand)
        
        d = doAgain()
        if not d:
            print("\n")
            break
except KeyboardInterrupt:
    print("")