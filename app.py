from pynput import keyboard
from modulefunc import loadSavecode
from pynput.keyboard import Key, Controller, KeyCode


def on_press(key):
    try:
        if key == keyboard.KeyCode(char='*'):
            loadSavecode.loadFile()
    except AttributeError:
        print(f'{key}')

def on_release(key):
    if key == keyboard.KeyCode(char='/'):
        print('')
        return False

def __main__():
    kbControl = Controller()
    
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listner:
        listner.join()

    listner = keyboard.Listener(
        on_press = on_press,
        on_release = on_release)
    listner.start()

    if on_release == False:
        exit()
    


if __name__ == '__main__':
    __main__()