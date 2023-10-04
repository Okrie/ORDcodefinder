from pynput import keyboard
from pynput._util import backend
from modulefunc import loadSavecode
from modulefunc import choiceRule
from pynput.keyboard import Key, Controller, KeyCode

from modulefunc import printResult

def on_press(key):
    try:
        if key == keyboard.KeyCode(char='*'):
            loadSavecode.loadFile()

        if key == keyboard.KeyCode(char='='):
            choiceRule.randomRule()

        #if key == keyboard.KeyCode(char=']'):
        #    choiceRule.load('rand')

        # if key == keyboard.KeyCode(char=']'):
        #     printResult.callCheeseKakao()
            
    except AttributeError:
        print(f'{key}')

def on_release(key):
    if key == keyboard.KeyCode(char='-'):
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
        return False
    


if __name__ == '__main__':
    import sys
    print('-'*40)
    print(' Go Code finder')
    print(' * => SaveCode Load')
    print(' = => Random Rules')
    print('-'*40, '\n')
    __main__()
    if __main__ == False:
        sys.exit()  
    