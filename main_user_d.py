class UserDisplay:
    def math_operator(self):
        user_operator = input("Please choose what math operation you need: 'Addition', 'Subtraction', 'Multiplication', 'Division', 'Square Root', or 'Power': ")
        return user_operator
    def user_number(self):
        first_number = float(input("Please enter number: "))
        return first_number
    def display_addition(self, addition):
        print("The sum is: " + str(addition))
    def display_subtraction(self, subtraction):
        print("The difference is: ", subtraction)
    def display_multiplication(self, multiplication):
        print("The product is: ", multiplication)
    def display_division(self, division):
        print("The quotient is: ", division)
    def math_operator2(self):
        math_operator2 = input("Do you want to calculate again? y/n: ")
        return math_operator2