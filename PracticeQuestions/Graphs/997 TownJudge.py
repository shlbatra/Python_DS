class Solution:
    def findJudge_2array(self, n: int, trust: List[List[int]]) -> int:
        list_trusting=[0] * (n+1)
        list_trusted=[0] * (n+1)
         
        for (i,j) in trust:
            list_trusting[i] = list_trusting[i]-1
            list_trusted[j] = list_trusted[j]+1
        print(list_trusting)
        print(list_trusted)
        for i in range(1,n+1):
            if list_trusting[i] == 0 and list_trusted[i] == (n-1):
                return i
        return -1

    def findJudge_1array(self, n: int, trust: List[List[int]]) -> int:
        list_trust=[0] * (n+1)

        if len(trust) < (n-1):
            return -1
            
        for (i,j) in trust:
            list_trust[i] = list_trust[i]-1
            list_trust[j] = list_trust[j]+1
        print(list_trust)
        for i in range(1,n+1):
            if list_trust[i] == (n-1):
                return i
        return -1

    def findJudge_Sahil(self, n: int, trust: List[List[int]]) -> int:
        dict_trusting={}
        dict_trusted={}
        
        if len(trust) == 0 and n==1:
            return n
        
        for (i,j) in trust:
            dict_trusting[i] = dict_trusting.get(i,0)+1
            dict_trusted[j] = dict_trusted.get(j,0)+1
                
        for i in dict_trusted.keys():
            if dict_trusting.get(i,0) == 0 and dict_trusted[i] == (n-1):
                return i
        return -1