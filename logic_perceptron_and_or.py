'''
We can run the program as "python logic_perceptron_and_or.py x_1 x_2 operation"
Eg:
>>>> python logic_perceptron_and_or.py 0 1 AND

TABLE for reference:
        #    AND           OR
        # 0, 0 -> 0     0, 0 -> 0
        # 0, 1 -> 0     0, 1 -> 1
        # 1, 0 -> 0     1, 0 -> 1
        # 1, 1 -> 1     1, 1 -> 1
'''

import argparse

parser = argparse.ArgumentParser(
    prog = "Logic Gates AND/OR",
    description="This program will implement AND and OR gate using simple neural network",
)

# There are other activation function but we will use this basic step function for simplicity
def activation_step(x):
    return 1 if x>=0 else 0

# Find the bias value for AND and OR case which will satisfy the conditions from the reference table above
def find_bias(operation, w1, w2):
    bias = 0
    final_bias = None
    while True:
        i1, i2 = 0, 0
        Y1 = activation_step(i1*w1 + i2*w2 + bias)
        i1, i2 = 1, 1
        Y4 = activation_step(i1*w1 + i2*w2 + bias)

        if operation == "AND":
            i1, i2 = 0, 1
            Z2 = i1*w1 + i2*w2 + bias
            Y2 = activation_step(Z2)

            i1, i2 = 1, 0
            Z3 = i1*w1 + i2*w2 + bias
            Y3 = activation_step(Z3)

            if Y1 == 0 and Y2 == 0 and Y3 == 0 and Y4 == 1:
                final_bias = bias
                break
            bias-=1
        elif operation == "OR":
            i1, i2 = 0, 1
            Z2 = i1*w1 + i2*w2 + bias
            Y2 = activation_step(Z2)

            i1, i2 = 1, 0
            Z3 = i1*w1 + i2*w2 + bias
            Y3 = activation_step(Z3)

            if Y1 == 0 and Y2 == 1 and Y3 == 1 and Y4 == 1:
                final_bias = bias
                break
            bias-=1
        else:
            print("Invalid Operator")
            break
    
    return final_bias


def simple_nn_model(x_1, x_2, operation):
    # Let's set weights to 1, 1 for both AND and OR case
    w1, w2 = 1, 1
    # We do not know the value for bias so we will find out what bias we can use for AND and OR
    bias = find_bias(operation, w1, w2)
    # print(f"BIAS for {operation} is {bias}")
    # Weighted sum
    Z = x_1*w1 + x_2*w2 + bias
    # Output
    Y = activation_step(Z)
    return Y, bias


if __name__=="__main__":
    parser.add_argument('x_1', nargs="?", help="Input x_1 as 0 or 1 only")
    parser.add_argument('x_2', nargs="?", help="Input x_2 as 0 or 1 only")
    parser.add_argument('operation', nargs="?", help="Input operation as AND or OR only")
    args = parser.parse_args()

    if args.x_1 is None:
        print("Please provide the arguments while executing the program -> x_1, x_2 and operation")
        exit(-2)

    x_1 = int(args.x_1)
    x_2 = int(args.x_2)
    operation = args.operation

    if x_1 not in [0, 1]:
        print("Please provide the arguments x_1 as 0 or 1 only")
        exit(-2)

    if x_2 not in [0, 1]:
        print("Please provide the arguments x_2 as 0 or 1 only")
        exit(-2)

    if operation != "AND" and operation != "OR":
        print("Please provide the arguments operation as AND or OR only")
        exit(-2)

    ## Pass the arguments to find the output
    output, bias = simple_nn_model(x_1, x_2, operation)
    print(f"Output: {output}, Bias: {bias}")

    ###Validation
    ### AND ####
    # print("AND")
    # print(simple_nn_model(0, 0, "AND")) 
    # print(simple_nn_model(0, 1, "AND"))
    # print(simple_nn_model(1, 0, "AND"))
    # print(simple_nn_model(1, 1, "AND"))

    ## OR ####
    # print("OR")
    # print(simple_nn_model(0, 0, "OR")) 
    # print(simple_nn_model(0, 1, "OR")) 
    # print(simple_nn_model(1, 0, "OR")) 
    # print(simple_nn_model(1, 1, "OR")) 








