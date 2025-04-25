# Lambda Functions

## ⚡ Wat is een lambda functie?
Een **lambda-functie** (ook wel **anonieme functie** genoemd) is een **éénregelige functie** in Python — zonder `def`, zonder naam (tenzij je die zelf toekent), en zonder expliciete `return`.

### 🆚 Vergelijking met een gewone functie
```python
def add_two(my_input):
    return my_input + 2
```

Kan worden geschreven als:
```python
add_two = lambda my_input: my_input + 2
```

Gebruik:
```python
print(add_two(3))    # 5
print(add_two(100))  # 102
print(add_two(-2))   # 0
```

---

## 🔍 Uitleg van de syntax
```python
lambda parameter(s): expressie
```
- `lambda` is het sleutelwoord dat een lambda-functie inleidt
- `parameter(s)` zijn de invoerwaarden van de functie
- de **expressie** is wat wordt **teruggegeven (return)** → zonder dat je `return` moet schrijven

> ✅ Lambda-functies zijn handig voor korte functies die **niet hergebruikt hoeven te worden** of die je meteen inline wilt gebruiken (bijv. in `sorted()`, `map()`, enz.)

---

## 🧠 Lambda met conditionele logica
Je kunt ook een **if-else**-constructie in één regel verwerken:

```python
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'
```

Gebruik:
```python
print(check_if_A_grade(91))  # 'Got an A!'
print(check_if_A_grade(70))  # 'Did not get an A.'
print(check_if_A_grade(20))  # 'Did not get an A.'
```

Uitleg:
- `lambda grade:` → definieert een functie met parameter `grade`
- `'Got an A!' if grade >= 90 else 'Did not get an A.'` → returnt een resultaat afhankelijk van de conditie

---

## 📌 Wanneer gebruik je lambda's?
Gebruik **lambda's**:
- voor **éénregelige functies**
- als **leesbaarheid** belangrijk is
- bij gebruik in functies als `map()`, `filter()`, `sorted()`...

Gebruik **gewone functies** met `def`:
- als je **meerdere regels code** nodig hebt
- als je de functie **op meerdere plekken gaat gebruiken**
- als je de functie een **docstring of naam** wilt geven voor duidelijkheid

---

## ✅ Samengevat
- Lambda’s zijn korte, anonieme functies die één expressie teruggeven.
- Geen `return` nodig: de expressie wordt automatisch teruggegeven.
- Perfect voor inline gebruik en conditionele logica in één lijn.
- Voor complexere logica of hergebruik: gebruik `def`.

In het volgende deel gaan we zien hoe lambda's vaak worden gecombineerd met functies als `map()`, `filter()` en `sorted()` om lijsten of iterables te transformeren! 🔁

