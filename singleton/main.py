#!/usr/bin/env python3
from settings import get_settings
from alternate_greeting import say_hi


def say_hello(name):
    return f'Hello, {name}'
    
def main():
    app_settings = get_settings()
    name = app_settings.name
    print(say_hello(name))
    print(say_hi(name))


if __name__ == '__main__':
    main()
