# Mutable Default Arguments

## 🧠 Inleiding: Een Veelvoorkomende Valstrik in Python

In Python is het mogelijk om standaardwaarden toe te kennen aan functieargumenten. Maar wanneer deze standaardwaarden **veranderlijk** (mutable) zijn — zoals lijsten of dictionaries — kan dit tot onverwacht gedrag leiden. Dit fenomeen wordt vaak aangeduid als een **"gotcha"**: een eigenschap van de programmeertaal die tegen je intuïtie ingaat en daardoor gemakkelijk tot fouten leidt.

## 🎓 Voorbeeldsituatie
Stel je voor dat we een applicatie maken voor een school en een functie schrijven om studenten aan te maken. Een student heeft een naam, een leeftijd en een lijst van behaalde cijfers (grades), die standaard leeg is.

```python
def createStudent(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades
    }
```

We maken twee studenten aan:

```python
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)
```

Daarna voegen we cijfers toe met deze functie:

```python
def addGrade(student, grade):
    student['grades'].append(grade)
    print(student['grades'])
```

En we voegen cijfers toe:

```python
addGrade(chrisley, 90)
addGrade(dallas, 100)
```

### Verwachte output:
```
[90]
[100]
```

### Werkelijke output:
```
[90]
[90, 100]
```

😱 Oeps! Wat is hier misgegaan?

## 🔍 Wat is het probleem?
Wanneer je een **mutable object** zoals een lijst opgeeft als standaardargument in een functie, **wordt dit object slechts één keer aangemaakt**, op het moment dat de functie wordt geïnterpreteerd — niet telkens als de functie wordt aangeroepen. Dat betekent dat alle aanroepen van die functie **dezelfde** standaardlijst gebruiken. Daardoor delen `chrisley` en `dallas` per ongeluk dezelfde lijst van cijfers.

## 🔁 Mutable versus Immutable in Python

Om de eerder besproken "gotcha" echt te begrijpen, moeten we eerst duidelijk maken wat Python beschouwt als **mutable** (veranderlijk) en **immutable** (onveranderlijk).

### ✅ Mutable types (veranderlijk)
Deze objecten kunnen worden aangepast nadat ze zijn aangemaakt:
- `list`
- `dict`
- `set`

Voorbeelden van wijzigingen:
- `.append()` aan een lijst
- `.remove()` van een element
- sleutels toevoegen/verwijderen bij een dictionary

### 🚫 Immutable types (onveranderlijk)
Deze objecten kunnen **niet** gewijzigd worden. Elke bewerking geeft een **nieuw object** terug:
- `int`, `float`, `bool`
- `str`
- `tuple`

Daarom zijn deze veilig om te gebruiken als standaardwaarden in functieparameters.

---

## 🧪 Hoe werkt dit bij functies?
Volgens de officiële Python-documentatie:
> "Standaardwaarden van parameters worden geëvalueerd van links naar rechts op het moment dat de functie wordt gedefinieerd."

Dat betekent:
- De waarde van het standaardargument wordt **één keer** aangemaakt (tijdens definitie).
- Bij elke oproep van de functie wordt **dezelfde instantie** van dat object gebruikt.

### Voorbeeld: `id()` toont het geheugenadres
```python
print(id(chrisley['grades']))
print(id(dallas['grades']))
```
Beide geven exact hetzelfde ID — ze delen dus **dezelfde lijst**.

---

## ✅ De oplossing: gebruik `None` als standaardwaarde
Gebruik `None` als speciale placeholder om aan te geven dat er geen waarde werd doorgegeven. Maak de lijst vervolgens binnen de functie aan:

```python
def createStudent(name, age, grades=None):
    if grades is None:
        grades = []
    return {
        'name': name,
        'age': age,
        'grades': grades
    }
```

Met deze aanpak krijgt elke student zijn **eigen** lijst van cijfers, ook al worden ze zonder argument `grades` aangemaakt.

```python
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

addGrade(chrisley, 90)
addGrade(dallas, 100)
```

Output:
```
[90]
[100]
```

---


> 📁 Deze samenvatting maakt deel uit van Sandra's GitHub-repository over de **Python Intermediate** cursus op Codecademy.

