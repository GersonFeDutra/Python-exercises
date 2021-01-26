products: tuple = ('Pencil', 1.75, 'Eraser', 2.0, 'Notebook', 15.90, 'Case', 25.0, 'Protractor', 4.20, 'Compass', 9.99,
                   'Bag', 120.32, 'Pens', 22.30, 'Book', 34.90)

print(f'{"-" * 30}\n{"PRICES LIST":^30}\n{"-" * 30}')

for i, item in enumerate(products):

    if i % 2 == 0:
        print(f'{item:.<21}', end='R$')
    else:
        print(f'{item:>7.2f}')
