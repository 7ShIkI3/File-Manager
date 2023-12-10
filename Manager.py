from tkinter import * 
import os
import shutil
import glob

class Parametre:
    def __init__(self) -> None:
        self.folder1Path:str = ""
        self.folder2Path:str = ""
        self.fileType:str = ""
    
    def set_folder1Path(self):
        self.folder1Path = str(input("Fichier a Trie : "))
        self.folder1Path = self.folder1Path.replace("\\", "/")
    
    def set_folder2Path(self):
        self.folder2Path = str(input("Destination : "))
        self.folder2Path = self.folder2Path.replace("\\", "/")

class FileRename:
    
    def __init__(self) -> None:
        self.parametre = Parametre()
    
    def fileTrie(self):
        i = 0
        path = self.parametre.folder1Path
        type = self.parametre.fileType
        name = "file"
        fichier = os.listdir(path)
        
        for filename in fichier:
            img_rename = name + str(i) + type
            source = os.path.join(path, filename)
            img_rename = os.path.join(path, img_rename)
            print("Source:", source)
            print("Destination:", img_rename)
            if os.path.exists(source):
                os.rename(source, img_rename)
                i += 1
          
class Filemanager:

    def __init__(self) -> None:
        self.parametre = Parametre()

    def fileManager(self):
        for folder in [self.parametre.folder1Path]:
            for file in glob.glob(os.path.join(folder, "*")):
                if os.path.isfile(file):  # Check if it's a regular file
                    destination_path = None

                    if file.endswith(".py"):
                        destination_path = os.path.join(self.parametre.folder2Path, "Python", os.path.basename(file))
                    elif file.endswith((".png", ".jpg", ".JPG", ".gif", ".jfif", ".raw")):
                        destination_path = os.path.join(self.parametre.folder2Path, "Image", os.path.basename(file))
                    elif file.endswith((".txt", ".docx", ".doc", ".odt", ".odp", ".pdf")):
                        destination_path = os.path.join(self.parametre.folder2Path, "Docs", os.path.basename(file))
                    elif file.endswith(".exe"):
                        destination_path = os.path.join(self.parametre.folder2Path, "Executable", os.path.basename(file))
                    elif file.endswith((".mp4", ".mkv")):
                        destination_path = os.path.join(self.parametre.folder2Path, "Video", os.path.basename(file))
                    elif file.endswith((".mp3")):
                        destination_path = os.path.join(self.parametre.folder2Path, "Musique", os.path.basename(file))

                    if destination_path:
                        os.makedirs(os.path.dirname(destination_path), exist_ok=True)  # Create destination folders if not exist
                        shutil.move(file, destination_path)
                    else:
                        print(f"Aucune destination valide trouvée pour le fichier : {file}")

#ancien affichage

"""
if __name__ == "__main__":
    print("TXT [A]")
    print("PNG [B]")
    val = str(input("> "))
    obj = FileRename()
    if val == "A":
        obj.parametre.fileType = ".txt"
    elif val == "B":
        obj.parametre.fileType = ".png"
    obj.parametre.set_folder1Path()
    obj.fileTrie()
"""

#futur affichage

if __name__ == "__main__":
    
    MaFenetre = Tk()
    
    obj = Filemanager()
    obj.parametre.set_folder1Path()
    obj.parametre.set_folder2Path()
    obj.fileManager()
    
    