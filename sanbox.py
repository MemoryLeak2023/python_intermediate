def print_animals(animal1, animal2, *args, animal4, **kwargs):
    print(animal1, animal2)
    print(args)
    print(animal4)
    print(kwargs)

print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')