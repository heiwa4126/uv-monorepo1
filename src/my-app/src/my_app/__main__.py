from lib_a import say as say_a
from lib_b import say as say_b


def main() -> None:
    print("Hello from my-app!")
    print(say_a())
    print(say_b())


if __name__ == "__main__":
    main()
