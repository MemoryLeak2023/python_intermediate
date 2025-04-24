# Built-In Higher-Order Functions

## 🔧 Wat zijn built-in higher-order functions?
Python heeft drie ingebouwde functies die echte krachtpatsers zijn als het gaat om het **bewerken van collecties**:
- `map()` → **transformatie**
- `filter()` → **selectie**
- `reduce()` → **samenvatten tot één waarde**

Deze functies werken met **iterables** (zoals lijsten) en gebruiken **functies als argument**. Daarom zijn het higher-order functions.

---

## 🗺️ `map()` - transformeren
```python
map(function, iterable)
```

Past `function` toe op **elk element** van de `iterable`.

### 🔍 Voorbeeld:
```python
def double(x):
    return x * 2

int_list = [3, 6, 9]
doubled = map(double, int_list)
print(list(doubled))  # [6, 12, 18]
```

### 💡 Met lambda:
```python
print(list(map(lambda x: x * 2, int_list)))
```
### 🔍 Voorbeeld 2:
Je hebt een puntenlijst waarvan de eerste drie resultaten op een schaal van 4 werden genoteerd en de laatste 2 op een schaal van 100. Herschrijf de lijst zodat alle resultaten op 100 punten staan.

```python
grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:

# assign the result of your map function to the variable grades_100scale

grades_100scale = map(lambda grade: grade*25 if grade <= 4.0 else grade, grade_list)

# convert grades_100scale to a list and save it as updated_grade_list 

updated_grade_list = list(grades_100scale)

# print updated_grade_list


print(updated_grade_list)
```
> ✅ `map()` is handig als je **iets wil wijzigen aan elk element** (zoals vermenigvuldigen, afronden, omzetten naar hoofdletters, ...).

---

## 🔍 `filter()` - filteren op voorwaarde
```python
filter(function, iterable)
```

Houdt **alleen die elementen** over waarvoor de functie `True` geeft.

### 🔍 Voorbeeld:
```python
names = ["margarita", "Linda", "Masako", "Maki", "Angela"]

M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names)
print(list(M_names))  # ['margarita', 'Masako', 'Maki']
```

> ✅ `filter()` is ideaal om **items te selecteren** die voldoen aan een bepaalde **voorwaarde**.

---

## ➕ `reduce()` - cumulatief samenvatten
```python
from functools import reduce
```

```python
reduce(function, iterable)
```

Reduce gebruikt een functie die telkens twee waarden combineert tot **één resultaat**.

### 🔍 Voorbeeld: alles vermenigvuldigen
```python
from functools import reduce
int_list = [3, 6, 9, 12]

result = reduce(lambda x, y: x * y, int_list)
print(result)  # 1944
```

Proces:
- 3 * 6 = 18
- 18 * 9 = 162
- 162 * 12 = 1944

➡️ Het resultaat is **één enkele waarde**.

### 🔍 Voorbeeld 2: strings samenvoegen
```python
letters = ['r', 'e', 'd', 'u', 'c', 'e']

# your code below:

# remember to import the reduce function
from functools import reduce
# store the result of your reduce function in the variable word
word = reduce(lambda x, y: x + y, letters)

# print word
print(word)
````


> ✅ `reduce()` gebruik je als je iets **wilt samenvatten**: optellen, vermenigvuldigen, strings samenvoegen, ...

---

## ✅ Samenvatting
| Functie  | Doel                        | Resultaat          | Voorbeeld                              |
|----------|-----------------------------|---------------------|----------------------------------------|
| `map()`  | Elke waarde aanpassen       | lijst van waarden   | `map(lambda x: x*2, lijst)`            |
| `filter()` | Waarden selecteren op test | lijst van subset    | `filter(lambda x: x > 5, lijst)`       |
| `reduce()` | Alles samenvatten tot één  | één enkele waarde   | `reduce(lambda x, y: x*y, lijst)`      |

---

Deze drie tools zijn de bouwstenen voor functionele patronen in Python en combineren perfect met lambda’s! 🚀



