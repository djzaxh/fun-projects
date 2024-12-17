try:
    favFoods = ["Sushi", "Burgers", "Tacos", "Manta", "Samsa"]
    i = 0
    addFood = input("What food do you want to add: ")
    favFoods.append(addFood)
    while i < len(favFoods):
        print(str(i) + ".", favFoods[i])
        i += 1
    choiceFood = input("Would you like to remove a food?(yes or no): ")
    if choiceFood != "yes" or "y":
        print("cya later")
    else:
        while True:
            delete = input("what food would you like to remove?(name): ")
            if delete in favFoods:
                favFoods.remove(delete)
                break
            else:
                print("enter vaild food")
            
        i = 0
        while i < len(favFoods):
            print(str(i) + ".", favFoods[i])
            i += 1
    if choiceFood == "yes":    
        while True:
            search = input("what food would you like to search for?: ")
            if search in favFoods:
                print(search, "is in this list")
            elif search == "exit":
                print("")
                break
            else:
                print(search, "is not in this list")
except KeyboardInterrupt:
    print("")

        