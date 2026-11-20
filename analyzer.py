import pandas as pd


#Charger les données
def charger_donnees(chemin):
    data = pd.read_csv(chemin)
    return data


#Aperçu général
def apercu(data):
    print("la dimension du dataset est de :", data.shape)
    print("les types de nos differentes colonnes sont : ", data.dtypes)
    print("\n les statistiques de notre fichiers sont :")
    print(data.describe(include="all"))


#Valeurs manquantes (nombre + pourcentage)
def valeurs_manquantes(data):
    nombre_de_valeurs_manquantes = data.isnull().sum()
    pourcentage = (nombre_de_valeurs_manquantes / len(data) * 100).round(2)
    resultat = pd.DataFrame({
        "manquantes": nombre_de_valeurs_manquantes,
        "pourcentage": pourcentage
    })
    # on garde seulement les colonnes qui ont un problème
    return resultat[resultat["manquantes"] > 0]


#Doublons
def doublons(data):
    nb = data.duplicated().sum()
    lignes = data[data.duplicated(keep=False)]   # toutes les lignes concernées
    return nb, lignes

#uniques
def valeurs_uniques(data):
    return data.nunique()

#verifier les types de donnees
def verifier_types(data):
    return data.dtypes


    

