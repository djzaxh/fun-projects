import time
import sys
import random

class Game:
    def __init__(self):
        self.health = 100
        self.lord_health = 100 

    def intro(self):
        self.loading_animation(5)
        ascii = [r"""
                                                ,----,                               
                                            ,/   .`|                               
            ,---,                            ,`   .'  :                       ___     
        .'  .' `\                        ;    ;     /                     ,--.'|_   
        ,---.'     \                     .'___,/    ,'                      |  | :,'  
        |   |  .`\  |            .--.--. |    :     |           ,--,  ,--,  :  : ' :  
        :   : |  '  |      .--, /  /    ';    |.';  ;   ,---.   |'. \/ .`|.;__,'  /   
        |   ' '  ;  :    /_ ./||  :  /`./`----'  |  |  /     \  '  \/  / ;|  |   |    
        '   | ;  .  | , ' , ' :|  :  ;_      '   :  ; /    /  |  \  \.' / :__,'| :    
        |   | :  |  '/___/ \: | \  \    `.   |   |  '.    ' / |   \  ;  ;   '  : |__  
        '   : | /  ;  .  \  ' |  `----.   \  '   :  |'   ;   /|  / \  \  \  |  | '.'| 
        |   | '` ,/    \  ;   : /  /`--'  /  ;   |.' '   |  / |./__;   ;  \ ;  :    ; 
        ;   :  .'       \  \  ;'--'.     /   '---'   |   :    ||   :/\  \ ; |  ,   /  
        |   ,.'          :  \  \ `--'---'             \   \  / `---'  `--`   ---`-'   
        '---'             \  ' ;                       `----'                         
                        `--`                                                       
            
        """]
        print(ascii[0])
        print("Welcome to DysText!")
        time.sleep(2)
        print("You are in a Dystopian city trying to stop Lord Malevok before he destroys the city.")
        time.sleep(2)
        print("To exit press ctrl-c or cmd-c to exit.")
        time.sleep(2)
        self.health_bar()
        time.sleep(2)
        print("Your objective is to stop Lord Malevok and get to 1000 health points.")

    def building_scenario(self):
        attempts = 2  
        opt1 = self.randomnum(200, 500)
        opt2 = self.randomnum(800, 1000)
        opt3 = self.randomnum(200, 500)
            
        print("You need to get to the top floor of the biggest tower")
        time.sleep(2)
        print("There are 3 towers that you have decided are the tallest. You know the heights but they are in different measurements!")
        time.sleep(2)
        print("You have to convert them to one measurement so you can determine which is the tallest.")
        time.sleep(2)
        for attempt in range(attempts): 
            print(f"Your options are {opt1} m, {opt2} ft, and {opt3} m")
            userInput = input("Which one is the right one, '1', '2' or '3'? ")
            
            correct_option = 1 if opt1 > (opt2 * 0.3048) and opt1 > opt3 else (2 if opt2 > (opt1 * 3.28084) and opt2 > opt3 else 3)
            
            if userInput == str(correct_option):
                print("You are right!")
                time.sleep(2)
                self.choose_path()
                break
            else:
                remaining_attempts = attempts - attempt - 1 
                print(f"Sorry, you're wrong. You have {remaining_attempts} attempt(s) left.")
                time.sleep(0.5)
                if remaining_attempts == 0: 
                    print("GAME OVER!")
    
    def choose_path(self):
        print("You approach the entrance to the tower.")
        time.sleep(2)
        print("You can either take the stairs or the elevator to the top floor.")
        time.sleep(2)

        while True:
            choice = input("Do you want to take the 'stairs' or the 'elevator'? ").lower()
            if choice == "stairs":
                print("You decided to take the stairs. It will take you longer!")
                self.stairs_animation()
                print("You finally reach the top floor, panting and out of breath.")
                self.fight_lord_malevok()
                break
            elif choice == "elevator":
                print("You decided to take the elevator. It will be faster!")
                self.elevator_animation()
                print("The elevator dings and you arrive smoothly at the top floor.")
                self.fight_lord_malevok()
                break
            else:
                print("Invalid choice. Please choose 'stairs' or 'elevator'.")

    def fight_lord_malevok(self):
        print("You have encountered Lord Malevok!")
        time.sleep(2)
        print("If you kill him you win!")
        time.sleep(2)
        print("If you don't kill him, you will die!")
        time.sleep(2)
        print("What weapon would you like?")
        time.sleep(0.5)

        weapons = {
            'sword': {'damage': 30, 'speed': 1},    
            'crossbow': {'damage': 20, 'speed': 2},  
            'bare hands': {'damage': 10, 'speed': 3} 
        }

        weaponChoice = input("Your options are: sword, crossbow, or bare hands: ").lower()

        if weaponChoice not in weapons:
            print("Invalid choice! You have no weapon.")
            return
        
        player_damage = weapons[weaponChoice]['damage']
        player_speed = weapons[weaponChoice]['speed']
        
        while self.health > 0 and self.lord_health > 0:
            player_strikes = self.randomnum(1, player_speed + 1)
            for _ in range(player_strikes):
                self.lord_health -= player_damage
                print(f"You strike Lord Malevok for {player_damage} damage! Lord Malevok's health is now {self.lord_health}.")
                time.sleep(4)
                if self.lord_health <= 0:
                    print("You defeated Lord Malevok! You win!")
                    return

            lord_damage = 40 
            self.health -= lord_damage
            print(f"Lord Malevok strikes you for {lord_damage} damage! Your health is now {self.health}.")
            time.sleep(1) 

            if self.health <= 0:
                print("You have been defeated by Lord Malevok! GAME OVER!")

    def loading_animation(self, duration):
        spinner = ['|', '/', '-', '\\']
        end_time = time.time() + duration
        idx = 0

        while time.time() < end_time:
            sys.stdout.write(f'\rLoading... {spinner[idx % len(spinner)]}')
            sys.stdout.flush()
            idx += 1
            time.sleep(0.1) 

        sys.stdout.write('\rLoading...\n')
    def stairs_animation(self):
        print("Starting to climb the stairs...")
        for i in range(1, 71): 
            time.sleep(0.27)
            print(f"Climbing step {i}...")
        print("You reach the top of the stairs, slightly out of breath.")
    
    def elevator_animation(self):
        print("Entering the elevator...")
        time.sleep(1) 
        print("Closing the doors...")
        time.sleep(1) 
        print("Going up...")
        for i in range(1, 26):
            time.sleep(0.2)
            print(f"Passing floor {i}...")
        print("Ding! You arrive at the top floor.")
    

    def health_bar(self):
        print(f"Your health is {self.health}.")

    def randomnum(self, x, y):
        return random.randint(x, y)
    
game_instance = Game()
try:
    game_instance.intro()
    time.sleep(2)
    game_instance.building_scenario()
except KeyboardInterrupt:
    print("\nGame exited. Thanks for playing!")
    sys.exit(0)