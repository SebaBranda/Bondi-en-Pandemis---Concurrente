import random
import threading
import time

cantLugares = 10
semaforoBondi = threading.Semaphore(cantLugares)

class Bondi():
    lugares = cantLugares

    def lugaresDisponibles(self):
        self.lugares
        return self.lugares

class Pasajero(threading.Thread):
    def init(self):
        super().__init__()
        self.name = f'Pasajero {self.nroPasajero()}'
        self.semaforoBondi = semaforoBondi

    def nroPasajero(self):
        return random.randit(1,25)

    def tiempoViaje(self):
        return random.randint(5,10)

    def run(self):
        #while (True):
            while Bondi.lugares > 0:
                semaforoBondi.acquire()
                print('Al fondo hay lugar... y baje por atras')
                Bondi.lugares -= 1
                print(f'Quedan {Bondi().lugaresDisponibles()} lugares')
                time.sleep(self.tiempoViaje())
                print(f'Me bajo aca!')
                Bondi.lugares += 1
                print(f'Quedan {Bondi().lugaresDisponibles()} lugares')
                semaforoBondi.release()

for i in range(20):
    Pasajero().start()
