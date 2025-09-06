class DecoratorExercise:
    def name_decorator(fun):
        def wrapper():
            print("THis is brfore decorator")
            fun();
            print("This is after decorator")
        return  wrapper

    @name_decorator
    def sayhello():
        print("Hello World")

    sayhello()

    def add_decorator(addition):
        def add_wrapper(*args, **kwargs):
            print("Addition of two numbers is")
            result = addition(*args, **kwargs)
            print("After addition")
            return result
        return add_wrapper

    @add_decorator
    def addition(a, b):
        return  a + b

    print(addition(7, 8))
