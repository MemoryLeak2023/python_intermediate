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

## ✅ De juiste aanpak
Gebruik altijd `None` als standaardwaarde voor een veranderlijk argument, en maak dan de lijst aan binnen de functie:

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

Zo wordt er bij elke aanroep van `createStudent()` een **nieuwe lijst** aangemaakt als er geen `grades` wordt meegegeven. Probleem opgelost!

---

In het volgende hoofdstuk gaan we dit fenomeen verder oefenen en beter begrijpen. ✅

> 📁 Deze samenvatting maakt deel uit van Sandra's GitHub-repository over de **Python Intermediate** cursus op Codecademy.

