lines = [
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
	"ten Lords-a-Leaping, ",
	"nine Ladies Dancing, ",
	"eight Maids-a-Milking, ",
	"seven Swans-a-Swimming, ",
	"six Geese-a-Laying, ",
	"five Gold Rings, ",
	"four Calling Birds, ",
	"three French Hens, ",
	"two Turtle Doves, ",
	"and a Partridge in a Pear Tree.",
]

ordinals = [
	'first',
	'second',
	'third',
	'fourth',
	'fifth',
	'sixth',
	'seventh',
	'eighth',
	'ninth',
	'tenth',
	'eleventh',
	'twelfth',
]

def recite(start_verse, end_verse):
	initializer = lambda verse: "On the %s day of Christmas my true love gave to me: "%ordinals[abs(verse)-1]
	get_line = lambda verse: [lines[-1].replace('and ', '')] if verse == 1 else [lines[day] for day in range(-verse, 0)]
	return [initializer(verse)+"".join(get_line(verse)) for verse in range(start_verse, end_verse+1)]