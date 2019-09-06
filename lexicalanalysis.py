from enum import Enum
from errors import SyntaxError

DELIMITER = " "
VALUES = ['T', 'F', '~', '^', 'v', '->', ')', '(', '.']


class TOKEN(Enum):
    T = 'T'
    F = 'F'
    NOT = '~'
    AND = '^'
    OR = 'v'
    IMP = '->'
    OPEN = '('
    CLOSE = ')'
    END = '.'

    def __str__(self):
        return str(self.value)

    # @classmethod
    # def values(cls):
    #   return list(map(lambda x: x.value, TokenType.__members__.values()))

selection_set = {
    'B': [{TOKEN.NOT.value, TOKEN.T.value, TOKEN.F.value, TOKEN.OPEN.value}],
    'IT': [{TOKEN.NOT.value, TOKEN.T.value, TOKEN.F.value, TOKEN.OPEN.value}],
    'IT_TAIL': [{TOKEN.IMP.value}, {TOKEN.END.value, TOKEN.CLOSE.value}],
    'OT': [{TOKEN.NOT.value, TOKEN.T.value, TOKEN.F.value, TOKEN.OPEN.value}],
    'OT_TAIL': [{TOKEN.OR.value}, {TOKEN.IMP.value, TOKEN.END.value, TOKEN.CLOSE.value}],
    'AT': [{TOKEN.NOT.value, TOKEN.T.value, TOKEN.F.value, TOKEN.OPEN.value}],
    'AT_TAIL': [{TOKEN.AND.value}, {TOKEN.OR.value, TOKEN.IMP.value, TOKEN.END.value, TOKEN.CLOSE.value}],
    'L': [{TOKEN.T.value, TOKEN.F.value, TOKEN.OPEN.value}, {TOKEN.NOT.value}],
    'A': [{TOKEN.T.value}, {TOKEN.F.value}, {TOKEN.OPEN.value}]
}


class LexicalAnalyser:
    def __init__(self, inpt):
        if inpt == '':
            raise SyntaxError(inpt, "Empty input")

        self.inpt = self.build_token_list(inpt.split())#[t for t in inpt.strip().split(DELIMITER)])
        print("Parsed input: {}".format(self.inpt))
        self.good_end = True if self.inpt[len(self.inpt)-1] == TOKEN.END.value else False
        self.lex = ''
        self.current_position = -1

    @classmethod
    def build_token_list(cls, lst):
        ls = []
        for i in lst:
            if i != TOKEN.IMP.value and len(i) > 1 and any(x in i for x in VALUES):
                tok_lst = [j for j in i]
                ls.extend(tok_lst)
            else:
                ls.append(i)

        final_ls = ls[:]
        for i in range(len(ls)):
            if ls[i] == '-':
                if i+1 != len(ls):
                    if ls[i+1] == '>':
                        final_ls[i] = '->'
                        del final_ls[i+1]
        return final_ls

    def get(self):
        self.current_position += 1

        try:
            for i in range(self.current_position,len(self.inpt)):
                self.current_position = i
                self.lex = self.inpt[self.current_position]

                if self.lex in DELIMITER:
                    continue
                else:
                    break
        except:
            pass

        if self.current_position >= len(self.inpt):
            raise IndexError("Reached end of input")

        return self.lex
        #--------------------------------------
        # if self.current_position == -1:
        #     self.current_position += 1
        #     self.lex = self.inpt[self.current_position]
        #
        # print("get was called. self.lex = {}, and position is {}".format(self.lex, self.current_position))
        #
        # while self.current_position < len(self.inpt):
        #     self.current_position += 1
        #     try:
        #         test = self.inpt[self.current_position] == DELIMITER
        #         continue
        #     elif self.current_position < len(self.inpt):
        #         self.lex = self.inpt[self.current_position]
        #         break
        # else:
        #     if self.current_position == len(self.inpt):
        #         raise IndexError("Reached end of input")
        #
        # return self.lex