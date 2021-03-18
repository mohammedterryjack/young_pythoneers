from os import system 

def say(message:str, operating_system:str) -> None:
    if operating_system=="mac":
        say_mac(message) 
    if operating_system=="windows":
        say_windows(message)

def say_mac(message:str) -> None:
    system(f"say '{message}'") 

def say_windows(message:str) -> None:
    system(f'''PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{message}');"''')