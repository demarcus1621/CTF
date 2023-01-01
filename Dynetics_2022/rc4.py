#!/usr/bin/env python

class RC4():
    def __init__(self, key):
        self.key = [ord(c) for c in key]
        self.S = None
        self.keystream = None

        self.i = 0
        self.j = 0

        self.KSA()
        
        # Get rid of weak IVs
        for i in range(1028):
            self.PRGA()

    def KSA(self):
        j = 0
        S = [i for i in range(256)]
        N = len(self.key)
    
        for i in range(256):
            j = (j + S[i] + self.key[i % N]) % 256
            S[i], S[j] = S[j], S[i]
    
        self.S = S
    
    def PRGA(self):
        self.i = (self.i + 1) % 256
        self.j = (self.j + self.S[self.i]) % 256
        self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
    
        K = self.S[(self.S[self.i] + self.S[self.j]) % 256]
        return K
    
    def encrypt(self, plaintext):
        ciphertext = []
        for c in plaintext:
            ciphertext.append(self.PRGA() ^ ord(c))
        
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = []
        for c in ciphertext:
            plaintext.append(chr(self.PRGA() ^ c))

        return ''.join(plaintext)

