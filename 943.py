class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        def mix(a,b):
            l=0
            ln=len(b)
            c=a
            for i in range(len(a)+1):
                if a[:i+1] == b[ln-i-1:]:
                    l=max(l,i-1)
                    c=a[i+1:]
                    
                if l==0:l=-1
            return b+c
        def tmix(a,b):
            w1=mix(a,b)
            w2=mix(b,a)
            return w2 if len(w1)>len(w2) else w1
        A=list(set(A))
        A.sort()
        if len(A)==1:return A[0]
        res=''
        while len(A)!=1:
            m=-1
            for i,j in itertools.combinations(A, 2):
                x=len(i)+len(j)-len(tmix(i,j))
                if m<x:
                    f1,f2=i,j
                    m=x
            res=tmix(f1,f2)
            A.remove(f1)
            A.remove(f2)
            A.append(res)
        return res
