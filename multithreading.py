import threading

def recursive_function(param):
    if param == 0:
        return
    print(param)
    t = threading.Thread(target=recursive_function, args=(param-1,))
    t.start()
    t.join()

recursive_function(5)
