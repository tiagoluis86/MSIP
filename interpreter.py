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
            self.pos += 1
            return token 
        
        self.error()

    def eat(self, token_type):
        """
        compara o type do token atual com o type do que foi passado
        marca o proximo token do self.current_token ou dá exceção
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """
        expr -> INTEGER PLUS INTEGER
        seta o token atual como o primeiro token pegado do input
        """
        self.current_token = self.gen_next_token()

        #a esperança é o que o token seja um INT
        left = self.current_token
        self.eat(INTEGER)

        #se espera que o token seja um "+"
        op = self.current_token
        self.eat(PLUS)

        #a esperança é o que esse token seja um INT
        right = self.current_token
        self.eat(INTEGER)

        """
        depois do que acontece acima, o self.current_token é setado como EOF token
        aqui a sequência INTEGER PLUS INTEGER de tokens foi encontrada e esse método pode retornar o resultado da adição das duas INT
        efetivamente interpretando o client input
        """
        result = left.value + right.value 
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