#!/usr/bin/env python

# Copyright 2009 David Stainton
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.  You may obtain a copy
# of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations under
# the License.
#

__author__ = "David Stainton"
__copyright__ = "Copyright 2009 David Stainton"
__license__ = "Apache License"


import sys
import math

class perceptron(object):

    def __init__(self, length):
        self.length = length
        self.weight = []
        self.threshold = .5

        # we add an extra input for required training bias
        # it makes the math actually work
        for elk in range(0,length+1):
            self.weight.append(0)

    # add extra input for training bias
    def adjust(self, input):
        new = [1] + input
        return new

    def eval(self, input):
        input = self.adjust(input)
        return dot_product(input, self.weight)
    
    def train(self, input, expected, rate):
        # call eval before adjusting
        # because eval adjusts so it can be
        # a public method
        output = self.eval(input)
        input = self.adjust(input)
        print "adjusted input: %s" % input

        train_step = (expected - output) * rate

        for elk in range(0,len(input)):
            train_todo = input[elk] * train_step
            self.weight[elk] += train_todo

        print "weights: %s" % self.weight
        print "output: %s" % output


class boolean_perceptron(perceptron):

    def eval(self, input):
        input = self.adjust(input)

        #print "input %s, weights: %s" % (input,self.weight)
        sum = dot_product(input, self.weight)
        
        if sum == self.threshold:
            output = 0
        if sum < self.threshold:
            output = 0
        if sum > self.threshold:
            output = 1
        return output


def dot_product(a, b):
    assert len(a) == len(b)

    sum = 0
    i = 0
    while i < len(a):
        sum += a[i] * b[i]
        i += 1
    return sum

# lets use a beta of 1.0 first...
def sigmoid(beta, x):
    return 1.0/ (1.0 + math.exp(-beta*x))


def main():

    # training set :
    #  a list of expected values for each input list

    input = [[1.0,], [1.5,], [2.0,]]
    expect = [2.0, 3.0, 4.0]


    # try to expose our perceptron to the training set 100 times
    repeat = 1000

    # create a perceptron object and initialize weight values...
    # pass input/weight list length
    p = perceptron(1)
    rate = 0.1
#    rate = 0.01
#    rate = math.e ** -6

    for i in range(0,repeat):
        for elk in range(len(expect)):
            p.train(input[elk], expect[elk], rate)
            #rate = rate * .99


    print "training complete."
    print "weights: %s" % p.weight

    # and now we use the trained perceptron
    # to evaluate the sets of data..

    for i in input:
        output = p.eval(i)
        print "%s eval = %s" % (i,output)

    print "fin."



if __name__ == "__main__":
    main()
