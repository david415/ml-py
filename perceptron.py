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

class perceptron(object):

    def __init__(self, values):
        self.weight = []
        self.threshold = .5
        self.learning_rate = .1
        for value in values:
            self.weight.append(value)

    def eval(self, input):
        sum = dot_product(input, self.weight)
        if sum == self.threshold:
            output = 0
        if sum < self.threshold:
            output = 0
        if sum > self.threshold:
            output = 1
        return output


    # returns a boolean indicating whether 
    # or not the output matches the expected output

    def train(self, input, expected):
        output = self.eval(input)
        if output != expected:
            for elk in range(0,len(input)):
                if input[elk] == 1:
                    change = (expected - output) * self.learning_rate
                    print "%s %s" % (elk, change)
                    self.weight[elk] += change
            return False

        return True


def dot_product(a, b):
    sum = 0
    i = 0
    while i < len(a):
        sum += a[i] * b[i]
        i += 1
    return sum


def main():

    # training set :
    #  a list of expected values for each input list
    # in this case the training set will teach boolean or

# NAND - inverted output after training!?
#    expect = [0,1,1,1]
#    input = [[1,1], [0,0], [0,1], [1,0]]

# OR
#    expect = [1,0,1,1]
#    input = [[1,1], [0,0], [0,1], [1,0]]

# cannot implement NOR.. why not?
#    expect = [0,1,0,0]
#    input = [[1,1], [0,0], [0,1], [1,0]]

# AND
    expect = [1,0,0,0]
    input = [[1,1], [0,0], [0,1], [1,0]]


    # try to expose our perceptron to the training set 10 times
    repeat = 10

    # create a perceptron object and initialize weight values...
    p = perceptron([0,0])

    # repeatedly train with the training data set
    for c in range(0,repeat):
        results = []

        for elk in range(len(expect)):
            results.append(p.train(input[elk], expect[elk]))
            print(p.weight)
            
        # if the training doesn't return an error for the entire set
        # then stop training
        if False not in results:
            break

    print "weights: %s" % p.weight

    print "training complete."

    # and now we use the trained perceptron
    # to evaluate the sets of data..

    for i in input:
        output = p.eval(i)
        print "%s eval = %s" % (i,output)

    print "fin."



if __name__ == "__main__":
    main()
