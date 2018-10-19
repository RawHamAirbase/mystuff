import numpy as np
import time
import sys

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

text = '''Hello!
This is a small neural network that I engineered.
It does a simple task:
It uses inputs and an output in the form of 0s and 1s,
and learns patterns.
Once it learns the pattern, it can generate the output of an
additional input by itself!\n'''
for char in text:
    sys.stdout.write(char)
    time.sleep(0.03)

X = np.array([[0,1,1],
              [0,0,0],
              [1,1,1],
              [1,0,1],
              [1,0,0]])

y = np.array([[0],
              [1],
              [1],
              [0],
              [0]])

print('Let me show you what I mean.')
listX = X.tolist()
listy = y.tolist()
listarw = ['--->','--->','--->','--->','--->']
print('input \t\toutput')
for valX,valy,arw in zip(listX,listy,listarw):
    print(valX,arw,valy)
text2 = '''If you look closely, you see that
there is a pattern.
If all the values of the input are 1, or all are 0,
then the output is 1.
Any other combination of inputs should produce a 0.\n'''
for char in text2:
    sys.stdout.write(char)
    time.sleep(0.03)

np.random.seed(1)

syn0 = 2*np.random.random((3,5)) - 1
syn1 = 2*np.random.random((5,5)) - 1
syn2 = 2*np.random.random((5,1)) - 1

for j in range(60000):

    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))
    l3 = nonlin(np.dot(l2,syn2))

    l3_error = y - l3
    l3_delta = l3_error*nonlin(l3,deriv=True)

    l2_error = l3_delta.dot(syn2.T)
    l2_delta = l2_error*nonlin(l2,deriv=True)

    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error*nonlin(l1,deriv=True)


    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print('Now I will give you the opportunity to try it out yourself!')
print('Just type the value and hit enter.')

while True:
    try:
        ud1 = int(input('First value?:'))
        assert -1 < ud1 < 2
        ud2 = int(input('Second value?:'))
        assert -1 < ud2 < 2
        ud3 = int(input('Third value?:'))
        assert -1 < ud3 < 2
    except:
        print('Invalid input. Please type a 0 or 1')
        continue
    ud = str([ud1, ud2, ud3])
    print("Your input set is " + ud)
    usin = nonlin(np.dot(np.array([ud1, ud2, ud3]), syn0))
    usin2 = nonlin(np.dot(usin , syn1))
    usin3 = nonlin(np.dot(usin2 , syn2))
    print('Output for '+ ud + ' --->' + str(np.round_(usin3)))
    print('Would you like to try again?')
    try:
        rep = input('Type yes/no:')
        if rep == 'yes':
            continue
        elif rep == 'no':
            break
        else:
            print('Input not recognised, leaving neural network.')
            break
    except:
        print('Input not recognised, leaving neural network.')
        break
input('Press enter to finish:')
