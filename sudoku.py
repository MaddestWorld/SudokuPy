from random import randint,shuffle

class Sudoku():
    ''''''
    def __init__(self):
        '''
        sudoku:           po generiranju narejen sudoku(v celoti)
        nedsudoku:        nedokoncan sudoku oziroma sudoku z zbrsanimi element
        trenutniSudoku:   uporabikov sudoku v x koraku
        '''
        self.sudoku=list()
        self.nedSodoku=list()
        self.trenutniSudoku=list()

    def generirajEnkrat(self,maxponovitev,izpis=False):
        '''Generira Sudoku enkrat pri tem pazi na pravilnost sudokuja: "Dela(zazeleni popravki)" '''
        mnozicaSt={1,2,3,4,5,6,7,8,9}
        napaka=False
        stPonovitev=0
        self.sudoku = [[0] * 9 for i in range(9)]
        seznamStolpcev=[[0] * 9 for i in range(9)]
        seznamTrojk=[[0] * 9 for i in range(9)]
        for vrstica in range(9):
            stolpec=0
            while stolpec<9:
                #v primeru neskoncnega ponavlanja
                if stPonovitev>maxponovitev:
                    return False
                sezGeneriranja=list(mnozicaSt.difference(set(self.sudoku[vrstica]).union(set(seznamStolpcev[stolpec]).union(seznamTrojk[3*(vrstica//3)+stolpec//3]))))
                #ce je sez generiranja prazen moramo iti na prejsne korake
                if len(sezGeneriranja)==0:
                    try:
                        stolpec = stolpec - 1
                        self.sudoku[vrstica][stolpec] = 0
                        seznamStolpcev[stolpec][vrstica] = 0
                        seznamTrojk[3 * (vrstica // 3) + (stolpec) // 3][3 * (vrstica % 3) + (stolpec) % 3] = 0
                        stolpec=stolpec-1
                        stPonovitev+=1
                    except:
                        pass
                    napaka=True
                elif napaka and (len(sezGeneriranja)==1 or len(sezGeneriranja)==2):
                    stolpec = stolpec - 1
                    for i in range(2):
                        try:
                            self.sudoku[vrstica][stolpec] = 0
                            seznamStolpcev[stolpec][vrstica] = 0
                            seznamTrojk[3 * (vrstica // 3) + (stolpec) // 3][3 * (vrstica % 3) + (stolpec) % 3] = 0
                            stolpec = stolpec - 1
                        except:
                            pass

                    napaka=False
                #izbrano stevilo se zapise v tabele
                else:
                    shuffle(sezGeneriranja)
                    stevilo=list(sezGeneriranja)[0]
                    self.sudoku[vrstica][stolpec]=stevilo
                    seznamStolpcev[stolpec][vrstica]=stevilo
                    seznamTrojk[3*(vrstica//3)+stolpec//3][3*(vrstica%3)+stolpec%3]=stevilo
                stolpec=stolpec+1
        if izpis==True:
            '''testiranje kasneje pobrisi'''
            print("V: " + str(self.sudoku))
            print("S: " + str(seznamStolpcev))
            print("T: " + str(seznamTrojk))
        return True

    def generiraj(self,maxponovitev,izpis=False):
        "generira sudoku dokler ni vredu"
        x = self.generirajEnkrat(maxponovitev,izpis)
        while not x:
            x = self.generirajEnkrat(maxponovitev,izpis)

    def pobrisiElemente(self,tezavnost):
        '''Pripravi sodoku za resevanje, to naradi tako da uposteva tezavnost ter na tezavnost izbrise st podatkov. '''
        self.nedSodoku = [[0] * 9 for i in range(9)]
        for vrsta in range(9):
            for stolpec in range(9):
                self.nedSodoku[vrsta][stolpec]=self.sudoku[vrsta][stolpec]

        stElementovZaPobrisati=81-tezavnost
        while stElementovZaPobrisati>0:
            vrstica=randint(0,8)
            stolpec=randint(0,8)
            if self.nedSodoku[vrstica][stolpec]!=0:
                self.nedSodoku[vrstica][stolpec]=0
                stElementovZaPobrisati-=1

    def nastavi(self):
        '''nastavi sudoku tako da ga uporabik lahko spreminja'''
        self.trenutniSudoku = [[0] * 9 for i in range(9)]
        for vrsta in range(9):
            for stolpec in range(9):
                self.trenutniSudoku[vrsta][stolpec] = self.nedSodoku[vrsta][stolpec]

    def posodobi(self,vrsta,stolpec,stevilo):
        '''posodobi trenutni sudoku, da se ujema z zaslonom'''
        self.trenutniSudoku[vrsta][stolpec]=stevilo

    def preveriEnakost(self):
        '''preveri in vrne ce je sudoku resen pravilno'''
        for vrsta in self.sudoku:
            for stolpec in vrsta:
                if self.trenutniSudoku[vrsta][stolpec]!=self.sudoku[vrsta][stolpec]:
                    return false
        return true

if __name__=="__main__":
    novo1=Sudoku()
    novo1.sudoku=[[2,9,5,7,4,3,8,6,1],
                  [4,3,1,8,6,5,9,2,7],
                  [8,7,6,1,9,2,5,4,3],
                  [3,8,7,4,5,9,2,1,6],
                  [6,1,2,3,8,7,4,9,5],
                  [5,4,9,2,1,6,7,3,8],
                  [7,6,3,5,3,4,1,8,9],
                  [9,2,8,6,7,1,3,5,4],
                  [1,5,4,9,3,8,6,7,2]]

    novo1.generiraj(10,False)
    novo1.pobrisiElemente(30)
    print(novo1.nedSodoku)
    print(novo1.sudoku)