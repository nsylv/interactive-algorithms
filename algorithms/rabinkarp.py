'''Python implementation of the Rabin-Karp substring searching algorithm

Pseudocode:
    RABIN-KARP(T,P)
        n <- |T|
        m <- |P|
        exp <- 26^(m-1)

        h_T <- hash(T_0,n)
        h_P <- hash(P)

        if h_T == h_P and VERIFYMATCH(0,m)
            then
                PRINT("Found match at position 0!")
                return 0

        for i=1 to n-m
            do
                #Roll the hash: remove the first character
                h_T <- h_T - exp*T[i-1]
                #Roll the hash: multiply by 26
                h_T <- h_T * 26
                #Roll the hash: add new character
                h_T <- h_T + T[i-1+m]   

                #Check for a match on the new hash
                if h_T == h_P and VERIFYMATCH(i,m)
                    then
                        PRINT("Found match at position ",i,"!")
                        return i

        PRINT("Found no match!")
        return -1
'''

def rabin_karp(text,pattern):
    '''Rabin-karp substring finding algorithm

    Runtime complexity (with preprocessing): O(m+n)
    Runtime complexity (w/o preprocessing): O(n)
    '''
    n = len(text)
    m = len(pattern)
    k = len(pattern)
    exp = 26**(m-1)

    #Preprocessing
    h_t,h_p = preprocessing(m,exp,text,pattern)
    
    if h_t == h_p and verify_match(0,text,pattern): #O(m)
        print 'Found match at position 0!'
        return 0

    for i in range(1,n-m): #O(n-m-1)
        h_t = h_t - exp*ord(text[i-1])    #roll the hash: remove the first character
        #h_t = h_t * 26                   #roll the hash: multiply by 26
        h_t = h_t + exp*ord(text[i-1+m])  #roll the hash: add new character

        #Check for a match on the new hash
        if h_t == h_p and verify_match(i,text,pattern): #O(m)
            print 'Found match at position {}!'.format(i)
            return i

    print 'Found no match!'
    return -1

def preprocessing(m,exp,text,pattern):
    ''' Completes preprocessing to get h_t and h_p initial values

    Runtime complexity: O(len(pattern))
    '''
    h_t = 0
    h_p = 0
    for i in range(m): # O(m)
        h_t += exp*ord(text[i])
        h_p += exp*ord(pattern[i])
    return h_t,h_p

def verify_match(start,text,pattern):
    '''Verify the text from the start position matches the pattern

    Runtime complexity: O(len(pattern))
    '''
    return text[start:start+len(pattern)] == pattern

if __name__ == '__main__':
    text = 'Hello world!'
    pattern = 'world'
    i = rabin_karp(text,pattern)
