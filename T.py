s='Kevin likes English.'
new=''
for i in range(len(s)):
    if i%3==0:
        new+=s[i]
print(new)
