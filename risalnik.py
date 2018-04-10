from tkinter import *
from sudoku import *


def preveriEnakost():
    '''preveri pravilnost sudokuja: potrebno narediti pop-out window s podobnim izpisom'''
    if sudoku.preveriEnakost():
        print("Cestitamo resili ste sudoku pravilno")
    else:
        print ("poskusite se enkrat")

def btnCommand(row, col, x,tabBarv,matrika):
    '''pritisk na gumb'''
    if tabBarv[row][col]=="red":
        if x==" ":
            x=0
        if x < 9:
            x = x + 1
        else:
            x = 0
        sudoku.trenutniSudoku[row][col] = x
        matrika[row][col].configure(text=x)
        createGrid(tabBarv)

def tabela_barv(sudoku):
    '''ustvari tabelo barv za mrezo gumbov'''
    tabelaBarv=[["black"] * 9 for i in range(9)]
    for vrstica in range(9):
        for stolpec in range(9):
            if sudoku.nedSodoku[vrstica][stolpec]==0:
                tabelaBarv[vrstica][stolpec]="red"
    return tabelaBarv

def nastavitevTezavnosti(tezavnost):
    '''nastavi tezavnost sudokuja in ga resetira'''
    sudoku.nastaviTezavnost(tezavnost)
    tabBarv = tabela_barv(sudoku)
    createGrid(tabBarv)


def createGrid(tabBarv):
    '''ustvari mrezo gumbov se poprej pa pobrise stare gumbe'''
    i=0
    #brisanje prej ustvarjenih gumbov
    for gumb in frame.winfo_children():
        if i>0:
            gumb.destroy()
        i+=1
    matrika = []
    #generiranje novih gumbov
    for rowindex in range(9):
        vrstica = []
        for colindex in range(9):
            #barvane ozadja gumba
            if (rowindex in (0, 1, 2, 6, 7, 8) and colindex in (3, 4, 5) or \
                        (rowindex in (3, 4, 5) and colindex in (0, 1, 2, 6, 7, 8))):
                colour = "light blue"
            else:
                colour = "white"

            #nastavitev vredonsti
            x = sudoku.trenutniSudoku[rowindex][colindex]
            if x==0:
                x=" "
            btn = Button(frame,font=("Helvetica",12), width=8, height=4, bg=colour, text=x, fg=tabBarv[rowindex][colindex],
                         command=lambda row=rowindex, col=colindex, x=x,: btnCommand(row, col, x,tabBarv,matrika))
            btn.grid(row=rowindex, column=colindex, sticky=N + S + E + W)
            vrstica.append(btn)
        matrika.append(vrstica)


frame = Tk()
menu = Menu(frame)
file = Menu(menu)
sudoku=Sudoku()
sudoku.generiraj(20,False)
#narediti je potrebno delujoce izbire trenutno to ne dela
file.add_command(label="Exit", command=frame.quit)
file.add_command(label="Tezka tezavnostnja stopnja", command=nastavitevTezavnosti(20))
file.add_command(label="Srednja tezavnostnja stopnja", command=nastavitevTezavnosti(30))
file.add_command(label="Lahka tezavnostnja stopnja", command=nastavitevTezavnosti(40))
menu.add_cascade(label="Izberi tezavnost", menu=file)
frame.config(menu=menu)
menu.add_cascade(label="Ostalo", menu=file)
file.add_command(label="Oddaj", command=preveriEnakost())
frame.mainloop()






