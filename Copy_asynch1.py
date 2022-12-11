import threading

# La fonction suivante sera exécutée dans un thread séparé

def copy_file(src, dest):

  with open(src, 'r') as f_src:

    with open(dest, 'w') as f_dest:

      # Copier les données du fichier source au fichier de destination

      f_dest.write(f_src.read())

# Définissez les chemins des fichiers source et de destination

src = '/path/to/src/file'

dest = '/path/to/dest/file'

# Créez un thread pour exécuter la fonction de copie de fichier

thread = threading.Thread(target=copy_file, args=(src, dest))

# Démarrez le thread pour lancer l'exécution de la fonction

thread.start()

# Faites quelque chose d'autre ici, pendant que le fichier est en cours de copie

# dans le thread séparé.

