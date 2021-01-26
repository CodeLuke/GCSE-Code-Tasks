# Our quiz!

from time import sleep
score = 0
name = input("What is your name?")
player = 0
def quiz():
    question1()
def question1():
    global name
    global player
    print("Hello",name,"welcome to a very british quiz , Huzzah!")
    print("Quiz starting in")
    sleep(0.5)
    print(5)
    sleep(0.5)
    print(4)
    sleep(0.5)
    print(3)
    sleep(0.5)
    print(2)
    sleep(0.5)
    print(1)
    sleep(0.5)
    print("*insert epic theme here*")
    print("Q1. Which biscuit is best with tea?")
    sleep(0.5)
    print("A.Jammie Dodger")
    sleep(0.5)
    print("B.Rich Tea")
    sleep(0.5)
    print("C.Bourbons")
    sleep(0.5)
    print("D.Custard Cream")
    sleep(0.5)
    answer = input("What is best?")
    if answer.lower() == "a":
        print("Wrong!Who wants jam in their tea")
    elif answer.lower() == "b":
        print("Wrong!They don't fit inside a mug *sigh*")
    elif answer.lower() == "c":
        print("Acceptable but not optimal + 50pts")
        player = player + 50
    elif answer.lower() == "d":
        ("Good Choice +100pts")
        player = player + 100
    else:
        print("Not a valid answer")
    print("Your current score is",player)
    question2()

def question2():
    global name
    global player    
    print("-----------------------------------------------------------------")
    sleep(0.5)
    print("On a scale of 1 to 10")
    sleep(1)
    answer = input("How successful is this quiz? ")
    if answer > "5":
        sleep(2)
        print("Nice to know!")
        player = player + 100
        question3()
        
    elif answer == "5":
        sleep(2)
        print("Bit harsh but ok")
        question3()
        player = player + 50
    elif answer < "5":
        sleep(2)
        print("Come on! Thats quite low")
        question3()
    else:
        print("Not valid")
        question2()

def question3():
    global name
    global player
    print("Do you that",name,"is a good name? ")
    print("A.Yes ")
    answer = input("B.No ")
    if answer.lower() == "yes":
        print("I agree +100pts")
        player = player + 100
        sleep(2)
        end()
    elif answer.lower() == "no":
        print("I agree +100pts")
        player = player + 100
        sleep(2)
        end()

def end():
    print("That's it! You scored",player,"pts")
    sleep(4)
    quit()

    
        
    
    
    
    





# Leave this at the bottom - it makes quiz run automatically when you
# run your code.
if __name__ == "__main__":
    quiz()
