import re
import os
import pandas as pd
from tqdm import tqdm
from q2 import download_audio, cut_audio
from typing import List


def filter_df(csv_path: str, label: str) -> List[str]:
    """
    Écrivez une fonction qui prend le path vers le csv traité (dans la partie notebook de q1) et renvoie une liste d'IDs avec seulement les rangées qui contiennent l'étiquette `label`.

    Par exemple:
    get_ids("audio_segments_clean.csv", "Speech") ne doit renvoyer que les IDs où l'un des libellés est "Speech"
    """
    df = pd.read_csv(csv_path)
    
    # Split the 'label_names' column by comma and check if the label exists
    filtered_df = df[df['label_names'].str.split('|').apply(lambda x: label in x)]
    
    return filtered_df


def data_pipeline(csv_path: str, label: str) -> None:
    """
    En utilisant vos fonctions précédemment créées, écrivez une fonction qui prend un csv traité et pour chaque vidéo avec l'étiquette donnée:
    1. Le télécharge à <label>_raw/<ID>.mp3
    2. Le coupe au segment approprié
    3. L'enregistre dans <label>_cut/<ID>.mp3
    (n'oubliez pas de créer le dossier audio/).

    Il est recommandé d'itérer sur les rangées de filter_df().
    Utilisez tqdm pour suivre la progression du processus de téléchargement (https://tqdm.github.io/)

    Malheureusement, il est possible que certaines vidéos ne peuvent pas être téléchargées. Dans de tels cas, votre pipeline doit gérer l'échec en passant à la vidéo suivante avec l'étiquette.
    """
    os.makedirs("audio", exist_ok=True)
    os.makedirs(f"audio/{label}_cut", exist_ok=True)
    os.makedirs(f"audio/{label}_raw", exist_ok=True)
    
    filtered_df = filter_df(csv_path, label)
    
    for _, row in tqdm(filtered_df.iterrows(), total=filtered_df.shape[0]):
        ID = row['# YTID']
        start_seconds = int(row[' start_seconds'])
        end_seconds = int(row[' end_seconds'])
        
        try:
            raw_audio_path = f"audio/{label}_raw/{ID}.mp3"
            cut_audio_path = f"audio/{label}_cut/{ID}.mp3"
            
            download_audio(ID, raw_audio_path)
            cut_audio(raw_audio_path, cut_audio_path, start_seconds, end_seconds)
        except:
            continue


def rename_files(path_cut: str, csv_path: str) -> None:
    """
    Supposons que nous voulons maintenant renommer les fichiers que nous avons téléchargés dans `path_cut` pour inclure les heures de début et de fin ainsi que la longueur du segment. Alors que
    cela aurait pu être fait dans la fonction data_pipeline(), supposons que nous avons oublié et que nous ne voulons pas tout télécharger à nouveau.

    Écrivez une fonction qui, en utilisant regex (c'est-à-dire la bibliothèque `re`), renomme les fichiers existants de "<ID>.mp3" -> "<ID>_<start_seconds_int>_<end_seconds_int>_<length_int>.mp3"
    dans path_cut. csv_path est le chemin vers le csv traité à partir de q1. `path_cut` est un chemin vers le dossier avec l'audio coupé.

    Par exemple
    "--BfvyPmVMo.mp3" -> "--BfvyPmVMo_20_30_10.mp3"

    ## ATTENTION : supposez que l'YTID peut contenir des caractères spéciaux tels que '.' ou même '.mp3' ##
    """
    df = pd.read_csv(csv_path)
    
    for file in os.listdir(path_cut):
        ID = file.split('.')[0]
        row = df[df['# YTID'] == ID]
        
        start_seconds = int(row[' start_seconds'])
        end_seconds = int(row[' end_seconds'])
        length = end_seconds - start_seconds
        
        os.rename(f"{path_cut}/{file}", f"{path_cut}/{ID}_{start_seconds}_{end_seconds}_{length}.mp3")


if __name__ == "__main__":
    print(filter_df("data/audio_segments_clean.csv", "Laughter"))
    data_pipeline("data/audio_segments_clean.csv", "Laughter")
    rename_files("Laughter_cut", "data/audio_segments_clean.csv")
