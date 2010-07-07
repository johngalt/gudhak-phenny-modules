import urllib2, re

def realm(phenny, input):
	realm = input.split(' ')[1:]
	realm = ' '.join(show)
	realm = realm.replace('\'', '&#039;')
	if not realm:
		phenny.say('Please supply a realm name')
		return
	
	html = urllib2.urlopen('http://www.worldofwarcraft.com/realmstatus/compat.html')
	data = html.read()
	data = data.split('\n')
	html.close()

	reg = re.compile('<td class = "serverStatus1" NOWRAP><b class = "smallBold" style = "color: (.*?)">' + realm + '<\/b><\/span><\/td>', re.I)
	
	status = None
	verify = 0
	
	for x in data:
		a = reg.match(x.lstrip())
		if a:
			status = a.group(1)
			verify = 1
			
	if verify:
		if status == '#234303':
			phenny.say('[Realm] ' + realm + ' is \00309\002UP\002\003')
		else:
			phenny.say('[Realm] ' + realm + ' is \00304\002DOWN\002\003')
	else:
		phenny.say('[Realm] invalid realm')
		
realm.commands = ['realm']
realm.example = ".realm Lightning's Blade"