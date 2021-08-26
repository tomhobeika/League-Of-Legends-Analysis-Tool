import league
import calculate
from colorama import Fore, Back, Style,init
from tabulate import tabulate
import os

version = '1.0.2'

#Puncuation Destroyer
def puncDestroy(word):
	letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	output = ""
	for x in word:
		if x in letters:
			output = output + x
	return output

def puncDestroySpaced(word):
	letters = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	output = ""
	for x in word:
		if x in letters:
			output = output + x
	return output

#Determine Range
def champRange(range):
	if range >= 450:
		return "Ranged"
	else:
		return "Melee"

# Initializes Colorama
init(autoreset=True)
champList = []

#Main
print(Fore.YELLOW+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(Fore.CYAN+'                   Welcome To The')
print(Fore.CYAN+'          League Of Legends Analysis Tool')
print(Fore.RED+'                       V{}'.format(version))
print(Fore.YELLOW+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("To use this tool, enter the 5 champions on the enemy")
print("team, either one by one, or seperated my commas, and")
print("an analysis of their composition will be displayed.\n")

while len(champList) < 5:
	champIn = input("Please enter {} more champions: ".format(5 - len(champList)))
	splitChamps = champIn.split(",")
	for x in splitChamps:
		x = puncDestroySpaced(x)
		x = x.title()
		x = puncDestroy(x)
		if x in league.champs['data']:
			champList.append(puncDestroy(x))

print("\nHere are the base stats for the 5 champions you are")
print("going up against:\n")

#Sets the tags for each selected champion
tagList = []
j = 0
for x in champList:
	try:
		tempChampTags = league.champs['data'][champList[j]]['tags'][0] + "/" + league.champs['data'][champList[j]]['tags'][1]
	except:
		tempChampTags = league.champs['data'][champList[j]]['tags'][0]

	tagList.append(tempChampTags)
	j = j + 1

#Adds each Champion to the dataset
data = []
i = -1
for x in champList:
	i = i + 1
	tempChamp = [league.champs['data'][champList[i]]['name'] , 
		league.champs['data'][champList[i]]['stats']['hp'] , 
		league.champs['data'][champList[i]]['stats']['hpperlevel']*17+league.champs['data'][champList[i]]['stats']['hp'] ,
		league.champs['data'][champList[i]]['stats']['armor'] , 
		league.champs['data'][champList[i]]['stats']['spellblock'] , 
		league.champs['data'][champList[i]]['info']['attack'],
		league.champs['data'][champList[i]]['info']['magic'],
		champRange(league.champs['data'][champList[i]]['stats']['attackrange']), 
		tagList[i]]
	data.append(tempChamp)

head = ["Name","HP","Final HP","Armor","MR","AD","AP","Range", "Role"]
print(tabulate(data,headers=head,tablefmt="grid"))

print(Fore.CYAN+"To DEFEND against this team comp, you should build:")
print(calculate.defend(champList))

print(Fore.RED+"To ATTACK against this team comp, you should build:")
print(calculate.attack(champList))

os.system('pause')