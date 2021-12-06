"""This is the addition calculation which is being inherits the
value A and B from calculation class"""

from calc.calculations.calculation import Calculation

#This is how you extened the addition class with caclulation
class Division(Calculation):
    """This addition class has one method to get the result of the
    calculation A and B from the calcualtion parent class"""
    def get_result(self):
        """Get Result is returning the self.value A and B"""
        div1 = enumerate(self.values)
        for i, value in (div1):
            if i != 0:
                div_num = div_num / value
            else:
                div_num = value
        return div_num