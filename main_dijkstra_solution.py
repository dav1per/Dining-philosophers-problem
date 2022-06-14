from threading import Thread, Lock
import time


number_of_philosophers = 5
chopsticks = [Lock() for _ in range(number_of_philosophers)]

def philosopher_eat(i):
    if i == number_of_philosophers:
        while chopsticks[0].locked():
            pass
        chopsticks[0].acquire()

        while chopsticks[i -1].locked():
            pass
        chopsticks[i - 1].acquire()
        time.sleep(4)
        chopsticks[i - 1].release()
        time.sleep(1)
        chopsticks[0].release()
    else:
        while chopsticks[i].locked():
            pass
        chopsticks[i].acquire()

        while chopsticks[i - 1].locked():
            pass
        chopsticks[i - 1].acquire()
        time.sleep(4)
        chopsticks[i].release()
        time.sleep(1)
        chopsticks[i - 1].release()





threads = []
for i in range(5):
    threads.append(Thread(target=philosopher_eat, args=(i + 1,)))


for thread in threads:
    thread.start()




    

