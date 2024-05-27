from enum import Enum

class EnumPalabras(Enum):
    SUM_PLUS = 'SUM+'
    RES_MINUS = 'RES-'
    MUL_TIMES = 'MUL*'
    DIV_DIVIDE = 'DIV/'
    MOD_MODULO = 'MOD%'
    PO_POWER = 'PO**'
    EQ_EQUAL = 'EQ=='
    NEQ_NOTEQUAL = 'NEQ!='
    LT_LESSTHAN = 'LT>'
    GT_GREATERTHAN = 'GT<'
    LE_LESSEQUAL = 'LE>='
    GE_GREATEREQUAL = 'GE<='
    AND_AND = 'AND&&'
    OR_OR = 'OR||'
    NOT_NOT = 'NOT!'
    SET_SET = 'SET='
    IADD_INCADD = 'IADD+='
    ISUB_INCSUB = 'ISUB-='
    PARENTHESIS = '()'
    BRACES = '{}'
    BRACKETS = '[]'
    SEMICOLON = ';'
    MINUS = '-'
    CIFOR = 'CIFOR'
    CIWHI = 'CIWHI'
    SI = 'SI'
    ELSE = 'ELSE'
    ELSI = 'ELSI'
    CLS = 'CLS'
    ITF = 'ITF'
    VAR = 'VAR'
    FNC = 'FNC'
    ENT32 = 'ent32'
    DEC12 = 'dec12'
    STR128 = 'str128'
    CHR48 = 'chr48'
    ENT = 'ENT'
    DEC = 'DEC'
    STR = 'STR'
    CHR = 'CHR'

categorias_tokens = {
    EnumPalabras.SUM_PLUS: 'Aritméticos',
    EnumPalabras.RES_MINUS: 'Aritméticos',
    EnumPalabras.MUL_TIMES: 'Aritméticos',
    EnumPalabras.DIV_DIVIDE: 'Aritméticos',
    EnumPalabras.MOD_MODULO: 'Aritméticos',
    EnumPalabras.PO_POWER: 'Aritméticos',
    EnumPalabras.EQ_EQUAL: 'Relacionales',
    EnumPalabras.NEQ_NOTEQUAL: 'Relacionales',
    EnumPalabras.LT_LESSTHAN: 'Relacionales',
    EnumPalabras.GT_GREATERTHAN: 'Relacionales',
    EnumPalabras.LE_LESSEQUAL: 'Relacionales',
    EnumPalabras.GE_GREATEREQUAL: 'Relacionales',
    EnumPalabras.AND_AND: 'Lógicos',
    EnumPalabras.OR_OR: 'Lógicos',
    EnumPalabras.NOT_NOT: 'Lógicos',
    EnumPalabras.SET_SET: 'Asignación',
    EnumPalabras.IADD_INCADD: 'Asignación',
    EnumPalabras.ISUB_INCSUB: 'Asignación',
    EnumPalabras.PARENTHESIS: 'Apertura_Y_Cierre',
    EnumPalabras.BRACES: 'Apertura_Y_Cierre',
    EnumPalabras.BRACKETS: 'Apertura_Y_Cierre',
    EnumPalabras.SEMICOLON: 'Terminal',
    EnumPalabras.MINUS: 'Separador',
    EnumPalabras.CIFOR: 'Palabras_reservadas',
    EnumPalabras.CIWHI: 'Palabras_reservadas',
    EnumPalabras.SI: 'Palabras_reservadas',
    EnumPalabras.ELSE: 'Palabras_reservadas',
    EnumPalabras.ELSI: 'Palabras_reservadas',
    EnumPalabras.ITF: 'Palabras_reservadas',
    EnumPalabras.VAR: 'Identificadores',
    EnumPalabras.FNC: 'Identificadores',
    EnumPalabras.CLS: 'Identificadores',
    EnumPalabras.ENT32: 'Valor_de_asignacion',
    EnumPalabras.DEC12: 'Valor_de_asignacion',
    EnumPalabras.STR128: 'Valor_de_asignacion',
    EnumPalabras.CHR48: 'Valor_de_asignacion',
    EnumPalabras.ENT: 'Tipo_de_dato',
    EnumPalabras.DEC: 'Tipo_de_dato',
    EnumPalabras.STR: 'Tipo_de_dato',
    EnumPalabras.CHR: 'Tipo_de_dato'
}

class Token:
    def __init__(self, palabra):
        try:
            self.palabra_reservada = EnumPalabras(palabra)
            self.categoria = categorias_tokens[self.palabra_reservada]
        except ValueError:
            raise ValueError(f"{palabra} no es una palabra reservada válida.")
        except KeyError:
            raise ValueError(f"No se encontró la categoría para la palabra reservada {palabra}.")

    def __repr__(self):
        return f"Token(palabra_reservada={self.palabra_reservada}, categoria={self.categoria})"


# Ejemplo de uso
token = Token('SUM+')
print(token.palabra_reservada)  # Salida: PalabraReservada.SUM_PLUS
print(token.categoria)  # Salida: Aritméticos