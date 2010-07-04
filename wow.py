from armory import Armory
from xml.parsers.expat import ExpatError

def wow(phenny, input):
	if not input:
		# return 'Invalid Syntax. Proper syntax: .wow Name @Realm @US/EU'
		phenny.say('Invalid Syntax. Proper syntax: .wow Name @Realm @US/EU')
	else:
		input = input.split(' ')
		input = ' '.join(input[1:])
		input = input.split('@')
		if input[0]:
			charName = input[0].upper()
		if input[1]:
			charRealm = input[1].rstrip()
		if input[2]:
			charRegion = input[2]
		if not input[0]:
			phenny.say('Invalid Syntax. Proper syntax: .wow Name @Realm @US/EU')
		else:
			# return 'Char Name: ' + charName + ' | Char Realm: ' + charRealm + ' | Char Region: ' + charRegion
			try:
				char = Armory().getCharacter(charName, charRealm, charRegion)
			except ExpatError:
				# return 'Error in retrieving character information'
				phenny.say('Error in retrieving character information')
				return
			except IndexError:
				phenny.say('Error in retrieving character information')
				return
			charTalents = '/'.join(map(str, char['talents']))
			charProf = ''
			for x in char['professions']:
				try:
					charProf += '%s: \00307%s\003 ' % (x['name'], x['value'])
				except KeyError:
					charProf += "No Skill "
					
			# TODO: add class specific skills; add rly.cc armory link
			phenny.say('--> (\00309 %s \003): \00309%s %s %s\003 (\00307%s\003) | Guild:\00309 %s \003' % (charName, char['level'], char['race'], char['class'], charTalents, char['guild']))
			phenny.say('--> (\00309 %s \003): H: \00309%s\003 %s: \00309%s\003 | %s | HKs:\00309 %s\003 | Resil:\00309 %s\003 | Achievs:\00309 %s\003' % (charName, char['bars']['health'], char['bars']['secondBar']['type'].upper(), char['bars']['secondBar']['effective'], charProf, char['lifetimehonorablekills'], char['defenses']['resilience']['value'], char['points']))
			phenny.say('--> (\00309 %s \003): Agility: \00309%s\003 | Strength: \00309%s\003 | Armor: \00309%s\003 | Spirit: \00309%s\003 | Stamina: \00309%s\003 | Intellect: \00309%s\003 | Spell Power: \00309%s\003 | Haste: \00309%s\003 | Spell Hit: \00309%s\003 | Melee Hit: \00309%s\003 | Ranged Hit: \00309%s\003' % (char['class'].upper(), char['stats']['agility'], char['stats']['strength'], char['stats']['armor'], char['stats']['spirit'], char['stats']['stamina'], char['stats']['intellect'], char['spell']['bonusHealing'], char['spell']['hasteRating']['hasteRating'], char['spell']['hitRating']['value'], char['mele']['hitRating']['value'], char['ranged']['hitRating']['value']))

wow.commands = ['wow']
wow.example = '.wow Taggart @Lightning\'s Blade @US'
