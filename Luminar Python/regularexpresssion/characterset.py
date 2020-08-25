from re import *
pattern='[abc]'
matcher=finditer(pattern,"abababababbababbbbabababab")
for match in matcher:
    print(match.start())
    print(match.group())
#"\s" space
#'\d' digit