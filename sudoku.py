from random import randint

class Sudoku():
    ''''''
    def __init__(self):
        self.sudoku=[[0]*9]*9
        self.nedSodoku=list()

    def generiraj(self):
        '''Generira Sudoku pri tem pazi na pravilnost sudokuja %%nedokoncano%%'''
        self.sudoku = [[0] * 9] * 9
        seznamStolpcev=[[0] * 9] * 9
        seznamTrojk=[[0]*9]*9
        stPonovitev=0
        for vrstica in range(9):
            for stolpec in range(9):
                while "":
                    stevilo=randint(1,9)
                    if (stevilo not in self.sudoku[vrstica]) and (stevilo not in seznamStolpcev[vrstica]):
                        if stolpec<=2 and vrstica<=2:
                            if stevilo not in seznamTrojk[0]:
                                self.sudoku[vrstica][stolpec]=stevilo
                        elif stolpec<=5 and vrstica<=2:
                            if stevilo not in seznamTrojk[1]:
                                self.sudoku[vrstica][stolpec]=stevilo
                        elif stolpec<=8 and vrstica<=2:
                            if stevilo not in seznamTrojk[2]:
                                self.sudoku[vrstica][stolpec]=stevilo
                        elif stolpec<=2 and vrstica<=5:
                            if stevilo not in seznamTrojk[3]:
                                self.sudoku[vrstica][stolpec]=stevilo
                        elif stolpec<=5 and vrstica<=5:
                            if stevilo not in seznamTrojk[4]:
                                self.sudoku[vrstica][stolpec]=stevilo
                        elif stolpec<=8 and vrstica<=5:
                            if stevilo not in seznamTrojk[5]:
                                self.sudoku[vrstica][stolpec]=stevilo
                        elif stolpec<=2 and vrstica<=8:
                            if stevilo not in seznamTrojk[6]:
                                self.sudoku[vrstica][stolpec]=stevilo
                        elif stolpec<=5 and vrstica<=8:
                            if stevilo not in seznamTrojk[7]:
                                self.sudoku[vrstica][stolpec]=stevilo
                        elif stolpec<=8 and vrstica<=8:
                            if stevilo not in seznamTrojk[8]:
                                self.sudoku[vrstica][stolpec]=stevilo

                    #posodobitev tabele stolpcev
                    if "":
                    seznamStolpcev[stolpec][vrstica]=self.sudoku[vrstica][stolpec]
                    if "":
                    #posodobitev tablele
                    seznamTrojk[stolpec%3]=self.sudoku[vrstica][stolpec]









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

novo1=Sudoku()
novo1.generiraj()
print(novo1.sudoku)