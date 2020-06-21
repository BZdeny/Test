# 3.1


def up_number(element):
    x = 1
    while x <= element:
        if x % 3 == 0 and x % 5 == 0:
            print('FooBar')
        else:
            if x % 3 == 0:
                print('Foo')
            else:
                if x % 5 == 0:
                    print('Bar')
                else:
                    print(x)
        x += 1


print('Проверка чисел от 1 до 100: ')
up_number(100)


# 3.2


def decorator_factory(multiplication):
    def decorator(n):
        def wrapped(*args):
            if isinstance(*args, int):
                return multiplication * n(*args)
        return wrapped
    return decorator


@decorator_factory(3)
def test(num):
    return num


print('Результат умножения фабрики со знач. 3 на декорируемую функцию со знач. 9: ')
print(test(9))
print('Результат умножения фабрики со знач. 3 на декорируемую функцию со строковым знач. b: ')
print(test('b'))
