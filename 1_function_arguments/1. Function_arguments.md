# Function Arguments (Herhaling)

In Python zijn er drie veelgebruikte soorten functieargumenten. Deze vormen de basis voor het werken met functies:

## 📌 1. Positionele argumenten
Dit zijn argumenten die worden doorgegeven op basis van hun **positie** in de functieaanroep.

```python
def print_name(first_name, last_name):
    print(first_name, last_name)

print_name('Jiho', 'Baggins')
```

➡️ `first_name` krijgt de waarde `'Jiho'`, en `last_name` krijgt `'Baggins'` — puur omdat dat de volgorde is van de argumenten bij de aanroep.

---

## 🏷️ 2. Keyword argumenten
Deze worden doorgegeven met een expliciete naam. De **volgorde** maakt hierbij niet uit.

```python
def print_name(first_name, last_name):
    print(first_name, last_name)

print_name(last_name='Baggins', first_name='Jiho')
```

➡️ Dankzij het gebruik van sleutelwoorden (`first_name=`, `last_name=`), begrijpt Python exact welke waarde bij welk parameter hoort — onafhankelijk van de volgorde.

---

## 🎁 3. Default argumenten
Je kunt standaardwaarden toekennen aan parameters in de functie-definitie. Daardoor hoef je ze bij de aanroep niet verplicht mee te geven.

```python
def print_name(first_name='Jiho', last_name='Baggins'):
    print(first_name, last_name)

print_name()
```

➡️ Omdat beide parameters een standaardwaarde hebben, werkt `print_name()` zonder enige argumenten. Python gebruikt dan de fallback-waarden.

---

## 🧠 Wat komt hierna?
Hoewel bovenstaande drie argumenttypes het vaakst voorkomen, bestaan er ook manieren om functies **flexibeler** te maken. Zo kun je bijvoorbeeld functies schrijven die **een variabel aantal argumenten** kunnen verwerken.



