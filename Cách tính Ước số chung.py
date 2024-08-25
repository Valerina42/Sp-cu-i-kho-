print('Cách tính ước số chung')
print('''n,m=map(int,input().split())
q=min(n,m)
for i in range (1,q+1):
    if m%i==0 and n%i==0:
        print(i,end=' ')''')
print('''kết quả:''')
n=int(input("nhập 1 số:"))
m=int(input("nhập 1 số:"))
q=min(n,m)
for i in range (1,q+1):
    if m%i==0 and n%i==0:
        print(i,end=' ')
