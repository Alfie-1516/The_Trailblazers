def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

user_input = input("Enter an expression (e.g., 1 + 2): ")
print(f"Result: {calculate(user_input)}")