import re
regexs=[re.compile(p,re.I) for p in ['THiS','that']]
text="does this match the pattern"
print("text:%r\n"%repr(text))
for regex in regexs:
	print('seek for "%s"->'%regex.pattern)
	if regex.search(text):
		print("match")
	else:
		print("unmatch")