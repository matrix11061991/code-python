import win32process
def list_processes():
    # Obtenir la liste des processus en cours d'exécution
    process_ids = win32process.EnumProcesses()
    # Afficher le nom et l'ID de chaque processus
    for process_id in process_ids:
        try:
            # Obtenir le nom du processus à partir de son ID
            process_handle = win32process.OpenProcess(win32process.PROCESS_QUERY_INFORMATION, False, process_id)
            _, process_name = win32process.GetModuleFileNameEx(process_handle, 0)
            print(f"Process name: {process_name}, Process ID: {process_id}")
        except:
            # Certaines informations de processus ne sont pas accessibles
            # (par exemple, si l'utilisateur n'a pas les autorisations appropriées)
            pass
list_processes()
