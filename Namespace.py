def test_function():
    def inner_function(*args):
        a = "Я в области видимости функции test_function"
        return a
    inner_function()
    a = inner_function()
    print(inner_function())

test_function()