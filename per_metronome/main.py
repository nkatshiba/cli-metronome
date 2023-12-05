import time
import pygame
import urwid

pygame.mixer.init()

beat_sound = pygame.mixer.Sound('sounds/high.wav')
accent_sound = pygame.mixer.Sound('sounds/bright.wav')


def query_bpm():
    user_input = input("Please enter something: ")
    print("You entered: " + user_input)
    return user_input


def main():
    bpm = float(query_bpm())
    beat = 0
    next_beat_time = time.time()

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
        beat = (beat + 1) % 4  # Increment beat first, then apply modulo
        if beat == 0:  # Now this will be true every four beats
            accent_sound.play()
        else:
            beat_sound.play()
        text.set_text(f"BPM: {bpm}\nBeat: {beat + 1}")  # Display beat as 1-4 for user-friendliness
        loop.set_alarm_at(next_beat_time, update)

    text = urwid.Text(f"BPM: {bpm}\nBeat: {beat}")
    filler = urwid.Filler(text, 'top')
    loop = urwid.MainLoop(filler, unhandled_input=on_key)
    loop.set_alarm_at(next_beat_time, update)
    loop.run()


if __name__ == "__main__":
    main()
