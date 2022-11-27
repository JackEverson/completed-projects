import winsound, time

freq1 = 500
freq2 = 1000
duration = 100
wait = 35 

def beep():
    winsound.Beep(freq1, duration) 
    time.sleep(0.1)
    winsound.Beep(freq2, duration) 
    time.sleep(0.1)
    winsound.Beep(freq1, duration) 
    time.sleep(0.1)
    winsound.Beep(freq2, duration) 
    time.sleep(0.1)

beep()
time.sleep(3)
beep()

try:
    while True:
        time.sleep(wait)
        beep()
            

except KeyboardInterrupt:
    print("Now exiting stretch timer")
    exit() 
