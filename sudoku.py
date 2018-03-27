from random import randint,shuffle

class Sudoku():
    ''''''
    def __init__(self):
        self.sudoku=[[0]*9]*9
        self.nedSodoku=list()
        self.upoSud=list()
        self.stResSud=0

    def generiraj(self):
        '''Generira Sudoku pri tem pazi na pravilnost sudokuja %%nedokoncano%%'''
        mnozicaSt={1,2,3,4,5,6,7,8,9}
        self.sudoku = [[0] * 9 for i in range(9)]
        seznamStolpcev=[[0] * 9 for i in range(9)]
        seznamTrojk=[[0] * 9 for i in range(9)]
        stPonovitev=0
        for vrstica in range(9):
            for stolpec in range(9):
                sezGeneriranja=list(mnozicaSt.difference(set(self.sudoku[vrstica]).union(set(seznamStolpcev[stolpec]).union(seznamTrojk[]))))
                shuffle(sezGeneriranja)
                print(sezGeneriranja)
                stevilo=list(sezGeneriranja)[0]
                self.sudoku[vrstica][stolpec]=stevilo
                #seznamStolpcev[stolpec][vrstica]=stevilo
        print("V: " + str(self.sudoku))
        print("S: "+ str(seznamStolpcev))
        print("T: "+str(seznamTrojk))






    def pobrisiElemente(self,tezavnost):
        '''Pripravi sodoku za resevanje, to naradi tako da uposteva tezavnost ter na tezavnost izbrise st podatkov. '''
        self.nedSodoku=self.sudoku
        stElementovZaPobrisati=81-tezavnost
        while stElementovZaPobrisati>0:
            vrstica=randint(0,8)
            stolpec=randint(0,8)
            if self.nedSodoku[vrstica][stolpec]!=".":
                self.nedSodoku[vrstica]=self.nedSodoku[vrstica][:stolpec]+"."+self.nedSodoku[vrstica][stolpec+1:]
                stElementovZaPobrisati-=1
    def posodobiSudoku(self):
        ''''''
    def preveriEnakost(self):
        ''''''
    def zapisiVDat(self):
        ''''''

novo1=Sudoku()
novo1.generiraj()
#print(novo1.sudoku)