import os

import shutil

from tkinter import Tk

from tkinter.filedialog import askopenfilename

# Obtenir le chemin d'accès au fichier à copier en utilisant une boîte de dialogue

root = Tk()

root.withdraw()

file_path = askopenfilename()

# Copier le fichier dans le même répertoire en utilisant shutil.copy

filename = os.path.basename(file_path)

shutil.copy(file_path, filename + '_copy')

