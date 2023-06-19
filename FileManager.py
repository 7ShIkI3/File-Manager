import os
import shutil
import glob

def lancer():
    if __name__ == "__main__":
        main()

def affichage():
    print("_" * 80)

def saut_de_ligne(n):
    for i in range(n):
        print()

def destination_trie():
    try:
        fichier = open("save.txt", "r", encoding="utf-8")
        contenu = fichier.readlines()
        fichier.close()

        save_list = []

        for i in range(len(contenu)):
            chemin_utilisateur = contenu[i].strip()
            save_list.append(chemin_utilisateur)

        return save_list

    except (FileNotFoundError, ValueError):
        save_list = []
        trie_download = input("Fichier download à trier : ").replace("\\", "/")
        save_list.append(trie_download)
        trie_desktop = input("Fichier desktop à trier : ").replace("\\", "/")
        save_list.append(trie_desktop)
        trie_document = input("Fichier document à trier : ").replace("\\", "/")
        save_list.append(trie_document)
        trie_video = input("Fichier document à trier : ").replace("\\", "/")
        save_list.append(trie_video)

        destination_img = str(input("Destination des fichiers img : ")).replace("\\", "/")
        save_list.append(destination_img)
        destination_text_file = str(input("Destination des fichiers texte : ")).replace("\\", "/")
        save_list.append(destination_text_file)
        destination_python = str(input("Destination des fichiers py : ")).replace("\\", "/")
        save_list.append(destination_python)
        destination_exe = str(input("Destination des fichiers exe : ")).replace("\\", "/")
        save_list.append(destination_exe)
        destination_exe = str(input("Destination des fichiers exe : ")).replace("\\", "/")
        save_list.append(destination_exe)
        destination_video = str(input("Destination des fichiers exe : ")).replace("\\", "/")
        save_list.append(destination_video)

        fichier = open("save.txt", "w", encoding="utf-8")
        for path in save_list:
            fichier.write(f"{path}\n")

        fichier.close()
        return save_list


def trie_fichiers(position: list):
    trie = position[:3]
    destination = position[3:9]

    for folder in trie:
        for file in glob.glob(os.path.join(folder, "*")):
            # Construire le chemin de destination complet
            destination_path = None
            
            if file.endswith(".py"):
                destination_path = os.path.join(destination[2], os.path.basename(file))
            elif file.endswith((".png", ".jpg", ".JPG", ".gif", ".jfif", ".raw")):
                destination_path = os.path.join(destination[0], os.path.basename(file))
            elif file.endswith((".txt", ".docx", ".doc", ".odt", ".odp")):
                destination_path = os.path.join(destination[1], os.path.basename(file))
            elif file.endswith(".exe"):
                destination_path = os.path.join(destination[3], os.path.basename(file))
            elif file.endswith((".mp4", ".mkv")):
                destination_path = os.path.join(destination[4], os.path.basename(file))
            
            # Vérifier si une destination valide a été trouvée
            if destination_path:
                # Déplacer le fichier vers la destination correspondante
                shutil.move(file, destination_path)
            else:
                print(f"Aucune destination valide trouvée pour le fichier : {file}")

def main():
    affichage()
    print("Welcome in FileManager !!")
    affichage()
    saut_de_ligne(2)
    save = destination_trie()
    trie_fichiers(save)
    affichage()
    print("We have cleaned your pc ;)")
    input()

lancer()
