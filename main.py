import random
import pyaudio
import numpy as np
import math
import sounddevice as sd


sample_rate = 44100  
duration = 0.3
volume = 0.2

echelle_majeure = {
    'Do': 261.63,
    'Ré': 293.66,
    'Mi': 329.63,
    'Fa': 349.23,
    'Sol': 392.00,
    'La': 440.00,
    'Si': 493.88
}

sequence_notes = []
for _ in range(20):
    note = random.choice(list(echelle_majeure.keys()))
    sequence_notes.append(note)

print(sequence_notes)


def generate_tone(frequency):
    samples = np.arange(int(duration * sample_rate))
    signal = volume * np.sin(2 * np.pi * frequency * samples / sample_rate)
    return signal.astype(np.float32)

def jouer_note(frequency):
    signal = generate_tone(frequency)
    sd.play(signal, sample_rate)
    sd.wait()

for note in sequence_notes:
    jouer_note (echelle_majeure[note])