# Local Namespace

## 🧬 Wat is de Local Namespace?
De **local namespace** is het **diepste niveau** van namespaces in Python. Deze ontstaat **telkens een functie wordt uitgevoerd**, en bestaat **alleen binnen die functie** zolang die actief is.

Voorbeeld:
```python
global_variable = 'global'

def add(num1, num2):
    nested_value = 'Inside Function'
    print(num1 + num2)

add(5, 10)
```

Hier zie je:
- `global_variable` bestaat in de **global namespace**.
- `num1`, `num2` en `nested_value` bestaan **alleen binnen `add()`** — dat is de **local namespace**.

---

## 🔍 De `locals()` functie
Net zoals we `globals()` kunnen gebruiken om de globale namespace te bekijken, kunnen we `locals()` gebruiken om te zien wat er zich **lokaal** afspeelt binnen een functie.

```python
def add(num1, num2):
    nested_value = 'Inside Function'
    print(num1 + num2)
    print(locals())

add(5, 10)
```

➡️ Output:
```
15
{'num1': 5, 'num2': 10, 'nested_value': 'Inside Function'}
```

### Wat valt op?
- `locals()` toont een dictionary van alle **lokaal gedefinieerde namen en hun waarden**.
- Zowel de **functieparameters** (`num1`, `num2`) als de **interne variabelen** (`nested_value`) worden weergegeven.
- De **globale variabele `global_variable` zit hier niet bij**, want die hoort bij een andere namespace.

> 📌 Als je `locals()` buiten een functie gebruikt, gedraagt die zich identiek aan `globals()`.

---

## 📦 Samengevat
- Elke functie genereert zijn **eigen lokale namespace** bij uitvoering.
- Deze verdwijnt zodra de functie klaar is.
- Je kunt `locals()` gebruiken om te zien welke namen in die functie beschikbaar zijn.
- Parameters van de functie maken ook deel uit van de lokale namespace.



