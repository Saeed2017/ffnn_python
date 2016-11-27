import math
import numpy
def TrainingData_Generation(opt):
   
    if opt == 1:
        TrainingData_input = [];
        TrainingData_output = [];
        for x in range(0, 60, 60/1000):
            TrainingData_input.append(x); 
            TrainingData_output.append(math.sin(x) * math.sin(x));
    
        TrainingData_input = numpy.zeros((1, 91));
        TrainingData_input[0, 15:25] = 1;
        TrainingData_input[0, 38:68] = 1;
        TrainingData_input[0, 73:83] = 1;

        TrainingData_output = numpy.zeros((1,91));
        TrainingData_output[0, 16:26] = 1;
        TrainingData_output[0, 39:69] = 1;
        TrainingData_output[0, 74:84] = 1;

        TrainingData_input = [TrainingData_input, TrainingData_output];
        TrainingData_output = 1 - TrainingData_output;

        TrainingData_input = [];
        TrainingData_output = [];

        for x in range(0, 120, 120/1000):
            TrainingData_input.append(x); 
            TrainingData_output.append(math.sin(x));

        input_length = len(TrainingData_input);
        TrainingData_input = numpy.ones((1, input_length));

    elif opt == 2:
        TrainingData_output = [];

        for aa in range(0, 120, 120/1000):
            TrainingData_output.append(math.sin(aa));

        TrainingData_input = numpy.ones((1, len(TrainingData_output)));

    elif opt == 3:
        bb = [];
        for aa in range(0, 120, 120/1000):
            bb = math.sin(aa);

        
    #more changes to be made
        
        
        
        
        
