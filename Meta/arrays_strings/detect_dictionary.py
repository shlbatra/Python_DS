# Dictionary of words and an alphabet string
# Time O(nk) where n num of words and k max word length 
# dictionary = ["zoo", "tick", "tack", "door"]; alphabet = "ghzstijbacdopnfklmeqrxyuvw"
# detect_dictionary(dictionary, alphabet) # -> True

def detect_dictionary(dictionary, alphabet):

    for i in range(0, len(dictionary)-1):
        word1 = dictionary[i]
        word2 = dictionary[i+1]
        res = lexical_order(word1, word2, alphabet)
        if res == False:
            return False
    return True


def lexical_order(word1, word2, alphabet):
    length = max(len(word1), len(word2))

    for i in range(0, length):
        value_1 = alphabet.index(word1[i]) if i < len(word1) else float('-inf') 
        value_2 = alphabet.index(word2[i]) if i < len(word2) else float('-inf')
        if value_1 < value_2:
            return True
        elif value_1 > value_2:
            return False
    return True

dictionary = ["zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
ans1 = detect_dictionary(dictionary, alphabet)
print(ans1)
         