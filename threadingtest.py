from threading import Thread
from time import sleep


counter = 0
print(counter)
def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)
    counter = local_counter
    print(f'counter={counter}')


# create threads
t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()



print(f'The final counter is {counter}')

# def KelvinToFahrenheit(Temperature):
#    assert (Temperature >= 0),"Colder than absolute zero!"
#    return ((Temperature-273)*1.8)+32

# print(KelvinToFahrenheit(273))
# print int(KelvinToFahrenheit(505.78))
# print KelvinToFahrenheit(-5)