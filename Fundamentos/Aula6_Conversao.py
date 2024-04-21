# conversão de tipos, coerção
# type convertion, typecasting, corcion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

#print(1 + 1, 1 + '1') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print('a' + 'b') #concatenou
#print('1' + 1) #TypeError: can only concatenate str (not "int") to str
print(1.1 + 1) #concatenou
print('1' + '1') #concatenou 11
print(int('1'), type(int('1'))) #converteu
print(int('1') + 1) #2
print(type (float('1.10') + 1)) #converteu também / <class 'float'>
print(bool('1')) #true
print(bool(-1)) #true
print(bool(' ')) #true
print(bool(0)) #false
print(type(str(1))) #<class 'str'>
print(str(11) + 'b')