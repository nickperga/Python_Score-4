from functions import *

print("Welcome to my score-4 game")
print("Do you have any saved game that you wanna continue playing?y/n")  #Checks if there is another existing game file
ans = input()
while(ans.lower() != 'y' and ans.lower() != 'n'): #Assures that the input given is valid
    ans = input("Wrong answer. Please try again!")
if(ans.lower() == 'n'):
    rows = int(input("Enter the number of rows you want on the board: "))  #If there is no previous game then user has to give the number of rows and lines of his table and my function creates the game table
    lines = int(input("Enter the number of lines you want on the board: "))
    table = create_table(rows, lines)

    empty_line = [lines - 1] * rows
    player_1_score = 0
    player_2_score = 0
    won = False
    full = False

else:
    print("Please give a valid file name.")
    f_name = input()  #If there is a previous game then the function below takes the csv file and extracts all of its information to format the game
    rows, lines, table, player_1_score, player_2_score, empty_line = CSV_to_Table(f_name) 
    won = False
    full = isFull(table)
 

player_1 = False
counter = 1

while((not won) and (not full)):
    if(not isFull(table)):
        if(player_1 == False):
            won = Player_plays(1, empty_line, table, lines, rows, counter)

            player_1 = True
        else:
            won = Player_plays(2, empty_line, table, lines, rows, counter)

            player_1 = False
    else:
        ans = input("Table is full. Wanna start a new game? y/n")
        while(ans.lower() != 'y' and ans.lower() != 'n'):
            ans = input("Wrong answer. Please try again!")
        if(ans.lower() == "y"):
            table = create_table(rows, lines)
        else:
            full = True

    if(won == True):
        if(player_1):
            print("Player 1 won the game. Congratulations!") #If a player wins the current game it asks if they want to continue playing
            player_1_score += 1
            answer = input("Want a new game to start?y/n")
            while(answer.lower() != 'y' and answer.lower() != 'n'):
                answer = input("Wrong answer. Please try again!")
            if(answer.lower() == 'y'):
                rows = int(input("Enter the number of rows you want on the board: "))
                lines = int(input("Enter the number of lines you want on the board: "))
                table = create_table(rows, lines)
                won = False
            else:
                print("Game ended with final score " + player_1_score + " for player 1 and " + player_2_score + " for player 2")

        else:
            print("Player 2 won the game. Congratulations!")
            player_2_score += 1
            answer = input("Want a new game to start?y/n")
            while(answer.lower() != 'y' and answer.lower() != 'n'):
                answer = input("Wrong answer. Please try again!")
            if(answer.lower() == 'y'):
                rows = int(input("Enter the number of rows you want on the board: "))
                lines = int(input("Enter the number of lines you want on the board: "))
                table = create_table(rows, lines)
                won = False
            else:
                print("Game ended with final score " + player_1_score + " for player 1 and " + player_2_score + " for player 2")
    
    if(player_1 == False): #After each turn the program asks the players if they want to continue playing or they want to save the current state of the game as a csv
        print("Will you continue the game?y/n")
        ans = input()
        while(ans.lower() != 'y' and ans.lower() != 'n'):
            ans = input("Wrong answer. Please try again!")
        if(ans.lower() == 'n'):
            print("Type the name that you want to give to your file.")
            f_name = input()
            Table_to_CSV(table, rows, f_name, player_1_score, player_2_score, empty_line)
            print("Your game has been saved.")
            break
    counter += 1


      

print("Game ended!")