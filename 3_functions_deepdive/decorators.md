# 🧩 Python Decorators

Een **decorator** in Python is een functie die **een andere functie aanpast of uitbreidt**, zonder die originele functie zelf te veranderen.

Je kan het zien als een "wrapper" rond je functie — een beetje zoals een cadeauverpakking: de inhoud blijft hetzelfde, maar je geeft het extra flair! 🎁

---

## 1. 🧠 Functies zijn objecten

In Python zijn functies **first-class citizens**:
- Ze kunnen worden **doorgegeven als argument**
- Ze kunnen worden **teruggegeven door een andere functie**
- Ze kunnen worden **opgeslagen in variabelen**

Voorbeeld:
```python
def zeg_hoi():
    print("Hoi!")

functie_ref = zeg_hoi
functie_ref()  # Roept zeg_hoi aan
```

---

## 2. 🔁 Functies binnen functies

Een functie kan een andere functie **definiëren** binnen zichzelf:
```python
def buiten():
    def binnen():
        print("Ik zit binnenin!")
    binnen()

buiten()
```

---

## 3. 🔄 Functies retourneren functies

```python
def bewerking_wiskunde(bewerking):
    def optellen(n1, n2):
        return n1 + n2
    def aftrekken (n1, n2):
        return n1 - n2

    if bewerking == '+':
        return optellen
    elif bewerking == '-':
        return aftrekken

optel_functie = bewerking_wiskunde('+')
aftrek_functie = bewerking_wiskunde('-')
```

---

## 4. 🎁 Een functie decoreren (manueel)

```python
def hoofd_functie():
    print("Ik ben de originele functie!")

def decorator(functie):
    def wrapper():
        print("Iets voor...")
        functie()
        print("...en iets erna!")
    return wrapper

versierd = decorator(hoofd_functie)
versierd()
```

**Output:**
```
Iets voor...
Ik ben de originele functie!
...en iets erna!
```

---

## 5. ✨ De syntaxis van een echte decorator

Python biedt een kortere notatie met `@`:
```python
def decorator(f):
    def wrapper():
        print("[Start]")
        f()
        print("[Einde]")
    return wrapper

@decorator # naam van de decorator
def hallo():
    print("Hallo wereld")

hallo()
```

---

## 6. ⚙️ Decorators met parameters

Je kan ook functies decoreren die **parameters** krijgen:
```python
def logger(functie):
    def wrapper(*args, **kwargs):
        print(f"Aanroepen met args={args}, kwargs={kwargs}")
        return functie(*args, **kwargs)
    return wrapper

@logger
def vermenigvuldig(a, b):
    return a * b

print(vermenigvuldig(3, 4))
```

**Output:**
```
Aanroepen met args=(3, 4), kwargs={}
12
```

---

## 🎯 Waarom zijn decorators nuttig?
- Logging
- Validatie
- Tijdmetingen
- Authenticatie
- Debuggen
- Herbruikbaarheid verhogen

---

## 🔥 Bonus: decorator met argumenten (meta-decorator)

```python
def herhaal(aantal):
    def decorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(aantal):
                f(*args, **kwargs)
        return wrapper
    return decorator

@herhaal(3)
def zwaai():
    print("👋")

zwaai()
```

**Output:**
```
👋
👋
👋
```

---

