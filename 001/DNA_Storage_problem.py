#see solution  https://www.codechef.com/practice/course/strings/STRINGS/problems/DNASTORAGE?tab=statement 

mapping={'00':'A','01':'T','10':'C','11':'G'}
T=int(input())
for _ in range(T):
    N=int(input())
    S=input()
    result=""
    for i in range(0,N,2):
        pair=S[i:i+2]
        result+=mapping[pair]
    print(result)
