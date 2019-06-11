import timeit
import time

while True:
    print("Start")
    start = timeit.timeit()
    time.sleep(5)
    end = timeit.timeit()
    print("%.2gs" % (end - start))
