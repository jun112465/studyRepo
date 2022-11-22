def find(msg, dic, s, e):
    if e > len(msg):
        return s,e-1
    elif msg[s:e] in dic:
        return find(msg, dic, s, e+1)
    else:
        dic.append(msg[s:e])
        return s,e-1
        
def solution(msg):
    dic = ['A','B','C','D','E','F','G','H','I','J','K',
           'L','M','N','O','P','Q','R','S','T','U','V',
           'W','X','Y','Z']
    
    answer = []

    s,e = 0,1
    while s < len(msg):
        s,e = find(msg, dic, s, e)
        answer.append(dic.index(msg[s:e])+1)
        s = e
        e = s+1
            
            
    return answer