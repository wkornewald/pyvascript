import json
def p(s): print(s)
from pymeta.bootbase import BootBase as GrammarBase
import string
class GeneratedTranslator(GrammarBase):
    globals = globals()
    def rule_grammar(self):
        _locals = {'self': self}
        self.locals['grammar'] = _locals
        def _G_many_1():
            _G_apply_1, lastError = self._apply(self.rule_stmt, "stmt", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_2, lastError = self.many(_G_many_1)
        self.considerError(lastError)
        _locals['s'] = _G_many_2
        _G_python_3, lastError = eval("'%s\\n' % '\\n'.join(s)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_3, self.currentError)


    def rule_block(self):
        _locals = {'self': self}
        self.locals['block'] = _locals
        def _G_lookahead_1():
            def _G_listpattern_1():
                def _G_many_1():
                    _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_many_2, lastError = self.many(_G_many_1)
                self.considerError(lastError)
                return (_G_many_2, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            return (_G_listpattern_2, self.currentError)
        _G_lookahead_2, lastError = self.lookahead(_G_lookahead_1)
        self.considerError(lastError)
        _G_python_3, lastError = eval('self.indent()', self.globals, _locals), None
        self.considerError(lastError)
        _locals['i'] = _G_python_3
        def _G_listpattern_4():
            def _G_many_1():
                _G_apply_1, lastError = self._apply(self.rule_stmt, "stmt", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            _G_many_2, lastError = self.many(_G_many_1)
            self.considerError(lastError)
            _locals['s'] = _G_many_2
            return (_locals['s'], self.currentError)
        _G_listpattern_5, lastError = self.listpattern(_G_listpattern_4)
        self.considerError(lastError)
        _G_python_6, lastError = eval('self.dedent()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_7, lastError = eval('self.make_block(s, i)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_7, self.currentError)


    def rule_funcblock(self):
        _locals = {'self': self}
        self.locals['funcblock'] = _locals
        def _G_lookahead_1():
            def _G_listpattern_1():
                def _G_many_1():
                    _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_many_2, lastError = self.many(_G_many_1)
                self.considerError(lastError)
                return (_G_many_2, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            return (_G_listpattern_2, self.currentError)
        _G_lookahead_2, lastError = self.lookahead(_G_lookahead_1)
        self.considerError(lastError)
        _G_python_3, lastError = eval('self.indent()', self.globals, _locals), None
        self.considerError(lastError)
        _locals['i'] = _G_python_3
        def _G_listpattern_4():
            def _G_many_1():
                _G_apply_1, lastError = self._apply(self.rule_stmt, "stmt", [])
                self.considerError(lastError)
                return (_G_apply_1, self.currentError)
            _G_many_2, lastError = self.many(_G_many_1)
            self.considerError(lastError)
            _locals['s'] = _G_many_2
            return (_locals['s'], self.currentError)
        _G_listpattern_5, lastError = self.listpattern(_G_listpattern_4)
        self.considerError(lastError)
        _G_python_6, lastError = eval('self.dedent()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_7, lastError = eval('self.make_func_block(s, i)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_7, self.currentError)


    def rule_stmt(self):
        _locals = {'self': self}
        self.locals['stmt'] = _locals
        def _G_or_1():
            def _G_or_1():
                def _G_listpattern_1():
                    _G_exactly_1, lastError = self.exactly('while')
                    self.considerError(lastError)
                    _G_apply_2, lastError = self._apply(self.rule_while, "while", [])
                    self.considerError(lastError)
                    _locals['e'] = _G_apply_2
                    return (_locals['e'], self.currentError)
                _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                self.considerError(lastError)
                return (_G_listpattern_2, self.currentError)
            def _G_or_2():
                def _G_listpattern_1():
                    _G_exactly_1, lastError = self.exactly('if')
                    self.considerError(lastError)
                    _G_apply_2, lastError = self._apply(self.rule_if, "if", [])
                    self.considerError(lastError)
                    _locals['e'] = _G_apply_2
                    return (_locals['e'], self.currentError)
                _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                self.considerError(lastError)
                return (_G_listpattern_2, self.currentError)
            def _G_or_3():
                def _G_listpattern_1():
                    _G_exactly_1, lastError = self.exactly('for')
                    self.considerError(lastError)
                    _G_apply_2, lastError = self._apply(self.rule_for, "for", [])
                    self.considerError(lastError)
                    _locals['e'] = _G_apply_2
                    return (_locals['e'], self.currentError)
                _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                self.considerError(lastError)
                return (_G_listpattern_2, self.currentError)
            def _G_or_4():
                def _G_listpattern_1():
                    _G_exactly_1, lastError = self.exactly('try')
                    self.considerError(lastError)
                    _G_apply_2, lastError = self._apply(self.rule_try, "try", [])
                    self.considerError(lastError)
                    _locals['e'] = _G_apply_2
                    return (_locals['e'], self.currentError)
                _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                self.considerError(lastError)
                return (_G_listpattern_2, self.currentError)
            def _G_or_5():
                def _G_listpattern_1():
                    _G_exactly_1, lastError = self.exactly('func')
                    self.considerError(lastError)
                    _G_apply_2, lastError = self._apply(self.rule_funcstmt, "funcstmt", [])
                    self.considerError(lastError)
                    _locals['e'] = _G_apply_2
                    return (_locals['e'], self.currentError)
                _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                self.considerError(lastError)
                return (_G_listpattern_2, self.currentError)
            _G_or_6, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4, _G_or_5])
            self.considerError(lastError)
            _G_python_7, lastError = eval("'%s\\n' % e", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_7, self.currentError)
        def _G_or_2():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('global')
                self.considerError(lastError)
                def _G_listpattern_2():
                    def _G_many_1():
                        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                        self.considerError(lastError)
                        return (_G_apply_1, self.currentError)
                    _G_many_2, lastError = self.many(_G_many_1)
                    self.considerError(lastError)
                    _locals['names'] = _G_many_2
                    return (_locals['names'], self.currentError)
                _G_listpattern_3, lastError = self.listpattern(_G_listpattern_2)
                self.considerError(lastError)
                return (_G_listpattern_3, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            _G_python_3, lastError = eval('self.register_globals(names)', self.globals, _locals), None
            self.considerError(lastError)
            _G_python_4, lastError = eval("''", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_4, self.currentError)
        def _G_or_3():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('pass')
                self.considerError(lastError)
                return (_G_exactly_1, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            _G_python_3, lastError = eval("''", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        def _G_or_4():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('call')
                self.considerError(lastError)
                def _G_lookahead_2():
                    def _G_listpattern_1():
                        _G_exactly_1, lastError = self.exactly('name')
                        self.considerError(lastError)
                        _G_exactly_2, lastError = self.exactly('JS')
                        self.considerError(lastError)
                        return (_G_exactly_2, self.currentError)
                    _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                    self.considerError(lastError)
                    def _G_many_3():
                        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
                        self.considerError(lastError)
                        return (_G_apply_1, self.currentError)
                    _G_many_4, lastError = self.many(_G_many_3)
                    self.considerError(lastError)
                    return (_G_many_4, self.currentError)
                _G_lookahead_3, lastError = self.lookahead(_G_lookahead_2)
                self.considerError(lastError)
                _G_apply_4, lastError = self._apply(self.rule_call, "call", [])
                self.considerError(lastError)
                _locals['e'] = _G_apply_4
                return (_locals['e'], self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            _G_python_3, lastError = eval('e', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        def _G_or_5():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['e'] = _G_apply_1
            _G_python_2, lastError = eval("'%s;' % e", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_2, self.currentError)
        _G_or_6, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4, _G_or_5])
        self.considerError(lastError)
        return (_G_or_6, self.currentError)


    def rule_expr(self):
        _locals = {'self': self}
        self.locals['expr'] = _locals
        def _G_listpattern_1():
            _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
            self.considerError(lastError)
            _locals['t'] = _G_apply_1
            _G_python_2, lastError = eval('t', self.globals, _locals), None
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_apply, "apply", [_G_python_2])
            self.considerError(lastError)
            _locals['ans'] = _G_apply_3
            return (_locals['ans'], self.currentError)
        _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
        self.considerError(lastError)
        _G_python_3, lastError = eval('ans', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_3, self.currentError)


    def rule_augassign(self):
        _locals = {'self': self}
        self.locals['augassign'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['op'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['l'] = _G_apply_2
        _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['r'] = _G_apply_3
        _G_python_4, lastError = eval('self.register_var(l)', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_5, lastError = eval("'%s %s %s' % (l, op, r)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_assign(self):
        _locals = {'self': self}
        self.locals['assign'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['l'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['r'] = _G_apply_2
        _G_python_3, lastError = eval('self.register_var(l)', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_4, lastError = eval("'%s = %s' % (l, r)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_4, self.currentError)


    def rule_get(self):
        _locals = {'self': self}
        self.locals['get'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['x'] = _G_apply_1
        _G_python_2, lastError = eval('x', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_getattr(self):
        _locals = {'self': self}
        self.locals['getattr'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['x'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['y'] = _G_apply_2
        _G_python_3, lastError = eval("'%s.%s' % (x, y)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_3, self.currentError)


    def rule_getitem(self):
        _locals = {'self': self}
        self.locals['getitem'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['x'] = _G_apply_1
        def _G_or_2():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('slice')
                self.considerError(lastError)
                def _G_or_2():
                    _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                def _G_or_3():
                    _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_or_4, lastError = self._or([_G_or_2, _G_or_3])
                self.considerError(lastError)
                _locals['start'] = _G_or_4
                def _G_or_5():
                    _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                def _G_or_6():
                    _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_or_7, lastError = self._or([_G_or_5, _G_or_6])
                self.considerError(lastError)
                _locals['end'] = _G_or_7
                return (_locals['end'], self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            _G_python_3, lastError = eval("'%s.slice(%s)' % (x, (start if start is not None else '0') + (', ' + end if end is not None else ''))", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        def _G_or_3():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('unop')
                self.considerError(lastError)
                _G_exactly_2, lastError = self.exactly('-')
                self.considerError(lastError)
                def _G_listpattern_3():
                    def _G_or_1():
                        _G_exactly_1, lastError = self.exactly('number')
                        self.considerError(lastError)
                        return (_G_exactly_1, self.currentError)
                    def _G_or_2():
                        _G_exactly_1, lastError = self.exactly('hexnumber')
                        self.considerError(lastError)
                        return (_G_exactly_1, self.currentError)
                    _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
                    self.considerError(lastError)
                    _G_apply_4, lastError = self._apply(self.rule_anything, "anything", [])
                    self.considerError(lastError)
                    _locals['i'] = _G_apply_4
                    def _G_pred_5():
                        _G_python_1, lastError = eval('i > 0', self.globals, _locals), None
                        self.considerError(lastError)
                        return (_G_python_1, self.currentError)
                    _G_pred_6, lastError = self.pred(_G_pred_5)
                    self.considerError(lastError)
                    return (_G_pred_6, self.currentError)
                _G_listpattern_4, lastError = self.listpattern(_G_listpattern_3)
                self.considerError(lastError)
                return (_G_listpattern_4, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            _G_python_3, lastError = eval("'%s.slice(%s)[0]' % (x, -i if i == 1 else '%s, %s' % (-i, -i+1))", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        def _G_or_4():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['y'] = _G_apply_1
            _G_python_2, lastError = eval("'%s[%s]' % (x, y)", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_2, self.currentError)
        _G_or_5, lastError = self._or([_G_or_2, _G_or_3, _G_or_4])
        self.considerError(lastError)
        return (_G_or_5, self.currentError)


    def rule_del(self):
        _locals = {'self': self}
        self.locals['del'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['x'] = _G_apply_1
        _G_python_2, lastError = eval("'delete %s' % x", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_unop(self):
        _locals = {'self': self}
        self.locals['unop'] = _locals
        def _G_or_1():
            _G_exactly_1, lastError = self.exactly('not')
            self.considerError(lastError)
            def _G_listpattern_2():
                _G_exactly_1, lastError = self.exactly('call')
                self.considerError(lastError)
                def _G_listpattern_2():
                    _G_exactly_1, lastError = self.exactly('name')
                    self.considerError(lastError)
                    _G_exactly_2, lastError = self.exactly('hasattr')
                    self.considerError(lastError)
                    return (_G_exactly_2, self.currentError)
                _G_listpattern_3, lastError = self.listpattern(_G_listpattern_2)
                self.considerError(lastError)
                def _G_listpattern_4():
                    _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                    self.considerError(lastError)
                    _locals['obj'] = _G_apply_1
                    _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
                    self.considerError(lastError)
                    _locals['attr'] = _G_apply_2
                    return (_locals['attr'], self.currentError)
                _G_listpattern_5, lastError = self.listpattern(_G_listpattern_4)
                self.considerError(lastError)
                return (_G_listpattern_5, self.currentError)
            _G_listpattern_3, lastError = self.listpattern(_G_listpattern_2)
            self.considerError(lastError)
            _G_python_4, lastError = eval('\'(typeof %s[%s] == "undefined")\' % (obj, attr)', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_4, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
            self.considerError(lastError)
            _locals['op'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['x'] = _G_apply_2
            _G_python_3, lastError = eval("'(%s%s)' % (self.op_map.get(op, op), x)", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_binop(self):
        _locals = {'self': self}
        self.locals['binop'] = _locals
        def _G_or_1():
            _G_exactly_1, lastError = self.exactly('not in')
            self.considerError(lastError)
            _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['x'] = _G_apply_2
            _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['y'] = _G_apply_3
            _G_python_4, lastError = eval("'!(%s in %s)' % (x, y)", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_4, self.currentError)
        def _G_or_2():
            _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
            self.considerError(lastError)
            _locals['op'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['x'] = _G_apply_2
            _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['y'] = _G_apply_3
            _G_python_4, lastError = eval("'(%s %s %s)' % (x, self.binop_map.get(op, op), y)", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_4, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_name(self):
        _locals = {'self': self}
        self.locals['name'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['n'] = _G_apply_1
        _G_python_2, lastError = eval('self.get_name(n)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_number(self):
        _locals = {'self': self}
        self.locals['number'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['n'] = _G_apply_1
        _G_python_2, lastError = eval('str(n)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_hexnumber(self):
        _locals = {'self': self}
        self.locals['hexnumber'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['n'] = _G_apply_1
        _G_python_2, lastError = eval('hex(n)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_string(self):
        _locals = {'self': self}
        self.locals['string'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['s'] = _G_apply_1
        _G_python_2, lastError = eval('json.dumps(s)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_call(self):
        _locals = {'self': self}
        self.locals['call'] = _locals
        def _G_or_1():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('name')
                self.considerError(lastError)
                _G_exactly_2, lastError = self.exactly('jsnew')
                self.considerError(lastError)
                return (_G_exactly_2, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            def _G_listpattern_3():
                _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                _locals['obj'] = _G_apply_1
                return (_locals['obj'], self.currentError)
            _G_listpattern_4, lastError = self.listpattern(_G_listpattern_3)
            self.considerError(lastError)
            _G_python_5, lastError = eval("'(new %s)' % obj", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_2():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('name')
                self.considerError(lastError)
                _G_exactly_2, lastError = self.exactly('len')
                self.considerError(lastError)
                return (_G_exactly_2, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            def _G_listpattern_3():
                _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                _locals['obj'] = _G_apply_1
                return (_locals['obj'], self.currentError)
            _G_listpattern_4, lastError = self.listpattern(_G_listpattern_3)
            self.considerError(lastError)
            _G_python_5, lastError = eval("'%s.length' % obj", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_3():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('name')
                self.considerError(lastError)
                _G_exactly_2, lastError = self.exactly('hasattr')
                self.considerError(lastError)
                return (_G_exactly_2, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            def _G_listpattern_3():
                _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                _locals['obj'] = _G_apply_1
                _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                _locals['attr'] = _G_apply_2
                return (_locals['attr'], self.currentError)
            _G_listpattern_4, lastError = self.listpattern(_G_listpattern_3)
            self.considerError(lastError)
            _G_python_5, lastError = eval('\'(typeof %s[%s] != "undefined")\' % (obj, attr)', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_4():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('name')
                self.considerError(lastError)
                _G_exactly_2, lastError = self.exactly('getattr')
                self.considerError(lastError)
                return (_G_exactly_2, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            def _G_listpattern_3():
                _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                _locals['obj'] = _G_apply_1
                _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                _locals['attr'] = _G_apply_2
                return (_locals['attr'], self.currentError)
            _G_listpattern_4, lastError = self.listpattern(_G_listpattern_3)
            self.considerError(lastError)
            _G_python_5, lastError = eval("'%s[%s]' % (obj, attr)", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_5():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('name')
                self.considerError(lastError)
                _G_exactly_2, lastError = self.exactly('setattr')
                self.considerError(lastError)
                return (_G_exactly_2, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            def _G_listpattern_3():
                _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                _locals['obj'] = _G_apply_1
                _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                _locals['attr'] = _G_apply_2
                _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
                self.considerError(lastError)
                _locals['value'] = _G_apply_3
                return (_locals['value'], self.currentError)
            _G_listpattern_4, lastError = self.listpattern(_G_listpattern_3)
            self.considerError(lastError)
            _G_python_5, lastError = eval("'%s[%s] = %s' % (obj, attr, value)", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_5, self.currentError)
        def _G_or_6():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('name')
                self.considerError(lastError)
                _G_exactly_2, lastError = self.exactly('JS')
                self.considerError(lastError)
                return (_G_exactly_2, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            def _G_or_3():
                def _G_listpattern_1():
                    def _G_listpattern_1():
                        _G_exactly_1, lastError = self.exactly('string')
                        self.considerError(lastError)
                        _G_apply_2, lastError = self._apply(self.rule_anything, "anything", [])
                        self.considerError(lastError)
                        _locals['js'] = _G_apply_2
                        return (_locals['js'], self.currentError)
                    _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                    self.considerError(lastError)
                    return (_G_listpattern_2, self.currentError)
                _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                self.considerError(lastError)
                _G_python_3, lastError = eval("'%s' % js", self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_3, self.currentError)
            def _G_or_4():
                def _G_listpattern_1():
                    _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                    self.considerError(lastError)
                    _locals['js'] = _G_apply_1
                    return (_locals['js'], self.currentError)
                _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                self.considerError(lastError)
                _G_python_3, lastError = eval("'eval(%s)' % js", self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_3, self.currentError)
            _G_or_5, lastError = self._or([_G_or_3, _G_or_4])
            self.considerError(lastError)
            return (_G_or_5, self.currentError)
        def _G_or_7():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['fn'] = _G_apply_1
            def _G_listpattern_2():
                def _G_many_1():
                    _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_many_2, lastError = self.many(_G_many_1)
                self.considerError(lastError)
                _locals['args'] = _G_many_2
                return (_locals['args'], self.currentError)
            _G_listpattern_3, lastError = self.listpattern(_G_listpattern_2)
            self.considerError(lastError)
            _G_python_4, lastError = eval("'%s(%s)' % (fn, ', '.join(args))", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_4, self.currentError)
        _G_or_8, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4, _G_or_5, _G_or_6, _G_or_7])
        self.considerError(lastError)
        return (_G_or_8, self.currentError)


    def rule_list(self):
        _locals = {'self': self}
        self.locals['list'] = _locals
        _G_python_1, lastError = eval('self.indent()', self.globals, _locals), None
        self.considerError(lastError)
        def _G_many_2():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_3, lastError = self.many(_G_many_2)
        self.considerError(lastError)
        _locals['xs'] = _G_many_3
        _G_python_4, lastError = eval('self.dedent()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_5, lastError = eval("'[%s]' % ', '.join(xs)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_tuple(self):
        _locals = {'self': self}
        self.locals['tuple'] = _locals
        _G_python_1, lastError = eval('self.indent()', self.globals, _locals), None
        self.considerError(lastError)
        def _G_many_2():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_3, lastError = self.many(_G_many_2)
        self.considerError(lastError)
        _locals['xs'] = _G_many_3
        _G_python_4, lastError = eval('self.dedent()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_5, lastError = eval("'[%s]' % ', '.join(xs)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_set(self):
        _locals = {'self': self}
        self.locals['set'] = _locals
        _G_python_1, lastError = eval('self.indent()', self.globals, _locals), None
        self.considerError(lastError)
        def _G_many_2():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_3, lastError = self.many(_G_many_2)
        self.considerError(lastError)
        _locals['xs'] = _G_many_3
        _G_python_4, lastError = eval('self.dedent()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_5, lastError = eval("'set([%s])' % ', '.join(xs)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_dict(self):
        _locals = {'self': self}
        self.locals['dict'] = _locals
        _G_python_1, lastError = eval('self.indent()', self.globals, _locals), None
        self.considerError(lastError)
        _locals['i'] = _G_python_1
        def _G_many_2():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        _G_many_3, lastError = self.many(_G_many_2)
        self.considerError(lastError)
        _locals['xs'] = _G_many_3
        _G_python_4, lastError = eval('self.dedent()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_5, lastError = eval('self.make_dict(xs, i)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_5, self.currentError)


    def rule_dictkv(self):
        _locals = {'self': self}
        self.locals['dictkv'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['k'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['v'] = _G_apply_2
        _G_python_3, lastError = eval("'%s: %s' % (k, v)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_3, self.currentError)


    def rule_self(self):
        _locals = {'self': self}
        self.locals['self'] = _locals
        _G_python_1, lastError = eval("'this'", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_1, self.currentError)


    def rule_break(self):
        _locals = {'self': self}
        self.locals['break'] = _locals
        _G_python_1, lastError = eval("'break'", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_1, self.currentError)


    def rule_continue(self):
        _locals = {'self': self}
        self.locals['continue'] = _locals
        _G_python_1, lastError = eval("'continue'", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_1, self.currentError)


    def rule_return(self):
        _locals = {'self': self}
        self.locals['return'] = _locals
        def _G_or_1():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['x'] = _G_apply_1
            _G_python_2, lastError = eval("'return %s' % x", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_2, self.currentError)
        def _G_or_2():
            _G_python_1, lastError = eval("'return'", self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_raise(self):
        _locals = {'self': self}
        self.locals['raise'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['x'] = _G_apply_1
        _G_python_2, lastError = eval("'throw %s' % x", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_while(self):
        _locals = {'self': self}
        self.locals['while'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['cond'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_2
        _G_python_3, lastError = eval("'while (%s) %s' % (cond, ''.join(body))", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_3, self.currentError)


    def rule_if(self):
        _locals = {'self': self}
        self.locals['if'] = _locals
        def _G_listpattern_1():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['cond'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_block, "block", [])
            self.considerError(lastError)
            _locals['t'] = _G_apply_2
            return (_locals['t'], self.currentError)
        _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
        self.considerError(lastError)
        def _G_listpattern_3():
            def _G_many_1():
                def _G_listpattern_1():
                    _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                    self.considerError(lastError)
                    _locals['c'] = _G_apply_1
                    _G_apply_2, lastError = self._apply(self.rule_block, "block", [])
                    self.considerError(lastError)
                    _locals['b'] = _G_apply_2
                    return (_locals['b'], self.currentError)
                _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                self.considerError(lastError)
                _G_python_3, lastError = eval('(c, b)', self.globals, _locals), None
                self.considerError(lastError)
                return (_G_python_3, self.currentError)
            _G_many_2, lastError = self.many(_G_many_1)
            self.considerError(lastError)
            _locals['ei'] = _G_many_2
            return (_locals['ei'], self.currentError)
        _G_listpattern_4, lastError = self.listpattern(_G_listpattern_3)
        self.considerError(lastError)
        def _G_optional_5():
            _G_apply_1, lastError = self._apply(self.rule_block, "block", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_optional_6():
            return (None, self.input.nullError())
        _G_or_7, lastError = self._or([_G_optional_5, _G_optional_6])
        self.considerError(lastError)
        _locals['e'] = _G_or_7
        _G_python_8, lastError = eval('self.make_if(cond, t, ei, e)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_8, self.currentError)


    def rule_ifexpr(self):
        _locals = {'self': self}
        self.locals['ifexpr'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['cond'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['t'] = _G_apply_2
        _G_apply_3, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['f'] = _G_apply_3
        _G_python_4, lastError = eval("'(%s ? %s : %s)' % (cond, t, f)", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_4, self.currentError)


    def rule_isliteral(self):
        _locals = {'self': self}
        self.locals['isliteral'] = _locals
        def _G_or_1():
            def _G_lookahead_1():
                def _G_listpattern_1():
                    def _G_or_1():
                        _G_exactly_1, lastError = self.exactly('name')
                        self.considerError(lastError)
                        return (_G_exactly_1, self.currentError)
                    def _G_or_2():
                        _G_exactly_1, lastError = self.exactly('number')
                        self.considerError(lastError)
                        return (_G_exactly_1, self.currentError)
                    def _G_or_3():
                        _G_exactly_1, lastError = self.exactly('hexnumber')
                        self.considerError(lastError)
                        return (_G_exactly_1, self.currentError)
                    def _G_or_4():
                        _G_exactly_1, lastError = self.exactly('string')
                        self.considerError(lastError)
                        return (_G_exactly_1, self.currentError)
                    _G_or_5, lastError = self._or([_G_or_1, _G_or_2, _G_or_3, _G_or_4])
                    self.considerError(lastError)
                    def _G_many_6():
                        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
                        self.considerError(lastError)
                        return (_G_apply_1, self.currentError)
                    _G_many_7, lastError = self.many(_G_many_6)
                    self.considerError(lastError)
                    return (_G_many_7, self.currentError)
                _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                self.considerError(lastError)
                return (_G_listpattern_2, self.currentError)
            _G_lookahead_2, lastError = self.lookahead(_G_lookahead_1)
            self.considerError(lastError)
            _G_python_3, lastError = eval('True', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        def _G_or_2():
            _G_python_1, lastError = eval('False', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_1, self.currentError)
        _G_or_3, lastError = self._or([_G_or_1, _G_or_2])
        self.considerError(lastError)
        return (_G_or_3, self.currentError)


    def rule_for(self):
        _locals = {'self': self}
        self.locals['for'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['var'] = _G_apply_1
        _G_python_2, lastError = eval('self.register_var(var)', self.globals, _locals), None
        self.considerError(lastError)
        def _G_or_3():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('call')
                self.considerError(lastError)
                def _G_listpattern_2():
                    _G_exactly_1, lastError = self.exactly('name')
                    self.considerError(lastError)
                    _G_exactly_2, lastError = self.exactly('range')
                    self.considerError(lastError)
                    return (_G_exactly_2, self.currentError)
                _G_listpattern_3, lastError = self.listpattern(_G_listpattern_2)
                self.considerError(lastError)
                def _G_listpattern_4():
                    def _G_many1_1():
                        _G_apply_1, lastError = self._apply(self.rule_isliteral, "isliteral", [])
                        self.considerError(lastError)
                        _locals['lit'] = _G_apply_1
                        _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
                        self.considerError(lastError)
                        _locals['e'] = _G_apply_2
                        _G_python_3, lastError = eval('(lit, e)', self.globals, _locals), None
                        self.considerError(lastError)
                        return (_G_python_3, self.currentError)
                    _G_many1_2, lastError = self.many(_G_many1_1, _G_many1_1())
                    self.considerError(lastError)
                    _locals['r'] = _G_many1_2
                    def _G_pred_3():
                        _G_python_1, lastError = eval('len(r) <= 3', self.globals, _locals), None
                        self.considerError(lastError)
                        return (_G_python_1, self.currentError)
                    _G_pred_4, lastError = self.pred(_G_pred_3)
                    self.considerError(lastError)
                    return (_G_pred_4, self.currentError)
                _G_listpattern_5, lastError = self.listpattern(_G_listpattern_4)
                self.considerError(lastError)
                return (_G_listpattern_5, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_block, "block", [])
            self.considerError(lastError)
            _locals['body'] = _G_apply_3
            _G_python_4, lastError = eval('self.make_for_range(var, r, body)', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_4, self.currentError)
        def _G_or_4():
            def _G_listpattern_1():
                _G_exactly_1, lastError = self.exactly('call')
                self.considerError(lastError)
                def _G_listpattern_2():
                    _G_exactly_1, lastError = self.exactly('name')
                    self.considerError(lastError)
                    _G_exactly_2, lastError = self.exactly('reversed')
                    self.considerError(lastError)
                    return (_G_exactly_2, self.currentError)
                _G_listpattern_3, lastError = self.listpattern(_G_listpattern_2)
                self.considerError(lastError)
                def _G_listpattern_4():
                    def _G_listpattern_1():
                        _G_exactly_1, lastError = self.exactly('call')
                        self.considerError(lastError)
                        def _G_listpattern_2():
                            _G_exactly_1, lastError = self.exactly('name')
                            self.considerError(lastError)
                            _G_exactly_2, lastError = self.exactly('range')
                            self.considerError(lastError)
                            return (_G_exactly_2, self.currentError)
                        _G_listpattern_3, lastError = self.listpattern(_G_listpattern_2)
                        self.considerError(lastError)
                        def _G_listpattern_4():
                            def _G_many1_1():
                                _G_apply_1, lastError = self._apply(self.rule_isliteral, "isliteral", [])
                                self.considerError(lastError)
                                _locals['lit'] = _G_apply_1
                                _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
                                self.considerError(lastError)
                                _locals['e'] = _G_apply_2
                                _G_python_3, lastError = eval('(lit, e)', self.globals, _locals), None
                                self.considerError(lastError)
                                return (_G_python_3, self.currentError)
                            _G_many1_2, lastError = self.many(_G_many1_1, _G_many1_1())
                            self.considerError(lastError)
                            _locals['r'] = _G_many1_2
                            def _G_pred_3():
                                _G_python_1, lastError = eval('len(r) <= 3', self.globals, _locals), None
                                self.considerError(lastError)
                                return (_G_python_1, self.currentError)
                            _G_pred_4, lastError = self.pred(_G_pred_3)
                            self.considerError(lastError)
                            return (_G_pred_4, self.currentError)
                        _G_listpattern_5, lastError = self.listpattern(_G_listpattern_4)
                        self.considerError(lastError)
                        return (_G_listpattern_5, self.currentError)
                    _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
                    self.considerError(lastError)
                    return (_G_listpattern_2, self.currentError)
                _G_listpattern_5, lastError = self.listpattern(_G_listpattern_4)
                self.considerError(lastError)
                return (_G_listpattern_5, self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_block, "block", [])
            self.considerError(lastError)
            _locals['body'] = _G_apply_3
            _G_python_4, lastError = eval('self.make_for_reversed_range(var, r, body)', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_4, self.currentError)
        def _G_or_5():
            _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
            self.considerError(lastError)
            _locals['data'] = _G_apply_1
            _G_apply_2, lastError = self._apply(self.rule_block, "block", [])
            self.considerError(lastError)
            _locals['body'] = _G_apply_2
            _G_python_3, lastError = eval('self.make_for(var, data, body)', self.globals, _locals), None
            self.considerError(lastError)
            return (_G_python_3, self.currentError)
        _G_or_6, lastError = self._or([_G_or_3, _G_or_4, _G_or_5])
        self.considerError(lastError)
        return (_G_or_6, self.currentError)


    def rule_defaultarg(self):
        _locals = {'self': self}
        self.locals['defaultarg'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['name'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['default'] = _G_apply_2
        _G_python_3, lastError = eval('(name, default)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_3, self.currentError)


    def rule_stararg(self):
        _locals = {'self': self}
        self.locals['stararg'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['name'] = _G_apply_1
        _G_python_2, lastError = eval('(name,)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_func(self):
        _locals = {'self': self}
        self.locals['func'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_funcstmt, "funcstmt", [])
        self.considerError(lastError)
        _locals['f'] = _G_apply_1
        _G_python_2, lastError = eval("'(%s)' % f", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_2, self.currentError)


    def rule_funcstmt(self):
        _locals = {'self': self}
        self.locals['funcstmt'] = _locals
        _G_python_1, lastError = eval('self.push_vars()', self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_2, lastError = self._apply(self.rule_anything, "anything", [])
        self.considerError(lastError)
        _locals['name'] = _G_apply_2
        def _G_listpattern_3():
            def _G_listpattern_1():
                def _G_many_1():
                    _G_apply_1, lastError = self._apply(self.rule_expr, "expr", [])
                    self.considerError(lastError)
                    return (_G_apply_1, self.currentError)
                _G_many_2, lastError = self.many(_G_many_1)
                self.considerError(lastError)
                _locals['args'] = _G_many_2
                return (_locals['args'], self.currentError)
            _G_listpattern_2, lastError = self.listpattern(_G_listpattern_1)
            self.considerError(lastError)
            _G_apply_3, lastError = self._apply(self.rule_anything, "anything", [])
            self.considerError(lastError)
            _locals['stararg'] = _G_apply_3
            return (_locals['stararg'], self.currentError)
        _G_listpattern_4, lastError = self.listpattern(_G_listpattern_3)
        self.considerError(lastError)
        _G_python_5, lastError = eval('self.register_globals(args)', self.globals, _locals), None
        self.considerError(lastError)
        _G_apply_6, lastError = self._apply(self.rule_funcblock, "funcblock", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_6
        _G_python_7, lastError = eval('self.pop_vars()', self.globals, _locals), None
        self.considerError(lastError)
        _G_python_8, lastError = eval('self.make_func(name, args, stararg, body)', self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_8, self.currentError)


    def rule_try(self):
        _locals = {'self': self}
        self.locals['try'] = _locals
        _G_apply_1, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['body'] = _G_apply_1
        _G_apply_2, lastError = self._apply(self.rule_expr, "expr", [])
        self.considerError(lastError)
        _locals['err'] = _G_apply_2
        _G_apply_3, lastError = self._apply(self.rule_block, "block", [])
        self.considerError(lastError)
        _locals['errbody'] = _G_apply_3
        def _G_optional_4():
            _G_apply_1, lastError = self._apply(self.rule_block, "block", [])
            self.considerError(lastError)
            return (_G_apply_1, self.currentError)
        def _G_optional_5():
            return (None, self.input.nullError())
        _G_or_6, lastError = self._or([_G_optional_4, _G_optional_5])
        self.considerError(lastError)
        _locals['finbody'] = _G_or_6
        _G_python_7, lastError = eval("'try %s catch(%s) %s' % (body, err, errbody) + (' finally %s' % finbody if finbody else '')", self.globals, _locals), None
        self.considerError(lastError)
        return (_G_python_7, self.currentError)
