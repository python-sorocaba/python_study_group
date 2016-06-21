def func(age=None, name=None, *args, **kwargs):
    print("My args: {}".format(args))
    print(type(args))
    print("My kwargs: {}".format(kwargs))
    print(type(kwargs))
    print("Age: {}".format(age))
    print("Name: {}".format(name))

func(name="Rafael")
func(1, 2, 3, teste="banana")
func(fruit="apple", name="Rafael")
func(name="Rafael")
func(name="Rafael", age=28)

people = {"name": "Rafael", "age": 28, "fruit": "apple"}
func(**people)   # func(name="Rafael", age=28)
