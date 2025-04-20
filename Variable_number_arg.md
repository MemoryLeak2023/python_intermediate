# Variable Number of Arguments (*args)

## 🌟 Functies met een variabel aantal argumenten

Sommige functies in Python, zoals `print()`, accepteren een willekeurig aantal argumenten:

```python
print('This', 'is', 'the', 'print', 'function')
```

➡️ De functie `print()` heeft **geen vast aantal verwachte parameters**. Of je nu één argument of honderd meegeeft: het werkt.

Maar hoe kan een functie dat?

---

## ✨ De kracht van de unpacking operator `*`
In Python kunnen we de `*`-operator gebruiken in de **parameterlijst van een functie** om aan te geven dat deze functie een **variabel aantal [positionele argumenten](Function_arguments.md)** mag ontvangen.

Dit wordt ook wel **positional argument packing** genoemd.

Voorbeeld:

```python
def my_function(*args):
    print(args)

my_function('Arg1', 245, False)
```

➡️ Output:
```
('Arg1', 245, False)
```

🧠 Wat gebeurt hier?
- De `*args` verzamelt **alle extra positionele argumenten** in een **tuple**.
- Je kunt dus meerdere, willekeurige argumenten doorgeven aan één functie.

---

## 📛 De naam `args` is niet verplicht
Je mag `args` eender welke naam geven — het sterretje `*` is wat telt.

```python
def my_function(*randomname):
    print(randomname)
```

➡️ Werkt exact hetzelfde. Zolang je maar `*naam` gebruikt.

---

## 📦 Samengevat
- Het sterretje `*` **pakt positionele argumenten samen in een tuple**.
- Deze techniek laat je toe om **flexibele functies** te schrijven, net zoals `print()` dat doet.
- De naam na `*` is vrij te kiezen, maar vaak gebruiken programmeurs `*args` als conventie.


Nu we de basis kennen van de `*args`-syntax voor variabel aantal argumenten, is het tijd om deze kracht **praktisch in te zetten**.


## 🔊 Voorbeeld 1: Alle argumenten in hoofdletters printen
Stel je wil een functie maken zoals `print()`, maar dan eentje die **alles in hoofdletters** toont. Met behulp van `*args` en een simpele `for`-lus:

```python
def shout_strings(*args):
    for argument in args:
        print(argument.upper())

shout_strings('Working on', 'learning', 'argument unpacking!')
```

➡️ Output:
```
WORKING ON
LEARNING
ARGUMENT UNPACKING!
```

### Wat gebeurt hier?
- `*args` verzamelt de strings in een tuple.
- We lopen met een `for`-lus door elk argument.
- `.upper()` converteert de string naar hoofdletters.

Let op: dit werkt alleen als de doorgegeven waarden strings zijn (anders zou `.upper()` een fout geven).

---

## ✂️ Voorbeeld 2: Zinnen afkappen op lengte
Je kunt `*args` ook combineren met **gewone positionele argumenten**.

```python
def truncate_sentences(length, *sentences):
    for sentence in sentences:
        print(sentence[:length])

truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
```

➡️ Output:
```
What's g
Looks li
```

### Analyse:
- `length` is een gewoon argument (positioneel): het bepaalt hoe lang elke zin mag zijn.
- `*sentences` verzamelt de overige argumenten in een tuple.
- In de lus nemen we van elke zin enkel de eerste `length` karakters via slicing (`sentence[:length]`).

---

## 🔁 Flexibele functies dankzij `*args`
Door `*args` te combineren met:
- **Iteratie** (zoals `for`-lussen), en
- **Andere argumenten** (zoals `length`),

...kun je functies maken die **zeer flexibel en krachtig** zijn — net zoals de ingebouwde `print()`-functie.

Hieronder een voorbeeld waarbij je klanten een tafel laat reserveren en hun bestelling opneemt. 💡
 ```python
 tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

def assign_and_print_order(table_number, *order_items):
  tables[table_number]['order'] = order_items
  for item in order_items:
    print(item)

assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Steak', 'Seabass','Wine Bottle')
print(tables)
```



