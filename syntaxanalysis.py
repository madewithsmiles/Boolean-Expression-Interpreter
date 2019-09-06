from lexicalanalysis import LexicalAnalyser, TOKEN, selection_set
from errors import SyntaxError


class SyntaxAnalyser:
    def __init__(self, LA):
        self.sa_stack = []
        self.LA = LA
        self.lex = self.LA.get()

    def run(self):
        return self.B()

    def OT_TAIL(self):
        if self.lex == TOKEN.OR.value:
            try:
                self.lex = self.LA.get()
            except:
                return False
            if self.AT():
                if self.AT_TAIL():
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.lex in selection_set['OT_TAIL'][1]:
                return True
            else:
                raise SyntaxError(
                    "expecting a {expected} but found : {found}".format(expected=str(selection_set['OT_TAIL']),
                                                                        found=self.lex))

    def AT(self):
        if self.L():
            if self.AT_TAIL():
                return True
            else:
                return False
        else:
            return False

    def AT_TAIL(self):
        if self.lex == TOKEN.AND.value:
            try:
                self.lex = self.LA.get()
            except:
                return False
            if self.L():
                if self.AT_TAIL():
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.lex in selection_set['AT_TAIL'][1]:
                return True
            else:
                return False
                # raise SyntaxError(
                #     "expecting an element from {ex} but found: {f}".format(ex=str(selection_set['AT_TAIL']),
                #                                                            f=self.lex))

    def L(self):
        if self.A():
            return True
        else:
            if self.lex == TOKEN.NOT.value:
                try:
                    self.lex = self.LA.get()
                except:
                    return False
                if self.L():
                    return True
                else:
                    return False
            else:
                raise SyntaxError(
                    "expecting an element from {e} but found: {f}".format(e=str(selection_set['L']), f=self.lex))

    def A(self):
        if self.lex == TOKEN.T.value:
            try:
                self.lex = self.LA.get()
            except:
                pass
            return True
        if self.lex == TOKEN.F.value:
            try:
                self.lex = self.LA.get()
            except:
                pass
            return True
        else:
            if self.lex == TOKEN.OPEN.value:
                try:
                    self.lex = self.LA.get()
                except:
                    return False
                if self.IT():
                    return True
                else:
                    return False
            else:
                return False
                # raise SyntaxError(
                #     "was expected an element from {e} but found: {f}".format(e=str(selection_set["A"]), f=self.lex))

    def OT(self):
        if self.AT():
            if self.OT_TAIL():
                return True
            else:
                return False
        else:
            return False

    def IT(self):
        if self.OT():
            if self.IT_TAIL():
                return True
            else:
                return False
        else:
            return False

    def IT_TAIL(self):
        if self.lex == TOKEN.IMP.value:
            try:
                self.lex = self.LA.get()
            except:
                return False
            if self.OT():
                if self.IT_TAIL():
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.lex in list(selection_set['IT_TAIL'][1]):
                return True
            else:
                raise SyntaxError(
                    "expecting an element of {ex} but found: {f}".format(ex=str(selection_set['IT_TAIL']), f=self.lex))

    def B(self):
        if self.LA.good_end:
            if self.IT():
                return True
            else:
                raise SyntaxError(
                    "Expected an element from {v} but found: {f}".format(v=str(selection_set["B"]), f=self.lex))
        else:
            raise SyntaxError("Missing {end} at the end of boolean expression".format(end=TOKEN.END.value))
