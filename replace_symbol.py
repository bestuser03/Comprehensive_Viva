def replace_symbol(new, k):
    symbol = '@$%&*'
    for special in symbol:
        new = new.replace(special, k)
    return new


string = input("Enter string: ")
k = "#"
print(string)
print(replace_symbol(string, k))
