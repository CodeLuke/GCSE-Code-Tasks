# An adventure game
health = 10
enemy = 10
gold = 0
strength = 1
rat = False
bear = False
skeleton = False
from random import randint
from time import sleep
inventory = []
newinventory = ""

def healthbar():                                                            #prints status bar
    global health, gold, strength, inventory

    print("-----------------------------------------------------------------------------------")
    print("You have",health,"HP",gold,"gold and in your inventory is: ", ", ".join(inventory))
    print("-----------------------------------------------------------------------------------")


def loseHP(hp,message):                   #removes health from player along with a message 
    global health,strength
    print(message)
    health = health - hp
    if health <= 0:
        print("                                          YOU DID NOT SUCCEED!GAME OVER!")
        sleep(1)
        print("YOU HAVE LOST ALL YOUR HP")
        gameover()

    else:
        print("                                          Your health is now",health,"HP")


def pos_check():                       #Checks where the player is through the game in order to put them there after an attacj
    global rat, bear, skeleton
    if rat == False:
        rat = True
        room3()
    elif bear == False:
        bear = True
        room6()
    elif skeleton == False:
        skeleton = True
        room9()


def question():             #asks the player how they want to attack the enemy
    global enemy
    if enemy == 0:
        enemy = 15
    if "sword" in inventory:                            
        answer = input("Attack,Dodge or Slash? ")      #If there is a sword in the player's inventory then they can use SLASH
        if answer.lower() == "attack":
            attack()
        elif answer.lower() == "dodge":
            block()
        elif answer.lower() == "slash":
            slash()
        
    else:
        answer = input("Attack or Dodge? ")
        if answer.lower() == "attack":
            attack()
        elif answer.lower() == "dodge":
            block()
        else:
            print("Not a valid response")
            question()


def enemyattack():                              #Controls enemy's damage (base damage * strength stat of that enemy
    global enemy
    global strength
    sleep(1)
    print("                                          Your enemy is now attacking")
    y = randint(1,6)
    sleep(1)
    if y == 1:
        print("                                          Your enemy missed")
        question()
    elif y == 2 or y == 3:
        loseHP(2*strength,"                                          Critical Damage!You have lost " + str(2 * strength )+"HP")
                                                                                     # converts formula's output into a string
         
    else:
        loseHP(1*strength,"                                          Hit! You lose " + str(1* strength) +"HP")
    question()

def attack():                                   #Controls damage of the move ATTACK
    global enemy
    global room9
    x = randint(1,8)
    if x == 1:
        sleep(1)
        print("You missed, no damage is done")
        sleep(1)
        print("Your enemy's health is still",enemy,"HP")
        sleep(2)
        enemyattack()
    elif x == 2 or x == 3:
        sleep(1)
        print("Critical hit +4DMG to your enemy")
        enemy = enemy - 4
        print("Your enemy's health is now",enemy, "HP")
        if enemy <= 0:
            sleep(1)
            print("You killed it!")
            pos_check()
            
        else:
            sleep(1)
            enemyattack()
    else:
        print("You hit! +2DMG to your enemy")
        enemy = enemy - 2
        print("Your enemy's health is now",enemy,"HP")
        if enemy <= 0:
            print("You killed it!")
            pos_check()
                
        else:
            sleep(1)
            enemyattack()



def block():                                    #Controls effectiveness of the move BLOCK
    blk = randint(1,4)
    if blk < 3:
        sleep(1)
        print("Successful Dodge! Your enemy couldn't attack you")
        question()
    elif blk >= 3:
        sleep(1)
        print("Dodge Failed!")
        enemyattack()


def slash():                                    #Controls effectivenes of move SLASH
    global enemy
    global bear,rat,skeleton
    x = randint(1,8)
    if x == 1:
        sleep(1)
        print("You missed, no damage is done")
        sleep(2)
        print("Your enemy's health is still",enemy, "HP")
        enemyattack()
    elif x == 2 or x == 3:
        sleep(1)
        print("Critical hit +6DMG to your enemy")
        enemy = enemy - 6
        sleep(1)
        print("Your enemy's health is now",enemy,"HP")
        if enemy <= 0:
            sleep(1)
            print("You killed it!")
            pos_check()
        else:
            sleep(1)
            enemyattack()
    else:
        sleep(1)
        print("You hit! +3DMG to your enemy")
        enemy = enemy -3
        print("Your enemy's health is now",enemy,"HP")
        if enemy <= 0:
            sleep(1)
            print("You killed it!")
            pos_check()
        else:
            sleep(1)
            enemyattack() 


    



def room1():                            #First Room
    global enemy
    print("------------")
    print("+ The Cave +")
    print("------------")
    print("You have entered a dark and desolate cave, a landslide has blocked the exit")
    sleep(.5)
    print("A.Go forward,who knows what lies ahead?")
    sleep(.5)
    print("B.Try as hard as possible to get out")
    sleep(.5)
    
    answer = input("What is your decision? ")
    if answer.lower() == "a":
        room2()
    elif answer.lower() == "b":
        loseHP(10,"Resistance is futile,you have wasted your energy,-10HP")
    else:
        print("Not a valid response")
        room1()


def room2():                        #Second Room
    global enemy
    enemy = 10
    print("A creature?")
    sleep(1)
    print("You see a small rat(1 strength) ahead,harmles but it has to be dealt with")
    sleep(2)
    print("               _..----.._    _")
    print("             .'  .--.    '-.(0)_")
    print(" '-.__.-'''=:|   ,  _)_ \__ . c\'-..")
    print("              '''------'---''---'-")
    sleep(3)
    print("You have 2 options Attack or Dodge")
    sleep(1)
    question()











def room3():            #Room 3
    print("-----------------------------------------------------------------------")
    if not "sword" in inventory:
        print("You enter a small corridor,Ahead is a trap door and to your right")
        print("Is an old ladder")
        answer = input("Ladder or Door? ")
        if answer.lower() == "ladder":
            ladder1()
        elif answer.lower() == "door":
            room4()
        else:
            print("Not a valid response")
            sleep(4)
            room3()
    else:
        sleep(2)
        print("You climb back down the ladder and go through the trap door")
        sleep(2)
        room4()





def ladder1():
    global inventory
    print("-------------------------------------------------------------------------")
    print("You find yourself in an attic, nothing is here except a sword")
    answer = input("Do you want to pick it up, yes or no ")
    if answer.lower() == "yes":
        print("You pick up the sword, you have learned SLASH")
        sleep(1)
        print("You strut back to the corridor feeling mightier than ever")
        sleep(1)
        inventory.append("sword")
        room3()
    elif answer.lower() == "no":
        sleep(1)
        print("The sword is left untouched and you retreat back to the corridor")
        room3()
    else:
        print("Not a valid response")
        ladder1()





def room4():        #room 4
    global health
    global inventory
    global gold
    if "sword" in inventory:
        healthbar()
    else:
        print("-----------------------------------------------------------------------------------")
        print("You have",health,"HP and in your inventory is nothing")
        print("-----------------------------------------------------------------------------------")
        
    sleep(2)
    print("You fall down but a magical cloud cushions your fall and heals you +10HP")
    health = health + 10
    sleep(2)
    print("You hear crunching under the soles of your feet,the skeletal remains of")
    sleep(3)
    print("past adventurers litter your vision,one has an old leather rucksack with worn straps")
    sleep(3)
    print("Would you like to take the rucksack")
    question1()







def question1(): #used as a checkpoint if the user inputs an invalid response
    global health
    global inventory
    global gold
    answer = input("Yes or No? ")
    if answer.lower() == "yes":
        print("You have found a ring of healing(+10HP),a rotten apple and 3 gold")
        health = health + 10
        inventory.append("ring of healing(+10HP)")
        inventory.append("a rotten apple")
        gold = gold + 3
        sleep(1)
        print("You continue on your journey,oblivious to how you will get out")
        room5()
    elif answer.lower() == "no":
        print("You can't help but think something may have been in there and continue along your journey")
        sleep(1)
        room5()
    else:
        print("not a valid response")
        sleep(1)
        question1() #resets back to the question rather than the beginning of room 4 to stop 10HP being added every time
        







def room5():
    global inventory, strength, enemy, bear
    healthbar() 
   
    sleep(3)
    print("A bear (1.5 strength) walks forward out of the shadows,it looks hungry")
    sleep(2)
    
    print("""
.'''.        ___,,,___        .'``."
: (\  `.'''```         ```'''-'  /) ;
 :  \                         `./  .'
  `.                            :.'
    /        _         _        \ 
   |         0}       {0         |
   |         /         \         |
   |        /           \        |
   |       /             \       |
    \     |      .-.      |     /
     `.   | . . /   \ . . |   .'
       `-._\.'.(     ).'./_.-'
           `\'  `._.'  '/'
             `. --'-- .'
               `-...-'""")

    if "a rotten apple" in inventory:                       #If the player has an apple then it can poison it
        sleep(3)
        print("You throw the rotten apple and luckily it is stupid enough to fall for your trap")
        bear = True
        sleep(3)
        inventory.remove("a rotten apple")        #removes apple from the player's inventory
          
        
        print("It dies and you are left with 1 less apple")
        room6()
    else:
        enemy = 15
        strength = 1.5
        question()
        





def room6():             #Room 6
    healthbar()
    print("You are shaken after the encounter with the bear,")
    sleep(2)
    print("You waddle around,regretting your decision to stay here")
    sleep(1)
    print("You continue down your path with little to no hope of escaping")
    sleep(2)
    print("SHRIEK")
    sleep(1)
    print("*shudder*")
    room7()


def room7():       #Room 7
    global inventory
    global health
    healthbar()
    print("You see a man lying on the floor")
    sleep(2)
    print("the light is flickering too much to see his face but you faintly here deathly groans")
    sleep(2)
    answer = input("Do you want to approach the figure? Yes or No ")
    if answer.lower() == "yes":
        print("The man welcomes you and is grateful for your kindness")
        inventory.append("a friend")
        sleep(2)
        room8()
    elif answer.lower() == "no":
        print("You leave the man where he lies")
        sleep(2)
        room8()
    else:
        print("Not a Valid Response")
        sleep(2)
        room7()


def room8():     #Room8
    healthbar()
    global enemy
    global strength
    global health
    print("You have been travelling and feel worn out")
    sleep(2)
    print("You begin")
    sleep(2)
    print("to feel")
    sleep(2)
    print("Tired")
    sleep(3)
    print("ZzZzZzZzZzZzZzZzZzZ")
    sleep(4)
    enemy = 20
    if "a friend" in inventory:
        print("You are awoken by your friend")
        sleep(2)
        print("He screams at you and at the corner of your eye you see")
        sleep(2)
        print("a large skeleton with a sword in his hand")
        sleep(2)
        question()
    else:
        sleep(2)
        loseHP(3,"You are caught off guard by a sword wielding skeleton and lose 3HP")
        sleep(2)
        question()

def room9():        #Room9
    sleep(1)
    sleep(3)
    print("You stumble forward,barely able to walk")
    sleep(2)
    print("You find a map")
    sleep(2)
    print("It reads...")
    sleep(2)
    print("YOU ARE LOST")
    sleep(2)
    print("It doesn't help you")
    sleep(2)
    endchoice()
        




def endchoice():   #the player's final choice
    healthbar()
    sleep(1)
    print("You see a light up ahead, a golden glow shines below you,but you see")
    sleep(2)
    print("sunlight above you")
    sleep(1)
    print("It could be your only way out but enough gold to last a lifetime lies below")
    sleep(3)
    print("It's your choice")
    sleep(1)
    print("A.Go lay claim to the riches that lie below")
    sleep(1)
    print("B.Leave the gold and escape back to your miserable life")
    answer = input("It's your choice ")
    if answer.lower() == "a":
        print("You frolick in your fortune and lay claim to millions")
        sleep(1)
        print("Congratulations! You now are a millionaire")
        sleep(3)
        print("However")
        sleep(2)
        print("You Grap the gold,filling your pockets when you trip over")
        sleep(1)
        print("an old lever on the floor, everything seems OK unitil you")
        sleep(1)
        print("see the entrance blocked,you are trapped")
        sleep(1)
        print("But hey, at least you've got all that gold")
        sleep(1)
        badending()
    elif answer.lower() == "b":
        print("You escape, the cave crashes down behind you")
        sleep(2)
        print("Thankfully you got out of there in time")
        sleep(2)
        print("You leave the cave not entirely sure how you got there")
        sleep(2)
        print("or what happpened")
        goodending()

    else:
        print("Not a Valid Respnse")
        endchoice()






def goodending():
    print("                              _")
    print("                    .-.      / \        _")
    print("        ^^         /   \    /^./\__   _/ \   ")
    print("      _        .--'\/\_ \__/.      \ /    \  ^^  ___")
    print("        / \_    _/ ^      \/  __  :'   /\/\  /\  __/   \    ")
    print("       /    \  /    .'   _/  /  \   ^ /    \/  \/ .`'\_/\   ")
    print("      /\/\  /\/ :' __  ^/  ^/    `--./.'  ^  `-.\ _    _:\ _")
    print("     /    \/  \  _/  \-' __/.' ^ _   \_   .'\   _/ \ .  __/ \   ")
    print("    /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  ^  \  ")
    print("   /  `-.__ ^   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.")
    print(" @/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \   %")
    print(" @(88%@)@%% @)&@&(88&@.-_=_-=_-=_-=_-=_.8@% &@&&8(8%@%8)(8@%8 8%@)%")
    print("@88:::&(&8&&8::JGS:&`.~-_~~-~~_~-~_~-~~=.'@(&%::::%@8&8)::&#@8::::")
    print("`::::::8%@@%:::::@%&8:`.=~~-.~~-.~~=..~'8::::::::&@8:::::&8::::::'")
    print("  `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'")
    credit()








def badending():

    print("           ;               ,           ")
    sleep(.5)
    print("         ,;                 '.         ")
    sleep(.5)
    print("        ;:                   :;        ")
    sleep(.5)
    print("       ::                     ::      ")
    sleep(.5)
    print("       ::                     ::      ")
    sleep(.5)
    print("       ':                     :       ")
    sleep(.5)
    print("      :.                    :         ")
    sleep(.5)
    print("    ;' ::                   ::  '     ")
    sleep(.5)
    print("    .'  ';                   ;'  '.     ")
    sleep(.5)
    print("   ::    :;                 ;:    ::   ")
    sleep(.5)
    print("   ;      :;.             ,;:     ::   ")
    sleep(.5)
    print("   :;      :;:           ,;'      ::   ")
    sleep(.5)
    print("   ::.      ':;  ..,.;  ;:'     ,.;:   ")
    sleep(.5)
    print("    '''...   '::,::::: ;:   .;.;'''    ")
    sleep(.5)
    print("        ''''....;:::::;,;.;'''         ")
    sleep(.5)
    print("    .:::.....''':::::::'',...;::::;.   ")
    sleep(.5)
    print("   ;:' '''''';.,;:::::;.'''''''  ':;   ")
    sleep(.5)
    print("  ::'         ;::;:::;::..         :;   ")
    sleep(.5)
    print(" ::         ,;:::::::::::;:..       :: ")
    sleep(.5)
    print(" ;'     ,;;:;::::::::::::::;';..    ':. ")
    sleep(.5)
    print("::     ;:  ::::::''''::::::  ':     :: ")
    sleep(.5)
    print(" :.    ::   ::::::;  :::::::   :     ; ")
    sleep(.5)
    print("  ;    ::   :::::::  :::::::   :    ;   ")
    sleep(.5)
    print("   '   ::   ::::::....:::::'  ,:   '   ")
    sleep(.5)
    print("    '  ::    :::::::::::::'   ::       ")
    sleep(.5)
    print("       ::     ':::::::::''    ::       ")
    sleep(.5)
    print("       ':       ''''''''      ::       ")
    sleep(.5)
    print("        ::                   ;:         ")
    sleep(.5)
    print("        ':;                 ;:'         ")
    sleep(.5)
    print("          ';              ,;'           ")
    sleep(.5)
    print("            ''           ''             ")
    sleep(.5)
    print("              ' '")
    sleep(2)
    gameover()





def gameover():
    print("  ________                        ________                     ")
    sleep(.5)
    print(" /  _____/_____    _____   ____   \_____  \___  __ ___________ ")
    sleep(.5)
    print("/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \ ")
    sleep(.5)
    print("\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/")
    sleep(.5)
    print(" \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|   ")
    sleep(.5)
    print("        \/     \/      \/     \/          \/          \/        ")
    sleep(3)
    credit()






def credit():
    print("Credits:")
    sleep(2)
    print("ASCII Art - ascii.com")
    sleep(1)
    print("Programming - Luke B")
    sleep(1)
    print("ASCII Text - Luke B")
    print("---------------------")
    print("       TESTERS       ")
    print("+Isaac         +Calum")
    print("+Matt A")
    print("---------------------")
    sleep(2)
    print("        |   |           |                    ,-               |         o         ")
    print("        |-  |-. ,-: ;-. | ,   . . ,-. . .    |  ,-. ;-.   ;-. | ,-: . . . ;-. ,-: ")
    print("        |   | | | | | | |<    | | | | | |    |- | | |     | | | | | | | | | | | | ")
    print("        `-' ' ' `-` ' ' ' `   `-| `-' `-`    |  `-' '     |-' ' `-` `-| ' ' ' `-| ")
    print("                              `-'           -'            '         `-'       `-'    ")
    

    sleep(10)
    quit()


# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    room1()
