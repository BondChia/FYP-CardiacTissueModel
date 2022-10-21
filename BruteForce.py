import time
import itertools

super_string = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def brute_force(super_string,MAX_PASSWORD_LENGTH,message):           
    start = time.time() 
    for guess_length in range(1,MAX_PASSWORD_LENGTH+1) :
        guesses = []
        guesses = [''.join(i) for i in itertools.permutations(super_string, guess_length)]
        for guess_ind in range(len(guesses)):
            if guesses[guess_ind] == message:
                print('We have found the key !!')
                end = time.time()
                print('Total time: %.2f seconds' % (end - start))
                return guesses[guess_ind]

guess = brute_force(super_string,12,'WE<3IOThehe')
