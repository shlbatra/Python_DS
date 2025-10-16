# Most frequent chars in string
# If same then return first

def most_freq_char(s):
    ch_dict = {}
    

    for ch in s:
        ch_dict[ch] = ch_dict.get(ch,0) + 1
    # print(ch_dict)

    most_freq = None

    for ch in s:
        if most_freq is None or ch_dict[ch] > ch_dict[most_freq]:
            most_freq = ch

    return most_freq

ans1 = most_freq_char("potato")
print(ans1)

ans1 = most_freq_char("saaahilll")
print(ans1)