import threading
import time


def dance():
    t = threading.current_thread()
    for i in range(5):
        print(f'{t.name} is Dancing...')
        time.sleep(0.2)


def sing():
    t = threading.current_thread()
    for i in range(5):
        print(f'{t.name} is Singing...')
        time.sleep(0.2)


if __name__ == '__main__':
    dance_t = threading.Thread(target=dance, name='T1')
    sing_t = threading.Thread(target=sing, name='T2')
    dance_t.start()
    sing_t.start()

