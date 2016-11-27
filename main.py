import sys
import random
import numpy
from ann_new import ann_new
from ann_simulate import ann_simulate
#import numpy
class mystruct:
    def __init__(self, numInputUnits, numHiddenNeurons, numOutputUnits):
        numAllUnits=1+ numInputUnits + sum(numHiddenNeurons) + numOutputUnits;
        self.numInputUnits = numInputUnits;
        self.numHiddenNeurons = numHiddenNeurons;
        self.numOutputUnits = numOutputUnits;
        self.numAllUnits=numAllUnits;
        self.numHiddenLayers=len(numHiddenNeurons);
        self.weights = [];
        self.weights.append({});

def test(s):
    print "Source = %d, Destination = %d, Value = %d\n" % (s.weights[4]['source'], s.weights[4]['dest'], s.weights[4]['value']);


if __name__ == '__main__':
    s = mystruct(4, [6, 5, 5], 2)
    ann_new(s, 4, [6, 5, 5], 2);
    #ann_simulate(s, numpy.matrix([[6, 6], [7, 7]]), 7);
    #print s.numWeights
    sys.exit(0)       
