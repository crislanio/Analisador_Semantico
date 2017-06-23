
# coding: utf-8

# In[124]:


from copy import copy
from copy import deepcopy
import fileinput
from collections import deque as Pilha
from itertools import chain # pra transformar lista de lista em lista

# Função que retorna uma lista com cada palavra do código
def splitCod(str):
    l = []
#     print(str.split())
    l.append(str.split())
    return l[0] # pra ser somente uma lista
# lc = splitCod(teste6)

topoPilhaSplit = Pilha ()
def arquivo(str):
    p = Pilha()
    topoPilha = 0
    arq = open(str, 'r')
    texto = arq.readlines()
    for linha in texto :
        p.append(linha)
        topoPilhaSplit.append(splitCod(linha))
    arq.close()
# print(arquivo('saida.txt'))

listaArquivoLinha = []
def arquivoPraLinha(str):
    p = Pilha()
    arq = open(str, 'r')
    texto = arq.readlines()
    for linha in texto :
        p.append(linha)
        listaArquivoLinha.append(splitCod(linha))

    novaListaArquivoLinha = list(chain(*listaArquivoLinha)) # olhar em :  https://pt.stackoverflow.com/questions/131258/converter-uma-lista-de-listas-em-uma-s%C3%B3-lista
    arq.close()
    return novaListaArquivoLinha
# print(arquivoPraLinha('saida.txt'))    


# In[125]:

lc = arquivoPraLinha('saida.txt')

def verifica_func_escopo(str):
    variaveis = []
    funcoes = []
    topoPilha = 0
    varCode = lc
    escopo = Pilha ()
    escopos = [escopo]         
#     print("Função")
#     print(lc)
    i = 0
    while i< len(lc):
        if (varCode[i] == "string") or varCode[i] == "int" and varCode[i+2] == "(": # ex: int X (
            if not (varCode[i] == "string") or varCode[i] == "int" and varCode[i+2] == "(":
                if (varCode[i]=="string" or varCode[i]=="int" and varCode[i+2]=="("):
                    if not (varCode[i+1], 'int') in escopos[topoPilha] or not (varCode[i+1], 'string') in escopos[topoPilha]:                    
                        escopos[topoPilha].append( (varCode[i+1], varCode[i]) ) # formato x, int
                        variaveis.append(varCode[i+1])
#                         print(variaveis)
#                         print(escopos)
                    else:
                        variaveis.append(varCode[i+1])
#                         print("- ",variaveis)
#                         print("Variável já declarada no escopo")
                        return True
#             return False
        i += 1


    
def duplicadoVarEscopo(p):
    _aux = []

    # removendo duplicados
    for x in p:
        if x not in _aux:
            _aux.append(x)
    # comparando os tamanhos
    if len(p) != len(_aux):
        return True # tem duplicados
    else:
        return False

p = Pilha()    
def verifica_var_escopo(str):
    listaVarDentroFunc = []    
    i = 0
    while i< len(topoPilhaSplit):
        k = 0
        while k < len(topoPilhaSplit[i]):
            if topoPilhaSplit[i][k] != '{':
                if topoPilhaSplit[i][k] == 'int' or topoPilhaSplit[i][k] == 'string':
                    p.append((topoPilhaSplit[i][k], topoPilhaSplit[i][k+1]))
                    listaVarDentroFunc.append((topoPilhaSplit[i][k], topoPilhaSplit[i][k+1]))
                if topoPilhaSplit[i][k] == '}':
                    p.pop()            
            k = k+1
        i = i+1
#     print(listaArquivoLinha)
#     print(p)
    
# print("verifica_var_escopo(lc) ",verifica_var_escopo(lc))
# print("duplicadoVarEscopo(p) ",duplicadoVarEscopo(p))

# Verificando casos int func (int x , string x) # parâmetros com tipos diferentes mas com o mesmo nome 
# Esse tipo de erro só pode acontecer em funções com 2 parâmetros
def verifica_param_func(str):
    var_func_Arquivo = []
    param_func = []
    topoPilha = 0
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if topoPilhaSplit[i][j] == '(':                    
                if (topoPilhaSplit[i][j+1] == 'int' or topoPilhaSplit[i][j+1] == 'string') and (topoPilhaSplit[i][j+4] == 'int' or topoPilhaSplit[i][j+4] == 'string'):
                    if (topoPilhaSplit[i][j+1] == topoPilhaSplit[i][j+4]) and (topoPilhaSplit[i][j+2] == topoPilhaSplit[i][j+5]) :
#                         print((topoPilhaSplit[i][j+1]," e ", topoPilhaSplit[i][j+4]) ," e ", (topoPilhaSplit[i][j+2], " == ", topoPilhaSplit[i][j+5]))
                        return False
                    elif (topoPilhaSplit[i][j+1] != topoPilhaSplit[i][j+4]) and (topoPilhaSplit[i][j+2] == topoPilhaSplit[i][j+5]) :
#                         print((topoPilhaSplit[i][j+1]," != ", topoPilhaSplit[i][j+4]) ," e ", (topoPilhaSplit[i][j+2]," == ", topoPilhaSplit[i][j+5]))
                        return False
                    else:
                        var_func_Arquivo.append (((topoPilhaSplit[i][j+1], topoPilhaSplit[i][j+2]), (topoPilhaSplit[i][j+4], topoPilhaSplit[i][j+5])))                    
                        param_func.append(((topoPilhaSplit[i][j+1], topoPilhaSplit[i][j+2]), (topoPilhaSplit[i][j+4], topoPilhaSplit[i][j+5])))  

#     print(param_func)   # parâmetros das funções
       
# print("verifica_param_func(lc) ",verifica_param_func(lc))
# print("duplicadoVarEscopo(p) ",duplicadoVarEscopo(p))


# In[126]:

##                               FUNÇÕES PARA VERIFICAÇÃO DE TIPOS
## NOTA: O PARA VERIFICAR O IF..ELSE... BASTA VERIFICAR AS OPERAÇÕES. CASO FALSAS. ERRO. 

# função que verifica se uma operação entre que envolve inteiros é válida
# int + int * int ... senao false
def operacaoInt():
    variaveisArquivo = []
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string'):
                variaveisArquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j]) )
                reversoListaVar=variaveisArquivo[::-1] # pegando as variáveis que primeiro aparecem do final para o início do arquivo

    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):                
            if (topoPilhaSplit[i][j] == '+' or topoPilhaSplit[i][j] == '-' or topoPilhaSplit[i][j] == '*' or topoPilhaSplit[i][j] == '/' or topoPilhaSplit[i][j] == '>=' or topoPilhaSplit[i][j] == '<=' or topoPilhaSplit[i][j] == '>' or topoPilhaSplit[i][j] == '<' or topoPilhaSplit[i][j] == '=='):
                if ((topoPilhaSplit[i][j-1], 'int') in reversoListaVar and (topoPilhaSplit[i][j+1], 'string') in reversoListaVar) or ((topoPilhaSplit[i][j-1], 'string') in reversoListaVar and (topoPilhaSplit[i][j+1], 'int') in reversoListaVar):                    
                    print(topoPilhaSplit[i][j-1]," Err entre Int-String",topoPilhaSplit[i][j+1])
                    return False
                else:                                                                                                                 
                    continue                                                                                                                      
#     print(reversoListaVar)
#     return True

# print("operacaoInt()  ",operacaoInt())

# função que verifica se uma operação entre que envolve inteiros é válida
#int a = int + int - int ... senao false
def operacaoInt2():
    variaveisArquivo = []
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string'):
                variaveisArquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j]) )
                reversoListaVar=variaveisArquivo[::-1] # pegando as variáveis que primeiro aparecem do final para o início do arquivo

    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):                
            if (topoPilhaSplit[i][j] == '+' or topoPilhaSplit[i][j] == '-' or topoPilhaSplit[i][j] == '*' or topoPilhaSplit[i][j] == '/' or topoPilhaSplit[i][j] == '>=' or topoPilhaSplit[i][j] == '<=' or topoPilhaSplit[i][j] == '>' or topoPilhaSplit[i][j] == '<' or topoPilhaSplit[i][j] == '=='):
                if ((topoPilhaSplit[i][j-1], 'int') in reversoListaVar and (topoPilhaSplit[i][j-3], 'string') in reversoListaVar) or ((topoPilhaSplit[i][j-2], 'int') in reversoListaVar and (topoPilhaSplit[i][j-3], 'string') in reversoListaVar):
#                     print(topoPilhaSplit[i][j-3]," EO-1 ",topoPilhaSplit[i][j-1], topoPilhaSplit[i][j+1])
                    return False                
                else:
                    continue                
    print(reversoListaVar)
#     return True

# print("operacaoInt2() ",operacaoInt2())

# função que verifica se existe uma operação entre string e int
# string a =  int
def caseStringIgualInt():
    variaveisArquivo = []
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string'):
                variaveisArquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j]) )
                reversoListaVar=variaveisArquivo[::-1] # pegando as variáveis que primeiro aparecem do final para o início do arquivo

    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):                

            if topoPilhaSplit[i][j] == '=':
                if topoPilhaSplit[i][j-2] == 'int':
                        continue

                # caso string recebe int: string a = 3
                elif (topoPilhaSplit[i][j+1][0] == '\"' and (topoPilhaSplit[i][j-1], 'string') in reversoListaVar) or (topoPilhaSplit[i][j+1][0] == '\'' and ((topoPilhaSplit[i][j-1], 'string') in reversoListaVar)):
#                     print(topoPilhaSplit[i][j-1]," 22 ",topoPilhaSplit[i][j+1])
                    continue 
                else:
#                     print("ERRO ",topoPilhaSplit[i][j-1]," E22 ",topoPilhaSplit[i][j+1]) 
                    return False
#     print(reversoListaVar)
#     return True

# print("caseStringIgualInt() ",caseStringIgualInt())

# Função que verifica se um inteiro recebe uma string 
# int a  =  string
def caseIntIgualString():
    variaveisArquivo = []
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string'):
                variaveisArquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j]) )
                reversoListaVar=variaveisArquivo[::-1] # pegando as variáveis que primeiro aparecem do final para o início do arquivo

    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):                

            if topoPilhaSplit[i][j] == '=':
                if topoPilhaSplit[i][j-2] == 'string':
                    continue
                # caso int recebe string: int a = "3"
                elif (topoPilhaSplit[i][j+1][0] == '\"' and ((topoPilhaSplit[i][j-1], 'int') in reversoListaVar)) or (topoPilhaSplit[i][j+1][0] == '\'' and ((topoPilhaSplit[i][j-1], 'int') in reversoListaVar)):                    
#                     print("ERRO ",topoPilhaSplit[i][j-1]," E11 ",topoPilhaSplit[i][j+1], topoPilhaSplit[i][j+1][0]) 
                    return False
                else:
#                     print(topoPilhaSplit[i][j-1]," 11 ",topoPilhaSplit[i][j+1], topoPilhaSplit[i][j+1][0]  )
                    continue 
#     print(reversoListaVar)
#     return True

# print("caseIntIgualString() ",caseIntIgualString())

# função que trata as operações entre string's. ==, !=
# string +-*/ string é pra dá erro
def operacaoString():
    variaveisArquivo = []
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string'):
                variaveisArquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j]) )
                reversoListaVar=variaveisArquivo[::-1] # pegando as variáveis que primeiro aparecem do final para o início do arquivo

    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):                
            if (topoPilhaSplit[i][j] == '+' or topoPilhaSplit[i][j] == '-' or topoPilhaSplit[i][j] == '*' or topoPilhaSplit[i][j] == '/' or topoPilhaSplit[i][j] == '+=' or topoPilhaSplit[i][j] == '++'):
                if ((topoPilhaSplit[i][j-1], 'string') in reversoListaVar and (topoPilhaSplit[i][j+1], 'string') in reversoListaVar) or ((topoPilhaSplit[i][j-1], 'string') in reversoListaVar and (topoPilhaSplit[i][j+1], 'int') in reversoListaVar):                    
#                     print(topoPilhaSplit[i][j-1]," EStrO-O ",topoPilhaSplit[i][j+1])
                    return False
                else:                                                                                                                 
                    continue                                                                                                                      
#     print(reversoListaVar)
#     return True
# print("operacaoString() ",operacaoString())


# Função que verifica quando tenho um inteiro entre operações de string's dá erro
# caso string ++ e == e !=
def string_add():
#     print("pilha ", topoPilhaSplit) # verificando se a pilha vem caregada
    variaveisArquivo = []
    for i in range(len(topoPilhaSplit)):
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string'):
                variaveisArquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j]) )
                reversoListaVar=variaveisArquivo[::-1] # pegando as variáveis que primeiro aparecem do final para o início do arquivo

    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):                
            if (topoPilhaSplit[i][j] == '==' or topoPilhaSplit[i][j] == '!='):
                if topoPilhaSplit[i][j-4] == 'int':
                    return False
                elif ((topoPilhaSplit[i][j-1], 'int') in reversoListaVar or (topoPilhaSplit[i][j+1], 'int') in reversoListaVar) or (not topoPilhaSplit[i][j-1][0] == '\"' and topoPilhaSplit[i][j-1][0].isdigit()) or (not topoPilhaSplit[i][j-1][0] == '\'' and topoPilhaSplit[i][j-1][0].isdigit()) or (not topoPilhaSplit[i][j+1][0] == '\"' and topoPilhaSplit[i][j+1][0].isdigit()) or (not topoPilhaSplit[i][j+1][0] == '\'' and topoPilhaSplit[i][j+1][0].isdigit()): 

#                     print(topoPilhaSplit[i][j-1]," ERRO ++ ",topoPilhaSplit[i][j+1])
                    return False
                else:           
#                     print(topoPilhaSplit[i][j-1]," ++ ",topoPilhaSplit[i][j+1])
                    continue                                                                                                                      
    
# print("string_add() ",string_add())

# função que verifica quando uma atribuição é string. 
# " e ", " e ', ' e ', " e '
def operacaoStringNaoVar():
    variaveisArquivo = []
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string'):
                variaveisArquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j]) )

    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):                
            if (topoPilhaSplit[i][j] == '==' or topoPilhaSplit[i][j] == '>' or topoPilhaSplit[i][j] == '<' or topoPilhaSplit[i][j] == '<=' or topoPilhaSplit[i][j] == '>=' or topoPilhaSplit[i][j] == '+' or topoPilhaSplit[i][j] == '-' or topoPilhaSplit[i][j] == '*' or topoPilhaSplit[i][j] == '/'):
                # " e ", " e ', ' e ', " e '
                if ((topoPilhaSplit[i][j-1][0] == '\"') and (topoPilhaSplit[i][j+1][0] == '\"')) or ((topoPilhaSplit[i][j-1][0] == '\'') and (topoPilhaSplit[i][j+1][0] == '\'')) or ((topoPilhaSplit[i][j-1][0] == '\'') and (topoPilhaSplit[i][j+1][0] == '\"')) or ((topoPilhaSplit[i][j-1][0] == '\"') and (topoPilhaSplit[i][j+1][0] == '\'')):                    
#                     print(topoPilhaSplit[i][j-1]," EO-O ",topoPilhaSplit[i][j+1])
                    return False
                else:                                                                                                                 
                    continue                                                                                                                      
#     return True

# print("operacaoStringNaoVar() ",operacaoStringNaoVar())

# Função que pega um inteiro. ex: "3" não é inteiro.
# operação int com int
def operacaoIntNaoVar():
    variaveisArquivo = []
    reversoListaVar = []
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string'):
                variaveisArquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j]) )
                reversoListaVar=variaveisArquivo[::-1] # pegando as variáveis que primeiro aparecem do final para o início do arquivo
# para pegar número ou um valor que não é variável nem número basta verificar se está na lista de variáveis
# e se a posição inicial tem aspas(com isso caracterizo um valor que não é string nem número)
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):                
            if (topoPilhaSplit[i][j] == '==' or topoPilhaSplit[i][j] == '<=' or topoPilhaSplit[i][j] == '>=' or topoPilhaSplit[i][j] == '+' or topoPilhaSplit[i][j] == '-' or topoPilhaSplit[i][j] == '*' or topoPilhaSplit[i][j] == '/' or topoPilhaSplit[i][j] == '>=' or topoPilhaSplit[i][j] == '<=' or topoPilhaSplit[i][j] == '>' or topoPilhaSplit[i][j] == '<'): # or topoPilhaSplit[i][j] == '==' or topoPilhaSplit[i][j] == '++'):
#int d; ou d = string
#"3" + 5 ; ou '3' + 5 ; ou "d" + 5 ; ou 'd' + 5 ; ou como 2° parâmetro

                if  (topoPilhaSplit[i][j-1][0] == '\"' and (topoPilhaSplit[i][j-1][1].isdigit()) and not (topoPilhaSplit[i][j-1][1],'int') in reversoListaVar) or      (topoPilhaSplit[i][j+1][0] == '\"' and (topoPilhaSplit[i][j+1][1].isdigit()) and not (topoPilhaSplit[i][j+1][1],'int') in reversoListaVar) or     (topoPilhaSplit[i][j-1][0] == '\'' and (topoPilhaSplit[i][j-1][1].isdigit()) and not (topoPilhaSplit[i][j-1][1],'int') in reversoListaVar) or      (topoPilhaSplit[i][j+1][0] == '\'' and (topoPilhaSplit[i][j+1][1].isdigit()) and not (topoPilhaSplit[i][j+1][1],'int') in reversoListaVar)  or                   (topoPilhaSplit[i][j-1][0] == '\"' and (not topoPilhaSplit[i][j-1][1].isdigit()) and not (topoPilhaSplit[i][j-1][1],'int') in reversoListaVar) or      (topoPilhaSplit[i][j+1][0] == '\"' and (not topoPilhaSplit[i][j+1][1].isdigit()) and not (topoPilhaSplit[i][j+1][1],'int') in reversoListaVar) or     (topoPilhaSplit[i][j-1][0] == '\'' and (not topoPilhaSplit[i][j-1][1].isdigit()) and not (topoPilhaSplit[i][j-1][1],'int') in reversoListaVar) or      (topoPilhaSplit[i][j+1][0] == '\'' and (not topoPilhaSplit[i][j+1][1].isdigit()) and not (topoPilhaSplit[i][j+1][1],'int') in reversoListaVar)  :
#                     print(topoPilhaSplit[i][j-1]," EO-O ",topoPilhaSplit[i][j+1])
                    return False
                else:                                                                                                                 
                    continue
#     print(reversoListaVar)
# print("operacaoIntNaoVar() ",operacaoIntNaoVar())

def analisadorDeTipos():
    if operacaoIntNaoVar()!=False and operacaoStringNaoVar()!=False and string_add() != False:
#         print("Sucesso") # pegar casos em que o arquivo tem somente algo do tipo
        return True
    elif operacaoIntNaoVar()!=False and operacaoStringNaoVar()!=False and caseIntIgualString() !=False and caseStringIgualInt()!=False and operacaoInt2()!=False and  operacaoInt()!=False and operacaoString()!=False and string_add() != False:
#         print("Sucesso")
        return True #"Sucesso"
    else:
#         print("Erro")
        return False# "Erro"    
# print(analisadorDeTipos())
# print(caseIntIgualString())



# In[127]:

# lc = arquivoPraLinha('saida.txt')

# retorna Erro se o parâmetro de retorno não é o mesmo do tipo da função
def tipo_funcao_mesmo_tipo_retorno_param():
    variaveisArquivo = []
    var_func_Arquivo = []
    so_tipo_var_func_Arquivo = []
    
    tiposVariaveisArquivo = []
    funcArquivo = []
    funcArquivoZeroParam = []
    funcArquivoUmParam = []
    funcArquivoDoisParam = []
    varParametrosReturn = [] # lista com os parâmetros e os tipos dos retornos
    reversoListaVar = []
    topoPilha = 0
# Pegando todas as variáveis e funções e colocando eles em uma lista na ordem que são declaradas    
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if ((topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and not topoPilhaSplit[i][j+2] == '(') or ((topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and topoPilhaSplit[i][j+2] == '('):
                var_func_Arquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j] ) )                    
                so_tipo_var_func_Arquivo.append(topoPilhaSplit[i][j])                    
                    
                
# Pegando todas as variáveis e colocando eles em uma lista na ordem que são declaradas    
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and not topoPilhaSplit[i][j+2] == '(':
                    variaveisArquivo.append( (topoPilhaSplit[i][j+1], topoPilhaSplit[i][j] ) )
                    tiposVariaveisArquivo.append( (topoPilhaSplit[i][j] ) )
                    
                    reversoListaVar=variaveisArquivo[::-1] 
# Pegando todas as funções com seus parâmetros e colocando eles em uma lista na ordem que são declaradas    
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and topoPilhaSplit[i][j+2] == '(':
                funcArquivo.append( (topoPilhaSplit[i][j] ) ) # pegando as funções na ordem que são declaradas
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and topoPilhaSplit[i][j+2] == '(' and topoPilhaSplit[i][j+3] == ')': 
                funcArquivoZeroParam.append( (topoPilhaSplit[i][j]) ) # *só preciso guardar a func
            
            if ((topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and topoPilhaSplit[i][j+2] == '(' and (topoPilhaSplit[i][j+3] == 'int' or topoPilhaSplit[i][j+3] == 'string') and topoPilhaSplit[i][j+5] ==')' ):
                    funcArquivoUmParam.append( (topoPilhaSplit[i][j]) ) # *só preciso a func

            if ((topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and topoPilhaSplit[i][j+2] == '(' and (topoPilhaSplit[i][j+3] == 'int' or topoPilhaSplit[i][j+3] == 'string') and (topoPilhaSplit[i][j+6] == 'int' or topoPilhaSplit[i][j+6] == 'string') and topoPilhaSplit[i][j+8] ==')' ):
                    funcArquivoDoisParam.append((topoPilhaSplit[i][j])) # func
    
# Pegando os parametros do retorno das funções
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if topoPilhaSplit[i][j] == 'return':
                # para return com 1 or 2 param tipo var or func
                if ((topoPilhaSplit[i][j+1], 'int') in var_func_Arquivo) and (topoPilhaSplit[i][j+2] == '+' or topoPilhaSplit[i][j+2] == '-' or topoPilhaSplit[i][j+2] == '*' or topoPilhaSplit[i][j+2] == '/' or topoPilhaSplit[i][j+2] == '++' or topoPilhaSplit[i][j+2] == '==') and topoPilhaSplit[i][j+4] == ';' or ((topoPilhaSplit[i][j+1], 'int') in var_func_Arquivo and topoPilhaSplit[i][j+2] == ';'):

# or porque caso tenha int string vai dá erro por outros métodos # retorno com um parâmetro ou dois parâmetros        
#obs: basto pegar um dos parâmetros pois se não for do mesmo tipo vai dá erro por outras operações
                    varParametrosReturn.append('int') # tipos das funções na ordem que são declaradas

                if ((topoPilhaSplit[i][j+1], 'string') in var_func_Arquivo) and (topoPilhaSplit[i][j+2] == '+' or topoPilhaSplit[i][j+2] == '-' or topoPilhaSplit[i][j+2] == '*' or topoPilhaSplit[i][j+2] == '/' or topoPilhaSplit[i][j+2] == '++' or topoPilhaSplit[i][j+2] == '==') and topoPilhaSplit[i][j+4] == ';' or ((topoPilhaSplit[i][j+1], 'string') in var_func_Arquivo and topoPilhaSplit[i][j+2] == ';'):
                    varParametrosReturn.append('string') # tipos das funções na ordem que são declaradas

# verificando se as funções de 1 parâmetro é igual ao retorno da função
    for l in range(len(funcArquivo)):
#         print("Aqui 1 ")
        if not(varParametrosReturn[l] == funcArquivo[l] ): # O caso é que se criar uma função que repare o tipo da funções com um e dois parâmetros de retorno dá 100% para todos os casos
#             print("Aqui 2 ")
#             print("Erro Int or String", varParametrosReturn[l], funcArquivo[l])
            return False
        else:
#             print("continuando ", varParametrosReturn[l], funcArquivo[l])
            continue
# print(tipo_funcao_mesmo_tipo_retorno_param())


# In[128]:

##                               sobrecarga de função
todasFuncoesArquivo = []
def sobrecarga_funcaoAux():
# Pegando todas as funções com seus parâmetros e colocando eles em uma lista na ordem que são declaradas    
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and topoPilhaSplit[i][j+2] == '(' and topoPilhaSplit[i][j+3] == ')': 
                todasFuncoesArquivo.append((topoPilhaSplit[i][j], topoPilhaSplit[i][j+1], (( )))) # add func e param            
            if ((topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and topoPilhaSplit[i][j+2] == '(' and (topoPilhaSplit[i][j+3] == 'int' or topoPilhaSplit[i][j+3] == 'string') and topoPilhaSplit[i][j+5] ==')' ):
                todasFuncoesArquivo.append((topoPilhaSplit[i][j], topoPilhaSplit[i][j+1], ( topoPilhaSplit[i][j+3] ,( ) ))) # add func e param

            if ((topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and topoPilhaSplit[i][j+2] == '(' and (topoPilhaSplit[i][j+3] == 'int' or topoPilhaSplit[i][j+3] == 'string') and (topoPilhaSplit[i][j+6] == 'int' or topoPilhaSplit[i][j+6] == 'string') and topoPilhaSplit[i][j+8] ==')' ):
                todasFuncoesArquivo.append((topoPilhaSplit[i][j], topoPilhaSplit[i][j+1], ( topoPilhaSplit[i][j+3] , topoPilhaSplit[i][j+6] ))) # add func e param
    
    
    # print("Funções ", todasFuncoesArquivo)  
# basta ver se há duplicados na função
def sobrecarga_funcao(todasFuncoesArquivo):
    _aux = []

    # removendo duplicados
    for x in todasFuncoesArquivo:
        if x not in _aux:
            _aux.append(x)
    # comparando os tamanhos
    if len(todasFuncoesArquivo) != len(_aux):
        return True # tem duplicados
    else:
        return False    
    
# print(sobrecarga_funcaoAux())
# print(sobrecarga_funcao(todasFuncoesArquivo))


# In[129]:

# III. Se as variáveis (e funções) estão sendo usadas sem serem declaradas.

# Função que verifica quando uma função está sendo declarada antes de ser usada                
def func_ordem_declaracao():
    variaveisArquivo = []
    funcArquivo = []
    reversoListaVar = []
    indicesFunc = []
    indicesVar = []
    
    topoPilha = 0
# Pegando todas as funções e colocando eles em uma lista na ordem que são declaradas    
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and topoPilhaSplit[i][j+2] == '(':
                    funcArquivo.append( (topoPilhaSplit[i][j+1]) )
                    indicesFunc.append((i,j))
# Pegando todas as variáveis e colocando eles em uma lista na ordem que são declaradas    
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if (topoPilhaSplit[i][j] == 'int' or topoPilhaSplit[i][j] == 'string') and not topoPilhaSplit[i][j+2] == '(':
                    variaveisArquivo.append( (topoPilhaSplit[i][j+1] ) )
                    indicesVar.append((i,j))
                    reversoListaVar=variaveisArquivo[::-1] 

# Verificando se as funções estão sendo declaradas antes de serem usadas
    for i in range(len(topoPilhaSplit)): 
        for j in range(len(topoPilhaSplit[i])):
            if topoPilhaSplit[i][j] == '(':
                # pegando declarações de funções
                if not (topoPilhaSplit[i][j-2] == 'int') and not(topoPilhaSplit[i][j-2] == 'string'):
                    for k in range(len(indicesFunc)):
                        if topoPilhaSplit[i][j-1] == funcArquivo[k]: # quando encontro uma função declarada
                            if (i,j) > indicesFunc[k]: # vejo se ela e declarada antes
#                                 print((i,j), indicesFunc[k])
                                continue
                            else:
                                # print("A função ", topoPilhaSplit[i][j-1], " foi declarada antes de ser usada: ", topoPilhaSplit[i][j-1], " tem índice ", (i,j), " a declaração dela tem índice ", indicesFunc[k])
                                return False

# Função que verifica quando uma variável está sendo declarada antes de ser usada  

# **** ESQUECI O CASO DE TER UMA PARÂMETRO DE FUNÇÃO COM O MESMO NOME DE UM RETORNO DE UMA FUNÇÃO 
# exemplo:  o a aparece no indice (2, 2) (0, 3)
# A variável  a  foi declarada antes de ser usada:  a  tem índice  (2, 2)  a declaração dela tem índice  (5, 0)
# False

# int fun ( int a , int b ) {
	
# 	return a + b ;
# }
# int main ( ) {
# 	int a = 3 ;
    
def var_ordem_declaracao():  
    i = 0
    topoPilha = 0
    varCode = lc
    escopo = Pilha ()
    escopos = [escopo] 
    variaveis = []
    while i < len(varCode):
        if varCode[i] == '=': # olho para toda declaração do tipo ALGO =
            if (varCode[i-2] == 'int' or varCode[i-2] == 'string'):
#                 print(varCode[i+1])
# depois basta verificar se na minha lista existe INT ALGO, ou INT ALGO e add a lista caso não exista
                if not ((varCode[i-1], 'int') in escopos[topoPilha] ==False) or not (varCode[i-1], 'string') in escopos[topoPilha]:                    
                    escopos[topoPilha].append( (varCode[i-1], varCode[i-2]) ) # formato x, int
                    variaveis.append( (varCode[i-1]))
# para pegar uma variável que está declarada antes de ser usada basta verificar se tenho INT or STRING op ALGO e ALGO já está em variáveis.                                
            if ((varCode[i-2] == 'int' or varCode[i-2] == 'string') and varCode[i+1] in variaveis):
#                 print ('variável usada antes de ser declarada varCode[i+1] ', varCode[i+1])
                return False
# para pegar uma variável que está declarada antes de ser usada basta verificar se tenho ALGO op INT or STRING e ALGO já está em variáveis.                                
            if ((varCode[i-2] == 'int' or varCode[i-2] == 'string') and varCode[i+3] in variaveis):
#                 print ('variável usada antes de ser declarada varCode[i+3] ', varCode[i+3])
                return False
# para pegar uma variável que está declarada antes de ser usada basta verificar se antes do ALGO não tem INT nem STRING.                
            elif (varCode[i-2] != 'int'and varCode[i-2] != 'string') and (varCode[i-1] in variaveis):
#                 print ('variável usada antes de ser declarada varCode[i-1] ', varCode[i-1])
                return False
        i += 1                
# print("func_ordem_declaracao() ",func_ordem_declaracao())    
# print("var_ordem_declaracao() ",var_ordem_declaracao())   


# In[130]:


# print("verifica_param_func(lc) ",verifica_param_func(lc))
# print("duplicadoVarEscopo(p) ",duplicadoVarEscopo(p))

def Analisador():
#     print(lc)
#     if duplicadoVarEscopo(p) != False and duplicadoVarEscopo(p) != False:# not verifica_var_escopo(lc): # erro nessa função
        #sobrecarga_funcao(todasFuncoesArquivo)!=True: 
        
#     if not verifica_func_escopo(lc) and analisadorDeTipos() != False and tipo_funcao_mesmo_tipo_retorno_param() !=False and func_ordem_declaracao() != False and sobrecarga_funcao(todasFuncoesArquivo) !=True: # and var_ordem_declaracao() != False :
#     if tipo_funcao_mesmo_tipo_retorno_param() !=False:
#         return "Sucesso"

    if not verifica_func_escopo(lc) and analisadorDeTipos() != False and func_ordem_declaracao() != False and sobrecarga_funcao(todasFuncoesArquivo) !=True  and var_ordem_declaracao() != False and duplicadoVarEscopo(p) != False and duplicadoVarEscopo(p) != False:
        return "Sucesso"
    else:
        return "Erro"
print(Analisador())
# print(teste6)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



