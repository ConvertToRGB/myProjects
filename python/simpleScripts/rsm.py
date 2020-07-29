#!python2
# coding: utf-8

a = raw_input('')
a = a.decode('cp866')

def repeat(s):
	if s:
		while not s[0].isalnum():
			s = s[1:]
		st = s
		first = s[0]
		if not st.find(first) == -1:
			index = st.find(first)
			letter = st[index]
			st = st.replace(letter, '')
		print s.encode('cp866'), first.encode('cp866')
		repeat(st)

repeat(a)

raw_input()