#encoding:utf-8
#1.
# with open('foo.txt') as file:
#     #f = open('foo.txt')   .....   f.close()
#     contents = file.read()
#     print contents


#2.
# file_name = 'foo.txt'
# with open(file_name) as file:
#     for line in file:
#         print line.rstrip()  # 等价于end=''

#3.
# file_name = 'foo.txt'
# with open(file_name) as file:
#     lines = file.readlines()
#     print lines
# for line in lines:
#         print line.rstrip()  # 等价于end=''

#4.写入文件的权限
# file_name = 'foo1.txt'
# with open(file_name,'a') as file:  #w: 写权限，会覆盖掉之前文件中的内容  r: 默认读权限   a:追加权限
#     file.write("www.python.org\n")
#     file.write("www.python.org\n")
#     file.write("www.python.org\n")

#5. 文件的指针
# file_name = 'foo1.txt'
# with open(file_name,'w') as file:
#     file.write("www.python.org\n")
#     #打印当前参考位置
#     print file.tell()
#     #从参考往后移动3个， 第二个参数“0”：开头；  “1”：当前   “2”：末尾
#     file.seek(3,0)
#     #显示游标
#     print file.tell()

with open("foo.txt") as file:
    print(file.fileno())

