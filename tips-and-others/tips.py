# formar string a partir dos elementos de uma lista
list_join = ['One', 'Second', 'Third']
print(" ".join(list_join))
print('----------')

# armazenar elementos de uma lista diretamente em variávies
list_example = [12, -44, -2]
max_, min_, med_ = list_example
print(max_, min_, med_)
print('----------')

# print N vezes uma string
print('Python\n' * 3)
print('----------')

# atribuição de múltiplas variávies
cod_, name, error = 201, "HTTP CREATED", False
print(cod_, name, error)
print('----------')

# formatar string com f-string
print(f"Cod = {cod_}\nName = {name}\nError = {error}")
print('----------')

# reverter string (palindrome)
string = 'Hello world'
print(
    f"Normal: {string[::1]}\n"
    f"Reverse: {string[::-1]}"
)
print('----------')

# trocar valor de 02 variávies
x, y = 1, 2
print(f"Before: x={x} & y={y}")
x, y = y, x
print(f"After: x={x} & y={y}")
print('----------')

# ler arquivo em um linha de codigo com (List Comprehensions)
file = [row.strip() for row in open('files/tips.txt')]
print("\n".join(file))

# The swapcase() method returns a string where all the upper case letters are lower case and vice versa
string_swap = 'AsSssS'
print(string_swap.swapcase())
