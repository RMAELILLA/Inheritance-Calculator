from main_calc import CalculatorOperator

class InheritanceCalc(CalculatorOperator):
    def cal_sqr_rt(self, first_number):
        sqr_rt = first_number ** (1/2)
        return sqr_rt