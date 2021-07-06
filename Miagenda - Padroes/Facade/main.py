#Código para métodos e exemplos de Facade

class Amplifier:
    def on(self):
        pass
    
    def off(self):
        pass
    
    def set_dvd(self):
        pass
    
    def set_surround_sound(self):
        pass
    
    def set_volume(self, vol):
        pass


class Tuner:
    pass


class DvdPlayer:
    def on(self):
        pass
    
    def play(self, movie):
        pass
    
    def stop(self):
        pass
    
    def eject(self):
        pass
    
    def off(self):
        pass


class CdPlayer:
    pass


class Projector:
    def on(self):
        pass
    
    def wide_screen_mode(self):
        pass
    
    def off(self):
        pass


class TheaterLights:
    def dim(self):
        pass
    
    def on(self):
        pass


class Screen:
    def down(self):
        pass
    
    def up(self):
        pass


class PopcornPopper:
    def on(self):
        pass
    
    def pop(self):
        pass
    
    def off(self):
        pass

class HomeTheaterFacade:
    def __init__(self, amp, tuner, dvd, cd, projector, lights, screen, popper):
        self.amp = amp
        self.tuner = tuner
        self.dvd = dvd
        self.cd = cd
        self.projector = projector
        self.lights = lights
        self.screen = screen
        self.popper = popper
    
    def watch_movie(self, movie):
        print("Iniciando filme")
        self.popper.on()
        self.popper.pop()
        self.lights.dim()
        self.screen.down()
        self.projector.on()
        self.projector.wide_screen_mode()
        self.amp.on()
        self.amp.set_dvd()
        self.amp.set_surround_sound()
        self.amp.set_volume(2)
        self.dvd.on()
        self.dvd.play(movie)
    
    def end_movie(self):
        print("Fim do filme")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.dvd.stop()
        self.dvd.eject()
        self.dvd.off()

if __name__ == "__main__":
    
    amp = Amplifier()
    tuner = Tuner()
    dvd = DvdPlayer()
    cd = CdPlayer()
    projector = Projector()
    lights = TheaterLights()
    screen = Screen()
    popper = PopcornPopper()
    
    home_theater = HomeTheaterFacade(amp, tuner, dvd, cd, projector, lights, screen, popper)
    home_theater.watch_movie("Filme: Kong")
    home_theater.end_movie()
