# Scope & Namespaces

## 📚 namespaces VS scopes
- Een **namespace** is een intern woordenboek van namen en de objecten waarnaar ze verwijzen.
- **Scope** bepaalt in welk deel van het programma een bepaalde naam zichtbaar of beschikbaar is.

> 💡 Naam = verwijzing naar object / Scope = geldigheid van die naam

---

## 🔠 De vier types namespaces in Python (herhaling)
| Namespace     | Voorbeeld               | Bestaat zolang...                | Inspecteerbaar met |
|---------------|-------------------------|----------------------------------|---------------------|
| Built-in      | `print()`, `len()`, `str()` | De interpreter draait          | `dir(__builtins__)` |
| Global        | Variabelen op bestandsniveau | Het script wordt uitgevoerd    | `globals()`         |
| Enclosing     | Variabelen in een buitenste functie | De enclosing functie actief is | `locals()` binnen enclosing |
| Local         | Variabelen in een functie | De functie wordt uitgevoerd     | `locals()` binnen functie |

---

## 📍 Wat is Scope?
Scope bepaalt **waar** een naam gebruikt mag worden. In Python volgen scopes de **LEGB-regel**:

### 🔍 L → Local
De meest directe, binnenin de functie waar de naam is gedeclareerd.
```python
def func():
    x = 10  # lokaal
```

### 🔁 E → Enclosing
De scope van een **omliggende functie** (bij geneste functies).
```python
def outer():
    x = 'outer'
    def inner():
        print(x)  # enclosing scope
```

### 🌍 G → Global
De module- of script-scope, buiten alle functies.
```python
x = 'global'  # globale scope
```

### ⚙️ B → Built-in
De Python-functies die standaard beschikbaar zijn.
```python
print(len("Hello"))  # built-in scope
```

---

## 🔧 Scope aanpassen met `global` en `nonlocal`

### `global`
Gebruik `global` binnen een functie om aan te geven dat je een **globale variabele** wil wijzigen:
```python
x = 5

def change():
    global x
    x = 10
```

### `nonlocal`
Gebruik `nonlocal` binnen een **geneste functie** om een variabele uit de **enclosing scope** te wijzigen:
```python
def outer():
    x = 'outer'
    def inner():
        nonlocal x
        x = 'changed'
```

---

## 🧠 Waarom is dit belangrijk?
- Begrip van scope en namespaces voorkomt bugs zoals `UnboundLocalError` of verwarring over welke waarde waar vandaan komt.
- Het helpt je bij **debuggen, refactoren en schrijven van duidelijke code**.
- Onmisbaar voor het gebruik van closures, decorators en geavanceerde functiestructuren.

---

## ✅ Samengevat
- **Namespace = waar Python een naam koppelt aan een object**
- **Scope = waar jij die naam mag gebruiken**
- Dankzij **LEGB** weet Python exact waar hij een naam moet zoeken
- Je kunt met `global` of `nonlocal` gericht ingrijpen op variabelen buiten de lokale context



