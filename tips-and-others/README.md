<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python dicas

#### _Let's Code!_

- Renomeando arquivo.
- **Factorial** - aplicar fatorial.
- **Anagram** - checar se string é anagrama.
- Retornando a memória utilizada por um objeto.
- Checando se um numero é _impar_ ou _par_.
- Trabalhando com `split` e `join`.
- Formatar string com `f-string`.
- Atribuição de múltiplas variávies.
- Trocar valor de 02 variávies.
- **Palindrome** - reverter string.
- Formar `string` a partir dos elementos de uma lista.
- String a partir dos elementos de uma lista.
- `swapcase()` o método retorna uma string onde todas as letras maiúsculas são minúsculas e vice-versa.
- [Operações básicas com lista.](list_basic_operation.py)

---

**Renomeando arquivo**

```python
import os


def rename_file(file, new_file):
    os.rename(file, new_file)
    print(f'\nRename {file} to {new_file}')
```

**`List Comprehensions`, ler arquivo em um linha de codigo**

```python
file = [row.strip() for row in open('files/tips.txt')]
print("\n".join(file))
```

**Factorial - aplicar fatorial**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


try:
    number = int(input("Enter the number: "))
    print(f"Factorial : {factorial(number)}")

except ValueError as e:
    print(f"Error : {e}")
```

**Anagram - checar se string é anagrama**

```python
def is_anagram(one, two):
    return sorted(one) == sorted(two)


print(f'Anagrams: {is_anagram("python", "php")}')
```

**Retornando a memória utilizada por um objeto**

```python
dic = {'a': 677, 'b': 494848, 'c': 0, 'd': 'memory'}
print(sys.getsizeof(dic))
```

**Checando se um numero é impar ou par**

```python
T = int(input("Tell me a beautiful number: "))
print("Yes" if T % 2 != 0 else "No")
```

**Trabalhando com split e join**

```python
def split_and_join(line):
    line = line.split(" ")
    return "-".join(line)


print(split_and_join('one two three'))  # one-two-three
```

**Formatar string com `f-string`**

```python
print(f"Cod = {cod_}\nName = {name}\nError = {error}")
```

**Atribuição de múltiplas variávies**

```python
cod_, name, error = 201, "HTTP CREATED", False
print(cod_, name, error)

list_example = [12, -44, -2]
max_, min_, med_ = list_example
print(max_, min_, med_)
```

**Trocar valor de 02 variávies**

```python
x, y = 1, 2
print(f"Before: x={x} & y={y}")
x, y = y, x
print(f"After: x={x} & y={y}")
```

**Palindrome - reverter string**

```python
string = 'Hello world'
print(
    f"Normal: {string[::1]}\n"
    f"Reverse: {string[::-1]}"
)
```

**String a partir dos elementos de uma lista**

```python
list_join = ['One', 'Second', 'Third']
print(" ".join(list_join))
```

**`swapcase()` o método retorna uma string onde todas as letras maiúsculas são minúsculas e vice-versa**

```python
string_swap = 'AsSssS'
print(string_swap.swapcase())
```

## Fim
