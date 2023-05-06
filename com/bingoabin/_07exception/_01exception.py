def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:  #或者直接使用except Exception as e  最后 print(str(e))
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(10,2)
