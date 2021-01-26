def notes(*values: float, situation: bool = False) -> dict:
    """
    Show information about the notes of a classroom.
    :param values: All the notes from the class.
    :param situation: If you add situation to the data.
    :return: All the information about the class:
        'qtd': The number of pupils in the class.
        'higher': The higher note from the class.
        'lower': The lower note from the class.
        'medium': The medium note from the class.
        'situation': (Optional) 'BAD' if medium < 4 or 'OK' if medium < 7, or 'GOOD' if higher.
    """
    qtd: int = len(values)
    data: dict = {
        'qtd': qtd,
        'higher': max(values),
        'lower': min(values),
        'medium': sum(values) / qtd
    }
    if situation:
        data['situation'] = 'GOOD' if data['medium'] > 7 else 'BAD' if data['medium'] < 5 else 'OK'

    return data


print(notes(5.5, 9.5, 10, 6.5, situation=True))
print(notes(5.5, 1.5, 3, 6.5, situation=True))
print(notes(5.5, 9.5, 10))
help(notes)
