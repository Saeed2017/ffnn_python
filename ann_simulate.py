import numpy
from activation_func import activation_function
def ann_simulate(self, inp, output_dimension):
    input_dimension = len(inp);
    input_length = len(inp.T);

    if input_dimension != self.numInputUnits:
        print "Number of input units and input patterns do not match";

    #setting parameters
    firstStep=0;
    lastStep=input_length;

    ACT = numpy.ones((self.numAllUnits, lastStep));
    ACT[0,:] = 1; #bias
    ACT[1:self.numInputUnits+1, firstStep:lastStep] = inp;
    ACTD = numpy.zeros((self.numAllUnits, lastStep));

    #assign parameters

    for step in range(firstStep, lastStep):
        #ffnn
        nextDest = self.weights[1]['dest'];
        Weight_Index = 1;

        while Weight_Index <= net.numWeights:
            unit_input_sums = 0;
            dest = nextDest;

            while dest == nextDest:
                unit_input_sum = unit_input_sum + self.weight[Weight_Index]['value'] * ACT[self.weight[Weight_Index]['source'] - 1, step];
                Weight_Index = Weight_Index + 1;
                nextDest = self.weights[Weight_Index]['dest'];

            if dest >= self.numAllUnits-self.numOutputUnits+1:
                #output unit, derivative = 1
                ACT[dest-1, step] = unit_input_sum;
                ACTD[dest-1, step] = 1;
            else:
                s = activation_function(unit_input_sum, 2);
                ACT[dest-1, step] = s.act;
                ACTD[dest-1, step] = s.act_d;


    output = ACT[(self.numAllUnits - self.numOutputUnits+1) : (self.numAllUnits - self.numOutputUnits + output_dimension), firstStep:lastStep];

    return output;
                
            
                
                
