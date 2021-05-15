'''s = "identifier"
for i in s:
    if i.islower():
        print(i,end="")
    else:
        print("",i,end="")'''

s = 'camelCaseProgram'
print(''.join(c if c.islower() else ' ' + c for c in s))