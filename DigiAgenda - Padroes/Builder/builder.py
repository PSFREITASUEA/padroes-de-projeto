class Hotel():
    def _init_(self, name, location):
        self.name = name    
        self.location = location
        
    def toString(self):
        return (f'Nome: {self.name}, Location: {self.location}')

class Reservation():
    def _init_(self, nameHotel, arrivalDate, nights):
        self.nameHotel = nameHotel
        self.arrivalDate = arrivalDate
        self.nights = nights
    
    def toString(self):
        return (f'Nome Hotel: {self.nameHotel}, Data: {self.arrivalDate}, Nights: {self.nights}')

class Vacation():
    def _init_(self):
        self.accommodations = []
        self.events = []
        self.reservas = []
        self.tickets = []  
 
    def setName(self, name):
        self.name = name

    def setAccommodations(self, accommodations):
        self.accommodations = accommodations
    
    def setReservas(self, reservas):
        self.reservas = reservas
    
    def setEvents(self, events):
        self.events = events
    
    def toString(self):
        display = ("---- " + "Seu plano de viagem" + " ----\n")
        
        for ac in self.accommodations:
            display += ac.toString() + "\n"

        for re in self.reservas:
            display += re.toString() + "\n"

        for event in self.events:
            display += (event + "\n")

        return display

class VacationBuilder():
    def _init_(self):
        self.name = ""
        self.hoteis = []
        self.reservas = []
        self.events = []
    
    def adicionaHotel(self, name, location):
        self.hoteis.append(Hotel(name, location))

    def adicionaReserva(self, nameHotel, date, nights):
        self.reservas.append(Reservation(nameHotel, date, nights))

    def adicionaEvento(self,event):
        self.events.append(event)
    
    def pegaPlanoDeFerias(self):
        vacation = Vacation()
        vacation.setName(self.name)
        vacation.setAccommodations(self.hoteis)
        vacation.setReservas(self.reservas)
        vacation.setEvents(self.events)
        return vacation

def main():
    vacation = VacationBuilder()
    vacation.adicionaHotel("Nome Hotel", "Manaus - AM")
    vacation.adicionaReserva("Nome Hotel", "10/07/2021", 3)
    vacation.adicionaEvento("Evento 1")
    vacation.adicionaEvento("Evento 2")
    
    seuPlanoDeFerias = vacation.pegaPlanoDeFerias()

    print(seuPlanoDeFerias.toString())

if _name_ == "_main_":
    main()