INTEGER, PLUS, MINUS, EOF = "INTEGER", "PLUS", "MINUS", "EOF" #EOF end of file para indicar que não há mais input restante

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
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("ERRO AO PASSAR O INPUT: ")

    def advance(self):
        """
        avança o pos e seta a o current_char
        """
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None 
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """
        Returna uma INT com vários dígitos do input
        """
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char 
            self.advance()
        return int(result)

    def gen_next_token(self):
        """
        Isso aqui é um lexical analyzer; quebra a sentença em tokens, um token por vez
        """

        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == "+":
                self.advance()
                return Token(PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(MINUS, "-")
            
            self.error()
        
        return Token(EOF, None)

    def eat(self, token_type):
        """
        compara o type do token atual com o type do que foi passado
        marca o proximo token do self.current_token ou dá exceção
        """
        if self.current_token.type == token_type:
            self.current_token = self.gen_next_token()
        else:
            self.error()

    def term(self):
        """
        Retorna um token INT
        """
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        """
        Parser / Interpreter
        Seta o token atual como o primeiro token a ser pego do input
        """
        self.current_token = self.gen_next_token()

        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()
        
        return result 


def main():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break 
        if not text:
            continue 
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == "__main__":
    main()