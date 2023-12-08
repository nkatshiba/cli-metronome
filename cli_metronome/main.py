import time

from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import urwid

pygame.mixer.init()
beat_sound = pygame.mixer.Sound('sounds/high.wav')
accent_sound = pygame.mixer.Sound('sounds/bright.wav')


def query_bpm():
    bpm = input("Choose BPM> ")
    print("BPM: " + bpm)
    return bpm


def main():
    bpm = float(query_bpm())
    beat = 0
    next_beat_time = time.time()
    beat_symbols = ['\\...', '.|..', '../.', '...-']  # List of beat symbols

    def on_key(key):
        nonlocal bpm, beat, next_beat_time
        if key == 'q':
            raise urwid.ExitMainLoop()
        elif key == '+':
            bpm = min(bpm + 1, 300)
        elif key == '-':
            bpm = max(bpm - 1, 20)

    def update(_loop, _data):
        nonlocal bpm, beat, next_beat_time
        next_beat_time += 60.0 / bpm
        beat = (beat + 1) % 4
        if beat == 0:
            accent_sound.play()
        else:
            beat_sound.play()
        text.set_text(f"BPM: {bpm}\nBeat: {beat_symbols[beat]}")  # Display the current beat symbol
        loop.set_alarm_at(next_beat_time, update)

    text = urwid.Text(f"BPM: {bpm}\nBeat: {beat_symbols[beat]}")
    filler = urwid.Filler(text, 'top')
    loop = urwid.MainLoop(filler, unhandled_input=on_key)
    loop.set_alarm_at(next_beat_time, update)
    loop.run()


if __name__ == "__main__":
    main()
