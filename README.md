Linear-attack
=============

Linear attack

run the program:
    python LinearAtk.py
    
The program generates a 32 bits K, and 5 round keys K^1,...,K^5, each round key has 16 bits.

The program will perform linear attack on 5-8 and 13-16 bits of fifth round key K^5.

First, 10000 pairs of plaintext-ciphertext generated by K.
The program use toy Substitution-Permutation Network with S-box and permutation as follow:
S-box:
0 1 2 3 4 5 6 7 8 9 A B C D E F
E 4 D 1 2 F B 8 3 A 6 C 5 9 0 7
permutation:
1 2 3  4 5 6  7  8 9 10 11 12 13 14 15 16
1 5 9 13 2 6 10 14 3  7 11 15  4  8 12 16

Second, the program applies linear attack on 5-8 and 13-16 bits of fifth round key K^5.
Calculating the bias of xor value between bits 5 7 8 of plaintext and bits 6 8 14 16 of U^4 can extract the value of 5-8 and 13-16 bits in fifth round key K^5

============
running example:

~> python LinearAtk.py
linear attack on a toy SPN
Key = 4241520912          //generated Key 
attack on K = 9 0         //5-8 and 13-16 bits of fifth round key K^5
generate plaintext-ciphertext pair...
linear attack!!
303.0                     //max value of N(a,b)
9 0                       //extract the key
