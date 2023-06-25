from .symbolTable import SymbolTable

class Generador():
    generador = None

    def __init__(self):
        #Contadores
        self.countTemp = 0 #Contador de temporales
        self.countLabel = 0 #Contador de etiquetas

        #Codigo
        self.codigo = ""
        self.funcs = ""
        self.nativas=""
        self.inFunc = False
        self.inNatives = False

        #Lista de temporales
        self.temps = []

        #Lista de nativas
        self.printString = False

        #Lista de imports
        self.imports = []
        self.imports2 = ['fmt','math'] #Imports quemados desde el inicio

    def cleanAll(self):
        #Contadores
        self.countTemp = 0
        self.countLabel = 0
        #Codigo
        self.codigo = ""
        self.funcs = ""
        self.nativas=""
        self.inFunc = False
        self.inNatives = False

        #Lista de temporales
        self.temps = []    

        #Lista de nativas
        self.printString = False

        #Lista de imports
        self.imports = []
        self.imports2 = ['fmt','math']

        Generador.generador = Generador() #Es una especie de patrón singleton

    #**********************************IMPORTS**************************************************
    def setImport(self,lib):
        if lib in self.imports2:
            self.imports2.remove(lib) #Si la librería está en la lista de imports permitidos y no ha sido importada previamente
        else:
            return
        
        code = f'import(\n\t\"{lib}\"\n);\n'
        self.imports.append(code) 

    #********************************************CODE******************************************
    def getHeader(self):
        code = '/*----------HEADER----------*/\npackage main;\n\n'
        if len(self.imports) > 0:
            for imp in self.imports:
                code+=imp
        if len(self.temps) > 0:
            code+="var "
            for temp in self.temps:
                code+=temp + ','
            code = code[:-1]
            code+= " float64;\n\n"
        code+= "var P, H float64;\nvar stack[30101999] float64;\nvar heap[30101999] float64;\n\n"
        return code
    
    def getCode(self):
        return f'{self.getHeader()}{self.nativas}{self.funcs}\nfunc main(){{\n{self.codigo}\n}}'
    
    def codeIn(self,code):
        if self.inNatives:
            if self.nativas == '':
                self.nativas = self.nativas + "/*----------NATIVA----------*/\n"

            self.nativas = self.nativas +"\t" + code

        elif self.inFunc:
            if self.funcs == '':
                self.funcs = self.funcs + "/*----------FUNCION----------*/\n"
            self.funcs = self.funcs+"\t"+code

        else:
            self.codigo = self.codigo + "\t" + code
    
    def addComment(self,comentario):
        self.codeIn(f'/* {comentario} */\n')

    def getInstance(self):
        if Generador.generador == None:
            Generador.generador = Generador()

        return Generador.generador

    def addSpace(self):
        self.codeIn('\n')


       #************************************TEMPORALES****************************************** 
    def addTemp(self):
        temp = f't{self.countTemp}'
        self.countTemp+=1
        self.temps.append(temp)
        return temp
    
    #*****************************************LABELS********************************************
    def newLabel(self):
        label = f'L{self.countLabel}'
        self.countLabel+=1
        return label
    
    def putLabel(self,label):
        self.codeIn(f'{label}:\n')
    
    def addIdent(self):
        self.codeIn('') #El método codeIn agrega una identación
    #****************************************GOTO************************************************

    def addGoto(self,label):
        self.codeIn(f'goto {label};\n')

    #*********************************************IF*********************************************
    def addIf(self, left, right, op, label):
        self.codeIn(f'if {left} {op} {right} {{goto {label};}}\n')
    #********************************************EXPRESIONES*************************************
    def addExp(self,result,left,rigt,op):
        self.codeIn(f'{result} = {left} {op} {rigt};\n')
        

    def addAsignacion(self,result,left):
        self.codeIn(f'{result} = {left};\n')
        

    def addPow(self,result,base,exponente):
        self.setImport('math')
        self.codeIn(f'{result} = math.Pow({base},{exponente});\n')
        

    #**********************************************FUNCIONES*************************************
    def addBeginFunc(self,id):
        if not self.inNatives:
            self.inFunc=True

        self.codeIn(f'func {id}(){{\n')

    def addEndFunc(self):
        if not self.inNatives:
            self.inFunc=False
        self.codeIn('}\n')

    ####################
    #NATIVAS
    ####################

    #######################
    #PRINT STRING
    #######################
    def fPrintString(self):
        self.setImport('fmt')
        if self.printString:
            return
        self.printString = True
        self.inNatives = True
        self.addBeginFunc('printString')
        #Salir de la función
        returnLbl = self.newLabel()

        compareLbl = self.newLabel()

        temStack = self.addTemp()
        temHeap = self.addTemp()

        self.addExp(temStack, 'P','1','+')
        self.getStack(temHeap,temStack)

        temC = self.addTemp()

        self.putLabel(compareLbl)
        self.addIdent()

        self.getHeap(temC,temHeap)
        self.addIdent()

        self.addIf(temC,'-1',"==",returnLbl)
        self.addIdent()
        self.addPrint('c',f'int({temC})')
        self.addIdent()
        self.addExp(temHeap,temHeap,'1','+')
        self.addIdent()

        self.addGoto(compareLbl)
        self.putLabel(returnLbl)
        self.addEndFunc()
        
        self.inNatives = False
        


    #**********************************************STACK****************************************
    def setStack(self,pos,value):
        self.codeIn(f'stack[int({pos})] = {value};\n')

    def getStack(self,place,pos):
        self.codeIn(f'{place} = stack[int({pos})];\n')

    #*******************************************ENTORNOS*****************************************
    def newEnv(self,size):
        self.codeIn('/*----------NUEVO ENTORNO----------*/\n')
        self.codeIn(f'P = P + {size};\n')

    def callFun(self,id):
        self.codeIn(f'{id}();\n')

    def retEnv(self,size):
        self.codeIn(f'P = P - {size};\n')
        self.codeIn('/*----------RETORNO DEL ENTORNO----------*/\n')

    #******************************************HEAP**********************************************
    def setHeap(self,pos,value):
        self.codeIn(f'heap[int({pos})] = {value};\n')

    def getHeap(self,place,pos):
        self.codeIn(f'{place} = heap[int({pos})];\n')

    def nextHeap(self):
        self.codeIn('H = H + 1;\n')

    #****************************************INSTRUCCIONES***************************************
    ######################
    #CONSOLE.LOG
    ######################
    def addPrint(self,typee,value):
        self.setImport('fmt')
        self.codeIn(f'fmt.Printf("%{typee}", {value});\n')
        #if type(value)==int:
        #    self.codeIn(f'fmt.Printf("%{typee}",({value}));\n')
        #else:
        #    self.codeIn(f'fmt.Printf("%{typee}",{value});\n') 
        #%d -> entero
        #%c -> caracter
        #%f -> flotante
        #%s -> string

    def printTrue(self):
        self.setImport('fmt')
        self.addIdent()
        self.addPrint("c", 116)
        self.addIdent()
        self.addPrint("c", 114)
        self.addIdent()
        self.addPrint("c", 117)
        self.addIdent()
        self.addPrint("c", 101)
    
    def printFalse(self):
        self.setImport('fmt')
        self.addIdent()
        self.addPrint("c", 102)
        self.addIdent()
        self.addPrint("c", 97)
        self.addIdent()
        self.addPrint("c", 108)
        self.addIdent()
        self.addPrint("c", 115)
        self.addIdent()
        self.addPrint("c", 101)

    