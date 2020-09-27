import os,threading
from configparser import ConfigParser
from pypresence import Presence
from time import sleep
#<---Variables--->
client_id = "673492752125919243"
config_manager = ConfigParser()
version_number = '0.1'
splash = """
  _____  _                                                 
 |  __ \| |                                                
 | |__) | |__   ___  _ __   ___   __ _ _ __ __ _ _ __ ___  
 |  ___/| '_ \ / _ \| '_ \ / _ \ / _` | '__/ _` | '_ ` _ \ 
 | |    | | | | (_) | | | | (_) | (_| | | | (_| | | | | | |
 |_|    |_| |_|\___/|_| |_|\___/ \__, |_|  \__,_|_| |_| |_|
                                  __/ |                    
                                 |___/                     """

#<---Handles Startup--->
def startup():
    if os.path.exists('configs'):
        print('Found Config Folder')
    else:
        os.path('configs')
        print("Config folder not found. Created Folder.")

    if os.path.exists('settings.ini'):
        print('Found Settings File');
    else:
        with open('settings.ini','w') as fh:
            fh.write('')
            fh.close()
        print('No settings file found. Created default.')

#<---Handles Discord Presence--->
def discord_presence(boolean):
    if boolean is True:
        print('Using DiscordRPC')
        while 1:
            RPC = Presence(client_id=client_id)
            RPC.connect()
            RPC.update(details="Using Phonogram v.01",state = "Debugging",large_image="phonographicon", large_text="Phonogram Testing",small_image="activesymbol", small_text="Connected!")
            sleep(15)
    else:
        return

#<---Handles Config Loading and Parsing--->
def load_configs():
    counter = 0
    configs_names = []
    configs = os.listdir('configs')
    for x in configs:
        counter += 1
        configs_names.append(x)
    print(f'Loaded {counter} config(s)')
    print(configs_names)

def menu():
    print(splash+f'v{version_number}')
    choice = input('Welcome to Phonogram.\nPlease Select an option below.\n1)Run Module\n2)Load Modules\n3)Exit\nSelection:')

menu()