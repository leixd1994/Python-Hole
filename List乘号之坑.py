b=[[0]*8]*8
b[0][0]=1

#请问改变了b的几个元素
print(b)
print("---------")
#答案是8个   List 乘号引用的是同一个指针

#正确写法1
b=[[0 for i in range(8)] for j in range(8)]
b[0][0]=1
print('正确写法1: ',b)

#正确写法2
b=[[0]*8 for i in range(8)]
b[0][0]=1
print('正确写法2: ',b)



