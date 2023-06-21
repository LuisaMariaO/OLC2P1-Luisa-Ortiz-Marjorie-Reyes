from .symbolTable import SymbolTable

class Generador():
    generador = None

    def __init__(self):
        #Contadores
        self.countTemp = 0 #Contador de temporales

        #Codigo
        self.codigo = ""

        #Lista de temporales
        self.temps = []

        #Lista de nativas

        #Lista de imports
        self.imports = []
        self.imports2 = ['fmt','math'] #Imports quemados desde el inicio

    def cleanAll(self):
        #Contadores
        self.countTemp = 0

        #Codigo
        self.codigo = ""

        #Lista de temporales
        self.temps = []    

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
        return f'{self.getHeader()}\nfunc main(){{\n{self.codigo}\n}}'
    
    def addComent(self,comentario):
        self.codigo += f'/* {comentario} */\n'

    def getInstance(self):
        if Generador.generador == None:
            Generador.generador = Generador()

        return Generador.generador

    def addSpace(self):
        self.codigo+='\n'


       #************************************TEMPORALES****************************************** 
    def addTemp(self):
        temp = f't{self.countTemp}'
        self.countTemp+=1
        self.temps.append(temp)
        return temp
    
    #*****************************************LABELS********************************************

    #****************************************GOTO************************************************

    #*********************************************IF*********************************************

    #********************************************EXPRESIONES*************************************
    def addExp(self,result,left,rigt,op):
        
        self.codigo += f'{result} = {left} {op} {rigt};\n'

    def addAsignacion(self,result,left):
        self.codigo += f'{result} = {left};\n'

    def addPow(self,result,base,exponente):
        self.setImport('math')
        self.codigo+= f'{result} = math.Pow({base},{exponente});\n'


    #**********************************************STACK****************************************
    def setStack(self,pos,value):
        self.codigo+=f'stack[int({pos})] = {value};\n'

    def getStack(self,place,pos):
        self.codigo += f'{place} = stack[int({pos})];\n'

    #*******************************************ENTORNOS*****************************************
    def newEnv(self,size):
        self.codigo += '/*----------NUEVO ENTORNO----------*/'
        self.codigo += f'P = P + {size};\n'

    def callFun(self,id):
        self.codigo += f'{id}();\n'

    def retEnv(self,size):
        self.codigo+= f'P = P - {size};\n'
        self.codig+= '/*----------RETORNO DEL ENTORNO----------*/'

    #******************************************HEAP**********************************************
    def setHeap(self,pos,value):
        self.codigo+= f'heap[int({pos})] = {value};\n'

    def getHeap(self,place,pos):
        self.codigo += f'{place} = heap[int({pos})];\n'

    def nextHeap(self):
        self.codigo += 'H = H + 1;\n'

    #****************************************INSTRUCCIONES***************************************
    ######################
    #CONSOLE.LOG
    ######################
    def addPrint(self,type,value):
        self.setImport('fmt')
        self.codigo += f'fmt.Printf("%{type}",{value});\n' 
        #%d -> entero
        #%c -> caracter
        #%f -> flotante
        #%s -> string

    