import random,wave,math,struct
from pathlib import Path
random.seed(2718)
n=22050*30
samples=[0.0]*n
# Original synthesis: filtered noise bed with irregular, decaying wood pops.
slow=0
for i in range(n):
 slow=.92*slow+.08*random.uniform(-1,1)
 samples[i]=slow*.12
for _ in range(190):
 start=random.randrange(n-7000); length=random.randrange(220,4200); amp=random.uniform(.08,.42)
 for j in range(length):
  samples[start+j]+=random.uniform(-1,1)*amp*math.exp(-j/(length*.12))
with wave.open(str(Path(__file__).resolve().parent.parent / 'media/source/crackle.wav'),'wb') as w:
 w.setparams((1,2,22050,0,'NONE','not compressed'))
 w.writeframes(b''.join(struct.pack('<h',int(max(-1,min(1,x))*32767)) for x in samples))
