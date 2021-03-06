from scipy import signal
import math
import cmath

class Etapa:
    H = signal.TransferFunction(1,[1,0])              #la funcion transerencia
    Q = 0
    fo = 0 
    sel = 0             #un booleano que nos dice si la etapa esta seleccionada
    Gmax = 0

    def loadData(self):
        if(len(self.H.poles) == 2):
            self.Q = abs(self.H.poles[0])/(abs(2*self.H.poles[0].real))
            self.fo = abs(self.H.poles[0])/(2*math.pi)
            w,mag,pha = signal.bode(self.H)
            self.Gmax = 10**(max(mag)/20)
