# Built-in Namespace

## 🧠 Wat is de Built-in Namespace?
De **built-in namespace** is één van de vier hoofdtypes van namespaces in Python. Het is de **hoogste** en meest universele laag, die automatisch beschikbaar is in elk Python-programma.

Dankzij deze namespace kunnen we functies zoals `print()`, `len()`, `str()` of `range()` gebruiken **zonder iets te importeren**.

Voorbeeld:
```python
color = str(123)   # werkt meteen
print(color)       # werkt ook meteen
```

Dat komt omdat deze namen voorkomen in de built-in namespace die **altijd actief is zolang de interpreter draait**.

---

## 🛠️ Hoe ziet die namespace eruit?
Met de volgende opdracht kun je de inhoud van de built-in namespace bekijken:

```python
print(dir(__builtins__))
```

➡️ Dit geeft een enorme lijst van functies, types, constanten en uitzonderingen.

Voorbeelden van wat je daarin vindt:
- ✅ **Functies**: `str()`, `zip()`, `slice()`, `sorted()`, `len()`, `input()`, `open()`...
- ⚠️ **Fouten (exceptions)**: `IndexError`, `KeyError`, `TypeError`, `ValueError`, `ZeroDivisionError`, ...
- 🔢 **Constanten**: `True`, `False`, `None`
- 🧱 **Types**: `int`, `float`, `list`, `dict`, `tuple`, `set`, `bool`, ...

---

## 📚 Wist je dat?
- Deze namespace wordt aangemaakt **bij het starten van de Python-interpreter**.
- Ze verdwijnt automatisch weer **wanneer het programma eindigt**.
- In totaal bevat de built-in namespace ongeveer **152 namen** (kan iets verschillen afhankelijk van de versie van Python).

Deze functies en types vormen de **basisbouwstenen van elke Python-toepassing** — zonder hen zou zelfs een simpele `print()` niet werken!

---


