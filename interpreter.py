INTEGER, PLUS, EOF = "INTEGER", "PLUS", "EOF" #EOF end of file para indicar que não há mais input restante

class Token(object):
    def __init__(self, type, value):
        #token pode ser INTEGER, PLUS ou EOF
        self.type = type 
        #token value pode ser 0,1,2,3,4,5,6,7,8,9,"+" ou None
        self.value = value 

    def __str__(self):
        #representação em str das class instances, tipo Token(INTEGER, 3)
        return "Token({type}, {value}".format(type=self.type, value=repr(self.value))

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    def __init__(self, text):
        #client string input, ex "3+5"
        self.text = text 
        #self.pos é um index da self.text
        self.pos = 0
        #atual token instance
        self.current_token = None

    def error(self):
        raise Exception("ERRO AO PASSAR O INPUT: ")

    def gen_next_token(self):
        """
        Isso aqui é um lexical analyzer; quebra a sentença em tokens, um token por vez
        """
        text = self.text 

        if self.pos > len(text) - 1:
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token 
        
        if current_char == "+":
            token = Token(PLUS, current_char)
