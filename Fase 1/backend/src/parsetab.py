
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftIGUALACIONDIFERENTEleftMAYORIGUALMENORIGUALMAYORMENORleftSUMARESTAleftMULTIPLICACIONDIVISIONMODULOrightNOTrightPOTENCIAleftPARABREPARCIERRAAND BOOLEAN CADENA CONSOLE DECIMAL DIFERENTE DIVISION DOSPTOS ENTERO FALSO ID IGUAL IGUALACION INTERFACE LET LLAVEABRE LLAVECIERRA LOG MAYOR MAYORIGUAL MENOR MENORIGUAL MODULO MULTIPLICACION NOT NULL NUMBER OR PARABRE PARCIERRA POTENCIA PTO PTOCOMA RESTA STRING SUMA VERDADEROinit : instruccionesinstrucciones : instrucciones instruccioninstrucciones : instruccioninstruccion : CONSOLE PTO LOG PARABRE expresion PARCIERRA PTOCOMAinstruccion : LET ID DOSPTOS tipo IGUAL expresion PTOCOMAinstruccion : LET ID IGUAL expresion PTOCOMAexpresion : expresion AND expresion\n                | expresion OR expresion\n                | NOT expresionexpresion : expresion MAYOR expresion\n                | expresion MENOR expresion\n                | expresion IGUALACION expresion\n                | expresion DIFERENTE expresion\n                | expresion MAYORIGUAL expresion\n                | expresion MENORIGUAL expresion\n                | expresion POTENCIA expresion\n                | expresion MODULO expresionexpresion : expresion SUMA expresion\n                | expresion RESTA expresion\n                | expresion MULTIPLICACION expresion\n                | expresion DIVISION expresionexpresion : ENTEROexpresion : DECIMALexpresion : CADENAexpresion : FALSO\n                | VERDADEROexpresion : IDexpresion : INTERFACE ID LLAVEABRE LLAVECIERRA PTOCOMAexpresion : NULLtipo : STRING\n            | NUMBER\n            | BOOLEAN'
    
_lr_action_items = {'CONSOLE':([0,2,3,6,29,63,64,],[4,4,-3,-2,-6,-4,-5,]),'LET':([0,2,3,6,29,63,64,],[5,5,-3,-2,-6,-4,-5,]),'$end':([1,2,3,6,29,63,64,],[0,-1,-3,-2,-6,-4,-5,]),'PTO':([4,],[7,]),'ID':([5,11,12,19,25,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[8,17,17,17,45,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'LOG':([7,],[9,]),'DOSPTOS':([8,],[10,]),'IGUAL':([8,13,14,15,16,],[11,28,-30,-31,-32,]),'PARABRE':([9,],[12,]),'STRING':([10,],[14,]),'NUMBER':([10,],[15,]),'BOOLEAN':([10,],[16,]),'NOT':([11,12,19,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'ENTERO':([11,12,19,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'DECIMAL':([11,12,19,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'CADENA':([11,12,19,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'FALSO':([11,12,19,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'VERDADERO':([11,12,19,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'INTERFACE':([11,12,19,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'NULL':([11,12,19,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'PTOCOMA':([17,18,20,21,22,23,24,26,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,65,66,],[-27,29,-22,-23,-24,-25,-26,-29,-9,63,64,-7,-8,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,66,-28,]),'AND':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,30,-22,-23,-24,-25,-26,-29,30,-9,30,-7,30,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-28,]),'OR':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,31,-22,-23,-24,-25,-26,-29,31,-9,31,-7,-8,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-28,]),'MAYOR':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,32,-22,-23,-24,-25,-26,-29,32,-9,32,32,32,-10,-11,32,32,-14,-15,-16,-17,-18,-19,-20,-21,-28,]),'MENOR':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,33,-22,-23,-24,-25,-26,-29,33,-9,33,33,33,-10,-11,33,33,-14,-15,-16,-17,-18,-19,-20,-21,-28,]),'IGUALACION':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,34,-22,-23,-24,-25,-26,-29,34,-9,34,34,34,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-28,]),'DIFERENTE':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,35,-22,-23,-24,-25,-26,-29,35,-9,35,35,35,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-28,]),'MAYORIGUAL':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,36,-22,-23,-24,-25,-26,-29,36,-9,36,36,36,-10,-11,36,36,-14,-15,-16,-17,-18,-19,-20,-21,-28,]),'MENORIGUAL':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,37,-22,-23,-24,-25,-26,-29,37,-9,37,37,37,-10,-11,37,37,-14,-15,-16,-17,-18,-19,-20,-21,-28,]),'POTENCIA':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,38,-22,-23,-24,-25,-26,-29,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-28,]),'MODULO':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,39,-22,-23,-24,-25,-26,-29,39,-9,39,39,39,39,39,39,39,39,39,-16,-17,39,39,-20,-21,-28,]),'SUMA':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,40,-22,-23,-24,-25,-26,-29,40,-9,40,40,40,40,40,40,40,40,40,-16,-17,-18,-19,-20,-21,-28,]),'RESTA':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,41,-22,-23,-24,-25,-26,-29,41,-9,41,41,41,41,41,41,41,41,41,-16,-17,-18,-19,-20,-21,-28,]),'MULTIPLICACION':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,42,-22,-23,-24,-25,-26,-29,42,-9,42,42,42,42,42,42,42,42,42,-16,-17,42,42,-20,-21,-28,]),'DIVISION':([17,18,20,21,22,23,24,26,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,43,-22,-23,-24,-25,-26,-29,43,-9,43,43,43,43,43,43,43,43,43,-16,-17,43,43,-20,-21,-28,]),'PARCIERRA':([17,20,21,22,23,24,26,27,44,48,49,50,51,52,53,54,55,56,57,58,59,60,61,66,],[-27,-22,-23,-24,-25,-26,-29,46,-9,-7,-8,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-28,]),'LLAVEABRE':([45,],[62,]),'LLAVECIERRA':([62,],[65,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,],[2,]),'instruccion':([0,2,],[3,6,]),'tipo':([10,],[13,]),'expresion':([11,12,19,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,],[18,27,44,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_Inicio','Sintactic.py',19),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_lista_instrucciones','Sintactic.py',23),
  ('instrucciones -> instruccion','instrucciones',1,'p_instruccion','Sintactic.py',29),
  ('instruccion -> CONSOLE PTO LOG PARABRE expresion PARCIERRA PTOCOMA','instruccion',7,'p_imprimir','Sintactic.py',36),
  ('instruccion -> LET ID DOSPTOS tipo IGUAL expresion PTOCOMA','instruccion',7,'p_declaraciones','Sintactic.py',41),
  ('instruccion -> LET ID IGUAL expresion PTOCOMA','instruccion',5,'p_asignaciones','Sintactic.py',46),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresiones_logicas','Sintactic.py',51),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresiones_logicas','Sintactic.py',52),
  ('expresion -> NOT expresion','expresion',2,'p_expresiones_logicas','Sintactic.py',53),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresiones_relacionales','Sintactic.py',62),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresiones_relacionales','Sintactic.py',63),
  ('expresion -> expresion IGUALACION expresion','expresion',3,'p_expresiones_relacionales','Sintactic.py',64),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresiones_relacionales','Sintactic.py',65),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresiones_relacionales','Sintactic.py',66),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresiones_relacionales','Sintactic.py',67),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresiones_relacionales','Sintactic.py',68),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresiones_relacionales','Sintactic.py',69),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresiones_aritmeticas','Sintactic.py',88),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresiones_aritmeticas','Sintactic.py',89),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_expresiones_aritmeticas','Sintactic.py',90),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresiones_aritmeticas','Sintactic.py',91),
  ('expresion -> ENTERO','expresion',1,'p_entero','Sintactic.py',102),
  ('expresion -> DECIMAL','expresion',1,'p_decimal','Sintactic.py',106),
  ('expresion -> CADENA','expresion',1,'p_cadena','Sintactic.py',110),
  ('expresion -> FALSO','expresion',1,'p_booleano','Sintactic.py',114),
  ('expresion -> VERDADERO','expresion',1,'p_booleano','Sintactic.py',115),
  ('expresion -> ID','expresion',1,'p_identificador','Sintactic.py',122),
  ('expresion -> INTERFACE ID LLAVEABRE LLAVECIERRA PTOCOMA','expresion',5,'p_interface','Sintactic.py',126),
  ('expresion -> NULL','expresion',1,'p_null','Sintactic.py',129),
  ('tipo -> STRING','tipo',1,'p_tipos','Sintactic.py',133),
  ('tipo -> NUMBER','tipo',1,'p_tipos','Sintactic.py',134),
  ('tipo -> BOOLEAN','tipo',1,'p_tipos','Sintactic.py',135),
]
