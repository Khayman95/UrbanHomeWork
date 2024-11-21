d = 0
def test_function(d):
    def inner_function (d):
        d = ('Я в области видимости функции test_function')
        print(d)
    inner_function(d)
test_function(d)