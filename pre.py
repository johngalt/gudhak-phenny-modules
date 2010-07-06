import urllib2, re

def pre(phenny, input):
	search = input.split(' ')[1:]
	search = '+'.join(search)
	if not search:
		phenny.say('Sorry, you did not specify any arguments')
		return
	html = urllib2.urlopen('http://orlydb.com/?q=' + search)
	data = html.read()
	data = data.split('\n')
	html.close()
	

	reTime = re.compile('<span class="timestamp">(.*?)<\/span>', re.I)
	reSection = re.compile('<span class="section"><a href="(.*?)">(.*?)</a><\/span>', re.I)
	reRelease = re.compile('<span class="release">(.*?)<\/span>', re.I)
	reInfo = re.compile('<span class="inforight"><span class="info">(.*?)<\/span><\/span>', re.I)
	
	info = ''
	line = 0
	x = 0
	y = 0
	z = 0

	for q in data:
		line += 1
		a = reTime.match(q.lstrip())
		b = reSection.match(q.lstrip())
		c = reRelease.match(q.lstrip())
		d = reInfo.match(q.lstrip())
		if a:
			if not x:
				time = a.group(1)
				x = 1
		elif b:
			if not y:
				section = b.group(2)
				y = 1
		elif c:
			if not z:
				release = c.group(1)
				z = 1
				infonum = line
		elif d:
			if (x,y,z) == (1,1,1):
				if line == infonum + 1:
					info = d.group(1)
				else:
					info = 'No info'
					
	if release:
		phenny.say('[\00309 %s \003] %s | %s | \002%s\002' % (section, release, time, info))
	else:
		phenny.say('No results found')

pre.commands = ['pre']
pre.exmaple = '.pre Curb Your Enthusiasm'

				