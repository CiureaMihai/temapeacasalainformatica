#Scrie o listă comprehensivă care generează o listă a primelor litere ale fiecărui cuvânt dintr-un anumit enunț.
#De exemplu, dacă enunțul este "Python este minunat", lista comprehensivă ar trebui să producă ['P', 'e', 'm'].

enunt = "Python este minunat"
primele_litere = [cuvant[0] for cuvant in enunt.split()]

print(primele_litere)



