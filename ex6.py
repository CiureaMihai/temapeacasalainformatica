#Scrie o listă comprehensivă care generează o listă a literelor majuscule dintr-un anumit șir de caractere.
#De exemplu, dacă șirul de caractere este "Salut Lume", lista comprehensivă ar trebui să producă ['S', 'L'].

sir = "Salut Lume"
litere_majuscule = [litera for litera in sir if litera.isupper()]

print(litere_majuscule)






