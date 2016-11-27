import random
def ann_new(self, numInputUnits, numHiddenNeurons, numOutputUnits):
        numAllUnits=1+ numInputUnits + sum(numHiddenNeurons) + numOutputUnits;
        weight = {'dest':0,'source':0,'value':0,'type':1};
        #self.weights.append({'dest':0,'source':0,'value':4,'type':3});
        bias = 0;
        index = 1;

        #connect the bias to all nodes
        for d in range(numInputUnits + 1, numInputUnits+sum(numHiddenNeurons)+1):
            self.weights.append({'dest':d, 'source':bias, 'value':1, 'type':1});
            print "Source = %d, Destination = %d, Value = %d\n" % (self.weights[index]['source'], self.weights[index]['dest'], self.weights[index]['value']);
            index = index + 1;

        #set weights from input layer to first hidden layer
        
        for d in range(numInputUnits+1, numInputUnits+1+numHiddenNeurons[0]):
            for s in range(1, numInputUnits + 1):
                #self.weights[index].append(weight);
                #self.weights[index]['dest'] = d;
                #self.weights[index]['source'] = s;
                self.weights.append({'dest':d, 'source':s, 'value':0, 'type':1});
                print "Source = %d, Destination = %d, Value = %d\n" % (self.weights[index]['source'], self.weights[index]['dest'], self.weights[index]['value']);
                index = index + 1;

       #set weights from one hidden layer to the next

        if self.numHiddenLayers > 1:
            for layer in range(1, self.numHiddenLayers):
                for d in range(numInputUnits+1+sum(numHiddenNeurons[0:layer]), numInputUnits+1+sum(numHiddenNeurons[0:layer+1])):
                    for s in range(numInputUnits+1+sum(numHiddenNeurons[0:layer])-numHiddenNeurons[layer-1], numInputUnits+1+sum(numHiddenNeurons[0:layer])):
                        self.weights.append({'dest':d, 'source':s, 'value':0, 'type':1});
                        print "Source = %d, Destination = %d, Value = %d\n" % (self.weights[index]['source'], self.weights[index]['dest'], self.weights[index]['value']);
                        index = index + 1;


        #set weights from hidden layer to output layer

        for d in range(numAllUnits - numOutputUnits, numAllUnits):
            for s in range(numAllUnits-numOutputUnits-numHiddenNeurons[self.numHiddenLayers-1], numAllUnits-numOutputUnits):
                self.weights.append({'dest':d, 'source':s, 'value':0, 'type':1});
                print "Source = %d, Destination = %d, Value = %d\n" % (self.weights[index]['source'], self.weights[index]['dest'], self.weights[index]['value']);
                index = index + 1;

        self.numWeights = index - 1;
        init_weights = 1;
        if init_weights == 1:
            range_magnitude = 0.5;
            for index in range(1, self.numWeights):
                self.weights[index]['value'] = random.random() * 2 * range_magnitude - range_magnitude;
