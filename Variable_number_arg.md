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
In Python kunnen we de `*`-operator gebruiken in de **parameterlijst van een functie** om aan te geven dat deze functie een **variabel aantal positionele argumenten** mag ontvangen.

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

---


