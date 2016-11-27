import math
import sys
class activation_function:
    def __init__(self, unit_input_sum, opt):
        if opt == 1:
            self.act = 1 / (1+math.exp(-unit_input_sum));
            self.act_d = self.act * (1 - self.act);

        elif opt == 2:
            self.act = (math.exp(unit_input_sum) - math.exp(-unit_input_sum)) /  (math.exp(unit_input_sum) + math.exp(-unit_input_sum));
            self.act_d = 1 - math.pow(self.act, 2);

        else:
            #sigmoid function
            self.act = 1 / (1 + math.exp(-unit_input_sum));
            self.act_d  = self.act * (1 - selc.act);



if __name__ == '__main__':
    s = activation_function(3,2);
    #s.initialize();
    sys.exit(0)   
