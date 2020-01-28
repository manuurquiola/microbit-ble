import sys
import random
import signal
import time
import binascii
import numpy as np

from bluepy import btle

from pymouse import PyMouse

m = Pymouse()
xmax,ymax = m.screensize()
x=0
y=0
posx=0
posy=0
R_clck=0
L_clck=0
Sens=1
Marg=50
device_mac="XX:XX:XX:XX:XX:XX" #introducir manualmente la  MAC de la microbit


def main(num_iterations=sys.maxsize):

    p = btle.Peripheral(device_mac, btle.ADDR_TYPE_RANDOM)

    p.setSecurityLevel("medium")

    #Defino las los servicios y caracteristicas que voy a usar
    svcAcel = p.getServiceByUUID("e95d0753-251d-470a-a062-fa1922dfa9a8")
    ch = svcAcel.getCharacteristics("e95dca4b-251d-470a-a062-fa1922dfa9a8")[0]
    chper = svc.getCharacteristics("e95dfb24-251d-470a-a062-fa1922dfa9a8")[0]
   
    svcButton = p.getServiceByUUID("e95d9882-251d-470a-a062-fa1922dfa9a8")
    chA = svcButton.getCharacteristics("e95dda90-251d-470a-a062-fa1922dfa9a8")[0]
    chB = svcButton.getCharacteristics("e95dda91-251d-470a-a062-fa1922dfa9a8")[0]

    print(ch)
    CCCD_UUID = 0x2902

    ch_cccd=ch.getDescriptors(forUUID=CCCD_UUID)[0]
    print(ch_cccd)
    ch_cccd.write(b"\x00\x00", False)
    
    
    
    #polling de estados de botones, hago clic al cambiar estado de 0 a (1 o 2), actualización de posición mediante acelerómetro.
    while True:
         
        coord = np.fromstring(ch.read(), dtype=np.int16, count=3)
        if abs(coord[0])>Marg or abs(coord[1])>Marg
            x = x + 10 *Sens *coord[0]/coord[0] #el cociente da el signo de la suma, Sens permite regular sensibilidad
            y = y + 10 *Sens *coord[1]/coord[1]
            m.move(x,y)
            pass
        if (R_clck==0) and (chB.read())
            R_clck=1
            posx,posy= m.position()
            m.click(posx, posy, 2)
            pass
        if (L_clck==0) and (chA.read())
            R_clck=1
            posx,posy= m.position()
            m.click(posx, posy, 1)
            pass
        if (R_clck==1) and (chB.read()==0)
            R_clck=0
            pass
        if (L_clck==1) and (chA.read()==0)
            R_clck=0
            pass
        
        
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
