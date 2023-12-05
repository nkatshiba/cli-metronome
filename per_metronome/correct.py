import time
import curses
import pygame

pygame.mixer.init()

beat_sound = pygame.mixer.Sound('sounds/high.wav')
accent_sound = pygame.mixer.Sound('sounds/bright.wav')


def main(stdscr):
    # Set up the screen
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Initialize BPM
    bpm = 120
    beat = 0

    # Initialize the time for the next beat
    next_beat_time = time.time()

    while True:
        # Calculate the time to wait before playing the next sound
        next_beat_time += 60.0 / bpm

        # Display the current BPM and beat
        stdscr.clear()
        stdscr.addstr(0, 0, f"BPM: {bpm}")
        stdscr.addstr(1, 0, f"Beat: {beat+1}")

        # Play the beat
        if beat == 0:
            # Accent on the first beat
            accent_sound.play()
        else:
            beat_sound.play()

        # Advance to the next beat
        beat = (beat + 1) % 4

        # Check for key presses
        c = stdscr.getch()

        if c == ord('q'):
            # Quit if 'q' is pressed
            break
        elif c == ord('+'):
            # Increase BPM if '+' is pressed
            bpm = min(bpm + 1, 300)
        elif c == ord('-'):
            # Decrease BPM if '-' is pressed
            bpm = max(bpm - 1, 20)

        # Wait for the next beat
        time.sleep(max(0, next_beat_time - time.time()))


if __name__ == "__main__":
    curses.wrapper(main)
