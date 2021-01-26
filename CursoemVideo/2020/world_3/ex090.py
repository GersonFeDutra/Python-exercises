pupil: dict = {
    'nome': input('What is the name of the pupil? '),
    'medium': float(input('What is the medium of the pupil? '))
}

if pupil['medium'] >= 7:
    pupil['situation'] = 'approved'
else:
    pupil['situation'] = 'disapproved'

print(pupil)
