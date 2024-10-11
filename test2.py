def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

example_function(a=10, b=20, c=30)
