class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        delim='#'
        combined_string=''
        for i in strs:
            size=len(i)
            combined_string = combined_string+str(size)+delim+i
        return combined_string
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        delim='#'
        lst,i=[],0
        while i < len(s):
            j = i 
            while s[j]!=delim:
                j = j + 1
            length=int(str(s[i:j]))
            substring=s[j+1:j+1+length]
            lst.append(substring)
            i = j+1+int(s[i:j])
        return lst


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))