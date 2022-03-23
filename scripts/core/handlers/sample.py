class SampleHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def hello_world():
        return "Hello World"

    @staticmethod
    def return_text(request_data):
        return f"Hi! I received the text '{request_data.text}' from you!"

    @staticmethod
    def two_number_calc(request_data):
        expr = request_data.expression
        num1 = float(request_data.num_1)
        num2 = float(request_data.num_2)
        try:
            if expr == '+':
                return {"output": num1 + num2}
            elif expr == '-':
                return {"output": num1 - num2}
            elif expr == '*':
                return {"output": num1 * num2}
            elif expr == '/':
                return {"output": num1 / num2}
            else:
                return None
        except Exception as e:
            raise Exception(f"Unknown expression {expr} given. Only expressions '+', '-', '*', '/' are supported")
