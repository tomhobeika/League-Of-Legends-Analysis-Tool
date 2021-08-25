import json

#Calculates
def calculateDefend(champList):
	#AD
	i = -1
	ad = 0
	for x in champList:
		i = i + 1
		ad = ad + league.champs['data'][champList[i]]['info'][attack]

	#HP
	i = -1
	hp = 0
	for x in champList:
		i = i + 1
		hp = hp + league.champs['data'][champList[i]]['hp']

	#AP
	i = -1
	ap = 0
	for x in champList:
		i = i + 1
		ap = ap + league.champs['data'][champList[i]]['info'][magic]

	#Armor
	i = -1
	armor = 0
	for x in champList:
		i = i + 1
		armor = armor + league.champs['data'][champList[i]]['armor']

	'''#HP
	i = -1
	for x in champList:
		i = i + 1
		hp = hp + league.champs['data'][champList[i]]['info'][magic]'''

	print("AD: "+ad)
	print("AP: "+ap)


def calculateAttack(champList):
	print("YAY")

	
#Opens Riot's champion data JSON
f = open('champion.json', encoding="utf8")
champs = json.load(f) # TODO Get this information straight from Riot servers

f.close()


