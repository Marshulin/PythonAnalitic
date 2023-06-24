# text = input().lower().split()
# vowels = 'аеоуюёэяи'
# result = set()
# for word in text:
#     count = 0
#     for i in word:
#         if i in vowels:
#             count += 1
#     result.add(count)
# if len(result) == 1:
#     print("param pam-pam")
# else:
#     print("Param pam")

def print_operation_table(operation, num_rows=6, num_columns=6):

    print(' '.join([str(i) for i in range(1, num_columns + 1)]))
    for i in range(1, num_rows + 1):
        print(i, end=' \t')
        for j in range(2, num_columns + 1):
            print(operation(i, j), end=' \t')
        print()
        
print_operation_table(lambda x, y: x * y)

    
