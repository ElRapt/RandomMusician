import random


echelle_majeure = ['Do', 'Ré', 'Mi', 'Fa', 'Sol', 'La', 'Si']

sequence_notes = []
for _ in range(4):
    note = random.choice(echelle_majeure)
    sequence_notes.append(note)

print(sequence_notes)
