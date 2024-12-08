def analyse_texte(texte):
    mot = texte.split()
    return {"nombredemot": len(mot), "nbr_caractere": len(texte)}
print(analyse_texte('Bonjour Brahim'))