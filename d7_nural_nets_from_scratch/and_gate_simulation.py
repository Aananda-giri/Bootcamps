import math

# AND gate data
data = [[0,0,0], [0,1,0], [1,0,0], [1,1,1]]
w1 = 0.456
w2 = 0.369
b = 0.42
alpha = 0.25

def sigmoid(z):
    # formula of sigmoid
    return 1/(1+math.exp(-z))

def calc_z(x1, x2, w1, w2, b):
    return w1*x1+w2*x2+b

# prediction
print(' training: ')
print('------------------')
print(f'x1: \t x2: \t out<actual>: \t z<predict>: \t sigmoid(z): ')
print(f'epoch: \t loss: \t\t w1:  \t w2:  \t b:')
for j in range(3):
    for i in range(4):
        x1 = data[i%4][0]
        x2 = data[i%4][1]
        out = data[i%4][2]

        z = calc_z(x1, x2, w1, w2, b)
        

        # backpropagation
        w1 -= 2*alpha*(sigmoid(z)-out)*(sigmoid(z))*(1-sigmoid(z))*x1
        w2 -= 2*alpha*(sigmoid(z)-out)*(sigmoid(z))*(1-sigmoid(z))*x2
        b -= 2*alpha*(sigmoid(z)-out)*(sigmoid(z))*(1-sigmoid(z))
        print(f'{j} \t {round(sigmoid(z)-out,4)} \t {round(w1,4)} \t {round(w2,4)} \t {round(b,4)}')
    print('\n')

# prediction
print(' prediction: ')
print('------------------')
print(f'x1: \t x2: \t\t out<actual>: \t\t z<predict>: \t sigmoid(z): ')
for i in range(4):
    x1 = data[i][0]
    x2 = data[i][1]
    out = data[i][2]

    z = calc_z(x1, x2, w1, w2, b)
    print(f' {x1} \t {x2} \t\t {out} \t\t\t {round(z)} \t\t {sigmoid(z)}')