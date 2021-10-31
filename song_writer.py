'''
Plays a song in major key or minor key. ctrl+C to kill the song.
'''
import numpy as np
import pyaudio
import random
import music_degree
from pynput import keyboard
from threading import Thread
from time import sleep
# from concurrent.futures import ThreadPoolExecutor

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class MusicMaker():
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.sample_rate = 44100
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=self.sample_rate,
                                  output=1,)


    def _init_piano_mode(self):
        # For the piano utility
        self.active_keys = []
        self.sostenuto = False
        # self.process_pool = ThreadPoolExecutor(max_workers=8)
        self.piano_mode = True


    def __enter__(self):
        return self


    def __exit__(self, *args, **kwargs):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


    def on_press(self, key):
        if key == keyboard.Key.esc:
            self.piano_mode = False
            return False
        try:
            k = key.char.lower()
        except:
            k = key.name.lower()
        if k in ['a', 's', 'd', 'f', 'j', 'k', 'l', ';']:
            if k not in self.active_keys:
                self.active_keys.append(k)
        if k == 'shift':
            self.sostenuto = True


    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.piano_mode = False
            return False
        try:
            k = key.char.lower()
        except:
            k = key.name.lower()
        if k in ['a', 's', 'd', 'f', 'j', 'k', 'l', ';']:
            self.active_keys = [_ for _ in self.active_keys if _ != k]
        if k == 'shift':
            self.sostenuto = False


    @threaded
    def piano_watcher(self, keys):
        key_mapper = {}
        for i, keyboard_key in enumerate(['a', 's', 'd', 'f', 'j', 'k', 'l', ';']):
            key_mapper[keyboard_key] = keys[i] if len(keys) > i else 0.0
        while self.piano_mode:
            sleep(0.1)
            self.sine_tone([key_mapper[_] for _ in self.active_keys if _ in key_mapper],
                           0.1, sostenuto=self.sostenuto)


    def sine_tone(self, frequency, duration, sostenuto = False):
        """Creates a tone for the given frequency and duration
        in the form of a sine wave.

        Args:
            frequency (float): The frequency of the tone to play.
            duration (float): How long to play the tone in seconds.
            sostenuto (boolean, optional): True if sustain should be applied.
                Default is False (exponential decay applied).
        """
        length = int(duration * self.sample_rate)
        waves = []
        if isinstance(frequency, list):
            if len(frequency) == 0:
                return
        else:
            frequency = [frequency]
        for f in frequency:
            factor = float(f) * (np.pi * 2) / self.sample_rate
            waves.append(np.sin(np.arange(length) * factor))
        waveform = sum(waves)
        if not sostenuto:
            waveform *= (2 ** (np.arange(length) * factor * -1 / 400.))
        self.stream.write(waveform.astype(np.float32).tostring())


    def random_song(self, key='C4', tempo=60, scale='major'):
        """Creates a random song given the scale and tempo in seconds per beat.

        Args:
            key (str, optional): The muscial scale to base the song on. Default is 'C4'.
            scale (str, optional): Either major or minor. Default is 'major'.
            tempo (int, optional): Measure of beats per minute. Default is 60.
        """
        tempo_seconds = 60./tempo
        tones = list(music_degree.get_key(key, scale=scale, with_rests=True).values())
        while True:
            self.sine_tone(random.choice(tones),
                           random.choice([tempo_seconds/4.,
                                          tempo_seconds/2.,
                                          tempo_seconds]))


    def play_song(self, melody, beats, tempo=60):
        """Plays zelda's lullaby from Nintendo's Ocarina of Time. It is 3/4 time, so
        I will be using 6ths.

        Args:
            melody (list[float]): List of notes to be played in the song.
            beats (list[float]): Number of beats for each of the notes in the melody.
            tempo (int, optional): Measure of beats per minute. Default is 60.
        """
        for i in range(len(melody)):
            self.sine_tone(melody[i], 60.*beats[i]/tempo)


    def play_piano(self, keys):
        """An interactive piano player that uses the keyboard as a keyboard!
        A set of 8 keys is required that can be minor or major and maps to
        the asdf and jkl; characters. Shift toggles sostenuto.

        Args:
            keys (dict): A set of notes and their frequencies for the keys
                to map to.
        """
        print('Starting Piano mode:',
              ' - Keys are in [asdfjkl;].'
              ' - Press ESC to quit.')
        self._init_piano_mode()
        self.piano_watcher(keys)
        listener = keyboard.Listener(on_press=self.on_press,
                                     on_release=self.on_release)
        listener.start()  # start to listen on a separate thread
        listener.join()  # remove if main thread is polling self.keys
        self.piano_mode = False


if __name__ == '__main__':
    mode = 'piano'

    with MusicMaker() as m:
        if mode == 'piano':
            note = input('Please input a base note [C4]: ') or 'C4'
            scale = input('Please input a scale ([major]/minor): ') or 'major'
            m.play_piano(music_degree.get_key(note, scale=scale, ordered_tones_only=True))
        if mode == 'random_song':
            m.random_song(key='C4', tempo=60, scale='minor')
        if mode == 'zeldas_lullaby':
            t = music_degree.tone_map
            melody = ['G3', 'B3', 'F3', 'E3', 'F3', 'G3', 'B3', 'F3',
                      'G3', 'B3', 'F4', 'E4', 'B3', 'A3', 'G3', 'F3',
                      'G3', 'B3', 'F3', 'E3', 'F3', 'G3', 'B3', 'F3',
                      'G3', 'B3', 'F4', 'E4', 'B3',
                      'B3', 'A3', 'G3', 'A3', 'G3', 'E3',
                      'A3', 'G3', 'F3', 'G3', 'F3', 'C3',
                      'B3', 'A3', 'G3', 'A3', 'G3', 'E3', 'A3', 'E4']
            beats = [2, 1, 2, 0.5, 0.5, 2, 1, 3, 2, 1, 2, 1, 2, 0.5, 0.5, 3,
                     2, 1, 2, 0.5, 0.5, 2, 1, 3, 2, 1, 2, 1, 6,
                     2, 0.5, 0.5, 0.5, 0.5, 2, 2, 0.5, 0.5, 0.5, 0.5, 2,
                     2, 0.5, 0.5, 0.5, 0.5, 1, 1, 6]
            m.play_song([t[_] for _ in melody],
                        [float(_) for _ in beats],
                        tempo=120)
        if mode == 'play_note':
            # I use this one for tuning
            note = input('Please input a note [C4]: ') or 'C4'
            tone = music_degree.tone_map[note]
            m.sine_tone(tone, 2, sostenuto = True)
        if mode == 'play_key':
            note = input('Please input a base note [C4]: ') or 'C4'
            scale = input('Please input a scale ([major]/minor): ') or 'major'
            key = music_degree.get_key(note, scale=scale)
            for tone in key.values():
                m.sine_tone(tone, 1, sostenuto = False)
