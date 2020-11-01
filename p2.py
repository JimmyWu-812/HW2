import numpy as np
from util import mod_inv

def get_key(cipher, plain):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!"
    S_encrypt = dict()
    for i in range(31):
        S_encrypt[chars[i]] = i
    
    cipherListInt = []
    for char in cipher:
        cipherListInt.append(S_encrypt[char])
    cipherMatrix = np.reshape(cipherListInt, (-1,3)).T

    plainListInt = []
    for char in plain:
        plainListInt.append(S_encrypt[char])
    plainMatrix = np.reshape(plainListInt, (-1,3)).T
    
    inv = mod_inv(plainMatrix)
    keyMatrix = np.matmul(cipherMatrix,inv)
    key = ""
    for a in keyMatrix:
        for b in a:
            key += str(round(b) % 31) + " "
    return key[:-1]
#get_key("C!QER,YNR","IS_THAT_W")