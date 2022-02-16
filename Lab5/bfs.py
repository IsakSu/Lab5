from bintreeFile import Bintree
from linkedQFile import *
alfabetslista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

    def writechain(self):
        if(not(self.parent == None)):
            self.parent.writechain()
            print(self.word)

class SolutionFound(Exception):
    pass

q = LinkedQ()
svenska = Bintree()
gamla = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()           # Ett trebokstavsord per rad
        if not ordet in svenska:
            svenska.put(ordet)

def makechildren(nod, q):
    #skapar barn för en nod och lägger in i en kö
    if(nod.word not in svenska):
        #Om startordet inte finns hoppar vi ut
        print(nod.word + " finns inte i trädet")
        return
    for i in range (len(nod.word)):
        tempstr = nod.word
        for j in range (len(alfabetslista)):
            tempstr = tempstr[:i] + alfabetslista[j] + tempstr[i+1:]
            #allt innan i + alfabet j + allt efter i+1
            if(tempstr in svenska and tempstr not in gamla and not tempstr == startord):
                gamla.put(tempstr)
                if(tempstr == slutord):
                    nod.writechain()
                    print(tempstr)
                    raise SolutionFound("Kortaste vägen hittad!")
                else:
                    q.enqueue(ParentNode(tempstr, nod))
    if(q.isEmpty() and slutord not in gamla):
        print("Det finns inte en väg till " + slutord)


startord = input("Skriv in ditt första ord \n")
slutord = input("Skriv in ditt sista ord \n")
q.enqueue(ParentNode(startord, None))
while not q.isEmpty():
    nod = q.dequeue()
    makechildren(nod, q)
