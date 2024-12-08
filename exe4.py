def compte_occurance(liste):
    return {i: liste.count(i) for i in set(liste)}
print(compte_occurance([1,2,2,4,5,6,7,6,8,1]))