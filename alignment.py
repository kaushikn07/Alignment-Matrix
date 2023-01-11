def find_solution(OPT, m, n):
        pass
def alignment(x, y):
    n = len(y)
    m = len(x)
    
    OPT = [ [ 0 for i in range(n+1)] for j in range(m+1)]
    
    for i in range(1,m+1):
        OPT[i][0] = i
        
    for j in range(1,n+1):
        OPT[0][j] = j
        
    for line in OPT:
        print(line)
        
    for i in range(1,m+1):
        for j in range(1,n+1):
            
s1='aaaaccccggggtttt'
s2='aaaaccccggggtttt'
alignment(s1,s2)
