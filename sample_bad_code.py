# Simple Python script with intentional issues for SonarCloud analysis

def divide_numbers(a, b):
    # Division by zero issue
    result = a / b
    return result


def unused_variable():
    # Unused variable issue
    x = 10
    return


def inconsistent_return():
    # Inconsistent return type issue
    if True:
        return "Success"
    else:
        return 42


def missing_docstring():
    # Missing docstring issue
    print("Hello, World!")


def main():
    # Unreachable code issue
    return "This line will never be reached."


if __name__ == "__main__":
    main()
