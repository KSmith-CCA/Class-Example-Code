password = input()
valid = 0
lower = 0
upper = 0
int_count = 0
invalid_char = 0

for i in range(len(password)):
    if password[i].islower():
        lower = lower +1
    elif password[i].isupper():
        upper = upper +1    
    elif password[i] >= '0' and password[i] <= '9':
        int_count = int_count + 1
    else:
        invalid_char = invalid_char + 1

if len(password) > 7 and len(password) < 13:
    valid = valid + 1
if lower > 2:
    valid = valid + 1
if upper > 1:
    valid = valid + 1
if int_count > 0:
    valid = valid + 1
if invalid_char <= 0:
    valid = valid + 1

if valid == 5:
    print('Valid')
else:
    print('Invalid')
