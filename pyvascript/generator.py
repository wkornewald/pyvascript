# Generates static grammar modules so the PyvaScript grammar doesn't need to be
# parsed on first import.
if __name__ == '__main__':
    import os, sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from pymeta.builder import TreeBuilder, writeBoot
    from pymeta.grammar_definition import OMetaGrammar
    from pyvascript.grammar import grammar_path, translator_path
    for name, path in (('Grammar', grammar_path), ('Translator', translator_path)):
        with open(path, 'r') as fp:
            source = fp.read()
        grammar = OMetaGrammar(source)
        tree = grammar.parseGrammar('Generated' + name, TreeBuilder)
        path = os.path.join(os.path.dirname(__file__), name.lower() + '_generated.py')
        with open(path, 'w') as fp:
            fp.write('import json\ndef p(s): print(s)\n')
            fp.write(writeBoot(tree))
