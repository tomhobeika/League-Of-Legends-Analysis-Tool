import league

def champRoleTest(champTag):
	if champTag == 'Assassin':
		return -1
	if champTag == 'Fighter':
		return 1
	if champTag == 'Mage':
		return -2
	if champTag == 'Marksman':
		return 1
	if champTag == 'Support':
		return -2
	if champTag == 'Tank':
		return 2

#Calculates
def defend(champList):
	output = ''
	#AD
	i = -1
	ad = 0
	for x in champList:
		i = i + 1
		ad = ad + league.champs['data'][champList[i]]['info']['attack']

	#AP
	i = -1
	ap = 0
	for x in champList:
		i = i + 1
		ap = ap + league.champs['data'][champList[i]]['info']['magic']

	#Boolean Definitions
	adStack = False
	apStack = False

	if ad >= ap:
		multAp = ap * 1.5
		if ad > multAp:
			adStack = True
			output = output + "This team is stacked AD. Build armor.\n"
	
	if ap >= ad:
		multAd = ad * 1.5
		if ap > multAd:
			apStack = True
			output = output + "This team is stacked AP. Build magic resist.\n"

	if not adStack and not apStack:
		output = output + "This team is evenly stacked between AD and AP. Build either armor or magic resist.\n"

	return output

def attack(champList):
	output = ''
	#HP
	i = -1
	hp = 0
	for x in champList:
		i = i + 1
		hp = hp + league.champs['data'][champList[i]]['stats']['hp']

	#Armor
	i = -1
	armor = 0
	for x in champList:
		i = i + 1
		armor = armor + league.champs['data'][champList[i]]['stats']['armor']

	#Magic Resist
	i = -1
	magicResist = 0
	for x in champList:
		i = i + 1
		magicResist = magicResist + league.champs['data'][champList[i]]['stats']['spellblock']

	#Final HP
	i = -1
	finalhp = 0
	for x in champList:
		i = i + 1
		finalhp = finalhp + ((league.champs['data'][champList[i]]['stats']['hpperlevel']*17)+league.champs['data'][champList[i]]['stats']['hp'])*league.champs['data'][champList[i]]['stats']['armor']

	#New HP
	tankScore = 0
	for x in champList:
		try:
			tempChampTags = league.champs['data'][x]['tags'][1]
			tankSCore = tankScore + champRoleTest(tempChampTags)

			tempChampTags = league.champs['data'][x]['tags'][0]  
			tankScore = tankScore + champRoleTest(tempChampTags)	
		except:
			tempChampTags = league.champs['data'][x]['tags'][0]
			tankScore = tankScore + champRoleTest(tempChampTags)

	#Boolean Definitions
	tank = False
	squishy = False
	mResist = False
	tArmor = False

	if tankScore >= 3:
		tank = True
		output = output + "This team is tanky. Build armor penetration or magic penetration.\n"
	elif tankScore <= -3:
		squishy = True
		output = output + "This team is squishy. Build lethality.\n"

	if armor > 170:
		output = output + "This team is high in armor. Build armor penetration.\n"
		tArmor = True

	if magicResist > 170:
		output = output + "This team is high in magic resist. Build magic penetration.\n"
		mResist = True

	if not tank and not squishy:
		if tankScore >= 2:
			output = output + "This team is average, but slightly more tanky.\n"
		if tankScore <= -2:
			output = output + "This team is average, but slightly more squishy.\n"
		else:
			output = output + "This team is not particularly tanky or squishy.\n"

	if not mResist and not tArmor:
		output = output + "This team does not lean particularly towards armor or magic resist.\n"

	return output

