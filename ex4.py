#Scrie un program care primește o listă de șiruri de caractere ca intrare. Programul ar trebui să afișeze
#fiecare șir de caractere pe o linie separată. Cu toate acestea, dacă un șir de caractere începe cu litera 'A',
#programul ar trebui să sara peste acel șir și să treacă la următorul folosind instrucțiunea continue.

siruri = input("Introduceti sirurile separate prin spatiu: ")
siruri = siruri.split()

for sir in siruri:
    if sir.startswith('A'):
        continue

    print(sir)