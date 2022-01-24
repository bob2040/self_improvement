import multiprocessing
import time
import os


def dance():

    print(f'Dance process PID {os.getpid()},its parent\'s process PID {os.getppid()}')
    for i in range(5):
        print('Dancing...')
        time.sleep(0.2)


def sing():
    print(f'Sing process PID {os.getpid()},its parent\'s process PID {os.getppid()}')
    for i in range(5):
        print('Singing...')
        time.sleep(0.2)


if __name__ == '__main__':
    print(f'Main process PID {os.getpid()},its parent\'s process PID {os.getppid()}')

    dance_process = multiprocessing.Process(target=dance, name='P1')
    sing_process = multiprocessing.Process(target=sing, name='P2')

    dance_process.start()
    sing_process.start()
