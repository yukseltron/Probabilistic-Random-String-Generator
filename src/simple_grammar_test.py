from GrammarTools import *


'''
Create our productions using the CFGrammarTools objects instead of by passing in a string that we parse.
Will save time, and if needed we can implement that later.

Grammar we are using:

first ::= "a" { second } "b"
second ::= [ "c first" ] ( "d" @ 0.2 | { "e" } @ 0.5 | "f" @ 0.3 )
third ::== "k"
'''


#Test 1:
#type check for int: PASSED, string: PASSED, and float: PASSED

print("TEST1")
start_symbol = "first"
terminals = ["dog", "cat", "clouds", "sun", "earth", "monsoon", "1.1", 1.2, "33", "f1", 3.1,1]
non_terminals = ["first", "second", "third"]

production_one_lhs = "first"
production_one_rhs = [["sings", 2.1], Repeat(["second"],0,1), [2]]
production_one = Production(production_one_lhs, production_one_rhs)

production_two_lhs = "second"
production_two_rhs = [Optional([3.1]), Alternation([Alternate(["1.1", 1.2], 0.2), Alternate(Repeat(["33", 2.3, "third"],0,1), 0.5), Alternate(["f1", 1], 0.3)])]
production_two = Production(production_two_lhs, production_two_rhs)

production_three_lhs = "third"
production_three_rhs = [Optional(["koolaid"])]
production_three = Production(production_three_lhs, production_three_rhs)

productions = [production_one, production_two, production_three]

grammar = CFGrammar(non_terminals, terminals, start_symbol, productions)

grammar.genRandSentence(start_symbol)
print("OUT:",grammar.output)


# print("TEST 1: PASSED")
# grammar.prettyPrint()
#print('\n')



#Test 2:
#Testing Alternation functionality: PASSED
#Basic 'poetry' generation (Complex CFGrammar)
print("TEST 2: PASSED")

start_symbol = "S"
terminals = ["dog", "cat", "clouds", "sun", "earth", "monsoon"]
non_terminals = ["S", "NP", "VP", "PN", "ART", "VERB", "NOUN", "ADJ", "PREP"]

production_S_lhs = "S"
production_S_rhs = [["NP", 0.5], ["VP", 0.5]]
production_S = Production(production_S_lhs, production_S_rhs)

production_NP_lhs = "NP"
production_NP_rhs = [Alternation([Alternate(["ART", "NOUN"], 0.2), Alternate(["ART", "ADJ", "NOUN"], 0.5), Alternate(["PN"], 0.3)])]
production_NP = Production(production_NP_lhs, production_NP_rhs)

production_VP_lhs = "VP"
production_VP_rhs = [Alternation([Alternate(["VERB", "NP"], 0.2), Alternate(Repeat(["VERB", "PREP", "NP"],0,1), 0.8)])]
production_VP = Production(production_VP_lhs, production_VP_rhs)

production_PN_lhs = "PN"
production_PN_rhs = [Alternation([Alternate(["Siberia"], 0.4), Alternate(["El Dorado"], 0.2), Alternate(["Earth"], 0.4)])]
production_PN = Production(production_PN_lhs, production_PN_rhs)

production_ART_lhs = "ART"
production_ART_rhs = [Alternation([Alternate(["a"], 0.4), Alternate(["the"], 0.6)])]
production_ART = Production(production_ART_lhs, production_ART_rhs)

production_VERB_lhs = "VERB"
production_VERB_rhs = [Alternation([Alternate(["smiles"], 0.4), Alternate(["sings"], 0.1), Alternate(["reprimands"], 0.1), Alternate(["reviles"], 0.1), Alternate(["revolves"], 0.1), Alternate(["resides"], 0.1), Alternate(["relaxes"], 0.1)])]
production_VERB = Production(production_VERB_lhs, production_VERB_rhs)

production_NOUN_lhs = "NOUN"
production_NOUN_rhs = [Alternation([Alternate(["monster"], 0.1), Alternate(["flower"], 0.1), Alternate(["pizza"], 0.1), Alternate(["dog"], 0.1), Alternate(["cat"], 0.1), Alternate(["ocean"], 0.1), Alternate(["sun"], 0.1), Alternate(["crevace"], 0.1), Alternate(["tsunami"], 0.1), Alternate(["volcano"], 0.1)])]
production_NOUN = Production(production_NOUN_lhs, production_NOUN_rhs)

production_ADJ_lhs = "ADJ"
production_ADJ_rhs = [Alternation([Alternate(["green"], 0.1), Alternate(["mean"], 0.1), Alternate(["lean"], 0.1), Alternate(["rough"], 0.1), Alternate(["soft"], 0.1), Alternate(["bright"], 0.1), Alternate(["dark"], 0.1), Alternate(["mellow"], 0.1), Alternate(["fiery"], 0.1), Alternate(["mystic"], 0.1)])]
production_ADJ = Production(production_ADJ_lhs, production_ADJ_rhs)

production_PREP_lhs = "PREP"
production_PREP_rhs = [Alternation([Alternate(["about"], 0.1), Alternate(["above"], 0.1), Alternate(["across"], 0.1), Alternate(["after"], 0.1), Alternate(["against"], 0.1), Alternate(["before"], 0.1), Alternate(["along"], 0.1), Alternate(["by"], 0.1), Alternate(["like"], 0.1), Alternate(["at"], 0.1)])]
production_PREP = Production(production_PREP_lhs, production_PREP_rhs)

productions = [production_S, production_NP, production_VP, production_PN, production_ART, production_VERB, production_NOUN, production_ADJ, production_PREP]

grammar = CFGrammar(non_terminals, terminals, start_symbol, productions)

grammar.genRandSentence(start_symbol)

test2out = Output(grammar.output)

print("OUT:",grammar.output)
print('\n')
print("string: ", test2out.returnString())

# Test 3:
# Testing probability functionalities: Alternation PASSED
# recipe generator:

print("TEST 3")
start_symbol = "S"
terminals = ["", "2", "3", "4", "5"]
non_terminals = ["EGG","BUN","COURSE", "BREAKFAST", "LUNCH", "DINNER", "DESSERT", "TOPPING", "NUMBER"]

production_S_lhs = "S"
production_S_rhs = [["COURSE"], 1]
production_S = Production(production_S_lhs, production_S_rhs)

production_COURSE_lhs = "COURSE"
production_COURSE_rhs = [Alternation([Alternate(["EGG"], 0.5), Alternate(["BUN"], 0.5)])]
production_COURSE = Production(production_COURSE_lhs, production_COURSE_rhs)

production_EGG_lhs = "EGG"
production_EGG_rhs = [Alternation([Alternate(["NUMBER", "eggs\n", "BREAKFAST"], 0.5), Alternate(Repeat(["NUMBER", "eggs\n", "DESSERT"],0,1), 0.5)])]
production_EGG = Production(production_EGG_lhs, production_EGG_rhs)

production_BUN_lhs = "BUN"
production_BUN_rhs = [Alternation([Alternate(["1 bun\n", "LUNCH"], 0.5), Alternate(["1 bun\n", "DINNER"], 0.5)])]
production_BUN = Production(production_BUN_lhs, production_BUN_rhs)

production_BREAKFAST_lhs = "BREAKFAST"
production_BREAKFAST_rhs = [Alternation([Alternate(["NUMBER", "strips of bacon\n", "NUMBER", "toast"], 0.8), Alternate(["NUMBER", "toast"], 0.2)])]
production_BREAKFAST = Production(production_BREAKFAST_lhs, production_BREAKFAST_rhs)

production_LUNCH_lhs = "LUNCH"
production_LUNCH_rhs = [Alternation([Alternate(["NUMBER", "strips of bacon\n", "NUMBER", "leaves of lettuce\n", "NUMBER", "slices of tomato\n"], 1)])]
production_LUNCH = Production(production_LUNCH_lhs, production_LUNCH_rhs)

production_DINNER_lhs = "DINNER"
production_DINNER_rhs = [Alternation([Alternate(["1 Burger Patty\n", "TOPPING"], 0.9), Alternate(["1 Burger Patty"], 0.1)])]
production_DINNER = Production(production_DINNER_lhs, production_DINNER_rhs)

production_DESSERT_lhs = "DESSERT"
production_DESSERT_rhs = [Alternation([Alternate(["NUMBER", "cups of flour\n", "NUMBER", "cups of water\n", "NUMBER", "tbsp of butter\n", "NUMBER", "cups of sugar\n"], 0.6), Alternate("", 0.4)])]
production_DESSERT = Production(production_DESSERT_lhs, production_DESSERT_rhs)

production_TOPPING_lhs = "TOPPING"
production_TOPPING_rhs = [Alternation([Alternate(["NUMBER", "strips of bacon\n", "TOPPING"], 0.2), Alternate(["NUMBER", "leaves of lettuce\n", "TOPPING"], 0.2), Alternate(["NUMBER", "slices of tomato\n", "TOPPING"], 0.3), Alternate(["NUMBER", "slices of pickle\n", "TOPPING"], 0.1), Alternate("", 0.2)])]
production_TOPPING = Production(production_TOPPING_lhs, production_TOPPING_rhs)


production_NUMBER_lhs = "NUMBER"
production_NUMBER_rhs = [Alternation([Alternate(["2"], 0.25), Alternate(["3"], 0.25), Alternate(["4"], 0.25), Alternate(["5"], 0.25)])]
production_NUMBER = Production(production_NUMBER_lhs, production_NUMBER_rhs)

productions = [production_S, production_COURSE, production_EGG, production_BUN, production_BREAKFAST, production_LUNCH, production_DINNER, production_TOPPING, production_NUMBER, production_DESSERT]

grammar = CFGrammar(non_terminals, terminals, start_symbol, productions)

grammar.genRandSentence(start_symbol)

test3out = Output(grammar.output)
print("OUT:",grammar.output)
print('\n')
print("string: ",test3out.returnString())



print("TEST 4")
#Test 4:
#Testing Repeat functionality: PASSED
start_symbol = "first"
terminals = ["dog", "cat", "clouds", "sun", "earth", "monsoon"]
non_terminals = ["first", "second", "third"]

production_one_lhs = "first"
production_one_rhs = [Repeat(["sings", "rests"],0,1), "runs"]
production_one = Production(production_one_lhs, production_one_rhs)

production_two_lhs = "second"
production_two_rhs = [Repeat([3.1, "third", "third"],0,1)]
production_two = Production(production_two_lhs, production_two_rhs)

production_three_lhs = "third"
production_three_rhs = [Repeat(["koolaid"],0,1)]
production_three = Production(production_three_lhs, production_three_rhs)

productions = [production_one, production_two, production_three]

grammar = CFGrammar(non_terminals, terminals, start_symbol, productions)

grammar.genRandSentence(start_symbol)

print("OUT:",grammar.output)
print('\n')
test4out = Output(grammar.output)
print("string: ",test4out.returnString())


#test4.5
print("TEST4.5")
start_symbol = "number"
terminals = [0,1,2,3,4,5,6,7,8,9]
non_terminals = ["number"]

number_lhs = "number"
number_rhs = [
    Repeat (
        Alternation(
            [
                Alternate([0,0], 0.1),
                Alternate([1], 0.1),
                Alternate([2], 0.1),
                Alternate([3], 0.1),
                Alternate([4], 0.1),
                Alternate([5], 0.1),
                Alternate([6], 0.1),
                Alternate([7], 0.1),
                Alternate([8], 0.1),
                Alternate([9], 0.1)
            ]
        ),0,3)
]
number = Production(number_lhs, number_rhs)
productions = [number]
grammar = CFGrammar(non_terminals, terminals, start_symbol, productions)

grammar.genRandSentence(start_symbol)

print("OUT:",grammar.output)
print('\n')
test4out = Output(grammar.output)
print("string: ",test4out.returnString())



#Test 5:
#Testing Optional functionality: PASSED
print("TEST 5")

start_symbol = "first"
terminals = ["dog", "cat", "clouds", "sun", "earth", "monsoon"]
non_terminals = ["first", "second", "third"]

production_one_lhs = "first"
production_one_rhs = [Optional(["c", "first"]), Optional(["cat", "second"]), Optional(["dog"])]
production_one = Production(production_one_lhs, production_one_rhs)

production_two_lhs = "second"
production_two_rhs = [Optional(["c", "first"]), Optional(["cat"]), Optional(["dog"])]
production_two = Production(production_two_lhs, production_two_rhs)


productions = [production_one, production_two]

grammar = CFGrammar(non_terminals, terminals, start_symbol, productions)

grammar.genRandSentence(start_symbol)

print("OUT:",grammar.output)
print('\n')
test4out = Output(grammar.output)
print("string: ",test4out.returnString())

#Test 6:
#Testing probability for alternate total > 1: PASSED
print("TEST 6")
start_symbol = "first"
terminals = ["dog", "cat", "clouds", "sun", "earth", "monsoon"]
non_terminals = ["first", "second", "third"]

production_one_lhs = "first"
production_one_rhs = [Alternation([Alternate(["sun", "second"], 0.1), Alternate(Repeat(["moon", "first"],0,1), 0.1), Alternate(["third"], 0.8)])]
production_one = Production(production_one_lhs, production_one_rhs)

production_two_lhs = "second"
production_two_rhs = [Alternation([Alternate(["1.1"], 0.2), Alternate(Repeat(["33"],0,1), 0.5), Alternate(["f1"], 0.3)])]
production_two = Production(production_two_lhs, production_two_rhs)

production_three_lhs = "third"
production_three_rhs = [Alternation([Alternate(["2.1"], 0.2), Alternate(Repeat(["3.3"],0,1), 0.5), Alternate(["fjjj1"], 0.3)])]
production_three = Production(production_three_lhs, production_three_rhs)

productions = [production_one, production_two, production_three]

grammar = CFGrammar(non_terminals, terminals, start_symbol, productions)

grammar.genRandSentence(start_symbol)

print("OUT:",grammar.output)
print('\n')
test4out = Output(grammar.output)
print("string: ",test4out.returnString())
