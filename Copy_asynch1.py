from concurrent.futures import ThreadPoolExecutor

# La fonction suivante sera exécutée dans un thread séparé
def copy_file(src, dest):
  with open(src, 'r') as f_src:
    with open(dest, 'w') as f_dest:
      # Copier les données du fichier source au fichier de destination
      f_dest.write(f_src.read())

# Définissez les chemins des fichiers source et de destination
src = '/path/to/src/file'
dest = '/path/to/dest/file'

# Créez un objet Executor pour exécuter la fonction de copie de fichier dans un thread séparé
executor = ThreadPoolExecutor()

# Soumettez la fonction à l'exécuteur pour qu'elle soit exécutée dans un thread séparé
future = executor.submit(copy_file, src, dest)

# Faites quelque chose d'autre ici, pendant que le fichier est en cours de copie
# dans le thread séparé.

# Vous pouvez également attendre la fin de l'exécution de la fonction en appelant la méthode `result()`
# sur l'objet `Future`

   
