from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        pass


class Subject(ABC):
    @property
    def observer(self) -> list[Observer]:
        return self._observers

    @abstractmethod
    def __init__(self):
        self._observers = None

    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class WeatherData(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self):
        for i in range(len(self._observers)):
            self._observers[i].update(self._temperature, self._humidity, self._pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self,temp, humidity, pressure):
        self._temperature = temp
        self._humidity = humidity
        self.measurements_changed()


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._temperature = 0
        self._humidity = 0
        self._weather_data = weather_data
        self._weather_data.register_observer(self)

    def update(self, temp, humidity, pressure):
        self._temperature = temp
        self._humidity = humidity
        self.display()

    def display(self):
        print(f'Current Conditions: {self._temperature} F degrees and {self._humidity}% humidity')


def main():
    weather_data = WeatherData()
    current_condition_display = CurrentConditionsDisplay(weather_data)

    weather_data.set_measurements(30, 65, 30.4)
    weather_data.set_measurements(34, 70, 29.2)
    weather_data.set_measurements(29, 90, 29.2)


if __name__ == "__main__":
    main()