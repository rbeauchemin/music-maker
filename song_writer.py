'''
Plays a song in major key or minor key. ctrl+C to kill the song.
'''
import numpy as np
import pyaudio
import random
import music_degree

try:
    from itertools import izip
except ImportError: # Python 3
    izip = zip
    xrange = range


def sine_tone(stream, frequency, duration):
    """Creates a tone for the given frequency and duration
       in the form of a sine wave.

    Args:
        stream (PyAudio stream object): An audio stream that tones can be added to.
        frequency (float): The frequency of the tone to play
        duration (float): How long to play the tone in seconds
    """

    length = int(duration * sample_rate)
    factor = float(frequency) * (np.pi * 2) / sample_rate
    waveform = np.sin(np.arange(length) * factor)
    stream.write(waveform.astype(np.float32).tostring())


def random_song(stream, key='C4', tempo=60, scale='major'):
    """Creates a random song given the scale and tempo in seconds per beat.

    Args:
        stream (PyAudio stream object): An audio stream that tones can be added to.
        key (str): The muscial scale to base the song on. Default is 'C4'
        scale (str): Either major or minor. Default is 'major'
        tempo (int): Measure of beats per minute. Default is 60.
    """
    tempo_seconds = 60./tempo
    tones = list(music_degree.get_key(key, scale=scale).values())
    while True:
        sine_tone(stream, random.choice(tones), random.choice([tempo_seconds/4.,
                                                               tempo_seconds/2.,
                                                               tempo_seconds]))


def zeldas_lullaby(stream):
    """Plays zelda's lullaby from Nintendo's Ocarina of Time. It is 3/4 time, so
       I will be using 6ths 

    Args:
        stream (PyAudio stream object): An audio stream that tones can be added to.
    """
    t = music_degree.tone_map
    melody = ['G3', 'B3', 'F3', 'E3', 'F3', 'G3', 'B3', 'F3',
              'G3', 'B3', 'F4', 'E4', 'B3', 'A3', 'G3', 'F3',
              'G3', 'B3', 'F3', 'E3', 'F3', 'G3', 'B3', 'F3',
              'G3', 'B3', 'F4', 'E4', 'B3',
              'B3', 'A3', 'G3', 'A3', 'G3', 'E3',
              'A3', 'G3', 'F3', 'G3', 'F3', 'C3',
              'B3', 'A3', 'G3', 'A3', 'G3', 'E3', 'A3', 'E4']
    sixths = [4, 2, 4, 1, 1, 4, 2, 6, 4, 2, 4, 2, 4, 1, 1, 6,
              4, 2, 4, 1, 1, 4, 2, 6, 4, 2, 4, 2, 12,
              4, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1, 2, 2, 12]

    for i in range(len(melody)):
        sine_tone(stream, t[melody[i]], sixths[i]/3.5)



if __name__ == '__main__':
    p = pyaudio.PyAudio()
    sample_rate = 44100
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=1,)
    
    
    # random_song(stream)
    zeldas_lullaby(stream)

    stream.stop_stream()
    stream.close()
    p.terminate()