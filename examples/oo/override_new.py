class People:
    def __new__(cls, *args, **kwargs):
        print("WOW! Call new method!")
        class_instance = super(People, cls).__new__(cls)
        return class_instance

    def __init__(self, name):
        self.name = name

    @staticmethod
    def hello():
        print("Hello")


if __name__ == "__main__":
    # dont call new
    People.hello()
    # call new
    people = People("Rafael")
