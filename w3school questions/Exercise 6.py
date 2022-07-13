class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self,A,D,N):
        #Your code here
        k=A.index(D)
        new_list = []
        new_list = A[k+1:]+A[0:k+1]
        return new_list
D = 2
N = 7
print(rotateArr([1,2,3,4,5],D,N))
import math
def main():
    T=int(input())

    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N = nd[0]
        D = nd[1]
        A = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)

        for i in A:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()