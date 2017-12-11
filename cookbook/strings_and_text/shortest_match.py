"""
Solution for regex matching the longest possible matches only. We want it to
select the shortest matches.
"""
import re

str_pat = re.compile(r'\"(.*)\"')
str_pat2 = re.compile(r'\"(.*?)\"')
text1 = 'Computer says "no."'
text2 = 'Computer says "no." Phone says "yes."'

result = str_pat.findall(text1)

# This is a problem because the match is greedy. It matches from the match to
# the end of the word, right? Matches all after "no."
result2 = str_pat.findall(text2)

# str_pat2 is a better result because adding the `?` causes the thing not to be
# greedy. It will stop after it finds the proper match.
result3 = str_pat2.findall(text2)

print(result)
print(result2)
print(result3)
