# Scope Resolution: de LEGB-regel
De **LEGB-regel** beschrijft **hoe Python op zoek gaat naar een naam**:
1. **Local** scope → in de actieve functie
2. **Enclosing** scope → in omliggende functies (bij nested functions)
3. **Global** scope → op bestands- of module-niveau
4. **Built-in** scope → standaard functies en types

Python doorloopt deze volgorde **van boven naar onder**, en **stopt zodra een naam gevonden wordt**.

### 🧪 Voorbeeld 1: naam in de global scope
```python
age = 27 # global scope

def func():
    def inner_func():
        print(age)
    inner_func()

func()
```
➡️ Output: `27`
- `age` is **niet lokaal** aan `inner_func()` → Python kijkt verder
- `age` is **niet in enclosing scope** → Python kijkt verder
- `age` **bestaat in globale scope** → gevonden ✅

### 🧪 Voorbeeld 2: naam overschreven in enclosing scope
```python
age = 27

def func():
    age = 42  # enclosing scope

    def inner_func():
        print(age)
    inner_func()

func()
```
➡️ Output: `42`
- Python **vindt age in de enclosing scope** en **stopt daar**
- De globale waarde wordt niet meer opgezocht

### 🚫 Wat als de naam nergens bestaat?
Als Python in geen van de vier scopes iets vindt, krijg je een:
```python
NameError: name 'x' is not defined
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



