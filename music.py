
import time, sys
from pygame import mixer

# pygame.init()
mixer.init()

a = mixer.Sound("A.wav")
Bb = mixer.Sound("Bb.wav")
c = mixer.Sound("C.wav")
cs1 = mixer.Sound("C1.wav")
d = mixer.Sound("D.wav")
f = mixer.Sound("F.wav")
e = mixer.Sound("E.wav")
g = mixer.Sound("G.wav")
#---------------------
c.play()
time.sleep(0.01)
c.play()
time.sleep(0.3)
d.play()
time.sleep(0.6)
c.play()
time.sleep(0.6)
f.play()
time.sleep(0.3)
e.play()
time.sleep(0.9)
#---------------------
c.play()
time.sleep(0.1)
c.play()
time.sleep(0.3)
d.play()
time.sleep(0.6)
c.play()
time.sleep(0.3)
g.play()
time.sleep(0.6)
f.play()
time.sleep(0.9)
#---------------------
c.play()
time.sleep(0.1)
c.play()
time.sleep(0.3)
cs1.play()
time.sleep(0.6)
a.play()
time.sleep(0.3)
f.play()
time.sleep(0.1)
f.play()
time.sleep(0.4)
e.play()
time.sleep(0.3)
d.play()
time.sleep(0.9)
#--------------------
Bb.play()
time.sleep(0.01)
Bb.play()
time.sleep(0.6)
a.play()
time.sleep(0.6)
f.play()
time.sleep(0.3)
g.play()
time.sleep(0.6)
f.play()
time.sleep(0.3)
