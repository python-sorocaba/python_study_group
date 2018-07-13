class JustPythonNumber:

    def __init__(self, value):
        self.value = value

    def __add__(self, new_value):
        return "JustPython " + str(self.value + new_value)
