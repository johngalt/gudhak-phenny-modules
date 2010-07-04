import urllib2,urllib
import xml.dom.minidom
import random
import socket
class Armory(object):
	"""Armory Sniffer"""
	
	def __init__(self):
		self.raiderData = {}
		self.userAgent = "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4"
			
	def _getXml(self):
		strFile = ""
		try:
			url = "http://"+self.raiderData["zone"].lower()+".wowarmory.com/character-sheet.xml?r="+self.raiderData["server"].replace(" ","+")+"&n="+self.raiderData["name"]
			values = {}
			headers = { 'User-Agent' : self.userAgent }
			data = urllib.urlencode(values)
			socket.setdefaulttimeout(2)
			req = urllib2.Request(url, data, headers)
			response = urllib2.urlopen(req)
			strFile = response.read()
		except Exception, e:
			raise e
		finally:
			return strFile
			
	def getCharacter(self,raiderName, raiderServer,raiderZone):
		
		self.raiderData["name"] = raiderName
		self.raiderData["server"] = raiderServer
		self.raiderData["zone"] = raiderZone
		
		oDoc = xml.dom.minidom.parseString( self._getXml() )
		
		self.raiderData["class"] = oDoc.getElementsByTagName("character")[0].getAttribute("class")
		self.raiderData["sex"] = oDoc.getElementsByTagName("character")[0].getAttribute("gender")
		self.raiderData["race"] = oDoc.getElementsByTagName("character")[0].getAttribute("race")
		
		self.raiderData["talents"] = [0,0,0]
		self.raiderData["talents"][0] = int( oDoc.getElementsByTagName("talentSpec")[0].getAttribute("treeOne") )
		self.raiderData["talents"][1] = int( oDoc.getElementsByTagName("talentSpec")[0].getAttribute("treeTwo") )
		self.raiderData["talents"][2] = int( oDoc.getElementsByTagName("talentSpec")[0].getAttribute("treeThree") )
		
		self.raiderData["faction"] = oDoc.getElementsByTagName("character")[0].getAttribute("faction")
		self.raiderData["battlegroup"] = oDoc.getElementsByTagName("character")[0].getAttribute("battleGroup")
		self.raiderData["guild"] = oDoc.getElementsByTagName("character")[0].getAttribute("guildName")
		self.raiderData["lastmodified"] = oDoc.getElementsByTagName("character")[0].getAttribute("lastModified")
		self.raiderData["level"] = int( oDoc.getElementsByTagName("character")[0].getAttribute("level") )
		
		self.raiderData["points"] = int( oDoc.getElementsByTagName("character")[0].getAttribute("points") )
		self.raiderData["suffix"] = oDoc.getElementsByTagName("character")[0].getAttribute("suffix")
		
		self.raiderData["lifetimehonorablekills"] = int( oDoc.getElementsByTagName("lifetimehonorablekills")[0].getAttribute("value") )
		
		self.raiderData["professions"] = [{},{}]
		try:
			self.raiderData["professions"][0]["key"] = oDoc.getElementsByTagName("skill")[0].getAttribute("key")
			self.raiderData["professions"][0]["name"] = oDoc.getElementsByTagName("skill")[0].getAttribute("name")
			self.raiderData["professions"][0]["max"] = int( oDoc.getElementsByTagName("skill")[0].getAttribute("max") )
			self.raiderData["professions"][0]["value"] = int( oDoc.getElementsByTagName("skill")[0].getAttribute("value") )
		except:
			pass
		
		try:
			self.raiderData["professions"][1]["key"] = oDoc.getElementsByTagName("skill")[1].getAttribute("key")
			self.raiderData["professions"][1]["name"] = oDoc.getElementsByTagName("skill")[1].getAttribute("name")
			self.raiderData["professions"][1]["max"] = int( oDoc.getElementsByTagName("skill")[1].getAttribute("max") )
			self.raiderData["professions"][1]["value"] = int( oDoc.getElementsByTagName("skill")[1].getAttribute("value") )
		except:
			pass
		
		self.raiderData["titles"] = []
		for title in oDoc.getElementsByTagName("title"):
			self.raiderData["titles"].append(title.getAttribute("value"))
			
		self.raiderData["stats"] = {}
		self.raiderData["stats"]["strength"] = int( oDoc.getElementsByTagName("strength")[0].getAttribute("effective") )
		self.raiderData["stats"]["agility"] = int( oDoc.getElementsByTagName("agility")[0].getAttribute("effective") )
		self.raiderData["stats"]["intellect"] = int( oDoc.getElementsByTagName("intellect")[0].getAttribute("effective") )
		self.raiderData["stats"]["stamina"] = int( oDoc.getElementsByTagName("stamina")[0].getAttribute("effective") )
		self.raiderData["stats"]["spirit"] = int( oDoc.getElementsByTagName("spirit")[0].getAttribute("effective") )
		self.raiderData["stats"]["armor"] = int( oDoc.getElementsByTagName("armor")[0].getAttribute("effective") )
		
		self.raiderData["bars"] = {}
		self.raiderData["bars"]["health"] = int( oDoc.getElementsByTagName("health")[0].getAttribute("effective") )
		self.raiderData["bars"]["secondBar"] = {}
		self.raiderData["bars"]["secondBar"]["casting"] = float( oDoc.getElementsByTagName("secondBar")[0].getAttribute("casting") )
		self.raiderData["bars"]["secondBar"]["effective"] = int( oDoc.getElementsByTagName("secondBar")[0].getAttribute("effective") )
		self.raiderData["bars"]["secondBar"]["notCasting"] = int( oDoc.getElementsByTagName("secondBar")[0].getAttribute("notCasting") )
		self.raiderData["bars"]["secondBar"]["type"] = oDoc.getElementsByTagName("secondBar")[0].getAttribute("type")
		
		self.raiderData["mele"] = {}
		self.raiderData["mele"]["power"] = int( oDoc.getElementsByTagName("power")[0].getAttribute("effective") )
		self.raiderData["mele"]["mainHandDamage"] = {}
		self.raiderData["mele"]["mainHandDamage"]["dps"] = float( oDoc.getElementsByTagName("mainHandDamage")[0].getAttribute("dps") )
		self.raiderData["mele"]["mainHandDamage"]["max"] = int( oDoc.getElementsByTagName("mainHandDamage")[0].getAttribute("max") )
		self.raiderData["mele"]["mainHandDamage"]["min"] = int( oDoc.getElementsByTagName("mainHandDamage")[0].getAttribute("min") )
		self.raiderData["mele"]["mainHandDamage"]["percent"] = float( oDoc.getElementsByTagName("mainHandDamage")[0].getAttribute("percent") )
		self.raiderData["mele"]["mainHandDamage"]["speed"] = float( oDoc.getElementsByTagName("mainHandDamage")[0].getAttribute("speed") )
		
		self.raiderData["mele"]["offHandDamage"] = {}
		self.raiderData["mele"]["offHandDamage"]["dps"] = float( oDoc.getElementsByTagName("offHandDamage")[0].getAttribute("dps") )
		self.raiderData["mele"]["offHandDamage"]["max"] = int( oDoc.getElementsByTagName("offHandDamage")[0].getAttribute("max") )
		self.raiderData["mele"]["offHandDamage"]["min"] = int( oDoc.getElementsByTagName("offHandDamage")[0].getAttribute("min") )
		self.raiderData["mele"]["offHandDamage"]["percent"] = float( oDoc.getElementsByTagName("offHandDamage")[0].getAttribute("percent") )
		self.raiderData["mele"]["offHandDamage"]["speed"] = float( oDoc.getElementsByTagName("offHandDamage")[0].getAttribute("speed") )
		
		self.raiderData["mele"]["hitRating"] = {}
		self.raiderData["mele"]["hitRating"]["value"] = int( oDoc.getElementsByTagName("hitRating")[0].getAttribute("value") )
		self.raiderData["mele"]["hitRating"]["penetration"] = int( oDoc.getElementsByTagName("hitRating")[0].getAttribute("penetration") )
		self.raiderData["mele"]["hitRating"]["increasedHitPercent"] = float( oDoc.getElementsByTagName("hitRating")[0].getAttribute("increasedHitPercent") )
		self.raiderData["mele"]["hitRating"]["reducedArmorPercent"] = float( oDoc.getElementsByTagName("hitRating")[0].getAttribute("reducedArmorPercent") )
		
		self.raiderData["mele"]["critChance"] = {}
		self.raiderData["mele"]["critChance"]["percent"] = float( oDoc.getElementsByTagName("critChance")[0].getAttribute("percent") )
		self.raiderData["mele"]["critChance"]["plusPercent"] = float( oDoc.getElementsByTagName("critChance")[0].getAttribute("plusPercent") )
		self.raiderData["mele"]["critChance"]["rating"] = int( oDoc.getElementsByTagName("critChance")[0].getAttribute("rating") )
		
		self.raiderData["mele"]["expertise"] = {}
		self.raiderData["mele"]["expertise"]["additional"] = int( oDoc.getElementsByTagName("expertise")[0].getAttribute("additional") )
		self.raiderData["mele"]["expertise"]["percent"] = float( oDoc.getElementsByTagName("expertise")[0].getAttribute("percent") )
		self.raiderData["mele"]["expertise"]["rating"] = int( oDoc.getElementsByTagName("expertise")[0].getAttribute("rating") )
		self.raiderData["mele"]["expertise"]["value"] = int( oDoc.getElementsByTagName("expertise")[0].getAttribute("value") )
		
		
		self.raiderData["ranged"] = {}
		self.raiderData["ranged"]["weaponSkill"] = {}
		self.raiderData["ranged"]["weaponSkill"]["rating"] = int( oDoc.getElementsByTagName("weaponSkill")[0].getAttribute("rating") )
		self.raiderData["ranged"]["weaponSkill"]["value"] = int( oDoc.getElementsByTagName("weaponSkill")[0].getAttribute("value") )
		self.raiderData["ranged"]["damage"] = {}
		self.raiderData["ranged"]["damage"]["dps"] = float( oDoc.getElementsByTagName("damage")[0].getAttribute("dps") )
		self.raiderData["ranged"]["damage"]["max"] = int( oDoc.getElementsByTagName("damage")[0].getAttribute("max") )
		self.raiderData["ranged"]["damage"]["min"] = int( oDoc.getElementsByTagName("damage")[0].getAttribute("min") )
		self.raiderData["ranged"]["damage"]["percent"] = float( oDoc.getElementsByTagName("damage")[0].getAttribute("percent") )
		self.raiderData["ranged"]["damage"]["speed"] = float( oDoc.getElementsByTagName("damage")[0].getAttribute("speed") )
		
		self.raiderData["ranged"]["power"] = int( oDoc.getElementsByTagName("power")[0].getAttribute("effective") )
		self.raiderData["ranged"]["hitRating"] = {}
		self.raiderData["ranged"]["hitRating"]["value"] = int( oDoc.getElementsByTagName("hitRating")[1].getAttribute("value") )
		self.raiderData["ranged"]["hitRating"]["penetration"] = int( oDoc.getElementsByTagName("hitRating")[1].getAttribute("penetration") )
		self.raiderData["ranged"]["hitRating"]["increasedHitPercent"] = float( oDoc.getElementsByTagName("hitRating")[1].getAttribute("increasedHitPercent") )
		self.raiderData["ranged"]["hitRating"]["reducedArmorPercent"] = float( oDoc.getElementsByTagName("hitRating")[1].getAttribute("reducedArmorPercent") )
		
		self.raiderData["ranged"]["critChance"] = {}
		self.raiderData["ranged"]["critChance"]["percent"] = float( oDoc.getElementsByTagName("critChance")[1].getAttribute("percent") )
		self.raiderData["ranged"]["critChance"]["plusPercent"] = float( oDoc.getElementsByTagName("critChance")[1].getAttribute("plusPercent") )
		self.raiderData["ranged"]["critChance"]["rating"] = int( oDoc.getElementsByTagName("critChance")[1].getAttribute("rating") )
		
		self.raiderData["spell"] = {}
		self.raiderData["spell"]["bonusDamage"] = {}
		self.raiderData["spell"]["bonusDamage"]["arcane"] = int( oDoc.getElementsByTagName("arcane")[1].getAttribute("value") )
		self.raiderData["spell"]["bonusDamage"]["fire"] = int( oDoc.getElementsByTagName("fire")[1].getAttribute("value") )
		self.raiderData["spell"]["bonusDamage"]["frost"] = int( oDoc.getElementsByTagName("frost")[1].getAttribute("value") )
		self.raiderData["spell"]["bonusDamage"]["holy"] = int( oDoc.getElementsByTagName("holy")[1].getAttribute("value") )
		self.raiderData["spell"]["bonusDamage"]["nature"] = int( oDoc.getElementsByTagName("nature")[1].getAttribute("value") )
		self.raiderData["spell"]["bonusDamage"]["shadow"] = int( oDoc.getElementsByTagName("shadow")[1].getAttribute("value") )
		
		self.raiderData["spell"]["bonusHealing"] = int( oDoc.getElementsByTagName("bonusHealing")[0].getAttribute("value") )
		
		self.raiderData["spell"]["penetration"] = int( oDoc.getElementsByTagName("penetration")[0].getAttribute("value") )
		
		self.raiderData["spell"]["hitRating"] = {}
		self.raiderData["spell"]["hitRating"]["increasedHitPercent"] = float( oDoc.getElementsByTagName("hitRating")[2].getAttribute("increasedHitPercent") )
		self.raiderData["spell"]["hitRating"]["penetration"] = int( oDoc.getElementsByTagName("hitRating")[2].getAttribute("penetration") )
		self.raiderData["spell"]["hitRating"]["reducedResist"] = float( oDoc.getElementsByTagName("hitRating")[2].getAttribute("reducedResist") )
		self.raiderData["spell"]["hitRating"]["value"] = int( oDoc.getElementsByTagName("hitRating")[2].getAttribute("value") )
		
		self.raiderData["spell"]["critChance"] = {}
		self.raiderData["spell"]["critChance"]["rating"] = int( oDoc.getElementsByTagName("critChance")[2].getAttribute("rating") )
		self.raiderData["spell"]["critChance"]["arcane"] = float( oDoc.getElementsByTagName("arcane")[2].getAttribute("percent") )
		self.raiderData["spell"]["critChance"]["fire"] = float( oDoc.getElementsByTagName("fire")[2].getAttribute("percent") )
		self.raiderData["spell"]["critChance"]["frost"] = float( oDoc.getElementsByTagName("frost")[2].getAttribute("percent") )
		self.raiderData["spell"]["critChance"]["holy"] = float( oDoc.getElementsByTagName("holy")[2].getAttribute("percent") )
		self.raiderData["spell"]["critChance"]["nature"] = float( oDoc.getElementsByTagName("nature")[2].getAttribute("percent") )
		self.raiderData["spell"]["critChance"]["shadow"] = float( oDoc.getElementsByTagName("shadow")[2].getAttribute("percent") )
		
		self.raiderData["spell"]["manaRegen"] = {}
		self.raiderData["spell"]["manaRegen"]["casting"] = float( oDoc.getElementsByTagName("manaRegen")[0].getAttribute("casting") )
		self.raiderData["spell"]["manaRegen"]["notCasting"] = float( oDoc.getElementsByTagName("manaRegen")[0].getAttribute("notCasting") )
		
		self.raiderData["spell"]["hasteRating"] = {}
		self.raiderData["spell"]["hasteRating"]["hastePercent"] = float( oDoc.getElementsByTagName("hasteRating")[0].getAttribute("hastePercent") )
		self.raiderData["spell"]["hasteRating"]["hasteRating"] = int( oDoc.getElementsByTagName("hasteRating")[0].getAttribute("hasteRating") )
		
		self.raiderData["resistances"] = {}
		self.raiderData["resistances"]["arcane"] = int( oDoc.getElementsByTagName("arcane")[0].getAttribute("value") )
		self.raiderData["resistances"]["fire"] = int( oDoc.getElementsByTagName("fire")[0].getAttribute("value") )
		self.raiderData["resistances"]["frost"] = int( oDoc.getElementsByTagName("frost")[0].getAttribute("value") )
		self.raiderData["resistances"]["holy"] = int( oDoc.getElementsByTagName("holy")[0].getAttribute("value") )
		self.raiderData["resistances"]["nature"] = int( oDoc.getElementsByTagName("nature")[0].getAttribute("value") )
		self.raiderData["resistances"]["shadow"] = int( oDoc.getElementsByTagName("shadow")[0].getAttribute("value") )
		
		self.raiderData["defenses"] = {}
		self.raiderData["defenses"]["defense"] = {}
		self.raiderData["defenses"]["defense"]["decreasePercent"] = float( oDoc.getElementsByTagName("defense")[0].getAttribute("decreasePercent") )
		self.raiderData["defenses"]["defense"]["increasePercent"] = float( oDoc.getElementsByTagName("defense")[0].getAttribute("increasePercent") )
		self.raiderData["defenses"]["defense"]["plusDefense"] = int( oDoc.getElementsByTagName("defense")[0].getAttribute("plusDefense") )
		self.raiderData["defenses"]["defense"]["rating"] = int( oDoc.getElementsByTagName("defense")[0].getAttribute("rating") )
		self.raiderData["defenses"]["defense"]["value"] = float( oDoc.getElementsByTagName("defense")[0].getAttribute("value") )
		self.raiderData["defenses"]["dodge"] = {}
		self.raiderData["defenses"]["dodge"]["increasePercent"] = float( oDoc.getElementsByTagName("dodge")[0].getAttribute("increasePercent") )
		self.raiderData["defenses"]["dodge"]["percent"] = float( oDoc.getElementsByTagName("dodge")[0].getAttribute("percent") )
		self.raiderData["defenses"]["dodge"]["rating"] = int( oDoc.getElementsByTagName("dodge")[0].getAttribute("rating") )
		self.raiderData["defenses"]["parry"] = {}
		self.raiderData["defenses"]["parry"]["increasePercent"] = float( oDoc.getElementsByTagName("parry")[0].getAttribute("increasePercent") )
		self.raiderData["defenses"]["parry"]["percent"] = float( oDoc.getElementsByTagName("parry")[0].getAttribute("percent") )
		self.raiderData["defenses"]["parry"]["rating"] = int( oDoc.getElementsByTagName("parry")[0].getAttribute("rating") )
		self.raiderData["defenses"]["block"] = {}
		self.raiderData["defenses"]["block"]["increasePercent"] = float( oDoc.getElementsByTagName("block")[0].getAttribute("increasePercent") )
		self.raiderData["defenses"]["block"]["percent"] = float( oDoc.getElementsByTagName("block")[0].getAttribute("percent") )
		self.raiderData["defenses"]["block"]["rating"] = int( oDoc.getElementsByTagName("block")[0].getAttribute("rating") )
		self.raiderData["defenses"]["resilience"] = {}
		self.raiderData["defenses"]["resilience"]["damagePercent"] = float( oDoc.getElementsByTagName("resilience")[0].getAttribute("damagePercent") )
		self.raiderData["defenses"]["resilience"]["hitPercent"] = float( oDoc.getElementsByTagName("resilience")[0].getAttribute("hitPercent") )
		self.raiderData["defenses"]["resilience"]["value"] = float( oDoc.getElementsByTagName("resilience")[0].getAttribute("value") )
		
		
		
		self.raiderData["items"] = []
		for item in oDoc.getElementsByTagName("item"):
			itemd = {}
			itemd["id"] = int( item.getAttribute("id") )
			itemd["durability"] = int( item.getAttribute("durability") )
			itemd["maxdurability"] = int( item.getAttribute("maxDurability") )
			itemd["icon"] = item.getAttribute("icon")
			itemd["slot"] = int( item.getAttribute("slot") )
			itemd["seed"] = int( item.getAttribute("seed") )
			itemd["permanentenchant"] = int( item.getAttribute("permanentenchant") )
			itemd["randomPropertiesId"] = int( item.getAttribute("randomPropertiesId") )
			
			itemd["gems"] = []
			try:
				itemd["gems"].append( int( item.getAttribute("gem0Id") ) )
				itemd["gems"].append( int( item.getAttribute("gem1Id") ) )
				itemd["gems"].append( int( item.getAttribute("gem2Id") ) )
			except:
				pass
				
			self.raiderData["items"].append(itemd)
			
		return self.raiderData