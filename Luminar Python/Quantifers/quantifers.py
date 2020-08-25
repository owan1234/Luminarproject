from re import *
pattern='a?'
matcher=finditer(pattern,"aabaaabaaabaaabaababaa")
for match in matcher:
    print(match.start())
    print(match.group())
        