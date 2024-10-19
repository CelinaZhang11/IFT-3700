"""
Ce devoir est basé sur [le cours de science des données de Greg Baker à SFU

Toutes les zones qui nécessitent des travaux sont marquées d'une étiquette "TODO".
"""
import pandas as pd


def city_lowest_precipitation(totals: pd.DataFrame) -> str:
    """
    Étant donné un dataframe où chaque ligne représente une ville et chaque colonne est un mois 
    de janvier à décembre d'une année particulière, retourne la ville avec les précipitations totales les plus faibles.
    """

    # Find the city with the lowest total precipitation
    city_lowest_precipitation = totals.sum(axis=1).idxmin()

    return city_lowest_precipitation


def avg_precipitation_month(totals: pd.DataFrame, counts: pd.DataFrame) -> pd.DataFrame:
    """
    Déterminez les précipitations moyennes à ces endroits pour chaque mois. Ce sera le total des précipitations pour 
    chaque mois, divisé par le total des observations pour ce mois.
    """

    # Calculer les précipitations totales pour chaque mois
    total_precipitation = totals.sum(axis=0)

    # Calculer le nombre total d'observations pour chaque mois
    total_counts = counts.sum(axis=0)

    # Calculer la précipitation moyenne pour chaque mois
    avg_precipitation_per_month = total_precipitation / total_counts

    return avg_precipitation_per_month


def avg_precipitation_city(totals: pd.DataFrame, counts: pd.DataFrame) -> pd.DataFrame:
    """
    Faites de même pour les villes : donnez la précipitation moyenne (précipitation quotidienne moyennes sur le mois) 
    pour chaque ville.
    """

    # Calculer les précipitations totales pour chaque ville
    total_precipitation = totals.sum(axis=1)

    # Calculer le nombre total d'observations pour chaque ville
    total_counts = counts.sum(axis=1)

    # Calculer la précipitation moyenne pour chaque ville
    avg_precipitation_per_city = total_precipitation / total_counts 

    return avg_precipitation_per_city


# pas de trimestriel car c'est un peu pénible


def main():
    totals = pd.read_csv("data/totals.csv").set_index(keys=["name"])
    counts = pd.read_csv("data/counts.csv").set_index(keys=["name"])

    # You can use this to steer your code
    print(f"Rangée avec la précipitations la plus faible:\n{city_lowest_precipitation(totals)}")
    print(f"La précipitation moyenne par mois:\n{avg_precipitation_month(totals, counts)}")
    print(f"La précipitation moyenne par ville:\n{avg_precipitation_city(totals, counts)}")


if __name__ == "__main__":
    main()
