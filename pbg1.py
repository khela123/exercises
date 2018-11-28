import random
pc=["Papel", "Gunting", "Bato"]
user=["Papel","Gunting","Bato"]

#user=none

def function():
    userScore=0
    pcScore=0;

    while pcScore <3 and userScore <3:
        print("Game options: (P)apel, (G)unting, (B)ato")
          
        inputchoice= input("Enter your choice: ")
        p=0
        g=1
        b=2

        if inputchoice in ("p", "P"):
            tempuser=user[p]
            print("Your choice: ",  user[p])

        elif inputchoice in("g", "G"):
            tempuser= user[g]
            print("Your choice: ",user[g])

        elif inputchoice in ("b", "B"):
            tempuser=user[b]
            print("Your choice: ",user[g])

        else:
            print("Invalid Input")
            continue;
        
        pcinput=random.randint(0, 2)
        print("Pc choice is: ",pc[pcinput])

        if pc[pcinput] == tempuser:
            print("Draw!")

        elif pc[pcinput] == "Gunting":
            if tempuser == "Bato":
                print("Player wins!")
                userScore=userScore+1
            else:
                print("PC wins!")
                pcScore=pcScore+1

        elif pc[pcinput] == "Bato":
            if tempuser == "Papel":
                print("Player wins!")
                userScore=userScore+1
            else:
                print("PC wins")
                pcScore=pcScore+1

        elif pc[pcinput] == "Papel":
            if tempuser == "Gunting":
                print("Player wins!")
                userScore=userScore+1
            else:
                print("PC wins!")
                pcScore=pcScore+1

        else:
            print("Invalid")

        print("User wins: ",userScore , end= '')
        print("PC wins: ",pcScore)

        if pcScore < userScore:
            print("You are the ultimate PGB Master!")
        else:
            print("Computer Wins!")
function()
