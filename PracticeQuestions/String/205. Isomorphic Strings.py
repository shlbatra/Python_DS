class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        final = zip(s,t)
        #print(tuple(final))
        dict_map_s_t = {}
        dict_map_t_s = {}
        for (i,j) in final:
            if j != dict_map_s_t.get(i,''):
                dict_map_s_t[i] = dict_map_s_t.get(i,'')+j
            if i != dict_map_t_s.get(j,''):
                dict_map_t_s[j] = dict_map_t_s.get(j,'')+i
            if len(dict_map_s_t[i]) > 1:
                print(False)
            if len(dict_map_t_s[j]) > 1:
                print(False)
        print(dict_map_s_t)
        print(dict_map_t_s)
        return True