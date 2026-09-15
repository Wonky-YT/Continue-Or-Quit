import time

pressed = input("Press C to continue and press Q to quit (followed by return): ").strip().lower()

if pressed == "q":
    print("Quitting...")

    time.sleep(4)

    print("Goodbye!")

    raise SystemExit

if pressed == "c":
    print("Continuing...")

    time.sleep(2)

    print("You continued")



else:
    print("Invalid input. Please press C to continue or Q to quit.")