import numpy as np
from util import mod_inv

def decode(cipher, key):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?!"
    S_encrypt = dict()
    S_decrypt = dict()
    for i in range(31):
        S_encrypt[chars[i]] = i
        S_decrypt[i] = chars[i]

    keyListString = key.split(' ')
    keyListInt = []
    for ele in keyListString:
        keyListInt.append(int(ele))
    keyMatrix = np.reshape(keyListInt, (3,3))
    keyMatrix = mod_inv(keyMatrix)
    
    cipherListInt = []
    for char in cipher:
        cipherListInt.append(S_encrypt[char])
    cipherMatrix = np.reshape(cipherListInt, (-1,3)).T
    plainMatrix = np.matmul(keyMatrix, cipherMatrix).T

    plain = ""
    for a in plainMatrix:
        for b in a:
            plain += S_decrypt[b % 31]
    return plain
#decode("C!QER,YNR","25 8 25 9 9 16 28 21 18")