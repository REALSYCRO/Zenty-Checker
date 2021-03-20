import json
import sys
import pyfiglet
from datetime import datetime
from dhooks import Webhook, Embed, File
from colorama import Fore, init
init(convert=True)
import os
import requests
import time
import getpass
from console.utils import set_title


set_title(f"Zenty Checker | by Zenty")

logo = f"""{Fore.RED}


███████╗███████╗███╗   ██╗████████╗██╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══███╔╝██╔════╝████╗  ██║╚══██╔══╝╚██╗ ██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
  ███╔╝ █████╗  ██╔██╗ ██║   ██║    ╚████╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
 ███╔╝  ██╔══╝  ██║╚██╗██║   ██║     ╚██╔╝      ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████╗███████╗██║ ╚████║   ██║      ██║       ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝      ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                        
{Fore.RESET}"""

print(logo)

print(f"{Fore.CYAN}Pls enter a mail:{Fore.RESET}")

Username = input("")

print(f"{Fore.GREEN}Mail was successfully saved.{Fore.RESET}")

print(f"{Fore.CYAN}Pls enter a password:{Fore.RESET}")

Password = getpass.getpass("")

payload = {'agent':{'name':'Minecraft', 'version':1},
'username':Username,
'password':Password}

print(f"{Fore.GREEN}Password was successfully saved.{Fore.RESET}")

print(f"{Fore.CYAN}Please enter a proxy. If you do not want to insert a proxy, please only enter a 1.{Fore.RESET}")

proxy = (input(""))

proxies = {"https": f"http://{proxy}"}



if proxy == "1":

	print(f"{Fore.GREEN}You have not selected a proxy.{Fore.RESET}")

	print(f"{Fore.BLUE}Login is being processed ...{Fore.RESET}")

	
	try:

		res = requests.post("https://authserver.mojang.com/authenticate", json=payload)



		if "error" in res.text:

			print(f"""{Fore.RED}[-]BAD{Fore.RESET}""")

		if "accessToken" in res.text:

			user = res.json()

			#user = ['availableProfiles']['name']

			print(f"""{Fore.GREEN}[+]GOOD {Fore.RESET}""" + Username + ":" + Password)

			try:

				hype = requests.post("https://api.slothpixel.me/api/players/" + user['name'])

				if "error" in hype.text:

						print("Can't find Hypixel Stats!")

				if "uuid" in hype.text:

					#BedWarsKills = hype["player"] ["stats"] ["BedWars"] ["kills"]

					hype_data = hype.json()

					print(user["availableProfiles"]["name"] + ":" + " [+]BedWarsKills: " + hype_data["kills"])




			except Exception as e:

				print(f"{Fore.RED}Couldn't get Hypixel Stats.{Fore.RESET}")

				print(e)

				input("")
	

	except:
		print(f"{Fore.RED}Something went wrong.{Fore.RESET}")

		ende = input("Pls press the Enter key.")


else:

	proxies = {"https": f"http://{proxy}"}

	print(f"{Fore.GREEN}Proxy successfully saved.{Fore.RESET}")

	print(f"{Fore.BLUE}Login is being processed...{Fore.RESET}")

	try:

		res = requests.post("https://authserver.mojang.com/authenticate", proxies=proxies, json=payload, timeout=1000)



		if "error" in res.text:

			print(f"""{Fore.RED}[-]BAD{Fore.RESET}""")

		if "accessToken" in res.text:

			hype = requests.post("https://api.slothpixel.me/api/players/" + Username)

			print(hype.text)

			print(f"""{Fore.GREEN}[+]GOOD {Fore.RESET}""" + Username + ":" + Password)
	

	except:

		print(f"{Fore.RED}Proxy is bad!{Fore.RESET}")

		ende = input("Pls press the Enter key.")
