import socket
import paramiko
import random

# Définir quelques couleurs pour le texte
colors = [
    "\033[91m",  # Rouge
    "\033[92m",  # Vert
    "\033[93m",  # Jaune
    "\033[94m",  # Bleu
    "\033[95m",  # Violet
    "\033[96m",  # Cyan
]
bold = "\033[1m"
white = "\033[97m"
reset = "\033[0m"

def random_color():
    return random.choice(colors)

def banner():
    banner_text = f"""{bold}{random_color()}
  ,----..                 ,---,.             ,---,                              ,-.                     
 /   /   \       ,---.  ,'  .' |           ,--.' |                          ,--/ /|                     
|   :     :     /__./|,---.'   |           |  |  :                        ,--. :/ |             __  ,-. 
.   |  ;. /,---.;  ; ||   |   .'           :  :  :                        :  : ' /            ,' ,'/ /| 
.   ; /--`/___/ \  | |:   :  |-,    ,---.  :  |  |,--.   ,---.     ,---.  |  '  /      ,---.  '  | |' | 
;   | ;   \   ;  \ ' |:   |  ;/|   /     \ |  :  '   |  /     \   /     \ '  |  :     /     \ |  |   ,' 
|   : |    \   \  \: ||   :   .'  /    / ' |  |   /' : /    /  | /    / ' |  |   \   /    /  |'  :  /   
.   | '___  ;   \  ' .|   |  |-, .    ' /  '  :  | | |.    ' / |.    ' /  '  : |. \ .    ' / ||  | '    
'   ; : .'|  \   \   ''   :  ;/| '   ; :__ |  |  ' | :'   ;   /|'   ; :__ |  | ' \ \'   ;   /|;  : |    
'   | '/  :   \   `  ;|   |    \ '   | '.'||  :  :_:,''   |  / |'   | '.'|'  : |--' '   |  / ||  , ;    
|   :    /     :   \ ||   :   .' |   :    :|  | ,'    |   :    ||   :    :;  |,'    |   :    | ---'     
 \   \ .'       '---" |   | ,'    \   \  / `--''       \   \  /  \   \  / '--'       \   \  /           
  `---`               `----'       `----'               `----'    `----'              `----'           
    CVE checker regreSSHion                   
    {bold}{white}@dbutelle{reset}\n"""
    return banner_text

print (banner())

def check_port_22(ip):
    """
    Vérifie si le port 22 est ouvert sur l'adresse IP spécifiée.
    
    Args:
    ip (str): L'adresse IP à vérifier.
    
    Returns:
    bool: True si le port 22 est ouvert, False sinon.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)  # Timeout après 3 secondes
        result = sock.connect_ex((ip, 22))
        sock.close()
        return result == 0  # 0 signifie que le port est ouvert
    except Exception as e:
        print(f"Erreur lors de la vérification du port: {e}")
        return False

def get_ssh_version(ip):
    """
    Récupère la version du serveur SSH sur l'adresse IP spécifiée.
    
    Args:
    ip (str): L'adresse IP du serveur SSH.
    
    Returns:
    str: La version du serveur SSH si elle peut être récupérée, None sinon.
    """
    try:
        transport = paramiko.Transport((ip, 22))
        transport.connect()
        banner = transport.remote_version
        transport.close()
        return banner
    except Exception as e:
        print(f"Erreur lors de la récupération de la version SSH: {e}")
        return None

def main(ip):
    """
    Fonction principale pour vérifier l'état du port 22 et récupérer la version SSH si le port est ouvert.
    
    Args:
    ip (str): L'adresse IP à vérifier.
    """
    print(banner())  # Affiche la bannière au début de l'exécution
    if check_port_22(ip):
        print(f"Le port 22 est ouvert sur {ip}.")
        version = get_ssh_version(ip)
        if version:
            print(f"Version SSH: {version}")
        else:
            print("Impossible de récupérer la version SSH.")
    else:
        print(f"Le port 22 est fermé sur {ip}.")

if __name__ == "__main__":
    ip = input("Entrez l'adresse IP à vérifier: ")
    main(ip)
