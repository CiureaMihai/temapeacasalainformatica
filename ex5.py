#Scrie o listă comprehensivă care generează o listă a lungimilor cuvintelor dintr-un anumit enunț.
#De exemplu, dacă enunțul este "Salut lume, cum te simți?", lista comprehensivă ar trebui să producă [5, 5, 3, 3, 4].

enunt = "Salut lume, cum te simti?"
lungimi_cuvinte = [len(cuvant) for cuvant in enunt.split()]

print(lungimi_cuvinte)







