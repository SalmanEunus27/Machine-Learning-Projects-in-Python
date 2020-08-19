# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 05:44:17 2020

@author: salman
"""
fh = open("lab1.txt")
inp = fh.read()
#print(inp)

if inp is not None:
    try:
        operator = Regex(r'(?<!--[\+\-\^\*/%])[\+\-]|[\^\*/%!]')<br /-->
		function = Regex(r'[a-zA-Z_][a-zA-Z0-9_]*(?=([ \t]+)?\()')
		variable = Regex(r'[+-]?[a-zA-Z_][a-zA-Z0-9_]*(?!([ \t]+)?\()')
		number = Regex(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?')
		lbrace = Word('(')
		rbrace = Word(')')
		assign = Literal(':=')
		linebreak = Word('\n')
		skip = Word(' \t')
        print(lexAllOnly.parseString(inp))
    except:
        ParseException, err:
		print(err.line)
		print(" "*(err.column-1) + "^")
		print(err)
	else:
        print('Invalid parameters.\n')

