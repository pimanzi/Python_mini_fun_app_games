command = ""
started = False


while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("car started.....")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started=False
            print("car is stopped")
    elif command == "help":
        print('''
        start - start the car
        stop - stop the car
        quit - quit the game''')
    elif command == "quit":
        print("bye")
        break
    else:
        print("we did not recognize that word")
