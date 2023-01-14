from tkinter import *
from functools import partial
from tkinter import messagebox

while True:
    try:
        n=input("Enter the first player name:")
        n1=input("Enter the second player name:")
        if n==n1:
            print("Try again you cant have same names")
            continue
        else:
            break
    except ValueError as e:
        print(e) 

sig = 0


global board
board = [[" " for x in range(3)] for y in range(3)]

def check_winner(b, l):
    if ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
        (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
        (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
        (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
        (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
        (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
        (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
        (b[0][2] == l and b[1][1] == l and b[2][0] == l)):
       
        if b[0][0] == l and b[0][1] == l and b[0][2] == l:
            button[0][0].config(bg="red")
            button[0][1].config(bg="red")
            button[0][2].config(bg="red")
        if b[1][0] == l and b[1][1] == l and b[1][2] == l:
            button[1][0].config(bg="red")
            button[1][1].config(bg="red")
            button[1][2].config(bg="red")
        if b[2][0] == l and b[2][1] == l and b[2][2] == l:
            button[2][0].config(bg="red")
            button[2][1].config(bg="red")
            button[2][2].config(bg="red")
        if b[0][0] == l and b[1][0] == l and b[2][0] == l:
            button[0][0].config(bg="red")
            button[1][0].config(bg="red")
            button[2][0].config(bg="red")
        if b[0][1] == l and b[1][1] == l and b[2][1] == l:
            button[0][1].config(bg="red")
            button[1][1].config(bg="red")
            button[2][1].config(bg="red")
        if b[0][2] == l and b[1][2] == l and b[2][2] == l:
            button[0][2].config(bg="red")
            button[1][2].config(bg="red")
            button[2][2].config(bg="red")
        if b[0][0] == l and b[1][1] == l and b[2][2] == l:
            button[0][0].config(bg="red")
            button[1][1].config(bg="red")
            button[2][2].config(bg="red")
        if b[0][2] == l and b[1][1] == l and b[2][0] == l:
            button[0][2].config(bg="red")
            button[1][1].config(bg="red")
            button[2][0].config(bg="red")         
        

def winner(b,l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))



def get_text(i, j, gb, l1, l2):
    global sig
    if board[i][j] == ' ':
        if sig % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = f"{n}"
   
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = f"{n1}"
        sig += 1
        button[i][j].config(text=board[i][j],bg='light gray')
    if winner(board, f"{n}"):
        check_winner(board,f"{n}")
        
        box = messagebox.showinfo("Winner", f"{n} won the match")
        
        
    elif winner(board, f"{n1}"):
        check_winner(board,f"{n1}")

        box = messagebox.showinfo("Winner", f"{n1} won the match")
    elif(isfull()):
        
        box = messagebox.showinfo("Tie Game", "Tie Game")

def isfree(i, j):
    return board[i][j] == " "




def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag


def gameboard_pl(game_board, l1, l2):
    wpl = partial(withplayer,game_board)
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=12)
            button[i][j].grid(row=m, column=n)

    reset_button = Button (game_board, text="Reset", command=wpl)
    reset_button.grid(row=0, column=0)

    game_board.mainloop()




def withplayer(game_board):
    global board
    board = [[" " for x in range(3)] for y in range(3)]
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    
    l1 = Button(game_board, text=f"Player 1: {n}", width=14,state=DISABLED)

    l1.grid(row=1, column=1)
    l2 = Button(game_board, text=f"Player 2: {n1}",
                width=14, state=DISABLED)
    
    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)


 
    play()


if __name__ == '__main__':
    men=Tk()
    withplayer(men)