#Código para métodos e exemplos de Command

class Command:
    def execute(self):
        raise NotImplementedError
    
    def undo(self):
        raise NotImplementedError


class GarageDoorUpCommand(Command):
    def __init__(self, door):
        self.door = door  # Receiver
    
    def execute(self):
        self.door.up()
        
    def undo(self):
        self.door.down()


class GarageDoorDownCommand(Command):
    def __init__(self, door):
        self.door = door  # Receiver
    
    def undo(self):
        self.door.up()


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light  # Receiver
    
    def execute(self):
        self.light.on()
        
    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light  # Receiver
    
    def execute(self):
        self.light.off()
        
    def undo(self):
        self.light.on()


class CeilingFanOnCommand(Command):
    def __init__(self, cf):
        self.cf = cf
    
    def execute(self):
        self.cf.on()
        
    def undo(self):
        self.cf.off()


class CeilingFanOffCommand(Command):
    def __init__(self, cf):
        self.cf = cf
    
    def execute(self):
        self.cf.off()
        
    def undo(self):
        self.cf.on()


class CeilingFanHighCommand(Command):
    def __init__(self, cf):
        self.cf = cf
        self.prev_speed = 0
    
    def execute(self):
        self.prev_speed = self.cf.speed
        self.cf.off()
    
    def undo(self):
        if self.prev_speed == self.cf.HIGH:
            self.cf.high()
        elif self.prev_speed == self.cf.MEDIUM:
            self.cf.medium()
        elif self.prev_speed == self.cf.LOW:
            self.cf.low()
        elif self.prev_speed == self.cf.OFF:
            self.cf.off()


class StereoOnCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()
        
    def undo(self):
        self.stereo.off()


class StereoOffCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.off()
        
    def undo(self):
        self.stereo.on()


class StereoSetCdCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.set_cd()
        
    def undo(self):
        pass
        

class NoCommand(Command):
    def execute(self):
        pass
    
    def undo(self):
        pass

class Light:
    def __init__(self, location=""):
        self.location = location
    
    def on(self):
        print("Luz ligada")
    
    def off(self):
        print("Light apagada")


class GarageDoor:
    def __init__(self, location=""):
        self.location = location
    
    def up(self):
        print("A porta da garagem está aberta")
    
    def down(self):
        print("A porta da garagem está fechada")
    

class Stereo:
    def __init__(self, location=""):
        self.location = location
    
    def on(self):
        print("Estéreo Ligado")
    
    def off(self):
        print("Estéreo Desligado")

    def set_cd(self):
        print("Estéreo está definido para entrada de CD")

    def set_volume(self, vol):
        print("Volume estéreo ajustado para ", vol)


class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0
    
    def __init__(self, location="", speed=OFF):
        self.location = location
        self.speed = speed
        
    def high(self):
        self.speed = self.HIGH

    def medium(self):
        self.speed = self.MEDIUM
        
    def low(self):
        self.speed = self.LOW
    
    def on(self):
        print("Ventilador de teto ligado")
    
    def off(self):
        print("Ventilador de teto desligado")
        self.speed = self.OFF

class SimpleRemoteControl:
    def __init__(self):
        self.slot = None
    
    def set_command(self, command):
        self.slot = command
    
    def button_was_pressed(self):
        self.slot.execute()


class RemoteControl:
    
    def __init__(self):
        self.on_commands = []
        self.off_commands = []
        self.undo_command = NoCommand()
        
        self.no_command = NoCommand()
        for i in range(7):
            self.on_commands.append(self.no_command)
            self.off_commands.append(self.no_command)
            
    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command
        
    def on__button_was_pushed(self, slot):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]
        
    def off__button_was_pushed(self, slot):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]
        
    def undo__button_was_pushed(self, slot):
        self.undo_command.undo()
        
    def __str__(self):
        descr = ["\n------ Remote Control -------\n"]
        for i in range(len(self.on_commands)):
            descr.append("[slot " + str(i) + "]" + self.on_commands[i].__class__.__name__
                         + " " + self.off_commands[i].__class__.__name__ + "\n")
        
        return descr

if __name__ == "__main__":
    
    remote = SimpleRemoteControl()
    light = Light()
    light_on = LightOnCommand(light)
    garage_door = GarageDoor()
    garage_door_open = GarageDoorUpCommand(garage_door)
    
    remote.set_command(light_on)
    remote.button_was_pressed()
    remote.set_command(garage_door_open)
    remote.button_was_pressed()
    
    remote_control = RemoteControl()
    living_room_light = Light("Sala de estar")
    kitchen_light = Light("Cozinha")
    ceiling_fan = CeilingFan("Sala de estar")
    garage_door2 = GarageDoor("")
    stereo = Stereo("Sala de estar")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)
    ceiling_fan_on = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)
    garage_door2_up = GarageDoorUpCommand(garage_door)
    garage_door2_down = GarageDoorDownCommand(garage_door)
    stereo_on = StereoOnCommand(stereo)
    stereo_off = StereoOffCommand(stereo)
    
    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_control.set_command(3, stereo_on, stereo_off)
    
        
    remote_control.on__button_was_pushed(0)
    remote_control.off__button_was_pushed(0)
    remote_control.on__button_was_pushed(1)
    remote_control.off__button_was_pushed(1)
    remote_control.on__button_was_pushed(2)
    remote_control.off__button_was_pushed(2)
    remote_control.on__button_was_pushed(3)
    remote_control.off__button_was_pushed(3)
