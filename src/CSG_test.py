from GrammarTools import *


#BEGINNING OF TEST 1

print ('TEST 1')
print ('Using the grammar: \n')
print ('first -> sun second @ 0.1 | moon first @ 0.1 | third second @ 0.1')
print ('third second -> 1.1 second @ 0.2 | 33 @ 0.5 | f1 @ 0.3')
print ('third -> 2.1 @ 0.2 | 3.3 @ 0.5 | fjjj1 @ 0.3')
print ()

start_symbol = ["first"]
terminals = ["dog", "cat", "clouds", "sun", "earth", "monsoon"]
non_terminals = ["first", "second", "third"]

production_one_lhs = ["first"]
production_one_rhs = [Alternation([Alternate(["sun", "second"], 0.1), Alternate(["moon", "first"], 0.1), Alternate(["third", "second"], 0.8)])]
production_one = SensitiveProduction(production_one_lhs, production_one_rhs)

production_two_lhs = ["third", "second"]
production_two_rhs = [Alternation([Alternate(["1.1"], 0.2), Alternate(["33"], 0.5), Alternate(["f1"], 0.3)])]
production_two = SensitiveProduction(production_two_lhs, production_two_rhs)

production_three_lhs = ["second"]
production_three_rhs = [Alternation([Alternate(["2.1"], 0.2), Alternate(["3.3"], 0.5), Alternate(["fjjj1"], 0.3)])]
production_three = SensitiveProduction(production_three_lhs, production_three_rhs)

productions = [production_one, production_two, production_three]

grammar = CSGrammar(non_terminals, terminals, start_symbol, productions)

grammar.genRandSentence(start_symbol)
#grammar.prettyPrint()

print ('Sample Output: ', grammar.output)
testout = Output(grammar.output)
print("string: ",testout.returnString())
print ('_________________________________________________________________\n')

#BEGINNING OF TEST 2

print ('TEST 2')
print ('Using the grammar: \n')
print ('S -> a B C @ 0.2 | a S B C @ 0.5')
print ('C B -> C ( a B C @ 0.2 | a S B C @ 0.5')
print ('C Z -> W Z')
print ('W Z -> W C')
print ('W C -> B C')
print ('a B -> a 3.3')
print ('3.3 B -> 3.3 3.3')
print ('3.3 C -> 3.3 100')
print ('100 C -> 100 100')
print ('A -> a')
print ('B -> 3.3')
print ('C -> 100')
print ('W -> W')
print ('Z -> z')
print ()

start_symbol = ["S"]
terminals = ["a", 3.3, 100, "w", "z"]
non_terminals = ["A","B","C","W","Z"]

S = SensitiveProduction(["S"], [Alternation([Alternate(["a","Z","W"], 0.2), Alternate(["a","S","C","B"], 0.5)])])
CB = SensitiveProduction(["C","B"], ["C",Alternation([Alternate(["a","W","C"], 0.2), Alternate(["a","W","W","W"], 0.5)])])
CZ = SensitiveProduction(["C","Z"], ["W","Z"])
WZ = SensitiveProduction(["W","Z"], ["W","C"])
WC = SensitiveProduction(["W","C"], ["B","C"])
aB = SensitiveProduction(["a","B"], ["a",3.3])
bB = SensitiveProduction([3.3,"B"], [3.3,3.3])
bC = SensitiveProduction([3.3,"C"], [3.3,100])
cC = SensitiveProduction([100,"C"], [100,100])
A = SensitiveProduction(["A"], ["a"])
B = SensitiveProduction(["B"], [3.3])
C = SensitiveProduction(["C"], [100])
W = SensitiveProduction(["W"], ["w"])
Z = SensitiveProduction(["Z"], ["z"])

productions = [S, CB, CZ, WZ, WC, aB, bB, bC, cC, A, B, C, W, Z]

grammar = CSGrammar(non_terminals, terminals, start_symbol, productions)

grammar.genRandSentence(start_symbol)

print ('Sample Output: ', grammar.output)
testout = Output(grammar.output)
print("string: ",testout.returnString())
print ('_________________________________________________________________\n')

#BEGINNING OF TEST 3

print ('TEST 3')
print ('Using the grammar: \n')
print ('start -> var')
print ('var -> int def @ 0.3 | double def @ 0.3 | string def @ 0.4')
print ('int def -> int definition := 0')
print ('double def -> double definition := 99.99')
print ('string def -> string definition := "abcd"')
print ('int definition -> int name')
print ('double definition -> double name')
print ('string definition -> string name')
print ('name -> { ( a @ 0.5 | b @ 0.5 ) }')
print ()

start = SensitiveProduction(["start"], ["var"])
var = SensitiveProduction(["var"], [Alternation([Alternate(["int", "def"], 0.3), Alternate(["double", "def"], 0.3), Alternate(["string",  "def"], 0.4)])])
int_var = SensitiveProduction(["int", "def"], ["int", "definition", ":=", 0, ";"])
double_var = SensitiveProduction(["double", "def"], ["double", "definition", ":=", 99.99, ";"])
string_var = SensitiveProduction(["string", "def"], ["string", "definition", ":=", '"abcd"', ";"])
int_definition = SensitiveProduction(["int", "definition"], ["int", "name"])
double_definition = SensitiveProduction(["double", "definition"], ["double", "name"])
string_definition = SensitiveProduction(["string", "definition"], ["string", "name"])
name = SensitiveProduction(["name"], [Alternation([Alternate(["a"], 0.5), Alternate(["b"], 0.5)])])

prods = [start, var, int_var, double_var, string_var, int_definition, double_definition, string_definition, name]
non_terminals = ["start", "var", "int", "double", "string", "def", "definition", "name"]
start_symbol = ["start"]
terminals = [0, 1, 1.1, 2.2, "abcd", "efgh", "a", "b"]

grammar = CSGrammar(non_terminals, terminals, start_symbol, prods)
grammar.genRandSentence(start_symbol)

print ('Sample Output: ', grammar.output)
testout = Output(grammar.output)
print("string: ",testout.returnString())
print ('_________________________________________________________________\n')