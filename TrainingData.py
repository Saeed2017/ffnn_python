import math
import numpy
import matplotlib.pyplot as pyplot

import sys
def TrainingData_Generation(opt):
   
    if opt == 1:
        train_in = numpy.arange(0, 60, 60/1000.0)   # 0:60/1000:60
        train_out = numpy.sin(train_in)
        input_length = len(train_in)
        
        train_in = numpy.ones(input_length)


    elif opt == 2:
        aa = numpy.arange(0, 120, 120/1000.0)   # 0:120/1000:120
        
        train_out = numpy.sin(aa)
        train_in = numpy.ones(len(train_out))
    elif opt == 3:
        aa = numpy.arange(0, 120, 120/1000.0)   # 0:120/1000:120
        bb = numpy.sin(aa)
        train_in  = numpy.zeros(50)
        train_out = numpy.zeros(50)
        train_in  = numpy.append(train_in, numpy.ones(200))
        train_out = numpy.append(train_out, bb[0:200])  # bb(1:200)
        train_in  = numpy.append(train_in, numpy.zeros(60))
        train_out = numpy.append(train_out, numpy.zeros(60))
        train_in  = numpy.append(train_in, numpy.ones(100))
        train_out = numpy.append(train_out, bb[0:100])  # bb(1:100)
        train_in  = numpy.append(train_in, numpy.zeros(30))
        train_out = numpy.append(train_out, numpy.zeros(30))

        train_in  = numpy.stack((train_in, numpy.append(0, train_in[:len(train_in)-1]), numpy.append([0, 0], train_in[:len(train_in)-2])))
        train_out = numpy.append(0, train_out[:len(train_out)-1])
    elif opt == 4:
        aa = numpy.concatenate((numpy.zeros(10), numpy.ones(10), numpy.zeros(10), numpy.ones(10), numpy.zeros(10), numpy.ones(10)))
        bb = numpy.concatenate((aa, aa, aa, aa, aa, aa, aa, aa, aa, aa, aa, aa))
        train_in = numpy.concatenate((numpy.zeros(90), numpy.ones(80), numpy.zeros(80), numpy.ones(60), numpy.zeros(100), numpy.ones(100), numpy.zeros(50)))
        input_length = len(train_in)
        
        train_out = numpy.multiply(train_in, bb[:input_length])  # bb(1:input_length)
        train_in = numpy.stack((train_in, numpy.append(0, train_in[:len(train_in)-1]), numpy.append([0, 0], train_in[:len(train_in)-2])))
    elif opt == 5:
        aa = numpy.arange(0, 50+0.1, 0.1)   #0:0.1:50
        bb = numpy.sin(aa)
        cc = [0] + bb
        dd = numpy.subtract(numpy.power(bb, 2), numpy.multiply(cc, 2))
                               
        train_out = numpy.zeros(len(dd))
        train_out[0] = dd[0]
                               
        for n in range(1, len(dd)):
            train_out[n] = dd[n] - train_out[n-1]
        train_in = numpy.stack((bb, cc))
    elif opt == 6:
        aa = numpy.multiply(numpy.random.random(1000), 2)
        bb = numpy.multiply(numpy.random.random(1000), 2)
        cc = numpy.multiply(aa, bb)
        dd = numpy.random.random(1000)
        
        train_out = numpy.multiply(numpy.subtract(cc, numpy.power(numpy.subtract(aa, bb), 2)), dd)
        train_in = numpy.stack((aa, bb, cc, dd))
    elif opt == 7:
        aa = numpy.arange(0, 1.5001, 0.001)  # 0:0.001:1.5
        bb = numpy.arange(0, 1.5001, 0.001)  # 0:0.001:1.5
        cc = numpy.multiply(aa, bb)
        
        train_out = numpy.subtract(cc, numpy.power(numpy.subtract(aa, bb), 2))
        train_in = numpy.stack((aa, bb, cc))
    elif opt == 8:
        aa = numpy.arange(0, 60, 0.1) # 0:0.1:60
        bb = numpy.sin(aa)
        lg = len(aa)
        bb_d = numpy.zeros(lg)
        for n in numpy.arange(1, lg):
            bb_d[n] = bb[n] - bb[n-1]
            
        train_in = numpy.stack((bb[2:len(bb)-1], bb_d[2:len(bb_d)-1]))
        train_out = bb_d[3:]
    else:           # Default sin() waveform
        aa = numpy.arange(0, 120+120/1000.0, 120/1000.0)
        
        train_out = numpy.sin(aa)
        train_in = numpy.ones(len(train_out))

    # Graph the Training Data Inputs and Outputs
    pyplot.figure()
    pyplot.title("Training Data Output")
    pyplot.plot(train_out)
    pyplot.show()
    
    return [train_in, train_out]


if __name__ == '__main__':
    for i in range(1, 10):
        TrainingData_Generation(i)
    sys.exit

        
    #more changes to be made
        
        
        
        
        
