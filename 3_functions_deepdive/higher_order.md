# Higher-Order Functions

## 🔁 Wat zijn Higher-Order Functions?
Een **higher-order function (HOF)** is een functie die **een andere functie accepteert als argument**, **een functie teruggeeft als resultaat**, of **beide** doet. Dit is mogelijk omdat in Python **functies first-class objects** zijn.

---

## 🧱 Functies zijn First-Class Objects
In Python:
- Functies kunnen opgeslagen worden in variabelen
- Functies kunnen als argument worden doorgegeven
- Functies kunnen teruggegeven worden door andere functies
- Functies kunnen opgeslagen worden in lijsten of dicts

Voorbeeld:
```python
uppercase = str.upper
print(uppercase("hello"))  # => 'HELLO'

string_fns = [str.upper, str.lower]
```

---

## 🎯 Voorbeeld van een Higher-Order Function als argument
```python
def total_bill(func, value):
    total = func(value)
    return total

# Hulp-functies

def add_tax(total):
    return total + total * 0.06

def add_tip(total):
    return total + total * 0.2

print(total_bill(add_tax, 100))  # => 106.0
print(total_bill(add_tip, 100))  # => 120.0
```

### 💬 Met geformatteerde boodschap:
```python
def total_bill(func, value):
    total = func(value)
    return f"The total amount owed is ${total:.2f}. Thank you! :)"
```

---

## 🔁 Higher-order functions en iteratie
Wat als je meerdere bedragen moet verwerken?
```python
def total_bills(func, list):
    new_bills = []
    for value in list:
        total = func(value)
        new_bills.append(f"Total amount owed is ${total:.2f}. Thank you! :)")
    return new_bills

bills = [115, 120, 42]
print(total_bills(add_tax, bills))
print(total_bills(add_tip, bills))
```
Opmerking:

    •	:.2f → Dat is de format specificatie:
	•	: → betekent: “nu komt een format-instructie”
	•	.2 → betekent: “gebruik 2 cijfers na de komma”
	•	f → betekent: “floatnotatie”, oftewel een decimaal getal

➡️ Eén functie die je kunt hergebruiken voor meerdere berekeningen zonder herhaling van code.

---

## 🔄 Functies als return value
Je kunt ook functies **teruggeven** vanuit een andere functie:
### 🎯 1. Vaste btw-tarieven (bijvoorbeeld per land of sector)
```python
def maak_btw_functie(tarief):
    def voeg_btw_toe(bedrag):
        return bedrag + bedrag * tarief
    return voeg_btw_toe

btw_belgie = maak_btw_functie(0.21)
btw_nederland = maak_btw_functie(0.21)
btw_duitsland = maak_btw_functie(0.19)

print(btw_belgie(100))     # 121.0
print(btw_duitsland(100))  # 119.0
```
### 🧱 2. Kortingssystemen (bijv. voor Black Friday of vaste klanten)
```python
def maak_korting_functie(korting_percentage):
    def pas_korting_toe(bedrag):
        return bedrag * (1 - korting_percentage)
    return pas_korting_toe

black_friday = maak_korting_functie(0.50)
vaste_klant = maak_korting_functie(0.10)

print(black_friday(200))  # 100.0
print(vaste_klant(200))   # 180.0
```
➡️ Dit is krachtig voor **functies op maat**, gebaseerd op specifieke parameters.

---

## ✅ Samenvatting
- Functies zijn **first-class objects** in Python
- Higher-order functions:
  - nemen functies als **argument** aan
  - geven functies **terug** als resultaat
  - of doen allebei
- Ze maken code:
  - **korter en herbruikbaar**
  - **minder foutgevoelig**
  - **eleganter en overzichtelijker**

Je hebt nu de bouwstenen in handen om krachtige functionele patronen te herkennen én zelf toe te passen! 🚀

Volgende stop: de ingebouwde higher-order functies van Python zoals `map()`, `filter()` en `reduce()`!

