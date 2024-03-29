<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python

## Manipulando arquivos CSV

#### _Let's Code!_

- Consolidando arquivos `CVS`.
- Percorrendo linha em arquivo `CSV`.
- Comparando 2 arquivos `CSV` e salvar a diferença.

---

**Consolidando arquivos `CVS`**

```python
import os
import pandas as pd

path = 'C:/Users/jleva/bases'
string = 'square'

quantity = 0
base_consolidate = None

for dir_, sub_path, files in os.walk(path):

    for file in files:
        if file.startswith(string, 0, -1):
            file_download = os.path.join(dir_, file)
            file_actual = pd.read_csv(file_download, sep=',')

            if quantity == 0:
                base_consolidate = file_actual
            else:
                base_consolidate = pd.concat([base_consolidate, file_actual])

            quantity += 1

print(f'Consolidated: {quantity}, files')

if quantity > 0:
    file_save = 'consolidated_' + string + '.csv'
    base_consolidate.to_csv(r'' + path + '/' + file_save, sep=';', index=False)
    print(f'Saved in: {file_save}')
```

**Percorrendo linha em arquivo `CSV`**

````python
import csv

file = "base_name.csv"
with open(file) as file:
    content = csv.reader(file)
    for row in content:
        print(row)
````

**Comparando 2 arquivos `CSV` e salvar a diferença**

````python
with open('1.csv', 'r') as t1, open('2.csv', 'r') as t2:
    file_one = t1.readlines()
    file_two = t2.readlines()

with open('difference.csv', 'w') as outFile:
    for line in file_two:
        if line not in file_one:
            outFile.write(line)

print("Finish!")
````