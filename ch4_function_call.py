"""Function-call stack demonstration script."""

def main():
    result = square(7)  # square's stack frame pushed onto stack here
    print('square(7):', result)
    # main's stack frame is popped here

def square(number):
    return number ** 2  # square's stack frame is popped here

main()  # execution begins here
