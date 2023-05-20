import random
import numpy as np
import sounddevice as sd
from pydub import AudioSegment
from pydub.playback import play
import os

# Constants
SAMPLE_RATE = 44100  
DURATION = 0.3
VOLUME = 0.2

MAJOR_SCALE = {
    'Do': 261.63,
    'Ré': 293.66,
    'Mi': 329.63,
    'Fa': 349.23,
    'Sol': 392.00,
    'La': 440.00,
    'Si': 493.88
}

PIANO_NOTES = {
    'Do': 'piano_notes/c1.wav',
    'Ré': 'piano_notes/d1.wav',
    'Mi': 'piano_notes/e1.wav',
    'Fa': 'piano_notes/f1.wav',
    'Sol': 'piano_notes/g1.wav',
    'La': 'piano_notes/a1.wav',
    'Si': 'piano_notes/b1.wav'
}

def generate_tone(frequency):
    """Generate a sinusoidal tone."""
    samples = np.arange(int(DURATION * SAMPLE_RATE))
    signal = VOLUME * np.sin(2 * np.pi * frequency * samples / SAMPLE_RATE)
    return signal.astype(np.float32)

def play_tone(frequency):
    """Play a tone of a given frequency."""
    signal = generate_tone(frequency)
    sd.play(signal, SAMPLE_RATE)
    sd.wait()

def create_sequence(num_notes):
    """Create a random sequence of notes."""
    sequence = []
    for _ in range(num_notes):
        note = random.choice(list(MAJOR_SCALE.keys()))
        sequence.append(note)
    return sequence

def play_note_sequence(sequence):
    """Play a sequence of notes."""
    for note in sequence:
        file_path = os.path.join(os.getcwd(), PIANO_NOTES[note])
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue
        try:
            piano_note = AudioSegment.from_wav(file_path)
            play(piano_note)
        except Exception as e:
            print(f"Failed to play note: {e}")

sequence_notes = create_sequence(5)
print(sequence_notes)
play_note_sequence(sequence_notes)
