# Introduction to Names and Namespaces

## 🏷️ Wat is een naam (name) in Python?
In Python is een **naam** (ook wel identifier of symbolische naam genoemd) een manier om een **object te benoemen**. Dat kan bijvoorbeeld een string, een lijst, een functie of zelfs een klasse zijn.

```python
color = "cyan"
```

➡️ In dit voorbeeld:
- `color` is de naam
- `'cyan'` is het object (een string)

We gebruiken namen om te **verwijzen naar objecten** — dit maakt het programmeren leesbaar en beheersbaar.

---

## 📦 Wat is een namespace?
Een **namespace** is een **verzameling van namen** en de objecten waarnaar ze verwijzen. Python beheert dit met een intern **woordenboek**:

```python
{'color': 'cyan'}
```

Wanneer je `print(color)` aanroept, kijkt Python in de namespace:
- Is `color` daar gedefinieerd?
- Zo ja, geef het bijbehorende object terug (in dit geval `'cyan'`).

➡️ Output:
```
cyan
```

---

## 🧠 Waarom zijn namespaces belangrijk?
Python-programma’s kunnen **honderden of duizenden namen** bevatten. Dankzij namespaces weet Python **waar welke naam thuishoort** en **welk object ermee bedoeld wordt**.

In de volgende onderdelen duiken we dieper in de **vier belangrijkste types namespaces**:

1. 🧱 **Built-in** — standaardfuncties zoals `print()`, `len()`, `range()`, ...
2. 🌐 **Global** — namen die op module-niveau gedefinieerd zijn
3. 🔁 **Enclosing** — namen in omliggende functies (nested functions)
4. 🧬 **Local** — namen binnen de actieve functie of scope

---



