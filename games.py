#Games to play.(pure cli only no pygame)
import os


def main():
    
    games = ["1.TIC TAC TOE"]
    print(r""" 
    __________________|      |____________________________________________
     ,--.    ,--.          ,--.   ,--.
    |oo  | _  \  `.       | oo | |  oo|
o  o|~~  |(_) /   ;       | ~~ | |  ~~|o  o  o  o  o  o  o  o  o  o  o
    |/\/\|   '._,'        |/\/\| |/\/\|
__________________        ____________________________________________
                  |      |
_______  _______  __   __  _______  _______ 
|       ||   _   ||  |_|  ||       ||       |
|    ___||  |_|  ||       ||    ___||  _____|
|   | __ |       ||       ||   |___ | |_____ 
|   ||  ||       ||       ||    ___||_____  |
|   |_| ||   _   || ||_|| ||   |___  _____| |
|_______||__| |__||_|   |_||_______||_______|""")
    print("Choose a Game: ")
    for i in games:
        print(i)
    choice = int(input(""))
    if(choice == 1):
        print("Welcome to tic tac toes!")
        tictac()
    else:
        print("Invalid choice!")

#Tic tac toe
class tictac:
    #Initalize variables.
    def __init__(self):
        self.grid = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
        self.gameover = False
        self.mainloop()

    def draw_grid(self):
        #Draws the grid
            for rows in range(3):
                for cols in range(3):

                    if(self.grid[rows][cols] == 1):
                        print("[O]",end=" ")
                    elif(self.grid[rows][cols] == 2):
                        print("[X]",end=" ")
                    elif(self.grid[rows][cols] == 0):
                        print("[ ]",end=" ")
                        
                    if(cols%3 == 2):
                        print("\n")
    #Check the grid to determine who wins.

    
    def check_grid(self):
            #Check each row 
            if(self.grid[0][0] == 1 and self.grid[0][1] == 1 and self.grid[0][2] == 1 or self.grid[0][0] == 2 and self.grid[0][1] == 2 and self.grid[0][2] == 2):
                    if(self.grid[0][0] == 1):
                        print("Player 1 wins")
                    elif(self.grid[0][0] == 2):
                        print("Player 2 wins")
                    os._exit(0)
                    self.gameover = True
            elif(self.grid[1][0] == 1 and self.grid[1][1] == 1 and self.grid[1][2] == 1 or self.grid[1][0] == 2 and self.grid[1][1] == 2 and self.grid[1][2] == 2):
                    if(self.grid[1][0] == 1):
                        print("Player 1 wins")
                    elif(self.grid[1][0] == 2):
                        print("Player 2 wins")
                    os._exit(0)
                    self.gameover = True
            elif(self.grid[2][0] == 1 and self.grid[2][1] == 1 and self.grid[2][2] == 1 or self.grid[2][0] == 2 and self.grid[2][1] == 2 and self.grid[2][2] == 2):
                    if(self.grid[2][0] == 1):
                        print("Player 1 wins")
                    elif(self.grid[2][0] == 2):
                        print("Player 2 wins")
                    os._exit(0)
                    self.gameover = True
            #Check each column
            if(self.grid[0][0] == 1 and self.grid[1][0] == 1 and self.grid[2][0] == 1 or self.grid[0][0] == 2 and self.grid[1][0] == 2 and self.grid[2][0] == 2):
                if(self.grid[0][0] == 1):
                    print("Player 1 wins")
                elif(self.grid[0][0] == 2):
                    print("Player 2 wins")
                os._exit(0)
                self.gameover = True
            elif(self.grid[0][1] == 1 and self.grid[1][1] == 1 and self.grid[2][1] == 1 or self.grid[0][1] == 2 and self.grid[1][1] == 2 and self.grid[2][1] == 2):
                if(self.grid[0][1] == 1):
                    print("Player 1 wins")
                elif(self.grid[0][1] == 2):
                    print("Player 2 wins")
                os._exit(0)
            elif(self.grid[0][2] == 1 and self.grid[1][2] == 1 and self.grid[2][2] == 1 or self.grid[0][2] == 2 and self.grid[1][2] == 2 and self.grid[2][2] == 2):
                if(self.grid[0][2] == 1):
                    print("Player 1 wins")
                elif(self.grid[0][2] == 2):
                    print("Player 2 wins")
                os._exit(0)
                self.gameover = True
            #Check diagonally
            if(self.grid[0][0] == 1 and self.grid[1][1] == 1 and self.grid[2][2] == 1 or self.grid[0][0] == 2 and self.grid[1][1] == 2 and self.grid[2][2] == 2):
                if(self.grid[0][0] == 1):
                    print("Player 1 wins")
                elif(self.grid[0][0] == 2):
                    print("Player 2 wins")
                self.gameover = True
                os._exit(0)
            elif(self.grid[0][2] == 1 and self.grid[1][1] == 1 and self.grid[2][0] == 1 or self.grid[0][2] == 2 and self.grid[1][1] == 2 and self.grid[2][0] == 2):
                if(self.grid[0][2] == 1):
                    print("Player 1 wins")
                elif(self.grid[0][2] == 2):
                    print("Player 2 wins")
                self.gameover = True
                os._exit(0)
                     
                     
                 
            

            

    #Mainloop
    def mainloop(self):
        while not self.gameover == True:
            #Get the user input.
            self.draw_grid()
            self.check_grid()
            self.p1x = int(input("Enter Player 1 x position(1-3): "))
            self.p1y = int(input("Enter Player 1 y position(1-3): "))   
            

            self.grid[self.p1y-1][self.p1x-1] = 1

            self.draw_grid()
            self.check_grid()
            self.p2x = int(input("Enter Player 2 x position(1-3): "))
            self.p2y = int(input("Enter Player 2 y position(1-3): "))
          
            self.grid[self.p2y-1][self.p2x-1] = 2

           




    


