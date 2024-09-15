def perceptron_input(inputs, weights):
    weighted_sum = []
    for i, w in zip(inputs, weights):
        weighted_sum.append(i * w)
    return sum(weighted_sum)

def perceptron_output(inputs, weights):
    if(perceptron_input(inputs, weights) >= 1.5):
        return 1
    else:
        return 0

if __name__ == "__main__":
    inputs = [1, 1, 2]
    weights = [1, 1, 0]

    
    print(perceptron_output(inputs, weights))