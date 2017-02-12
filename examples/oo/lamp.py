import time


class Lamp:
    def __init__(self, color):
        if color == "green":
            color = "\033[92m"
        elif color == "red":
            color = "\033[91m"

        self.color = color

    def on(self):
        print("{}ON".format(self.color))


if __name__ == "__main__":
    red_lamp = Lamp(color="red")
    green_lamp = Lamp(color="green")

    try:
        while True:
            red_lamp.on()
            time.sleep(1)
            green_lamp.on()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\033[0m")
