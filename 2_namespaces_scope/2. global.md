# Global Namespace

## 🌐 Wat is de Global Namespace?
De **global namespace** bestaat één niveau onder de built-in namespace. Ze bevat **alle niet-geneste namen** die op module- of bestandsniveau gedeclareerd zijn — met andere woorden: alles wat je direct in je `.py`-bestand definieert.

Deze namespace wordt aangemaakt **wanneer je script wordt uitgevoerd**, en blijft bestaan zolang de interpreter actief is.

---

## 📁 Voorbeeld
Stel we hebben een script `main.py`:

```python
import random

first_name = "Jaya"
last_name = "Bodegard"

def print_variables():
    random_number = random.randint(0,9)
    print(first_name)
    print(last_name)
    print(random_number)
```

Hier definiëren we:
- Twee globale variabelen: `first_name` en `last_name`
- Een functie: `print_variables()`
- Een geïmporteerde module: `random`

Allemaal maken ze deel uit van de **global namespace** — behalve `random_number`, want die zit **in een functie** (lokaal).

---

## 🔍 De `globals()` functie
Python biedt een ingebouwde functie `globals()` om de globale namespace van je programma te inspecteren:

```python
print(globals())
```

➡️ Output (ingekort):
```python
{
 '__name__': '__main__',
 '__file__': 'main.py',
 'first_name': 'Jaya',
 'last_name': 'Bodegard',
 'print_variables': <function print_variables at 0x...>,
 'random': <module 'random' from '/usr/lib/...'>
}
```

### Wat valt op?
- `first_name`, `last_name` en `print_variables` zitten in de globale namespace.
- `random` is er ook, maar wordt weergegeven als een **moduleobject** — niet als individuele functies van `random` zelf.
- Variabelen die **binnen functies** gedefinieerd zijn (zoals `random_number`) staan hier **niet in**.

---

## 🧠 Let op bij imports
Wanneer je `import random` gebruikt:
- Wordt niet de hele inhoud van `random` toegevoegd aan jouw namespace.
- Enkel de naam `random` komt in jouw globale namespace terecht.
- De rest zit in een **aparte namespace** die enkel via `random.` toegankelijk is.

➡️ Dit voorkomt dat jouw namespace overspoeld raakt met honderden namen uit externe modules.

---

## 📌 Samengevat
- De globale namespace bevat **alle top-level namen** in je script.
- Gebruik `globals()` om te inspecteren welke namen daar allemaal in zitten.
- Variabelen binnen functies zijn **niet** globaal — die leer je straks kennen onder de lokale namespace.

Op naar het volgende niveau: de **local namespace**! 🧪

