#Scrie un program care primește o listă de numere ca intrare. Programul ar trebui să calculeze produsul tuturor numerelor din listă.
#Cu toate acestea, dacă produsul depășește 100, programul ar trebui să oprească calculul și să afișeze un mesaj care indică că produsul este prea mare.
#Folosește o buclă while și instrucțiunea break pentru a încheia bucla când este necesar.

numere = input("Introduceti numerele separate prin spatiu: ")
numere = numere.split()

produs = 1
i = 0
while i < len(numere):
    numar = int(numere[i])
    produs *= numar

    if produs > 100:
        print("Produsul este prea mare!")
        break

    i += 1

print("Produsul este:", produs)