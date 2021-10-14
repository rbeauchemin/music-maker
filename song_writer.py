'''
Plays a song in major key or minor key. ctrl+C to kill the song.
'''
import numpy as np
import pyaudio
import random
import music_degree
from pynput import keyboard


class MusicMaker():
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.sample_rate = 44100
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=self.sample_rate,
                                  output=1,)


    def __enter__(self):
        return self


    def __exit__(self, *args, **kwargs):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


    def sine_tone(self, frequency, duration, sostenuto = False):
        """Creates a tone for the given frequency and duration
        in the form of a sine wave.

        Args:
            frequency (float): The frequency of the tone to play.
            duration (float): How long to play the tone in seconds.
            sostenuto (boolean): If sustain should be applied. Default is False (exp. decay).
        """

        length = int(duration * self.sample_rate)
        factor = float(frequency) * (np.pi * 2) / self.sample_rate
        waveform = np.sin(np.arange(length) * factor)
        if not sostenuto:
            waveform *= (2 ** (np.arange(length) * factor * -1 / 400.))
        self.stream.write(waveform.astype(np.float32).tostring())


    def random_song(self, key='C4', tempo=60, scale='major'):
        """Creates a random song given the scale and tempo in seconds per beat.

        Args:
            key (str): The muscial scale to base the song on. Default is 'C4'.
            scale (str): Either major or minor. Default is 'major'.
            tempo (int): Measure of beats per minute. Default is 60.
        """
        tempo_seconds = 60./tempo
        tones = list(music_degree.get_key(key, scale=scale, with_rests=True).values())
        while True:
            self.sine_tone(self.stream,
                           random.choice(tones),
                           random.choice([tempo_seconds/4.,
                                          tempo_seconds/2.,
                                          tempo_seconds]))


    def zeldas_lullaby(self):
        """Plays zelda's lullaby from Nintendo's Ocarina of Time. It is 3/4 time, so
        I will be using 6ths.

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
            # /3.5 corrects the tempo
            self.sine_tone(self.stream, t[melody[i]], sixths[i]/3.5)


if __name__ == '__main__':
    mode = 'play_key'

    with MusicMaker() as m:
        if mode == 'random_song':
            m.random_song()
        elif mode == 'zelda':
            m.zeldas_lullaby()
        elif mode == 'play_note':
            note = input('Please input a note [C4]: ') or 'C4'
            tone = music_degree.tone_map[note]
            m.sine_tone(tone, 1, sostenuto = False)
        elif mode == 'play_key':
            note = input('Please input a base note [C4]: ') or 'C4'
            scale = input('Please input a scale ([major]/minor): ') or 'major'
            key = music_degree.get_key(note, scale=scale)
            for tone in key.values():
                m.sine_tone(tone, 1, sostenuto = False)
