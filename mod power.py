# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    def pow(a,b,m):
        raised=a**b
        print(raised)
        print(raised%m)
        
    pow(a,b,m)
