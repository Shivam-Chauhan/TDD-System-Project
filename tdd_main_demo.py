from tdd_main import StringCalculator

class StringCalculatorDemo:

    """
        Demo class used to executre StringCalculator, not the test one.
        In order to exc just run demo_exc.
    """

    def demo_exc(self):
        """
            Function executing sample cases.
        """
        string_cal_obj = StringCalculator()
        print(string_cal_obj.add(""))
        print(string_cal_obj.add("1"))
        print(string_cal_obj.add("1,2"))
        print(string_cal_obj.add("//[***]\n1***2***3"))
        print(string_cal_obj.add("//[###][@@]\n1###2@@3"))
        
# starting point...
StringCalculatorDemo().demo_exc()