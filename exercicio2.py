def perceptron_input(inputs, weights):
    bias = -1.5
    weighted_sum = []
    for i, w in zip(inputs, weights):
        weighted_sum.append(i * w)
    return sum(weighted_sum) + bias

def perceptron_output(inputs, weights):
    if(perceptron_input(inputs, weights) > 1.5):
        return 1
    else:
        return 0

if __name__ == "__main__":
    inputs = [1, 1, 2]
    weights = [1, 1, 0]
    print("Teste 1")
    print(perceptron_output(inputs, weights))

    print("Teste 2")
    inputs = [1, 2, 2]
    weights = [0, 1, 1]
    print(perceptron_output(inputs, weights))

    print("Teste 3")
    inputs = [1, 1, 1]
    weights = [1, -2, -1]
    print(perceptron_output(inputs, weights))