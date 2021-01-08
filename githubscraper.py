import time
import requests
import json
import os
import colorama
from pprint import pprint
import platform
import sys
from colorama import Fore
wi = Fore.WHITE
rd = Fore.RED
yl = Fore.YELLOW
mg = Fore.MAGENTA
gr = Fore.GREEN
cy = Fore.CYAN
os_sys = platform.system()
def help():
    help = print(wi + gr + '''
    =============================================
    +|           GitHub Profile Scraper        |+
    =============================================
    +|  M a d e    By    F o n d e r E l i t e |+
    +|-----------------------------------------|+
    +|      -h          Help                   |+
    +|      -s         Start Scraping          |+
    +|      -u         Username                |+
    +|      -c         Check Files             |+
    +|      -up        Update                  |+
    +|      -q         Quit                    |+
    +|      Ex   ./githubscraper -u -s (Start)  |+
     ===========================================
     ''')
def choice():
    sure = ['y','n']
    choice = input("Are You Sure? y/n: ")
    if choice == sure[0]:
        time.sleep(1)
        print(Fore.YELLOW + "(っ◔◡◔)っ ♥ Quitting.... ♥")
        sys.exit()
    else:
        print(Fore.RED + 'Cancelled.')

def scrape():
    user = input('Input a username: ')
    time.sleep(1)
    print(Fore.YELLOW + f'Scraping Github-User: {user}')
    time.sleep(2)
    scrape = requests.get(f'https://api.github.com/users/{user}')
    scraped = scrape.json()
    save = open('user-details.txt','w+')
    saved = save.write(str(scraped))
    time.sleep(2)
    pprint(scraped)
    print(Fore.CYAN + 'Saving Details to user-details.txt')
    print(wi + gr + 'DONE!!!')

def username():
    userr = input('Input a username: ')
    time.sleep(1)
    print(Fore.YELLOW + f'Validating Github-User: {userr}')
    time.sleep(2)
    scrapee = requests.get(f'https://api.github.com/users/{userr}')
    scrapedd = scrapee.status_code
    if scrapedd == 200:
     print(Fore.GREEN + 'User is Valid!')
    else:
     print(Fore.RED + 'Invalid User!!!')
     print(yl + "Either user is not on Github or account was deleted.")
    time.sleep(2)

def checkfile():
 file1 = os.path.exists('githubscraper.py')
 file2 = os.path.exists('requirements.txt')
 file3 = os.path.exists('bash.sh')
 file4 = os.path.exists('README.md')
 file5 = os.path.exists("LICENSE")
 if file1 and file2 and file3 and file4 and file4 and file5 == True:
    print(mg + 'Checking if all files are present')
    time.sleep(2)
    print(cy + "Files Are Safe!")
 else:
     print(rd +  "Some Files are missing!")
     print(yl + "Please consider checking your files again.")
def banner():
    print(Fore.CYAN + '''
          ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀G I T H U B
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀SCRAPER
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀Scrape Github Account details
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀Using this tool!
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⠀⠀⠀
                                                                                                           
        ''')
banner()
time.sleep(2)
helpme = print(wi + gr + ''' 
=============================================
+|           GitHub Profile Scraper        |+
=============================================
+|  M a d e    By    F o n d e r E l i t e |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -s         Start Scraping          |+
+|      -u         Username                |+
+|      -c         Check Files             |+
+|      -u         Update                  |+
+|      -q         Quit                    |+
+|      Ex   ./gs -u -s            (Scrape)|+
 ===========================================
 ''')
print(yl + '''
Made By FonderElite || Droid
Visit My Github Page: https://github.com/Fonderelite
''')
while True:
 command = input(gr + '[+]' + Fore.RED + os_sys + "-User: ")
 if command == './githubscrape -h':
     print(wi + gr + ''' 
     =============================================
     +|           GitHub Profile Scraper        |+
     =============================================
     +|  M a d e    By    F o n d e r E l i t e |+
     +|-----------------------------------------|+
     +|      -h          Help                   |+
     +|      -s         Start Scraping          |+
     +|      -u         Username                |+
     +|      -c         Check Files             |+
     +|      -up        Update                  |+
     +|      -q         Quit                    |+
     +|      Ex   ./gs -u -s   (Start Scraping) |+
      ===========================================
      ''')
 elif command == './gs -q':
   choice()
 elif command == './gs -u -s':
    scrape()
 elif command == './gs -u':
     username()
 elif command == './gs -c':
     checkfile()
 elif command == './gs -up':
     sys.stdout.write('\r cloning to the repository.')
     time.sleep(1)
     sys.stdout.write('\r cloning to the repository..')
     time.sleep(1)
     sys.stdout.write('\r Cloning to the repository...')
     time.sleep(1)
     os.system('git clone https://github.com/fonderelite/Github-Scraper\n')
     print(gr + ' Done!!!')
 else:
     for i in range(1):
        print(Fore.RED + '''
 ___  __   __   __    __           
|__  |__) |__) /  \ |__)      
|___ |  \ |  \ \__/ |  \      ''')
        print(Fore.BLUE + '''
           __n__n__
    .------`-/00/-'
   /  ##  ## (oo)   Please Try Again.
  / \## __   ./
     |//YY \|/
     |||   |||   \|/
               ''')
