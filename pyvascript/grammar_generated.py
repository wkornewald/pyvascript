import json
def p(s): print(s)
from pymeta.bootbase import BootBase as GrammarBase
import string
class GeneratedGrammar(GrammarBase):
    globals = globals()
    def rule_grammar(self):
        _locals = {'self': self}
        self.locals['grammar'] = _locals
        def _G_many_1():
            _G_apply_1, lastError = self._apply(self.rule_line, "line", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_2, lastError = self.many(_G_many_1)
        self.considerError(lastError)
        _locals['l'] = _G_many_2
        def _G_many_3():
            _G_apply_1, lastError = self._apply(self.rule_emptyline, "emptyline", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_4, lastError = self.many(_G_many_3)
        self.considerError(lastError)
        _G_apply_5, lastError = self._apply(self.rule_end, "end", [])
        self.considerError(lastError)
        _G_python_6, lastError = eval('l', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_6, self.currentError)


    def rule_hspace(self):
        _locals = {'self': self}
        self.locals['hspace'] = _locals
        def _G_or_1():
            _G_exactly_1, lastError = self.exactly(' ')
            self.considerError(lastError)
            return (_G_exactly_1, self.currentError)
        def _G_or_2():
            _G_exactly_1, lastError = self.exactly('\t')
            self.considerError(lastError)
            return (_G_exactly_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_vspace(self):
        _locals = {'self': self}
        self.locals['vspace'] = _locals
        _G_exactly_1, lastError = self.exactly('\n')
        self.considerError(lastError)
        return (_G_exactly_1, self.currentError)


    def rule_optspace(self):
        _locals = {'self': self}
        self.locals['optspace'] = _locals
        def _G_or_1():
            def _G_pred_1():
                _G_python_1, lastError = eval('self.parenthesis', self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_1, self.currentError)
            _G_pred_2, lastError = self.pred(_G_pred_1)
            self.considerError(lastError)
            def _G_many_3():
                def _G_or_1():
                    _G_apply_1, lastError = self._apply(self.rule_hspace, "hspace", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                def _G_or_2():
                    def _G_optional_1():
                        _G_exactly_1, lastError = self.exactly('\\')
                        self.considerError(lastError)
                        return (_G_exactly_1, self.currentError)
                    def _G_optional_2():
                        return (None, self.input.nullError())
                    _G_or_3, lastError = self._or([_G_optional_1, _G_optional_2])
                    self.considerError(lastError)
                    _G_apply_4, lastError = self._apply(self.rule_vspace, "vspace", [])
                    self.considerError(lastError)
                    return (_G_apply_4, self.currentError)
                def _G_or_3():
                    _G_apply_1, lastError = self._apply(self.rule_comment, "comment", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_or_4, lastError = self._or([_G_or_1, _G_or_2, _G_or_3])
                self.considerError(lastError)
                return (_G_or_4, self.currentError)
            _G_many_4, lastError = self.many(_G_many_3)
            self.considerError(lastError)
            return (_G_many_4, self.currentError)
        def _G_or_2():
            def _G_many_1():
                def _G_or_1():
                    _G_apply_1, lastError = self._apply(self.rule_hspace, "hspace", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                def _G_or_2():
                    _G_exactly_1, lastError = self.exactly('\\')
                    self.considerError(lastError)
                    _G_apply_2, lastError = self._apply(self.rule_vspace, "vspace", [])
                    self.considerError(lastError)
                    return (_G_apply_2, self.currentError)
                _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
                self.considerError(lastError)
                return (_G_or_3, self.currentError)
            _G_many_2, lastError = self.many(_G_many_1)
            self.considerError(lastError)
            def _G_optional_3():
                _G_apply_1, lastError = self._apply(self.rule_comment, "comment", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            def _G_optional_4():
                return (None, self.input.nullError())
            _G_or_5, lastError = self._or([_G_optional_3, _G_optional_4])
            self.considerError(lastError)
            return (_G_or_5, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_mandspace(self):
        _locals = {'self': self}
        self.locals['mandspace'] = _locals
        def _G_or_1():
            def _G_pred_1():
                _G_python_1, lastError = eval('self.parenthesis', self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_1, self.currentError)
            _G_pred_2, lastError = self.pred(_G_pred_1)
            self.considerError(lastError)
            def _G_many1_3():
                def _G_or_1():
                    _G_apply_1, lastError = self._apply(self.rule_hspace, "hspace", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                def _G_or_2():
                    def _G_optional_1():
                        _G_exactly_1, lastError = self.exactly('\\')
                        self.considerError(lastError)
                        return (_G_exactly_1, self.currentError)
                    def _G_optional_2():
                        return (None, self.input.nullError())
                    _G_or_3, lastError = self._or([_G_optional_1, _G_optional_2])
                    self.considerError(lastError)
                    _G_apply_4, lastError = self._apply(self.rule_vspace, "vspace", [])
                    self.considerError(lastError)
                    return (_G_apply_4, self.currentError)
                def _G_or_3():
                    _G_apply_1, lastError = self._apply(self.rule_comment, "comment", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_or_4, lastError = self._or([_G_or_1, _G_or_2, _G_or_3])
                self.considerError(lastError)
                return (_G_or_4, self.currentError)
            _G_many1_4, lastError = self.many(_G_many1_3, _G_many1_3())
            self.considerError(lastError)
            return (_G_many1_4, self.currentError)
        def _G_or_2():
            def _G_many1_1():
                def _G_or_1():
                    _G_apply_1, lastError = self._apply(self.rule_hspace, "hspace", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                def _G_or_2():
                    _G_exactly_1, lastError = self.exactly('\\')
                    self.considerError(lastError)
                    _G_apply_2, lastError = self._apply(self.rule_vspace, "vspace", [])
                    self.considerError(lastError)
                    return (_G_apply_2, self.currentError)
                _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
                self.considerError(lastError)
                return (_G_or_3, self.currentError)
            _G_many1_2, lastError = self.many(_G_many1_1, _G_many1_1())
            self.considerError(lastError)
            def _G_optional_3():
                _G_apply_1, lastError = self._apply(self.rule_comment, "comment", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            def _G_optional_4():
                return (None, self.input.nullError())
            _G_or_5, lastError = self._or([_G_optional_3, _G_optional_4])
            self.considerError(lastError)
            return (_G_or_5, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_indentation(self):
        _locals = {'self': self}
        self.locals['indentation'] = _locals
        def _G_many_1():
            _G_apply_1, lastError = self._apply(self.rule_hspace, "hspace", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_2, lastError = self.many(_G_many_1)
        self.considerError(lastError)
        _locals['i'] = _G_many_2
        def _G_pred_3():
            _G_python_1, lastError = eval('len(i) == self.indent_stack[-1]', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_1, self.currentError)
        _G_pred_4, lastError = self.pred(_G_pred_3)
        self.considerError(lastError)
        return (_G_pred_4, self.currentError)


    def rule_indent(self):
        _locals = {'self': self}
        self.locals['indent'] = _locals
        def _G_many_1():
            _G_apply_1, lastError = self._apply(self.rule_hspace, "hspace", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_2, lastError = self.many(_G_many_1)
        self.considerError(lastError)
        _locals['i'] = _G_many_2
        def _G_pred_3():
            _G_python_1, lastError = eval('len(i) > self.indent_stack[-1]', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_1, self.currentError)
        _G_pred_4, lastError = self.pred(_G_pred_3)
        self.considerError(lastError)
        _G_python_5, lastError = eval('self.indent_stack.append(len(i))', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_dedent(self):
        _locals = {'self': self}
        self.locals['dedent'] = _locals
        _G_python_1, lastError = eval('self.dedent()', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_1, self.currentError)


    def rule_comment(self):
        _locals = {'self': self}
        self.locals['comment'] = _locals
        _G_exactly_1, lastError = self.exactly('#')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_line_rest, "line_rest", [])
        self.considerError(lastError)
        _locals['c'] = _G_apply_2
        _G_python_3, lastError = eval("['comment', c]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_3, self.currentError)


    def rule_emptyline(self):
        _locals = {'self': self}
        self.locals['emptyline'] = _locals
        def _G_many_1():
            _G_apply_1, lastError = self._apply(self.rule_hspace, "hspace", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_2, lastError = self.many(_G_many_1)
        self.considerError(lastError)
        def _G_optional_3():
            def _G_or_1():
                _G_exactly_1, lastError = self.exactly('\\')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            def _G_or_2():
                _G_apply_1, lastError = self._apply(self.rule_comment, "comment", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
            self.considerError(lastError)
            return (_G_or_3, self.currentError)
        def _G_optional_4():
            return (None, self.input.nullError())
        _G_or_5, lastError = self._or([_G_optional_3, _G_optional_4])
        self.considerError(lastError)
        _locals['c'] = _G_or_5
        _G_apply_6, lastError = self._apply(self.rule_vspace, "vspace", [])
        self.considerError(lastError)
        return (_G_apply_6, self.currentError)


    def rule_block(self):
        _locals = {'self': self}
        self.locals['block'] = _locals
        def _G_or_1():
            def _G_many1_1():
                _G_apply_1, lastError = self._apply(self.rule_emptyline, "emptyline", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            _G_many1_2, lastError = self.many(_G_many1_1, _G_many1_1())
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_indent, "indent", [])
            self.considerError(lastError)
            _G_apply_4, lastError = self._apply(self.rule_stmt, "stmt", [])
            self.considerError(lastError)
            _locals['s'] = _G_apply_4
            _G_apply_5, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            def _G_or_6():
                _G_apply_1, lastError = self._apply(self.rule_vspace, "vspace", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            def _G_or_7():
                _G_apply_1, lastError = self._apply(self.rule_end, "end", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            _G_or_8, lastError = self._or([_G_or_6, _G_or_7])
            self.considerError(lastError)
            def _G_many_9():
                _G_apply_1, lastError = self._apply(self.rule_line, "line", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            _G_many_10, lastError = self.many(_G_many_9)
            self.considerError(lastError)
            _locals['l'] = _G_many_10
            _G_apply_11, lastError = self._apply(self.rule_dedent, "dedent", [])
            self.considerError(lastError)
            _G_python_12, lastError = eval('[s] + l', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_12, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_stmt, "stmt", [])
            self.considerError(lastError)
            _locals['s'] = _G_apply_2
            _G_apply_3, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            def _G_lookahead_4():
                def _G_or_1():
                    _G_apply_1, lastError = self._apply(self.rule_vspace, "vspace", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                def _G_or_2():
                    _G_apply_1, lastError = self._apply(self.rule_end, "end", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
                self.considerError(lastError)
                return (_G_or_3, self.currentError)
            _G_lookahead_5, lastError = self.lookahead(_G_lookahead_4)
            self.considerError(lastError)
            _G_python_6, lastError = eval('[s]', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_6, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_line(self):
        _locals = {'self': self}
        self.locals['line'] = _locals
        def _G_many_1():
            _G_apply_1, lastError = self._apply(self.rule_emptyline, "emptyline", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_2, lastError = self.many(_G_many_1)
        self.considerError(lastError)
        _locals['e'] = _G_many_2
        _G_apply_3, lastError = self._apply(self.rule_indentation, "indentation", [])
        self.considerError(lastError)
        _G_apply_4, lastError = self._apply(self.rule_stmt, "stmt", [])
        self.considerError(lastError)
        _locals['s'] = _G_apply_4
        _G_apply_5, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        def _G_or_6():
            _G_apply_1, lastError = self._apply(self.rule_vspace, "vspace", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_7():
            _G_apply_1, lastError = self._apply(self.rule_end, "end", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_8, lastError = self._or([_G_or_6, _G_or_7])
        self.considerError(lastError)
        _G_python_9, lastError = eval('s', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_9, self.currentError)


    def rule_line_rest(self):
        _locals = {'self': self}
        self.locals['line_rest'] = _locals
        def _G_many_1():
            def _G_not_1():
                _G_apply_1, lastError = self._apply(self.rule_vspace, "vspace", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            _G_not_2, lastError = self._not(_G_not_1)
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_anything, "anything", [])
            self.considerError(lastError)
            _locals['x'] = _G_apply_3
            return (_locals['x'], self.currentError)
        _G_many_2, lastError = self.many(_G_many_1)
        self.considerError(lastError)
        _locals['x'] = _G_many_2
        _G_python_3, lastError = eval("''.join(x)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_3, self.currentError)


    def rule_stmt(self):
        _locals = {'self': self}
        self.locals['stmt'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_pass, "pass", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_global, "global", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_3():
            _G_apply_1, lastError = self._apply(self.rule_continue, "continue", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_4():
            _G_apply_1, lastError = self._apply(self.rule_break, "break", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_5():
            _G_apply_1, lastError = self._apply(self.rule_return, "return", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_6():
            _G_apply_1, lastError = self._apply(self.rule_raise, "raise", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_7():
            _G_apply_1, lastError = self._apply(self.rule_while, "while", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_8():
            _G_apply_1, lastError = self._apply(self.rule_del, "del", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_9():
            _G_apply_1, lastError = self._apply(self.rule_if, "if", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_10():
            _G_apply_1, lastError = self._apply(self.rule_def, "def", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_11():
            _G_apply_1, lastError = self._apply(self.rule_for, "for", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_12():
            _G_apply_1, lastError = self._apply(self.rule_try, "try", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_13():
            _G_apply_1, lastError = self._apply(self.rule_augassign, "augassign", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_14():
            _G_apply_1, lastError = self._apply(self.rule_assign, "assign", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_15, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4, _G_or_5, _G_or_6, _G_or_7, _G_or_8, _G_or_9, _G_or_10, _G_or_11, _G_or_12, _G_or_13, _G_or_14])
        self.considerError(lastError)
        return (_G_or_15, self.currentError)


    def rule_global(self):
        _locals = {'self': self}
        self.locals['global'] = _locals
        _G_match_string_1, lastError = self.match_string('global')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_python_3, lastError = eval("'name'", self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_4, lastError = self._apply(self.rule_innercsv, "innercsv", [_G_python_3])
        self.considerError(lastError)
        _locals['names'] = _G_apply_4
        _G_python_5, lastError = eval("['global', names]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_continue(self):
        _locals = {'self': self}
        self.locals['continue'] = _locals
        _G_match_string_1, lastError = self.match_string('continue')
        self.considerError(lastError)
        _G_python_2, lastError = eval("['continue']", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_break(self):
        _locals = {'self': self}
        self.locals['break'] = _locals
        _G_match_string_1, lastError = self.match_string('break')
        self.considerError(lastError)
        _G_python_2, lastError = eval("['break']", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_del(self):
        _locals = {'self': self}
        self.locals['del'] = _locals
        _G_match_string_1, lastError = self.match_string('del')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_get, "get", [])
        self.considerError(lastError)
        _locals['x'] = _G_apply_3
        _G_python_4, lastError = eval("['del', x]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_4, self.currentError)


    def rule_pass(self):
        _locals = {'self': self}
        self.locals['pass'] = _locals
        _G_match_string_1, lastError = self.match_string('pass')
        self.considerError(lastError)
        _G_python_2, lastError = eval("['pass']", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_return(self):
        _locals = {'self': self}
        self.locals['return'] = _locals
        def _G_or_1():
            _G_match_string_1, lastError = self.match_string('return')
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['e'] = _G_apply_3
            _G_python_4, lastError = eval("['return', e]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_4, self.currentError)
        def _G_or_2():
            _G_match_string_1, lastError = self.match_string('return')
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            def _G_lookahead_3():
                def _G_or_1():
                    _G_apply_1, lastError = self._apply(self.rule_vspace, "vspace", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                def _G_or_2():
                    _G_apply_1, lastError = self._apply(self.rule_end, "end", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
                self.considerError(lastError)
                return (_G_or_3, self.currentError)
            _G_lookahead_4, lastError = self.lookahead(_G_lookahead_3)
            self.considerError(lastError)
            _G_python_5, lastError = eval("['return']", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_raise(self):
        _locals = {'self': self}
        self.locals['raise'] = _locals
        _G_match_string_1, lastError = self.match_string('raise')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['e'] = _G_apply_3
        _G_python_4, lastError = eval("['raise', e]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_4, self.currentError)


    def rule_augassign(self):
        _locals = {'self': self}
        self.locals['augassign'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_get, "get", [])
        self.considerError(lastError)
        _locals['l'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        def _G_or_3():
            _G_match_string_1, lastError = self.match_string('+=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_4():
            _G_match_string_1, lastError = self.match_string('-=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_5():
            _G_match_string_1, lastError = self.match_string('*=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_6():
            _G_match_string_1, lastError = self.match_string('/=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_7():
            _G_match_string_1, lastError = self.match_string('//=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_8():
            _G_match_string_1, lastError = self.match_string('%=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_9():
            _G_match_string_1, lastError = self.match_string('^=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_10():
            _G_match_string_1, lastError = self.match_string('&=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_11():
            _G_match_string_1, lastError = self.match_string('|=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_12():
            _G_match_string_1, lastError = self.match_string('~=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_13():
            _G_match_string_1, lastError = self.match_string('<<=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_14():
            _G_match_string_1, lastError = self.match_string('>>=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        _G_or_15, lastError = self._or([_G_or_3, _G_or_4, _G_or_5, _G_or_6, _G_or_7, _G_or_8, _G_or_9, _G_or_10, _G_or_11, _G_or_12, _G_or_13, _G_or_14])
        self.considerError(lastError)
        _locals['op'] = _G_or_15
        _G_apply_16, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_apply_17, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['r'] = _G_apply_17
        _G_python_18, lastError = eval("['augassign', op, l, r]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_18, self.currentError)


    def rule_assign(self):
        _locals = {'self': self}
        self.locals['assign'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_get, "get", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_3, lastError = self.exactly('=')
            self.considerError(lastError)
            _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_apply_5, lastError = self._apply(self.rule_assign, "assign", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_5
            _G_python_6, lastError = eval("['assign', l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_6, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_expr(self):
        _locals = {'self': self}
        self.locals['expr'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_ifexpr, "ifexpr", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_innerifexpr, "innerifexpr", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_innerifexpr(self):
        _locals = {'self': self}
        self.locals['innerifexpr'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_orop, "orop", [])
        self.considerError(lastError)
        return (_G_apply_1, self.currentError)


    def rule_orop(self):
        _locals = {'self': self}
        self.locals['orop'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_orop, "orop", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_match_string_3, lastError = self.match_string('or')
            self.considerError(lastError)
            _locals['op'] = _G_match_string_3
            _G_apply_4, lastError = self._apply(self.rule_andop, "andop", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_4
            _G_python_5, lastError = eval("['binop', op, l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_andop, "andop", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_andop(self):
        _locals = {'self': self}
        self.locals['andop'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_andop, "andop", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_match_string_3, lastError = self.match_string('and')
            self.considerError(lastError)
            _locals['op'] = _G_match_string_3
            _G_apply_4, lastError = self._apply(self.rule_notop, "notop", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_4
            _G_python_5, lastError = eval("['binop', op, l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_notop, "notop", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_notop(self):
        _locals = {'self': self}
        self.locals['notop'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_match_string_2, lastError = self.match_string('not')
            self.considerError(lastError)
            _locals['op'] = _G_match_string_2
            _G_apply_3, lastError = self._apply(self.rule_mandspace, "mandspace", [])
            self.considerError(lastError)
            _G_apply_4, lastError = self._apply(self.rule_notop, "notop", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_4
            _G_python_5, lastError = eval("['unop', op, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_cmpop, "cmpop", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_comparison(self):
        _locals = {'self': self}
        self.locals['comparison'] = _locals
        def _G_or_1():
            def _G_or_1():
                _G_match_string_1, lastError = self.match_string('in')
                self.considerError(lastError)
                _G_python_2, lastError = eval("'in'", self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_2, self.currentError)
            def _G_or_2():
                _G_match_string_1, lastError = self.match_string('not')
                self.considerError(lastError)
                _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
                self.considerError(lastError)
                _G_match_string_3, lastError = self.match_string('in')
                self.considerError(lastError)
                _G_python_4, lastError = eval("'not in'", self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_4, self.currentError)
            def _G_or_3():
                _G_match_string_1, lastError = self.match_string('is')
                self.considerError(lastError)
                _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
                self.considerError(lastError)
                _G_match_string_3, lastError = self.match_string('not')
                self.considerError(lastError)
                _G_python_4, lastError = eval("'is not'", self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_4, self.currentError)
            def _G_or_4():
                _G_match_string_1, lastError = self.match_string('is')
                self.considerError(lastError)
                _G_python_2, lastError = eval("'is'", self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_2, self.currentError)
            _G_or_5, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4])
            self.considerError(lastError)
            _locals['x'] = _G_or_5
            _G_apply_6, lastError = self._apply(self.rule_mandspace, "mandspace", [])
            self.considerError(lastError)
            _G_python_7, lastError = eval('x', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_7, self.currentError)
        def _G_or_2():
            _G_match_string_1, lastError = self.match_string('<=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_3():
            _G_match_string_1, lastError = self.match_string('>=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_4():
            _G_match_string_1, lastError = self.match_string('<')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_5():
            _G_match_string_1, lastError = self.match_string('>')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_6():
            _G_match_string_1, lastError = self.match_string('!=')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        def _G_or_7():
            _G_match_string_1, lastError = self.match_string('==')
            self.considerError(lastError)
            return (_G_match_string_1, self.currentError)
        _G_or_8, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4, _G_or_5, _G_or_6, _G_or_7])
        self.considerError(lastError)
        return (_G_or_8, self.currentError)


    def rule_cmpop(self):
        _locals = {'self': self}
        self.locals['cmpop'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_cmpop, "cmpop", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_comparison, "comparison", [])
            self.considerError(lastError)
            _locals['op'] = _G_apply_3
            _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_apply_5, lastError = self._apply(self.rule_bitor, "bitor", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_5
            _G_python_6, lastError = eval("['binop', op, l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_6, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_bitor, "bitor", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_bitor(self):
        _locals = {'self': self}
        self.locals['bitor'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_bitor, "bitor", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_3, lastError = self.exactly('|')
            self.considerError(lastError)
            _locals['op'] = _G_exactly_3
            _G_apply_4, lastError = self._apply(self.rule_bitxor, "bitxor", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_4
            _G_python_5, lastError = eval("['binop', op, l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_bitxor, "bitxor", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_bitxor(self):
        _locals = {'self': self}
        self.locals['bitxor'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_bitxor, "bitxor", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_3, lastError = self.exactly('^')
            self.considerError(lastError)
            _locals['op'] = _G_exactly_3
            _G_apply_4, lastError = self._apply(self.rule_bitand, "bitand", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_4
            _G_python_5, lastError = eval("['binop', op, l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_bitand, "bitand", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_bitand(self):
        _locals = {'self': self}
        self.locals['bitand'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_bitand, "bitand", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_3, lastError = self.exactly('&')
            self.considerError(lastError)
            _locals['op'] = _G_exactly_3
            _G_apply_4, lastError = self._apply(self.rule_shift, "shift", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_4
            _G_python_5, lastError = eval("['binop', op, l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_shift, "shift", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_shift(self):
        _locals = {'self': self}
        self.locals['shift'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_shift, "shift", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            def _G_or_3():
                _G_match_string_1, lastError = self.match_string('<<')
                self.considerError(lastError)
                return (_G_match_string_1, self.currentError)
            def _G_or_4():
                _G_match_string_1, lastError = self.match_string('>>')
                self.considerError(lastError)
                return (_G_match_string_1, self.currentError)
            _G_or_5, lastError = self._or([_G_or_3, _G_or_4])
            self.considerError(lastError)
            _locals['op'] = _G_or_5
            _G_apply_6, lastError = self._apply(self.rule_addop, "addop", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_6
            _G_python_7, lastError = eval("['binop', op, l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_7, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_addop, "addop", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_addop(self):
        _locals = {'self': self}
        self.locals['addop'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_addop, "addop", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            def _G_or_3():
                _G_exactly_1, lastError = self.exactly('+')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            def _G_or_4():
                _G_exactly_1, lastError = self.exactly('-')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            _G_or_5, lastError = self._or([_G_or_3, _G_or_4])
            self.considerError(lastError)
            _locals['op'] = _G_or_5
            _G_apply_6, lastError = self._apply(self.rule_mulop, "mulop", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_6
            _G_python_7, lastError = eval("['binop', op, l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_7, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_mulop, "mulop", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_mulop(self):
        _locals = {'self': self}
        self.locals['mulop'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_mulop, "mulop", [])
            self.considerError(lastError)
            _locals['l'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            def _G_or_3():
                _G_exactly_1, lastError = self.exactly('*')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            def _G_or_4():
                _G_exactly_1, lastError = self.exactly('/')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            def _G_or_5():
                _G_exactly_1, lastError = self.exactly('//')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            def _G_or_6():
                _G_exactly_1, lastError = self.exactly('%')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            _G_or_7, lastError = self._or([_G_or_3, _G_or_4, _G_or_5, _G_or_6])
            self.considerError(lastError)
            _locals['op'] = _G_or_7
            _G_apply_8, lastError = self._apply(self.rule_unop, "unop", [])
            self.considerError(lastError)
            _locals['r'] = _G_apply_8
            _G_python_9, lastError = eval("['binop', op, l, r]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_9, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_unop, "unop", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_unop(self):
        _locals = {'self': self}
        self.locals['unop'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            def _G_or_2():
                _G_exactly_1, lastError = self.exactly('-')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            def _G_or_3():
                _G_exactly_1, lastError = self.exactly('+')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            def _G_or_4():
                _G_exactly_1, lastError = self.exactly('~')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            _G_or_5, lastError = self._or([_G_or_2, _G_or_3, _G_or_4])
            self.considerError(lastError)
            _locals['op'] = _G_or_5
            _G_apply_6, lastError = self._apply(self.rule_unop, "unop", [])
            self.considerError(lastError)
            _locals['e'] = _G_apply_6
            _G_python_7, lastError = eval("['unop', op, e]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_7, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_callable, "callable", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_callable(self):
        _locals = {'self': self}
        self.locals['callable'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_lambda, "lambda", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_3():
            _G_apply_1, lastError = self._apply(self.rule_deflambda, "deflambda", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_4():
            _G_apply_1, lastError = self._apply(self.rule_get, "get", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_5, lastError = self._or([_G_or_2, _G_or_3, _G_or_4])
        self.considerError(lastError)
        return (_G_or_5, self.currentError)


    def rule_slice(self):
        _locals = {'self': self}
        self.locals['slice'] = _locals
        def _G_or_1():
            def _G_optional_1():
                _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            def _G_optional_2():
                return (None, self.input.nullError())
            _G_or_3, lastError = self._or([_G_optional_1, _G_optional_2])
            self.considerError(lastError)
            _locals['start'] = _G_or_3
            _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_5, lastError = self.exactly(':')
            self.considerError(lastError)
            _G_apply_6, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            def _G_optional_7():
                _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            def _G_optional_8():
                return (None, self.input.nullError())
            _G_or_9, lastError = self._or([_G_optional_7, _G_optional_8])
            self.considerError(lastError)
            _locals['end'] = _G_or_9
            _G_python_10, lastError = eval("['slice', start, end]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_10, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['e'] = _G_apply_1
            _G_python_2, lastError = eval('e', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_2, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_get(self):
        _locals = {'self': self}
        self.locals['get'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_get, "get", [])
            self.considerError(lastError)
            _locals['obj'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_3, lastError = self.exactly('.')
            self.considerError(lastError)
            _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_apply_5, lastError = self._apply(self.rule_name, "name", [])
            self.considerError(lastError)
            _locals['n'] = _G_apply_5
            _G_python_6, lastError = eval("['getattr', obj, n]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_6, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_get, "get", [])
            self.considerError(lastError)
            _locals['obj'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_3, lastError = self.exactly('[')
            self.considerError(lastError)
            _G_python_4, lastError = eval('self.enter_paren()', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_5, lastError = self._apply(self.rule_slice, "slice", [])
            self.considerError(lastError)
            _locals['s'] = _G_apply_5
            _G_python_6, lastError = eval('self.leave_paren()', self.globals, _locals), None
            self.considerError(lastError)
            _G_exactly_7, lastError = self.exactly(']')
            self.considerError(lastError)
            _G_python_8, lastError = eval("['getitem', obj, s]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_8, self.currentError)
        def _G_or_3():
            _G_apply_1, lastError = self._apply(self.rule_get, "get", [])
            self.considerError(lastError)
            _locals['obj'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_3, lastError = self.exactly('(')
            self.considerError(lastError)
            _G_python_4, lastError = eval("'expr'", self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_5, lastError = self._apply(self.rule_csv, "csv", [_G_python_4])
            self.considerError(lastError)
            _locals['params'] = _G_apply_5
            _G_exactly_6, lastError = self.exactly(')')
            self.considerError(lastError)
            _G_python_7, lastError = eval("['call', obj, params]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_7, self.currentError)
        def _G_or_4():
            _G_apply_1, lastError = self._apply(self.rule_immediate, "immediate", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_5, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4])
        self.considerError(lastError)
        return (_G_or_5, self.currentError)


    def rule_immediate(self):
        _locals = {'self': self}
        self.locals['immediate'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_number, "number", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_string, "string", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_3():
            _G_apply_1, lastError = self._apply(self.rule_list, "list", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_4():
            _G_apply_1, lastError = self._apply(self.rule_tuple, "tuple", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_5():
            _G_apply_1, lastError = self._apply(self.rule_dict, "dict", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_6():
            _G_apply_1, lastError = self._apply(self.rule_set, "set", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_7():
            _G_apply_1, lastError = self._apply(self.rule_name, "name", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_8():
            _G_exactly_1, lastError = self.exactly('(')
            self.considerError(lastError)
            _G_python_2, lastError = eval('self.enter_paren()', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['ix'] = _G_apply_3
            _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_5, lastError = self.exactly(')')
            self.considerError(lastError)
            _G_python_6, lastError = eval('self.leave_paren()', self.globals, _locals), None
            self.considerError(lastError)
            _G_python_7, lastError = eval('ix', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_7, self.currentError)
        _G_or_9, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4, _G_or_5, _G_or_6, _G_or_7, _G_or_8])
        self.considerError(lastError)
        return (_G_or_9, self.currentError)


    def rule_name_start(self):
        _locals = {'self': self}
        self.locals['name_start'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_letter, "letter", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_2():
            _G_exactly_1, lastError = self.exactly('$')
            self.considerError(lastError)
            return (_G_exactly_1, self.currentError)
        def _G_or_3():
            _G_exactly_1, lastError = self.exactly('_')
            self.considerError(lastError)
            return (_G_exactly_1, self.currentError)
        _G_or_4, lastError = self._or([_G_or_1, _G_or_2, _G_or_3])
        self.considerError(lastError)
        return (_G_or_4, self.currentError)


    def rule_name_rest(self):
        _locals = {'self': self}
        self.locals['name_rest'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_name_start, "name_start", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_digit, "digit", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_iname(self):
        _locals = {'self': self}
        self.locals['iname'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_name_start, "name_start", [])
        self.considerError(lastError)
        _locals['s'] = _G_apply_1
        def _G_many_2():
            _G_apply_1, lastError = self._apply(self.rule_name_rest, "name_rest", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_3, lastError = self.many(_G_many_2)
        self.considerError(lastError)
        _locals['r'] = _G_many_3
        _G_python_4, lastError = eval("s + ''.join(r)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_4, self.currentError)


    def rule_iskeyword(self):
        _locals = {'self': self}
        self.locals['iskeyword'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['x'] = _G_apply_1
        def _G_pred_2():
            _G_python_1, lastError = eval('self.is_keyword(x)', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_1, self.currentError)
        _G_pred_3, lastError = self.pred(_G_pred_2)
        self.considerError(lastError)
        return (_G_pred_3, self.currentError)


    def rule_name(self):
        _locals = {'self': self}
        self.locals['name'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_iname, "iname", [])
        self.considerError(lastError)
        _locals['n'] = _G_apply_1
        def _G_not_2():
            _G_python_1, lastError = eval('n', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_iskeyword, "iskeyword", [_G_python_1])
            self.considerError(lastError)
            return (_G_apply_2, self.currentError)
        _G_not_3, lastError = self._not(_G_not_2)
        self.considerError(lastError)
        _G_python_4, lastError = eval("['name', n]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_4, self.currentError)


    def rule_escaped_char(self):
        _locals = {'self': self}
        self.locals['escaped_char'] = _locals
        _G_exactly_1, lastError = self.exactly('\\')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['x'] = _G_apply_2
        _G_python_3, lastError = eval("('\\\\' + x).decode('string_escape')", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_3, self.currentError)


    def rule_string3(self):
        _locals = {'self': self}
        self.locals['string3'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['e'] = _G_apply_1
        _G_python_2, lastError = eval('e', self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_match_string, "match_string", [_G_python_2])
        self.considerError(lastError)
        def _G_many_4():
            def _G_or_1():
                _G_apply_1, lastError = self._apply(self.rule_escaped_char, "escaped_char", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            def _G_or_2():
                def _G_not_1():
                    def _G_or_1():
                        def _G_pred_1():
                            _G_python_1, lastError = eval('len(e) != 3', self.globals, _locals), None
                            self.considerError(lastError)
                            return (_G_python_1, self.currentError)
                        _G_pred_2, lastError = self.pred(_G_pred_1)
                        self.considerError(lastError)
                        _G_apply_3, lastError = self._apply(self.rule_vspace, "vspace", [])
                        self.considerError(lastError)
                        return (_G_apply_3, self.currentError)
                    def _G_or_2():
                        _G_python_1, lastError = eval('e', self.globals, _locals), None
                        self.considerError(lastError)
                        _G_apply_2, lastError = self._apply(self.rule_match_string, "match_string", [_G_python_1])
                        self.considerError(lastError)
                        return (_G_apply_2, self.currentError)
                    _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
                    self.considerError(lastError)
                    return (_G_or_3, self.currentError)
                _G_not_2, lastError = self._not(_G_not_1)
                self.considerError(lastError)
                _G_apply_3, lastError = self._apply(self.rule_anything, "anything", [])
                self.considerError(lastError)
                return (_G_apply_3, self.currentError)
            _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
            self.considerError(lastError)
            return (_G_or_3, self.currentError)
        _G_many_5, lastError = self.many(_G_many_4)
        self.considerError(lastError)
        _locals['c'] = _G_many_5
        _G_python_6, lastError = eval('e', self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_7, lastError = self._apply(self.rule_match_string, "match_string", [_G_python_6])
        self.considerError(lastError)
        _G_python_8, lastError = eval("''.join(c)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_8, self.currentError)


    def rule_string2(self):
        _locals = {'self': self}
        self.locals['string2'] = _locals
        def _G_or_1():
            _G_python_1, lastError = eval('\'"""\'', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_string3, "string3", [_G_python_1])
            self.considerError(lastError)
            return (_G_apply_2, self.currentError)
        def _G_or_2():
            _G_python_1, lastError = eval('"\'\'\'"', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_string3, "string3", [_G_python_1])
            self.considerError(lastError)
            return (_G_apply_2, self.currentError)
        def _G_or_3():
            _G_python_1, lastError = eval('\'"\'', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_string3, "string3", [_G_python_1])
            self.considerError(lastError)
            return (_G_apply_2, self.currentError)
        def _G_or_4():
            _G_python_1, lastError = eval('"\'"', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_string3, "string3", [_G_python_1])
            self.considerError(lastError)
            return (_G_apply_2, self.currentError)
        _G_or_5, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4])
        self.considerError(lastError)
        return (_G_or_5, self.currentError)


    def rule_string(self):
        _locals = {'self': self}
        self.locals['string'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_string2, "string2", [])
        self.considerError(lastError)
        _locals['s'] = _G_apply_1
        def _G_many_2():
            _G_apply_1, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_string2, "string2", [])
            self.considerError(lastError)
            return (_G_apply_2, self.currentError)
        _G_many_3, lastError = self.many(_G_many_2)
        self.considerError(lastError)
        _locals['es'] = _G_many_3
        _G_python_4, lastError = eval("['string', s + ''.join(es)]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_4, self.currentError)


    def rule_hexdigit(self):
        _locals = {'self': self}
        self.locals['hexdigit'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_letterOrDigit, "letterOrDigit", [])
        self.considerError(lastError)
        _locals['x'] = _G_apply_1
        _G_python_2, lastError = eval('self.hex_digits.find(x.lower())', self.globals, _locals), None
        self.considerError(lastError)
        _locals['v'] = _G_python_2
        def _G_pred_3():
            _G_python_1, lastError = eval('v >= 0', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_1, self.currentError)
        _G_pred_4, lastError = self.pred(_G_pred_3)
        self.considerError(lastError)
        _G_python_5, lastError = eval('v', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_hexlit(self):
        _locals = {'self': self}
        self.locals['hexlit'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_hexlit, "hexlit", [])
            self.considerError(lastError)
            _locals['n'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_hexdigit, "hexdigit", [])
            self.considerError(lastError)
            _locals['d'] = _G_apply_2
            _G_python_3, lastError = eval('(n * 16 + d)', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_hexdigit, "hexdigit", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_number(self):
        _locals = {'self': self}
        self.locals['number'] = _locals
        def _G_or_1():
            _G_match_string_1, lastError = self.match_string('0x')
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_hexlit, "hexlit", [])
            self.considerError(lastError)
            _locals['n'] = _G_apply_2
            _G_python_3, lastError = eval("['hexnumber', n]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        def _G_or_2():
            def _G_many1_1():
                _G_apply_1, lastError = self._apply(self.rule_digit, "digit", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            _G_many1_2, lastError = self.many(_G_many1_1, _G_many1_1())
            self.considerError(lastError)
            _locals['ws'] = _G_many1_2
            def _G_or_3():
                _G_exactly_1, lastError = self.exactly('.')
                self.considerError(lastError)
                def _G_many1_2():
                    _G_apply_1, lastError = self._apply(self.rule_digit, "digit", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_many1_3, lastError = self.many(_G_many1_2, _G_many1_2())
                self.considerError(lastError)
                _locals['fs'] = _G_many1_3
                _G_python_4, lastError = eval("['number', float('%s.%s' % (''.join(ws), ''.join(fs)))]", self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_4, self.currentError)
            def _G_or_4():
                _G_python_1, lastError = eval("['number', int(''.join(ws))]", self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_1, self.currentError)
            _G_or_5, lastError = self._or([_G_or_3, _G_or_4])
            self.considerError(lastError)
            return (_G_or_5, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_innercsv(self):
        _locals = {'self': self}
        self.locals['innercsv'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['rule'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        def _G_many_3():
            _G_python_1, lastError = eval('rule', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_apply, "apply", [_G_python_1])
            self.considerError(lastError)
            _locals['e'] = _G_apply_2
            _G_apply_3, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_4, lastError = self.exactly(',')
            self.considerError(lastError)
            _G_apply_5, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_python_6, lastError = eval('e', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_6, self.currentError)
        _G_many_4, lastError = self.many(_G_many_3)
        self.considerError(lastError)
        _locals['es'] = _G_many_4
        def _G_optional_5():
            def _G_pred_1():
                _G_python_1, lastError = eval("rule != 'tupleexpr' or len(es)", self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_1, self.currentError)
            _G_pred_2, lastError = self.pred(_G_pred_1)
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_python_4, lastError = eval('rule', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_5, lastError = self._apply(self.rule_apply, "apply", [_G_python_4])
            self.considerError(lastError)
            _locals['l'] = _G_apply_5
            _G_python_6, lastError = eval('es.append(l)', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_6, self.currentError)
        def _G_optional_6():
            return (None, self.input.nullError())
        _G_or_7, lastError = self._or([_G_optional_5, _G_optional_6])
        self.considerError(lastError)
        _G_apply_8, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_python_9, lastError = eval('es', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_9, self.currentError)


    def rule_csv(self):
        _locals = {'self': self}
        self.locals['csv'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['rule'] = _G_apply_1
        _G_python_2, lastError = eval('self.enter_paren()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_3, lastError = eval('rule', self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_4, lastError = self._apply(self.rule_innercsv, "innercsv", [_G_python_3])
        self.considerError(lastError)
        _locals['es'] = _G_apply_4
        _G_python_5, lastError = eval('self.leave_paren()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_6, lastError = eval('es', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_6, self.currentError)


    def rule_list(self):
        _locals = {'self': self}
        self.locals['list'] = _locals
        _G_exactly_1, lastError = self.exactly('[')
        self.considerError(lastError)
        _G_python_2, lastError = eval("'expr'", self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_csv, "csv", [_G_python_2])
        self.considerError(lastError)
        _locals['v'] = _G_apply_3
        _G_exactly_4, lastError = self.exactly(']')
        self.considerError(lastError)
        _G_python_5, lastError = eval("['list'] + v", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_tuple(self):
        _locals = {'self': self}
        self.locals['tuple'] = _locals
        _G_exactly_1, lastError = self.exactly('(')
        self.considerError(lastError)
        _G_python_2, lastError = eval("'tupleexpr'", self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_csv, "csv", [_G_python_2])
        self.considerError(lastError)
        _locals['v'] = _G_apply_3
        _G_exactly_4, lastError = self.exactly(')')
        self.considerError(lastError)
        _G_python_5, lastError = eval("['tuple'] + v", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_dict(self):
        _locals = {'self': self}
        self.locals['dict'] = _locals
        _G_exactly_1, lastError = self.exactly('{')
        self.considerError(lastError)
        _G_python_2, lastError = eval("'dictexpr'", self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_csv, "csv", [_G_python_2])
        self.considerError(lastError)
        _locals['v'] = _G_apply_3
        _G_exactly_4, lastError = self.exactly('}')
        self.considerError(lastError)
        _G_python_5, lastError = eval("['dict'] + v", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_set(self):
        _locals = {'self': self}
        self.locals['set'] = _locals
        _G_exactly_1, lastError = self.exactly('{')
        self.considerError(lastError)
        _G_python_2, lastError = eval("'expr'", self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_csv, "csv", [_G_python_2])
        self.considerError(lastError)
        _locals['v'] = _G_apply_3
        _G_exactly_4, lastError = self.exactly('}')
        self.considerError(lastError)
        _G_python_5, lastError = eval("['set'] + v", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_tupleexpr(self):
        _locals = {'self': self}
        self.locals['tupleexpr'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        return (_G_apply_1, self.currentError)


    def rule_dictexpr(self):
        _locals = {'self': self}
        self.locals['dictexpr'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_string, "string", [])
        self.considerError(lastError)
        _locals['k'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_3, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_apply_5, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['v'] = _G_apply_5
        _G_python_6, lastError = eval("['dictkv', k, v]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_6, self.currentError)


    def rule_ifexpr(self):
        _locals = {'self': self}
        self.locals['ifexpr'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_innerifexpr, "innerifexpr", [])
        self.considerError(lastError)
        _locals['t'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_match_string_3, lastError = self.match_string('if')
        self.considerError(lastError)
        _G_apply_4, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_5, lastError = self._apply(self.rule_innerifexpr, "innerifexpr", [])
        self.considerError(lastError)
        _locals['cond'] = _G_apply_5
        _G_apply_6, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_match_string_7, lastError = self.match_string('else')
        self.considerError(lastError)
        _G_apply_8, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_9, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['f'] = _G_apply_9
        _G_python_10, lastError = eval("['ifexpr', cond, t, f]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_10, self.currentError)


    def rule_if(self):
        _locals = {'self': self}
        self.locals['if'] = _locals
        _G_match_string_1, lastError = self.match_string('if')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['cond'] = _G_apply_3
        _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_5, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_6, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_6
        def _G_many_7():
            _G_apply_1, lastError = self._apply(self.rule_elif, "elif", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_8, lastError = self.many(_G_many_7)
        self.considerError(lastError)
        _locals['ei'] = _G_many_8
        def _G_optional_9():
            _G_apply_1, lastError = self._apply(self.rule_else, "else", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_optional_10():
            return (None, self.input.nullError())
        _G_or_11, lastError = self._or([_G_optional_9, _G_optional_10])
        self.considerError(lastError)
        _locals['e'] = _G_or_11
        _G_python_12, lastError = eval("['if', [cond, body]] + [ei] + ([e] if e else [])", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_12, self.currentError)


    def rule_elif(self):
        _locals = {'self': self}
        self.locals['elif'] = _locals
        def _G_many_1():
            _G_apply_1, lastError = self._apply(self.rule_emptyline, "emptyline", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_2, lastError = self.many(_G_many_1)
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_indentation, "indentation", [])
        self.considerError(lastError)
        _G_match_string_4, lastError = self.match_string('elif')
        self.considerError(lastError)
        _G_apply_5, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_6, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['cond'] = _G_apply_6
        _G_apply_7, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_8, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_9, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_9
        _G_python_10, lastError = eval('[cond, body]', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_10, self.currentError)


    def rule_else(self):
        _locals = {'self': self}
        self.locals['else'] = _locals
        def _G_many_1():
            _G_apply_1, lastError = self._apply(self.rule_emptyline, "emptyline", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_2, lastError = self.many(_G_many_1)
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_indentation, "indentation", [])
        self.considerError(lastError)
        _G_match_string_4, lastError = self.match_string('else')
        self.considerError(lastError)
        _G_apply_5, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_6, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_7, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_7
        _G_python_8, lastError = eval('body', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_8, self.currentError)


    def rule_while(self):
        _locals = {'self': self}
        self.locals['while'] = _locals
        _G_match_string_1, lastError = self.match_string('while')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['cond'] = _G_apply_3
        _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_5, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_6, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_6
        _G_python_7, lastError = eval("['while', cond, body]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_7, self.currentError)


    def rule_for(self):
        _locals = {'self': self}
        self.locals['for'] = _locals
        _G_match_string_1, lastError = self.match_string('for')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_name, "name", [])
        self.considerError(lastError)
        _locals['var'] = _G_apply_3
        _G_apply_4, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_match_string_5, lastError = self.match_string('in')
        self.considerError(lastError)
        _G_apply_6, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_7, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['data'] = _G_apply_7
        _G_apply_8, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_9, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_10, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_10
        _G_python_11, lastError = eval("['for', var, data, body]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_11, self.currentError)


    def rule_arg(self):
        _locals = {'self': self}
        self.locals['arg'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_name, "name", [])
            self.considerError(lastError)
            _locals['var'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_3, lastError = self.exactly('=')
            self.considerError(lastError)
            _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_apply_5, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['default'] = _G_apply_5
            _G_python_6, lastError = eval("['defaultarg', var, default]", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_6, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_name, "name", [])
            self.considerError(lastError)
            _locals['var'] = _G_apply_1
            _G_python_2, lastError = eval('var', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_2, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_argsstart(self):
        _locals = {'self': self}
        self.locals['argsstart'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_arg, "arg", [])
        self.considerError(lastError)
        _locals['a'] = _G_apply_2
        _G_apply_3, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_4, lastError = self.exactly(',')
        self.considerError(lastError)
        _G_python_5, lastError = eval('a', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_funcargs(self):
        _locals = {'self': self}
        self.locals['funcargs'] = _locals
        def _G_or_1():
            _G_exactly_1, lastError = self.exactly('*')
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_name, "name", [])
            self.considerError(lastError)
            _locals['stararg'] = _G_apply_2
            _G_python_3, lastError = eval('[[], stararg[1]]', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        def _G_or_2():
            _G_python_1, lastError = eval('self.enter_paren()', self.globals, _locals), None
            self.considerError(lastError)
            def _G_or_2():
                def _G_many1_1():
                    _G_apply_1, lastError = self._apply(self.rule_argsstart, "argsstart", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_many1_2, lastError = self.many(_G_many1_1, _G_many1_1())
                self.considerError(lastError)
                _locals['a'] = _G_many1_2
                _G_python_3, lastError = eval('a', self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_3, self.currentError)
            def _G_or_3():
                _G_python_1, lastError = eval('self.leave_paren()', self.globals, _locals), None
                self.considerError(lastError)
                def _G_pred_2():
                    _G_python_1, lastError = eval('False', self.globals, _locals), None
                    self.considerError(lastError)
                    return (_G_python_1, self.currentError)
                _G_pred_3, lastError = self.pred(_G_pred_2)
                self.considerError(lastError)
                return (_G_pred_3, self.currentError)
            _G_or_4, lastError = self._or([_G_or_2, _G_or_3])
            self.considerError(lastError)
            _locals['args'] = _G_or_4
            _G_python_5, lastError = eval('self.leave_paren()', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_6, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_7, lastError = self.exactly('*')
            self.considerError(lastError)
            _G_apply_8, lastError = self._apply(self.rule_name, "name", [])
            self.considerError(lastError)
            _locals['stararg'] = _G_apply_8
            _G_python_9, lastError = eval('[args, stararg[1]]', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_9, self.currentError)
        def _G_or_3():
            _G_python_1, lastError = eval("'arg'", self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_csv, "csv", [_G_python_1])
            self.considerError(lastError)
            _locals['args'] = _G_apply_2
            _G_python_3, lastError = eval('[args, None]', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        _G_or_4, lastError = self._or([_G_or_1, _G_or_2, _G_or_3])
        self.considerError(lastError)
        return (_G_or_4, self.currentError)


    def rule_def(self):
        _locals = {'self': self}
        self.locals['def'] = _locals
        _G_match_string_1, lastError = self.match_string('def')
        self.considerError(lastError)
        _G_python_2, lastError = eval('self.get_indent()', self.globals, _locals), None
        self.considerError(lastError)
        _locals['i'] = _G_python_2
        _G_apply_3, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_python_4, lastError = eval('self.indent_stack.append(i)', self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_5, lastError = self._apply(self.rule_name, "name", [])
        self.considerError(lastError)
        _locals['name'] = _G_apply_5
        _G_apply_6, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_7, lastError = self.exactly('(')
        self.considerError(lastError)
        _G_apply_8, lastError = self._apply(self.rule_funcargs, "funcargs", [])
        self.considerError(lastError)
        _locals['args'] = _G_apply_8
        _G_exactly_9, lastError = self.exactly(')')
        self.considerError(lastError)
        _G_apply_10, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_11, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_12, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_12
        _G_python_13, lastError = eval('self.indent_stack.pop()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_14, lastError = eval("['func', name, args, body]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_14, self.currentError)


    def rule_deflambda(self):
        _locals = {'self': self}
        self.locals['deflambda'] = _locals
        _G_match_string_1, lastError = self.match_string('def')
        self.considerError(lastError)
        _G_python_2, lastError = eval('self.get_indent()', self.globals, _locals), None
        self.considerError(lastError)
        _locals['i'] = _G_python_2
        def _G_lookahead_3():
            def _G_or_1():
                _G_apply_1, lastError = self._apply(self.rule_hspace, "hspace", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            def _G_or_2():
                _G_exactly_1, lastError = self.exactly('(')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
            self.considerError(lastError)
            return (_G_or_3, self.currentError)
        _G_lookahead_4, lastError = self.lookahead(_G_lookahead_3)
        self.considerError(lastError)
        _G_python_5, lastError = eval('self.enter_deflambda(i)', self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_6, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_7, lastError = self.exactly('(')
        self.considerError(lastError)
        _G_apply_8, lastError = self._apply(self.rule_funcargs, "funcargs", [])
        self.considerError(lastError)
        _locals['args'] = _G_apply_8
        _G_exactly_9, lastError = self.exactly(')')
        self.considerError(lastError)
        _G_apply_10, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_11, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_12, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_12
        _G_python_13, lastError = eval('self.leave_deflambda()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_14, lastError = eval("['func', None, args, body]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_14, self.currentError)


    def rule_lambda(self):
        _locals = {'self': self}
        self.locals['lambda'] = _locals
        _G_match_string_1, lastError = self.match_string('lambda')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_3, lastError = self._apply(self.rule_funcargs, "funcargs", [])
        self.considerError(lastError)
        _locals['args'] = _G_apply_3
        _G_apply_4, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_5, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_6, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['e'] = _G_apply_6
        _G_python_7, lastError = eval("['func', None, args, [e]]", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_7, self.currentError)


    def rule_try(self):
        _locals = {'self': self}
        self.locals['try'] = _locals
        _G_match_string_1, lastError = self.match_string('try')
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_3, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_4, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_4
        def _G_many_5():
            _G_apply_1, lastError = self._apply(self.rule_emptyline, "emptyline", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_6, lastError = self.many(_G_many_5)
        self.considerError(lastError)
        _G_apply_7, lastError = self._apply(self.rule_indentation, "indentation", [])
        self.considerError(lastError)
        _G_match_string_8, lastError = self.match_string('except')
        self.considerError(lastError)
        _G_apply_9, lastError = self._apply(self.rule_mandspace, "mandspace", [])
        self.considerError(lastError)
        _G_apply_10, lastError = self._apply(self.rule_name, "name", [])
        self.considerError(lastError)
        _locals['err'] = _G_apply_10
        _G_apply_11, lastError = self._apply(self.rule_optspace, "optspace", [])
        self.considerError(lastError)
        _G_exactly_12, lastError = self.exactly(':')
        self.considerError(lastError)
        _G_apply_13, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['errbody'] = _G_apply_13
        def _G_optional_14():
            def _G_many_1():
                _G_apply_1, lastError = self._apply(self.rule_emptyline, "emptyline", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            _G_many_2, lastError = self.many(_G_many_1)
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_indentation, "indentation", [])
            self.considerError(lastError)
            _G_match_string_4, lastError = self.match_string('finally')
            self.considerError(lastError)
            _G_apply_5, lastError = self._apply(self.rule_optspace, "optspace", [])
            self.considerError(lastError)
            _G_exactly_6, lastError = self.exactly(':')
            self.considerError(lastError)
            _G_apply_7, lastError = self._apply(self.rule_block, "block", [])
            self.considerError(lastError)
            return (_G_apply_7, self.currentError)
        def _G_optional_15():
            return (None, self.input.nullError())
        _G_or_16, lastError = self._or([_G_optional_14, _G_optional_15])
        self.considerError(lastError)
        _locals['finbody'] = _G_or_16
        _G_python_17, lastError = eval("['try', body, err, errbody] + ([finbody] if finbody else [])", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_17, self.currentError)
