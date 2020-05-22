import random

import numpy as np
import matplotlib.pyplot as plt



# ------------------------------------ Simple Network ------------------------------------
 
#   O 
#  w1\
#      O
#   w2/
#   O

#  1 Layer : [2, 1] 3 neurones and 2 connections 


ITERATION = 10000
LEARNING_RATE = 0.2



def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(z):
    return sigmoid(z) * (1-sigmoid(z))

def squared_error(pred, target):
    return (target - pred) ** 2

def error_derivative(pred, target):
    return 2 * (target - pred)
        
def gen_data2():
        input_x = [[1, 1],
            [2, 1],
            [2, .5],
            [3, 1.5],
            [3.5, .5],
            [4, 1.5],
            [5.5, 1]]
        y = [0, 0, 0, 0, 1, 1, 1, 1]

        return input_x, y


class SimpleNetwork:
    def __init__(self, input_x, y, learning_rate):
        self.input_x = input_x
        self.y = y

        self.w1 = np.random.randn()
        self.w2 = np.random.randn()
        self.b = np.random.randn()

        self.learning_rate = learning_rate


    def feedforward(self, x1, x2):
        self.z = self.w1 * x1 + self.w2 * x2 + self.b
        return sigmoid(self.z)


    def get_derivatives(self, pred, target):
        # now we find the slope of the error
        # bring derivative through square function
        derror_dpred = error_derivative(pred, target)

        # bring derivative through sigmoid
        # derivative of sigmoid can be written using more sigmoids! d/dz sigmoid(z) = sigmoid(z)*(1-sigmoid(z))
        dpred_dz = sigmoid_derivative(self.z)

        return derror_dpred, dpred_dz


    def backpropagation(self, pred, target, x1, x2):
        # now we compare the model prediction with the target
        error = squared_error(pred, target)

        derror_dpred, dpred_dz = self.get_derivatives(pred, target)

        # now we can get the partial derivatives using the chain rule
        derror_dw1 = derror_dpred * dpred_dz * x1
        derror_dw2 = derror_dpred * dpred_dz * x2
        derror_db =  derror_dpred * dpred_dz

        # now we update our parameters!
        self.w1 -= self.learning_rate * derror_dw1
        self.w2 -= self.learning_rate * derror_dw2
        self.b -= self.learning_rate * derror_db


    def predict(self, x1, x2):
        z = x1*self.w1 + x2*self.w2 + self.b
        return round(sigmoid(z), 2)


    def print_prediction(self, x, y, z):
        print("data : {}, {} -> prediction : {}, reality : {}".format(x, y, self.predict(x, y), z))


    def train(self, iter, test):
        x1, x2 = test
        self.learning_curve = []

        for i in range(iter):
            x1, x2, y = self.get_random_row()

            pred = self.feedforward(x1, x2)
            self.backpropagation(pred, y, x1, x2)

            if i%20 == 0:
                output = self.predict(x1, x2)
                self.learning_curve.append(output)


    def get_random_row(self):
            idx = random.randint(0, len(self.input_x)-1)
            x1, x2 = self.input_x[idx]
            y = self.y[idx] 
            return x1, x2, y 




# ----------------------- Main -----------------------

def simple_network():
    # Init
    input_x, y = gen_data2()

    # create
    sn = SimpleNetwork(input_x, y, LEARNING_RATE)

    # train
    test = [4.5, 1]
    sn.train(ITERATION, test)

    # test
    plt.plot(sn.learning_curve)
    plt.ylabel('Learning Curve')
    plt.show()



simple_network()