'''Python implementation of the Rabin-Karp substring searching algorithm for multiple patterns

Note: all patterns must have the same length
'''

def rabin_karp_multi(text,patterns=[]):
    '''Rabin-Karp substring finding algorithm

    Inputs:
        text ~ string ~ the whole text to search
        patterns ~ list<string> ~ the patterns from which to find a match

    Runtime complexity (with preprocessing): O(km+n+k)
    Runtime complexity (w/o preprocessing): O(n+k)
    '''
    k = len(patterns[0])
    n = len(text)
    exp = 26**(k-1)
    
    hashed_patterns,h_s = preprocessing(k,exp,text,patterns) #O(km)

    #the 0-case match
    if h_s in hashed_patterns and verify_match(0,k,text,patterns): #O(m) and O(VERIFY)
        print 'Found match at position 0!'
        return 0

    for i in range(1,n-k): #O(n-m-1)
        h_s = h_s - exp*ord(text[i-1])
        h_s = h_s + exp*ord(text[i-1+k])

        if h_s in hashed_patterns and verify_match(i,k,text,patterns): #O(m) and O(VERIFY)
            print 'Found match at position {}!'.format(i)
            return i

    print 'Found no match!'
    return -1

def preprocessing(k,exp,text,patterns):
    '''Completes preprocessing to get hashed_patterns and h_s (hashed text)

    Runtime complexity: O(number_patterns*len(longest_pattern))
    '''
    hashed_patterns = set()
    h_s = 0

    #Preprocessing
    for pattern in patterns: #O(km) I think
        h_p = 0
        h_s = 0 #reset to 0 each time, so only the last iteration counts
        for i in range(k): #O(k)
            h_p += exp*ord(pattern[i])
            h_s += exp*ord(text[i])
        hashed_patterns.add(h_p)
    return hashed_patterns,h_s


def verify_match(i,k,text,patterns):
    '''Verify the text from the start position matches the pattern

    Runtime complexity: O(k+m)
    '''
    return text[i:i+k] in patterns
