import requests
from colorama import Fore

# The possible urls for skånetrafiken Login page. 
# For the most part, the one that ends with .1 is on bus, .2 is on train.
urls = ["http://172.16.0.2/portal.php", "http://172.16.0.1/portal.php"]  

# Post data to send to the login page.
data = {"connect": ""}

session = requests.Session()

for url in urls:
    try:
        getresp = session.get(url, timeout=5)
        if (getresp.status_code == 200):
            print(Fore.BLUE + "[+] Found login host(%s). Attempting to connect...".format(url))
            postresp = session.post(url, data=data, timeout=5)
            if (postresp.status_code == 200):
                print(Fore.GREEN + "[+] Successfully logged in to the network.\n[+] Recieving internet connection efter login may take upto 30 seconds, be patient...\n")
                input(Fore.WHITE + "Press enter to exit.")
                exit(0)
    except:
        if urls.index(url) == 0:
            print(Fore.RED + "[i] Host %s is not reachable, attempting %s".format(url, urls[1]))
            continue

input(Fore.YELLOW + "[-] Could not connect to host. \n\n" + Fore.WHITE + "Press enter to exit.")