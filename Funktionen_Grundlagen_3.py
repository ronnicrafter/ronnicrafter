## Beispiel 1: Schreibe eine Funktion namens alle_elemente_ausgabe, die einen einzigen Parameter liste besitzt und alle Elemente von liste untereinander ausgibt.
## Rufe die Funktion anschließend mit dem Argument [7, 2, 5, 8, 4] auf.
def alle_elemente_ausgabe(liste):
    i = 0
    while i < len(liste):
        print(liste[i])
        i = i + 1
alle_elemente_ausgabe([7, 2, 5, 8, 4])

## Aufgabe 1: Schreibe eine Funktion namens alle_elemente_ausgabe_2, die einen einzigen Parameter liste besitzt und das Doppelte aller Elemente von liste untereinander ausgibt.
## (Annahme: liste enthält nur Zahlen.)
## Rufe die Funktion anschließend mit dem Argument [7, 2, 5, 8, 4] auf.
def alle_elemente_ausgabe_2(liste):
    for element in liste:
        print(element * 2)
alle_elemente_ausgabe_2([7, 2, 5, 8, 4])

## Aufgabe 2: Schreibe eine Funktion namens alle_elemente_ausgabe_hoch_2, die einen einzigen Parameter liste besitzt und das Quadrat aller Elemente von liste untereinander ausgibt.
## (Annahme: liste enthält nur Zahlen.)
## Rufe die Funktion anschließend mit dem Argument [7, 2, 5, 8, 4] auf.
def alle_elemente_ausgabe_hoch_2(liste):
    for element in liste:
        print(element ** 2)
alle_elemente_ausgabe_hoch_2([7, 2, 5, 8, 4])


## Aufgabe 3: Schreibe eine Funktion jedes_zweite_element_ausgabe, die einen einzigen Parameter liste besitzt und jedes zweite Element von liste untereinander ausgibt.
## (Annahme: liste enthält nur Zahlen.)
## Rufe die Funktion anschließend mit dem Argument [23, 11, 18, 7, 12, 15, 24, 10] auf.


## Aufgabe 4: Schreibe eine Funktion jedes_dritte_element_ausgabe, die einen einzigen Parameter liste besitzt und jedes dritte Element von liste untereinander ausgibt.
## (Annahme: liste enthält nur Zahlen.)
## Rufe die Funktion anschließend mit dem Argument [23, 11, 18, 7, 12, 15, 24, 10] auf.


## Aufgabe 5: Schreibe eine Funktion jedes_element_ausgabe_rückwärts, die einen einzigen Parameter liste besitzt und jedes Elemente von liste untereinander ausgibt,
## vom letzten bis zum ersten.
## (Annahme: liste enthält nur Zahlen.)
## Rufe die Funktion anschließend mit dem Argument [23, 11, 18, 7, 12, 15, 24, 10] auf.


## Aufgabe 6: Schreibe eine Funktion jedes_element_größer_15, die einen einzigen Parameter liste besitzt und jedes Elemente von liste, das größer als 15 ist, untereinander ausgibt.
## (Annahme: liste enthält nur Zahlen.)
## Rufe die Funktion anschließend mit dem Argument [23, 11, 18, 7, 12, 15, 24, 10] auf.


## Aufgabe 7: Schreibe eine Funktion jedes_element_kleiner_13, die einen einzigen Parameter liste besitzt und jedes Elemente von liste, das kleiner als 13 ist, untereinander ausgibt.
## (Annahme: liste enthält nur Zahlen.)
## Rufe die Funktion anschließend mit dem Argument [23, 11, 18, 7, 12, 15, 24, 10] auf.


## Aufgabe 8: Schreibe eine Funktion jedes_element_größer_10_kleiner_20, die einen einzigen Parameter liste besitzt und jedes Elemente von liste, das größer als 10 und kleiner als 20 ist, untereinander ausgibt.
## (Annahme: liste enthält nur Zahlen.)
## Rufe die Funktion anschließend mit dem Argument [23, 11, 18, 7, 12, 15, 24, 10] auf.
