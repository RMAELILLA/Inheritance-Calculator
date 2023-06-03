class CalculatorOperator:
    def cal_add(self, first_number, second_number):
        addition = first_number + second_number
        return addition
    def cal_subtract(self, first_number, second_number):
        subtraction = first_number - second_number
        return subtraction
    def cal_multiply(self, first_number, second_number):
        multiplication = first_number * second_number
        return multiplication
    def cal_divide(self, first_number, second_number):
        try:
            division = first_number / second_number
            return division
        except ZeroDivisionError:
            print("Cannot process division, your divisor is zero")