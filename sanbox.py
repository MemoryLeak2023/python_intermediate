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

def total_bill(func, value):
    total = func(value)
    return f"The total amount owed is ${total:.2f}. Thank you! :)"

print(total_bill(add_tax, 100))