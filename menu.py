import sys
import time

def loading_bar():
    for i in range(20):
        bar = "#" * i + "-" * (20 - i)
        sys.stdout.write(f"\rMarking emails... [{bar}]")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\nDone!")

def show_menu():
    print("oOo ------ Welcome to EMAIL CLEANER ------ oOo\n")
    print("\nChoose your desired option: \n")
    print("\t[1] - Read emails from the last N days\n")
    print("\t[2] - Read emails older than N days\n")
    print("\t[3] - Delete emails from a specific sender\n")
    print("\t[4] - Exit\n")

