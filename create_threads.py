import threading

#creates threads
def create_threads(ips, function):
    threads = []

    for ip in ips:
        th = threading.Thread(target=function, args=(ip,))
        th.start()
        threads.append(th)
    
    for th in threads:
        th.join()