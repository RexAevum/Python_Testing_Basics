# write a function that takse a string argumnent and retunrs the number pf vowels in it



def vowels(string):
	vowels = ['a', 'e', 'i', 'o', 'u']
	count = 0
	for ch in string.lower():
		if ch in vowels:
			count += 1
	return count

print (vowels('Hello world'))

def test_count_sunny_001():
	assert vowels('hello world') == 3

def test_count_sunny_002():
	assert vowels('HELLO WORLD') == 3

def test_count_sunny_003():
	assert vowels('aeiou') == 5
	assert vowels("AEIOU") == 5

def test_count_rain_001():
	assert vowels('') == 0

def test_count_rain_002():
	assert vowels('1231241') == 0

def test_count_rain_003():
	assert vowels('zsfgytlnm') == 0

