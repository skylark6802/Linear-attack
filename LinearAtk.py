import random
import math

def permutation(P,v):
    w = 0
    for i in range(16):
        if not v & int(math.pow(2,15-i)) == 0:
            w = w | int(math.pow(2,16-P[i]))

    return w

def attack(x,u_2,u_4):
    z = 0
    if not x & 2048 == 0:
        z = z ^ 1
    if not x & 512 == 0:
        z = z ^ 1
    if not x & 256 == 0:
        z = z ^ 1
    if not u_2 & 4 == 0:
        z = z ^ 1
    if not u_2 & 1 == 0:
        z = z ^ 1
    if not u_4 & 4 == 0:
        z = z ^ 1
    if not u_4 & 1 == 0:
        z = z ^ 1

    return z

if __name__ == '__main__':
    print 'linear attack on a toy SPN'
   
    S = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
    P = [1,5,9,13,3,6,10,14,3,7,11,15,4,8,12,16]
    num_pair = 10000
    K = random.getrandbits(32)
    print 'Key =',K
    # round key
    Kr = []
    k = 65535
    for r in range(5):
        Kr.append((K>>(16-4*r))&k)
    print 'attack on K =',((Kr[4]>>8)&15),(Kr[4]&15)
    print 'generate plaintext-ciphertext pair...'
    plaintext = []
    ciphertext = []
    for iteration in range(num_pair):
        p = random.getrandbits(16)
        plaintext.append(p)
        w = p
        for r in range(1,4):
            u = w^Kr[r-1]
            v = 0
            for i in range(4):
                temp_u = (u>>(12-4*i))&15
                v = v | (S[temp_u]<<(12-4*i))
            w = permutation(P,v)
        u = w^Kr[3]
        v = 0
        for i in range(4):
            temp_u = (u>>(12-4*i))&15
            v = v | (S[temp_u]<<(12-4*i))
        y = v ^ Kr[4]
        ciphertext.append(y)

    print 'linear attack!!'
    Count = [0]*256
    S_inv = [14,3,4,8,1,12,10,15,7,13,9,6,11,2,0,5]
    for i in range(num_pair):
        x = plaintext[i]
        y = ciphertext[i]
        for j in range(256):
            v_2 = (j>>4) ^ ((y>>8) & 15)
            v_4 = (j&15) ^ (y&15)
            u_2 = S_inv[v_2]
            u_4 = S_inv[v_4]
            z = attack(x,u_2,u_4)
            if z == 0:
                Count[j] += 1
    max_value = -1
    maxkey = -1
    for j in range(256):
        Count[j] = math.fabs(float(Count[j]) - float(num_pair)*0.5)
        if Count[j] > max_value:
            max_value = Count[j]
            maxkey = j
    print max_value
    print (maxkey>>4),(maxkey&15)
