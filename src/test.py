from GrammarTools import *

test = Optional(Optional("hello"))
#print (test.evaluate(), end='')

test = Repeat(Optional("a"))
#print (test.evaluate(), end='')

test = Options([Option("d", 0.33), Option(Repeat("e"), 0.33), Option("f", 0.33)])
#print (test.evaluate())

'''
#Testing out the weighted probability for generating sentences

d = 0
e = 0
f = 0

for i in range (1000000):
    sample = test.evaluate()
    if 'd' in sample:
        d += 1
    elif 'e' in sample:
        e += 1
    elif 'f' in sample:
        f += 1

total = d + e + f

print ('total: ' + str(total))
print ('percent d: ' + str(d / total))
print ('percent d: ' + str(e / total))
print ('percent f: ' + str(f / total))
'''

production_one_lhs = "first"
production_one_rhs = ["a", Repeat("second"), "b"]
production_one = Production(production_one_lhs, production_one_rhs)

production_two_lhs = "second"
production_two_rhs = [Optional("c first"), Options([Option("d", 0.2), Option(Repeat("e"), 0.5), Option("f", 0.3)])]
production_two = Production(production_two_lhs, production_two_rhs)

print (str(production_one) + "  --->  " + production_one.evaluate())
print (str(production_two) + "  --->  " + production_two.evaluate(), end='')