


'''
Dev Notes: 

Type: Issues/Problems

Dodge input has an inherent issue of fetching keypress
even if the key is pressed much sooner than intended. This allows player
to pre-press the key and always succeed in dodging. Precisely timed keypress
MIGHT be acheivable using msvcrt module but the module seems to hold no regards
for time or effort and refuses to work.

On a side thought, the issue might be because of sleep module, not readchar or the input()
method. That being said, the sleep module is fundamnetally what drives the program, hence it
remains a problem nevertheless.

Type: Compatibility

Python 3.x interpreter with 'pip' to install modules.
Not tested on Linux or MacOS. Likely incompatible with either.

Type: Project Purpose

This project essentially pushes the terminal output to it's limits. It will never be used to
generate real time images hence the program is destined to die here, althought not without
fulfilling its purpose. The input and the interface of the command line have been thoroughly
utilized and tested to their boundaries. It is more of a learning experience than it is a 
well thought-out project.
'''


#Made by: Zia Ahmed Khan
#No additional resources used (except Google for troubleshooting)

#import required modules
#Note: readchar,colorama are not preinstalled in python

"""To install external modules (colorama and readchar):
Win + R to open Run Window
Type 'cmd' and press Enter
Terminal window will open
Type 'pip install colorama'
Press Enter
Type 'pip install readchar'
Press Enter

Then the program should work properly""" 

import random
import time
import colorama
import readchar

#msvcrt module may be used instead of readchar but it did not work, hence used readchar

from colorama import Fore, Back, Style
rd=readchar
colorama.init(autoreset=True)

#Starting variable assignement for later use

u=False
s=3
turn=3
p=3

#Explaination part

input("\t\t\t\t\t\tPress Enter to begin")
print("Your Health=", Fore.GREEN+"♥♥♥")
print("Enemy Health=", Fore.RED+"♥♥♥")
print("\t\t\t\t\t\tPress Enter to dodge when \"Now!\" is prompted.")
input("\t\t\t\t\t\tPress Enter to continue")
print("\t\t\t\t\t\tAfter dodging opponent, you can attack with either a kick or a punch")
print("\t\t\t\t\t\tPress p to punch and k to kick")
input("\t\t\t\t\t\tPress Enter when ready")

#Enemy ASCII Art

print(Fore.RED+"""								 . .                                             
                                                ,%(%*                                               
                                                /(&((                                               
                                                .(((,                                               
                                           ....,,/#/**,,*,                                          
                                          .,,***/(#((//,%/,                                         
                                          ,(%#,/#(/(#**%%#(*                                        
                                         /(* *,,((##(**/  (#/                                       
                                        *((   ,/*(#(/(((   (((                                      
                                        *(.  .@@@@@@@@@@    ((#                                     
                                       ,@&   &@@@@@@@@@@#   /*&.                                    
                                       (#&& /@@@@@@@@@@@@, /.&&(                                    
                                       /(#  %@@@@@@@@@@@@@                                          
                                            &@@@@@ @@@@@@@*                                         
                                           /&@@@@@ @@@@@@@(                                         
                                             (#(/     */((                                          
                                            ,(#(       .((/                                         
                                            *##(        (((,                                        
                                            .#(.        .((*                                        
                                             (#          ((*                                        
                                             (#          .#*                                        
                                          ,*/#(.         .//*,  

                                          AN ENEMY HAS APPEARED""")

#Game Start

while turn>0:
	for i in range (0,5):
		r=random.randint(1,5)
		print("\n\t\t\t\t\t\tGet ready!")
		time.sleep(r)
		print(Fore.RED+"\n\t\t\t\t\t\tNow!")
		b=time.time()
		parry=input()
		z=time.time()	
		c=z-b
		if c<0.5:
			print(Fore.GREEN+"\n\t\t\t\t\t\tSucessful dodge")
			print("Your Health=", Fore.GREEN+(s*"♥"))
			print("Enemy Health=", Fore.RED+(p*"♥"))
		else:
			print(Fore.RED+"\n\t\t\t\t\t\tFailed dodge-♥")
			s=s-1
			print("Your Health=", Fore.GREEN+(s*"♥"))
			print("Enemy Health=", Fore.RED+(p*"♥"))
		if s<1:
			u=True
			break
	for y in range (0,5):
		if u:
			print(Fore.RED+"\n\t\t\t\t\t\tYou lost.")
			opa=input()
			break
		else:
			r=random.randint(1,5)
			
			op=random.randint(1,2)
			print("\t\t\t\t\t\tYour move!")
			time.sleep(r)
			print(Fore.RED+"\n\t\t\t\t\t\tNow!")
			ch=rd.readkey()
			if ch=='k' and op==1:
				print(Fore.GREEN+"\t\t\t\t\t\tSuccessful Kick")
				p=p-1
				print("Your Health=", Fore.GREEN+(s*"♥"))
				print("Enemy Health=", Fore.RED+(p*"♥"))
			elif ch=='k' and op==2:
				print(Fore.RED+"\t\t\t\t\t\tFailed Kick")
				print("Your Health=", Fore.GREEN+(s*"♥"))
				print("Enemy Health=", Fore.RED+(p*"♥"))
			elif ch=='p' and op==1:
				print(Fore.RED+"\t\t\t\t\t\tFailed Punch")
				print("Your Health=", Fore.GREEN+(s*"♥"))
				print("Enemy Health=", Fore.RED+(p*"♥"))
			elif ch=='p' and op==2:
				print(Fore.GREEN+"\t\t\t\t\t\tSuccessful Punch")
				p=p-1
				print("Your Health=", Fore.GREEN+(s*"♥"))
				print("Enemy Health=", Fore.RED+(p*"♥"))
			elif ch!='p' and ch!='k':
				print("Invalid Input")
				break
			if p<1:
				print(Fore.GREEN+"\t\t\t\t\t\tOpponent down!")
				break

	if s>0 and p<1:
		print(Fore.BLUE+"\t\t\t\t\t\t\t!!You won!!")
		opa=input()
		break
	else:
		print(Fore.RED+"\t\t\t\t\t\t----!!Next Round!!----")
		turn=turn-1
		continue