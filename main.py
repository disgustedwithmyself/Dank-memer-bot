from os import system
from time import sleep
from threading import Thread

try:
    import keyboard
except ModuleNotFoundError:
    system("pip install keyboard")
    system("cls")
try:
    import rich
except ModuleNotFoundError:
    system("pip install rich")
    system("cls")

from keyboard import send, write
from rich.console import Console

console = Console()

console.print("Start input in discord", style="bold red")
sleep(10)


def daily():
    i = 0
    while True:
        write("pls daily")
        send("enter")
        i += 1
        console.print(f"daily {i} times", style="bold green")
        sleep(86405)


def monthly():
    i = 0
    while True:
        write("pls monthly")
        send("enter")
        i += 1
        console.print(f"monthly {i} times", style="bold green")
        sleep(2592005)


def beg():
    i = 0
    while True:
        write("pls beg")
        send("enter")
        i += 1
        console.print(f"beg {i} times", style="bold green")
        sleep(50)


def deposit():
    while True:
        i = 0
        write("pls deposit all")
        send("enter")
        i += 1
        console.print(f"deposited {i} times", style="bold green")
        sleep(55)


console.print("Bot started", style="bold green")
sleep(1)
Thread(target=monthly, args=()).start()
sleep(1)
Thread(target=daily, args=()).start()
sleep(1)
Thread(target=beg, args=()).start()
sleep(1)
Thread(target=deposit, args=()).start()
sleep(1)
