from cowsay import get_output_string


def say() -> str:
    return get_output_string("cow", "Hello from lib-b!")
