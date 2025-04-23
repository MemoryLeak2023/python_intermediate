# Enclosing Namespace

## 🔁 Wat is een Enclosing Namespace?
De **enclosing namespace** is een **bijzondere vorm van lokale namespace** die ontstaat bij **geneste functies**.

- Een enclosing namespace ontstaat **binnen een functie**, wanneer daarin **nog een functie genest** wordt.
- Ze blijft bestaan zolang de enclosing functie actief is.

---

## 🧪 Voorbeeld: geneste functies
```python
global_variable = 'global'

def outer_function():
    outer_value = "outer"

    def inner_function():
        inner_value = "inner"

    inner_function()

outer_function()
```

### Wat gebeurt hier?
- `outer_function()` is de **enclosing function**.
- `inner_function()` is de **enclosed (geneste) function**.
- Wanneer we `outer_function()` aanroepen, ontstaat een namespace waarin ook `inner_function` wordt gedefinieerd.

---

## 🔍 Enclosing namespaces inspecteren
Hoewel Python geen `enclosing()`-functie heeft, kunnen we met `locals()` zien wat er in de enclosing namespace leeft.

```python
def outer_function():
    outer_value = "outer"

    def inner_function():
        inner_value = "inner"

    inner_function()
    print(locals())

outer_function()
```

➡️ Output:
```python
{'outer_value': 'outer', 'inner_function': <function outer_function.<locals>.inner_function at 0x7f46b56bc820>}
```

🧠 Wat valt op?
- `outer_value` is een gewone lokale variabele in `outer_function()`
- `inner_function` is een functie-object binnen de enclosing namespace — je ziet dat aan de naam: `outer_function.<locals>.inner_function`
- De namespace van `inner_function()` zelf is niet zichtbaar van buitenaf (want die bestaat enkel **tijdens de uitvoering** van die functie)

---

## 📦 Samengevat
- Enclosing namespaces ontstaan bij **geneste functies**.
- De enclosing namespace is **de lokale context van de buitenste functie** waarin de binnenste functies gedefinieerd zijn.
- Je kunt `locals()` gebruiken binnen de enclosing functie om deze context te inspecteren.
- Enclosing namespaces zijn belangrijk bij **closures**, **decorators** en **scopingregels**.


