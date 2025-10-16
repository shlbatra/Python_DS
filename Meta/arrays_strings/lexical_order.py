# lexical order for words based on dictionary provided

# Time - len of shorter word
# Space - O(1) - Track few vars


def lexical_order(word_1, word_2, alphabet):

    length = max(len(word_1), len(word_2))

    for i in range(length):
        val_1 = alphabet.index(word_1[i]) if i < len(word_1) else float('-inf')
        val_2 = alphabet.index(word_2[i]) if i < len(word_2) else float('-inf')
        print(val_1, val_2)
        if val_1 < val_2: # When first is earlier
            return True
        elif val_1 > val_2: # When second is earlier
            return False
    return True # When both match
        
        
alphabet = "abcdefghijklmnopqrstuvwxyz"
ans1 = lexical_order("app", "application", alphabet)
print(ans1)