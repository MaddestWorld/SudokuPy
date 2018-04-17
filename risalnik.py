from tkinter import *
from sudoku import *
from tkinter import messagebox
trenutna_tezavnost=40


def preveriEnakost():
    '''preveri pravilnost sudokuja'''
    if sudoku.preveriEnakost():
        messagebox.showinfo("Obvestilo","Čestitamo rešili ste sudoku pravilno")
        nastavitevTezavnosti(trenutna_tezavnost)
    else:
        messagebox.showinfo("Obvestilo", "Rešitev sudokuja ni pravilna. Prosim poskusite ponovno. ")

def pritisnjenaTipka(event):
    '''nastavi zadnji pritisnjen gumb na vrednost pritisnjene tipke, če to le ustreza pravilom sudokuja'''
    tabBarv = tabela_barv(sudoku)
    if (event.char in '0123456789') and tabBarv[vrsticaZadGumba][stolpecZadGumba]=="red":
        sudoku.trenutniSudoku[vrsticaZadGumba][stolpecZadGumba]=int(event.char)
        matrika[vrsticaZadGumba][stolpecZadGumba].configure(text=int(event.char))
        createGrid(tabBarv)

def btnCommand(row, col, x,tabBarv,matrika):
    '''pritisk na gumb'''
    global vrsticaZadGumba
    global stolpecZadGumba
    vrsticaZadGumba = row
    stolpecZadGumba = col
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
    trenutna_tezavnost=tezavnost
    sudoku.nastaviTezavnost(tezavnost)
    tabBarv = tabela_barv(sudoku)
    createGrid(tabBarv)


def createGrid(tabBarv):
    '''ustvari mrezo gumbov se poprej pa pobrise stare gumbe'''
    global matrika
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
frame.title("Sudoku")
menu = Menu(frame)
file = Menu(menu)
file2=Menu(menu)
sudoku=Sudoku()
sudoku.generiraj(20,False)
file.add_command(label="Izhod", command=frame.quit)
file2.add_command(label="Težka težavnostnja stopnja", command=lambda :nastavitevTezavnosti(30))
file2.add_command(label="Srednja težavnostnja stopnja", command=lambda :nastavitevTezavnosti(40))
file2.add_command(label="Lahka težavnostnja stopnja", command=lambda :nastavitevTezavnosti(50))
menu.add_cascade(label="Izberi težavnost", menu=file2)
frame.config(menu=menu)
menu.add_cascade(label="Ostalo", menu=file)
file.add_command(label="Oddaj", command=preveriEnakost)
nastavitevTezavnosti(trenutna_tezavnost)
frame.bind("<Key>",pritisnjenaTipka)
frame.mainloop()






