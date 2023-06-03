from main_calc import CalculatorOperator
from user_d import UserDisplay
from inheritance_calc import InheritanceCalc

class Calc:
    def __init__(self):
        self.user_d = UserDisplay()
        self.inheritance_calc = CalculatorOperator()
        self.inheritance_calc = InheritanceCalc()
    def run(self):
        math_operator = self.user_d.math_operator().lower()

        if math_operator in ["addition", "subtraction", "multiplication", "division"]:
            try:
                first_number = self.user_d.user_number()
                second_number = self.user_d.user_number()

                if math_operator == "addition":
                    addition = self.inheritance_calc.cal_add(first_number, second_number)
                    self.user_d.display_addition(addition)
                elif math_operator == "subtraction":
                    subtraction = self.inheritance_calc.cal_subtract(first_number, second_number)
                    self.user_d.display_subtraction(subtraction)
                elif math_operator == "multiplication":
                    multiplication = self.inheritance_calc.cal_multiply(first_number, second_number)
                    self.user_d.display_multiplication(multiplication)
                elif math_operator == "division":
                    division = self.inheritance_calc.cal_divide(first_number, second_number)
                    self.user_d.display_division(division)
            except ValueError:
                print("Field cannot include non-integer or non-numerical values or be blank.")
            
        else:
            print("I don't understant your input, please choose one only in the four math operators.")

        self.math_operator2()

    def math_operator2(self):
        math_calculator2 = self.user_d.math_operator2()

        if math_calculator2.lower() == "y":
            self.run()
        elif math_calculator2.lower() == "n":
            print("Thank you for using this program. Have a Good day!")
        else:
            print("Please choose 'y' only if yes or 'n' only if no")

math_calculator = Calc()
math_calculator.run()