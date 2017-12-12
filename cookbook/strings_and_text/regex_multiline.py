import re

comment = re.compile(r'/\*(.*?)\*/')

# This syntax isn't obvious. The structure of the pattern I mean. It will handle
# newlines.
comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')

# Including a flag that handles the newlines. It includes newlines in the dot
# thing.
comment3 = re.compile(r'/\*((?:.|\n)*?)\*/', re.DOTALL)

text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment*/'''

find1 = comment.findall(text1)

#This will fail becaues it can't handle newlines.
find2 = comment.findall(text2)

# Pattern that handles the newline.
find3 = comment2.findall(text2)

find4 = comment3.findall(text2)

print(find1)
print(find2)
print(find3)
print(find4)
