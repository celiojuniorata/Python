# \r return \n quebra e linha, padrão do windows -> CRLF
# \n -> LF
print(12, 'ola', sep=', ', end='\n##') #, end='.' -> \n quebra de linha
print(56, 78, sep="/ ") #argumento sep= 'separador'
print('04', '05', '1996', sep="/")
# Print() -> NameError: name 'Print' is not defined. Did you mean: 'print'?