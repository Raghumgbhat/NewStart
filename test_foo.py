def upper_reverse(text):
	return ''.join(text.upper())
def test_upper_reverse():
	assert upper_reverse('hello') == 'HELLO'
