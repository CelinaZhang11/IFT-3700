"""
Ce devoir est basé sur [le cours de science des données de Greg Baker à SFU

Toutes les zones qui nécessitent des travaux sont marquées d'une étiquette "TODO".
"""

import numpy as np


def city_lowest_precipitation(totals: np.array) -> int:
    """
    Étant donné un tableau 2D où chaque ligne représente une ville, et chaque colonne est un mois de janvier 
    à décembre d'une année particulière, retourne la ville avec les précipitations totales les plus faibles.
    """

    # Calculer les précipitations totales pour chaque ville (somme des colonnes pour chaque ligne)
    total_precipitations_per_city = np.sum(totals, axis=1)
    
    # Trouver l'index de la ville avec les précipitations les plus faibles
    city_with_lowest_precipitation = np.argmin(total_precipitations_per_city)
    
    return city_with_lowest_precipitation


def avg_precipitation_month(totals: np.array, counts: np.array) -> np.array:
    """
    Déterminez les précipitations moyennes à ces endroits pour chaque mois. Ce sera le total
    précipitations pour chaque mois (axe 0), divisé par le total des observations pour ce mois.
    """

    # Calculer les précipitations totales pour chaque mois (somme des lignes pour chaque colonne)
    total_precipitations_per_month = np.sum(totals, axis=0)

    # Calculer les moyennes des précipitations pour chaque mois
    avg_precipitations_per_month = total_precipitations_per_month / np.sum(counts, axis=0)

    return avg_precipitations_per_month


def avg_precipitation_city(totals: np.array, counts: np.array) -> np.array:
    """
    Faites de même pour les villes: donnez les précipitations moyennes (précipitations quotidiennes moyennes sur le mois) 
    pour chaque ville.
    """

    # Calculer les précipitations totales pour chaque ville (somme des colonnes pour chaque ligne)
    total_precipitations_per_city = np.sum(totals, axis=1)

    # Calculer les moyennes des précipitations pour chaque ville
    avg_precipitations_per_city = total_precipitations_per_city / np.sum(counts, axis=1)

    return avg_precipitations_per_city


def quarterly_precipitation(totals: np.array) -> np.array:
    """
    Calculez les précipitations totales pour chaque trimestre dans chaque ville (c'est-à-dire les totaux pour chaque station sur des groupes de trois mois). Vous pouvez supposer que le nombre de colonnes sera divisible par 3.

    Astuce: Utilisez la fonction de reshape pour reformer en un tableau 4n sur 3, additionner et reformer en n sur 4.
    """

    if totals.shape[1] != 12:
        raise NotImplementedError("Le tableau d'entrée n'a pas 12 mois!")

    # Reformer le tableau en un tableau 4n sur 3
    reshaped_totals = totals.reshape(totals.shape[0], 4, 3)

    # Calculer les précipitations totales pour chaque trimestre (axe=2)
    quarterly_precipitations = np.sum(reshaped_totals, axis=2)

    # Reformer le tableau en n sur 4
    quarterly_precipitations = quarterly_precipitations.reshape(totals.shape[0], 4)

    return quarterly_precipitations


def main():
    data = np.load("data/monthdata.npz")
    totals = data["totals"]
    counts = data["counts"]

    # You can use this to steer your code
    print(f"Rangée avec la précipitations la plus faible:\n{city_lowest_precipitation(totals)}")
    print(f"La précipitation moyenne par mois:\n{avg_precipitation_month(totals, counts)}")
    print(f"La précipitation moyenne par ville:\n{avg_precipitation_city(totals, counts)}")
    print(f"La précipitations trimestrielle:\n{quarterly_precipitation(totals)}")


if __name__ == "__main__":
    main()
