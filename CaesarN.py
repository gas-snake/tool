
#a = 'e6ece1e7fbb8b4b5e2e6b9e5b7e3e6e4e4b8b5e5b8b7e3b3b5b8b6b7b3b5e1e1e4e5e6e4b1fdfd'
#a = '89ff304c2d12a856d71ef5175e81cea831b4ecab8add5ee6a68da2a7f1'
#a = '79737175206f6c206c713175786670783372786f35696f6c346f757866'
a = '777d70766a75262326222672772072742728297224297027702724702970202875737325296c'
a_bytes = bytes.fromhex(a)
print('字符串转字节码',a_bytes)
A_Ord = ''
print ("1"+"1")
for i in a_bytes:
    #print (i)

    A_Ord=A_Ord + " " +str(i)

print('字节码转十进制',A_Ord)
A_Ord = ''
b = ''
for i in a_bytes:

    A_Ord=A_Ord + " " +str(i-17)
    #print(i-164)
    #print(chr(i-128))
    b = b + chr(i-17)

print('字节码转十进制 再减128 ',A_Ord)
print('字节码转十进制 再减128再转字符 ',b)

#print(chr(66))

