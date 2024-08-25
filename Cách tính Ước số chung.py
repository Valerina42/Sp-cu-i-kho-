print('Cách tính ước số chung')
#Ước số chung của 2 số là mhững số mà 2 số đó cùng chia hết. Ví dụ: ƯSC(4,8)={1,2,4}
print('''n,m=map(int,input().split())
q=min(n,m)
for i in range (1,q+1):
    if m%i==0 and n%i==0:
        print(i,end=' ')''')
print('''Kết quả:''')
#Dòng này không có ý nghĩa để chạy câu lệnh mà chỉ in ra để người dùng thấy cách sử dụng câu lệnh.
n=int(input("nhập 1 số:"))
m=int(input("nhập 1 số:"))
#Người dùng sẽ nhập vào 2 số nguyên n và m
#2 giá trị sẽ được gán lần lượt cho biến n và m.
q=min(n,m)
#Biến q sẽ nhận giá trị nhỏ hơn giữa n và m, vì ước số chung của 2 số không thể lớn hơn số nhỏ hơn trong 2 số đó.
for i in range (1,q+1):
    if m%i==0 and n%i==0:
        print(i,end=' ')
#Dòng này lặp qua các số từ 1=>q
#Nó sẽ kiểm tra xem i có phải là ước của cả n và m hay không trong mỗi lần lặp.
#Nếu thoả mãn đủ điều kiện, in ra i.
