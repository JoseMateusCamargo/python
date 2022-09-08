<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="150">

# Python

## How to Use

- Usando **Generators**.
- Usando função `filter` com lambda.
- Usando função `map`.
- _Métodos_ usado em uma `lista`.
- Como passar uma lista como um _argumento_ usando `argparse`.
- Dominando **Dicionários**.

---

**Usando Generators**

`getsizeof` retorna o tamanho de um objeto em bytes. O objeto pode ser qualquer tipo de objeto. Todos os objetos
internos retornarão resultados corretos, mas isso não precisa ser verdadeiro para extensões de terceiros,
pois é específico da implementação.

```python
import sys

# Lista simples
print(sys.getsizeof([x for x in range(100)]))  # 904

# Usando generators, trocando [] por ()
print(sys.getsizeof((x for x in range(100))))  # 112
# 87% na redução to tamanho do objeto
```

**Usando função `filter` com lambda**

```Python
print(list(filter(lambda x: x % 2, range(15))))  # [1, 3, 5, 7, 9, 11, 13]
```

**Usando função `map`**

```Python
x_map = list(map(int, input('Enter with numbers: ').split()))  # Input: 1 2 3
print(x_map)  # [1, 2, 3]
```

**Métodos usado em uma `lista`**

```Python
input = ['A', 'B', 'B', 'C']

input.append('D')  # ['A', 'B', 'B', 'C', 'D']
input.insert(1, 'E')  # ['A', 'E', 'B', 'B', 'C']
input.pop(1)  # ['A', 'B', 'C']
input.remove('B')  # ['A', 'B', 'C']
input.sort()  # ['C', 'B', 'B', 'A']
input.index('C')  # 3
input.count('B')  # 2
```

**Como passar uma lista como um argumento usando `argparse`**

```Python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--list", nargs="+", default=["a", "b"])

value = parser.parse_args()
print(value.list)

# Convert list to string using List Comprehension
string = ' '.join([str(item) for item in value.list])
print(string)

# Convert list to string using Join Function
print(' '.join(value.list))

# Convert list to string using map() Function
print(' '.join(map(str, value.list)))

# input: app.py --list one second
# output: ['one', 'second']
```

**Dominando Dicionários**

```Python
# Criando um dicionario
dic = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# Criando dicionario utilizando a função dict()
dic2 = dict(key4='value4', key5='value5', key6='value6')

print(dic)
print(dic2)

# Acessando elementos
print(dic['key2'])
# Acessando elementos utilizando função get()
print(dic2.get('key4'))

# Atualizando elementos
dic['key3'] = 'value3_update'
dic['key7'] = 'value7'
print(dic)
# Atualizando elementos utilizando função update()
dic2.update({'key6': 'value6_update', 'key8': 'value8'})
print(dic2)

# Deletanto elementos utilizando palavra reservada #del
del dic['key1']
print(dic)
# Deletanto elementos utilizando função pop()
key4 = dic2.pop('key4')
print(dic2)
print(key4)

# Juntanto dicionarios utilizando o operador **
all_in_one = {**dic, **dic2}
print(all_in_one)
```