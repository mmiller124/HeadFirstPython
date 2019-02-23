paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)

#Marvin, the Paranoid Android
#0123456789012345678901234567
#0000000000111111111122222222

for char in letters[:6]:
    print('\t',char)
print()  
for char in letters[-7:]:
    print('\t'*2,char)
print()  
for char in letters[12:20]:
    print('\t'*3,char)

# '\t' tells print to print a tab
# you can ask for multiple tabs by multiplying it -> '\t'*3
