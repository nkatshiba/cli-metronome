import npyscreen
import pygame
import time
import threading

pygame.mixer.init()

beat_sound = pygame.mixer.Sound('sounds/high.wav')
accent_sound = pygame.mixer.Sound('sounds/bright.wav')


class MetronomeApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.bpm = 120
        self.addForm('MAIN', MetronomeForm, name="Metronome")


class MetronomeForm(npyscreen.Form):
    def create(self):
        self.bpm = self.add(npyscreen.TitleSlider,
                            out_of=300, name="BPM", value=120)
        self.beat = self.add(npyscreen.TitleFixedText, name="Beat", value="1")

        # Start the metronome thread
        metronome_thread = threading.Thread(target=self.update, daemon=True)
        metronome_thread.start()

    def while_waiting(self):
        self.parentApp.bpm = int(self.bpm.value)

    def update(self):
        while True:
            for beat in range(4):
                self.beat.value = str(beat + 1)
                self.beat.display()

                if beat == 0:
                    accent_sound.play()
                else:
                    beat_sound.play()

                time.sleep(60.0 / self.parentApp.bpm)


if __name__ == "__main__":
    app = MetronomeApp()
    app.run()
