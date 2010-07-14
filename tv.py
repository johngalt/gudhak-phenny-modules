import urllib2

def tv(phenny, input):
	show = input.split(' ')[1:]
	show = ' '.join(show)
	if not show:
		phenny.reply('Sorry, you did not supply a show name')
	else:
		show = show.replace(' ', '%20')
		html = urllib2.urlopen('http://services.tvrage.com/tools/quickinfo.php?show=' + show).read()
		data = html.split('\n')
		z = 0
		
		for x in data:
			y = x.split('@')
			if y[0] == 'Show Name':
				showName = y[1]
			elif y[0] == 'Premiered':
				showPremiered = y[1]
			elif y[0] == 'Started':
				showStarted = y[1]
			elif y[0] == 'Ended':
				if y[1]:
					showEnded = y[1]
				else:
					showEnded = 'Still Running'
			elif y[0] == 'Country':
				showCountry = y[1]
			elif y[0] == 'Genres':
				showGenres = y[1]
			elif y[0] == 'Network':
				showNetwork = y[1]
			elif y[0] == 'Airtime':
				showAirTime = y[1]
			elif y[0] == 'Runtime':
				showRunTime = y[1]
	
		phenny.say('\002TV -->\002 \037Show Name:\037 ' + showName + ' | \037Premiered:\037 ' + showPremiered + ' | \037Started:\037 ' + showStarted + ' | \037Ended:\037 ' + showEnded + ' | \037Country:\037 ' + showCountry)
		phenny.say('\037Genres:\037 ' + ', '.join(showGenres.split('|')) + ' | \037Network:\037 ' + showNetwork + ' | \037Airtime:\037 ' + showAirTime)
		
tv.commands = ['tv']
tv.example = '.tv House'

def next(phenny, input):
    show = input.split(' ')[1:]
    show = ' '.join(show)
    if not show:
        phenny.reply('Sorry, you did not supply a show name')
    else:
        show = show.replace(' ', '%20')
        html = urllib2.urlopen('http://services.tvrage.com/tools/quickinfo.php?show=' + show).read()
        data = html.split('\n')
        z = 0
	showName,showNextRaw = None, None
		
        for x in data:
            y = x.split('@')
            if y[0] == 'Show Name':
                showName = y[1]
            elif y[0] == 'Next Episode':
                showNextRaw =  y[1]
	if showNextRaw:
		showNext = showNextRaw.split('^')
	else:
		showNext = None

        if not showName:
            phenny.say('Could not find tv show with that name')
        elif not showNext[0]:
            phenny.say('Next episode is not available')
        else:
            phenny.say('\002Next -->\002 The next episode of\037 ' + showName + '\037 is \037' + showNext[1] + '\037 (' + showNext[0] + ') on ' + showNext[2])

next.commands = ['next']
next.example = '.next House'

def last(phenny, input):
    show = input.split(' ')[1:]
    show = ' '.join(show)
    if not show:
        phenny.reply('Sorry, you did not supply a show name')
    else:
        show = show.replace(' ', '%20')
        html = urllib2.urlopen('http://services.tvrage.com/tools/quickinfo.php?show=' + show).read()
        data = html.split('\n')
        z = 0
	showName,showLastRaw = None, None
	for x in data:
            y = x.split('@')
            if y[0] == 'Show Name':
                showName = y[1]
            elif y[0] == 'Latest Episode':
                showLastRaw =  y[1]
	if showLastRaw:
		showLast = showLastRaw.split('^')
	else:
		showLast = None

        if not showName:
            phenny.say('Could not find tv show with that name')
        elif not showLast[0]:
            phenny.say('Last episode of not available')
        else:
            phenny.say('\002Last -->\002 The last episode of\037 ' + showName + '\037 was \037' + showLast[1] + '\037 (' + showLast[0] + ') on ' + showLast[2])

last.commands = ['last']
last.example = '.last House'

