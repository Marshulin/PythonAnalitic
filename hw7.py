text = input().lower().split()
vowels = 'аеоуюёэяи'
result = set()
for word in text:
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    result.add(count)
if len(result) == 1:
    print("param pam-pam")
else:
    print("Param pam")
    
