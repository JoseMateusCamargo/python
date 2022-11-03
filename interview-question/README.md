<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python

## Interview questions

Scripts com questões utilizadas em entrevistas técnicas.
Scripts com questões utilizadas em entrevistas técnicas.

#### _Let's Code!_

- **Microsoft Interview Question**
    - 01 - Search a Word in a 2D Grid of characters.
    - 02 - Check if a word exists in a grid or not.
- **GeeksForGeeks Questions**
    - 01 - Average Min Max.
    - 02 - Count Even Odd.
- **Outros**
    - Questão da Piramide.
    - Ordenar `array`.
    - Algoritmo para somar apenas números pares usando `list comprehension`.
    - Check se contem um numero `X` em uma lista.
    - Recupere o numero removido de uma lista.
    - Encontrar número duplicado na lista de inteiros.
    - Compare a interseção de duas listas.

---

### Microsoft Interview Question

**01 - Search a Word in a 2D Grid of characters**

Dada uma grade 2D de caracteres e uma palavra, encontre todas as ocorrências dessa palavra na grade.
Uma palavra pode ser correspondida nas 8 direções a qualquer momento. Diz-se que a palavra é encontrada em uma direção
se todos os caracteres corresponderem nessa direção (não na forma de zig-zag). As 8 direções são: Horizontalmente à
esquerda, Horizontalmente à direita, Verticalmente para cima e 4 direções em
diagonal. [Code](https://github.com/JoseMateusCamargo/python/blob/master/interview-question/microsoft-question/findmatch2Din8D.py)

**02 - Check if a word exists in a grid or not**

Dada uma grade 2D de caracteres e uma palavra, a tarefa é verificar se essa palavra existe ou não na grade. Uma palavra
pode ser correspondida em 4 direções a qualquer momento. As 4 direções são: horizontalmente esquerda e direita,
verticalmente para cima e para
baixo. [Code](https://github.com/JoseMateusCamargo/python/blob/master/interview-question/microsoft-question/findmatch2Din4D.py)

---

### GeeksForGeeks Questions

**01 - Average Min Max**

Explanation: The minimum element in the list `(6 4 8 12 3)` is 3 and maximum is 12, so average excluding min and max is
`18/3 = 6`
. [Code](https://github.com/JoseMateusCamargo/python/blob/master/interview-question/geeksforgeeks-question/average_min_max_geeksforgeeks.py)

**02 - Count Even Odd**

Explanation: In the given list `(1 2 3 4 5 6 7)`, there are 3 even numbers (2, 4, 6) and 4 odd elements (1, 3, 5, 7)
. [Code](https://github.com/JoseMateusCamargo/python/blob/master/interview-question/geeksforgeeks-question/count_even_odd_geeksforgeeks.py)

---

### Outros

* Questão da Piramide.
* Ordenar `array`.
* Algoritmo para somar apenas números pares usando `list comprehension`.
* Check se contem um numero `X` em uma lista.
* Recupere o numero removido de uma lista.
* Encontrar número duplicado na lista de inteiros.
* Compare a interseção de duas listas.

**Questão da Piramide**

``` 
Print this pattern:

    *
   * *
  * * *
 * * * *
* * * * *
```

Code:

````python
def pyramid(n):
    k = n - 1

    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")

        k = k - 1
        for j in range(0, i + 1):
            print("*", end=" ")

        print("\n")


pyramid(5)
````

**Ordenar array**

````python
arr = [5, 4, 8, 9, 4, 2, 4, 5, 0]
temp = 0

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print('Array sorted in ascendant order: ')

for i in range(0, len(arr)):
    print(arr[i])
````

ou

````python
arr = [5, 4, 8, 9, 4, 2, 4, 5, 0]
arr.sort()
print(arr)
````

**Algoritmo para somar apenas números pares usando `list comprehension`**

````python
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = [x for x in array if x % 2 == 0]
print(sum(result))
````

**Check se contem um numero X em uma lista**

````python
list_ = [3, 3, 4, 5, 2, 111, 5]
print(111 in list_)  # true
````

**Recupere o numero removido de uma lista**

````python
def get_missing_number(list_missing):
    return set(range(list_missing[len(list_missing) - 1])[1:]) - set(lt)


lt = list(range(1, 100))
lt.remove(76)
print(get_missing_number(lt))  # {76}
````

**Encontrar número duplicado na lista de inteiros**

````python
def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)


elements = (1, 2, 33, 1)
print(find_duplicates(elements))  # [1]
````

**Compare a interseção de duas listas**

````python
def intersect(list1, list2):
    res, list2_copy = [], list2[:]
    for el in list1:
        if el in list2_copy:
            res.append(el)
            list2_copy.remove(el)

````

### Direitos de uso (Use rights)

<p>
  Você tem todo o direito de usar esse material para seu próprio aprendizado.<br/>
  You can use this material for your own learning.
</p>