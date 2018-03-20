from random import randint

class Sudoku():
    ''''''
    def __init__(self):
        self.sodoku=list(""*9)
        self.nedSodoku=list()

    def generiraj(self):
        '''Generira Sudoku pri tem pazi na pravilnost sudokuja %%nedokoncano%%'''
        strst=0
        self.sodoku=list("1"*9)
        print(self.sodoku)
        for i in range(len(self.sodoku)):
            self.sodoku[i]=""
            while len(self.sodoku[i])<=9:
                print(self.sodoku)
                strst=str(randint(1,9))
                if strst in self.sodoku[i]:
                    pass
                else:
                   if len(self.sodoku[i])<=3:
                       if i<3:
                           if strst in self.sodoku[i-1]:
                               pass
                           elif i==2 and (strst in self.sodoku[i-2]):
                               pass
                           else:
                               self.sodoku[i]+=strst
                       elif i<6:
                           if i==4 and (strst in self.sodoku[i-1]):
                               pass
                           elif i==5 and (strst in self.sodoku[i-2]):
                               pass
                           else:
                               self.sudoku[i]+=strst
                       else:
                           if i==7 and (strst in self.sodoku[i-1]):
                               pass
                           elif i==8 and (strst in self.sodoku[i-2]):
                               pass
                           else:
                               self.sodoku[i]+=strst

    def pobrisiElemente(self,tezavnost):
        '''Pripravi sodoku za resevanje, to naradi tako da uposteva tezavnost ter na tezavnost izbrise st podatkov. '''
        self.nedSodoku=self.sodoku
        stElementovZaPobrisati=81-tezavnost
        while stElementovZaPobrisati>0:
            vrstica=randint(0,8)
            stolpec=randint(0,8)
            if self.nedSodoku[vrstica][stolpec]!=".":
                self.nedSodoku[vrstica]=self.nedSodoku[vrstica][:stolpec]+"."+self.nedSodoku[vrstica][stolpec+1:]
                stElementovZaPobrisati-=1

novo1=Sudoku()
novo1.generiraj()
print(novo1.sodoku)