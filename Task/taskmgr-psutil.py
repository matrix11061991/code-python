import psutil
def list_processes():
    # Obtenir la liste des processus en cours d'exécution
    processes = psutil.process_iter()
    # Afficher le nom et l'ID de chaque processus
    for process in processes:
        print(f"Process name: {process.name()}, Process ID: {process.pid}")
list_processes()
