## Beispiel 1: Schreibe eine Funktion namens funktion1, die einen einzigen Parameter namens parameter1 besitzt.
def funktion1(parameter1):
    pass # pass tut nichts, muss aber geschrieben werden, weil der Funktionskörper nicht leer sein darf.

## Aufgabe 1: Schreibe eine Funktion namens begrüßung, die einen einzigen Parameter namens grußformel besitzt.
def begrüßung(grußformel):
    pass

## Aufgabe 2: Schreibe eine Funktion namens produkt_vorbereitung, die zwei Parameter namens zahl1 und zahl2 besitzt.
def produkt_vorbereitung(zahl1,zahl2):
    pass

## Aufgabe 3: Schreibe eine Funktion namens hallo, die keinen Parameter besitzt und "Hallo" ausgibt (ab hier muss kein pass mehr geschrieben werden).
def hallo( ):
    print("Hallo")
hallo()

## Aufgabe 4: Schreibe eine Funktion namens doppeltes, die einen einzigen Parameter namens zahl besitzt und das Doppelte von zahl ausgibt.
def doppeltes(zahl):
    print(zahl)
doppeltes (2*5)


## Aufgabe 5: Schreibe eine Funktion namens summe, die zwei Parameter namens zahl1 und zahl2 besitzt und die Summe dieser Zahlen ausgibt.
def Summe(zahl1,zahl2):
    print(zahl1+zahl2)
Summe (1,2)

## Aufgabe 6: Schreibe eine Funktion namens differenz, die zwei Parameter namens zahl1 und zahl2 besitzt und die Differenz dieser Zahlen ausgibt.
def differenz(zahl1,zahl2):
    print(zahl1 - zahl2)
differenz(10,3)

## Aufgabe 7: Schreibe eine Funktion namens produkt, die zwei Parameter namens zahl1 und zahl2 besitzt und das Produkt dieser Zahlen ausgibt.
def produkt(zahl1,zahl2):
    print(zahl1 * zahl2)
produkt(3,7)

## Aufgabe 8: Schreibe eine Funktion namens positiv, die einen einzigen Parameter namens zahl besitzt und "Positiv" ausgibt, falls zahl größer 0 ist, ansonsten "Nicht positiv".
def positiv(zahl):
    if zahl > 0:
        print("positiv")
    else:
        print("Nicht positiv")
positiv(-2)

## Aufgabe 9: Schreibe eine Funktion namens größer, die zwei Parameter namens zahl1 und zahl2 besitzt und 1 ausgibt, falls zahl1 größer ist als zahl2, ansonsten 2.
def größer(zahl1,zahl2):
    if zahl1 > zahl2:
        print("1")
    else:
        print("2")
größer(10,3)

## Aufgabe 10: Schreibe eine Funktion namens größere, die zwei Parameter namens zahl1 und zahl2 besitzt und den maximalen Wert unter ihnen ausgibt.
def größere(zahl1,zahl2):
    if zahl1 > zahl2:
        print(zahl1)
    else:
        print(zahl2)
größere(20,21)

## Aufgabe 11: Schreibe eine Funktion namens größte, die drei Parameter namens zahl1, zahl2 und zahl3 besitzt und den maximalen Wert unter ihnen ausgibt.
def größte(zahl1,zahl2,zahl3):
    if zahl1 > zahl2 and zahl1 > zahl3:
        print(zahl1)
    if zahl2 > zahl3 and zahl2 > zahl1:
        print(zahl2)
    else:
        print(zahl3)  
größte(71,3,85)

## Aufgabe 12: Schreibe eine Funtion namens quadratOderMal10, die einen einzigen Parameter namens zahl besitzt und den maximalen Wert unter dessen Quadrat und dessen Zehnfachem ausgibt.
def quadratOderMal10(zahl):
    if zahl*zahl > zahl*10:
        print(zahl*zahl)
    else:
        print(zahl*10)
quadratOderMal10(11)

## Aufgabe 13: Schreibe eine Funktion namens summe_oder_differenz, die zwei Parameter namens zahl1 und zahl2 besitzt und den maximalen Wert unter dessen Summe und dessen Differenz ausgibt.
def summe_oder_differenz(zahl1,zahl2):
    if zahl1 + zahl2 > zahl1 - zahl2:
        print(zahl1 + zahl2)
    else:
        print(zahl1 - zahl2)
summe_oder_differenz(3,5)