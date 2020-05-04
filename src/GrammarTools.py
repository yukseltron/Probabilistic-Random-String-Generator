import random
import re
import math
#import output

'''
To use this class to create a string, we will start at the start symbol and find the production for the start symbol.
Then, we can use a loop to iterate through the the production and start creating the sentence. If we come across
a reference to another production, then we will go to that production and create that section of the sentence. We
know that it is a reference to another production because it will not be wrapped in double quotes.
'''

class Production:

    #this will take a string as the LHS and a string as the RHS
    def __init__ (self, LHS, RHS):
        self.LHS = LHS
        self.RHS = RHS

    def __repr__ (self):
        string = [self.LHS, " ::= ",self.RHS]
        return string

    #This function will be used to evaluate a single production
    def evaluate (self):
        output = []
        #print(self.RHS)
        for prod in self.RHS:
            #print("PROD:",prod)
            if type(prod) == list:
                if type(prod) == Optional or type(prod) == Repeat or type(prod) == Alternation:
                    val = prod.evaluate()
                    output.append(val)
                else:
                    val = prod
                    output.append(val)
            elif isinstance(prod, Optional) or isinstance(prod, Repeat) or isinstance(prod, Alternation):
                val = prod.evaluate()
                #print("VAL",val)
                output.append(val)
            else:
                val = prod
                output.append(val)

        return output

class Alternation:

    #This class will store a list of Option objects
    def __init__ (self, alternations):
        self.alternations = alternations

    def __repr__ (self):
        string = '( '
        for alternate in self.alternations:
            string += str(alternate) + " | "
        return string[:-3] + ' )'

    #This function will return a result of which option was picked by using a weighted probability
    def evaluate (self):
        try:
            weights = []
            probabilityTotalCheck = 0.0 #checking probability is well defined (must == 1 after loop)
            count = 0
            #print("P:", probabilityTotalCheck) testing purposes
            for alternate in self.alternations:
                probabilityTotalCheck += alternate.probability
                weights += [count] * (int(alternate.probability * 100))
                count += 1

            #print("P:", probabilityTotalCheck) testing purposes
            if math.ceil(probabilityTotalCheck) != 1.0 :
                raise ProbabilitySumError #sum of probability weights in production do not total 1
        except ProbabilitySumError:
                    print ("ERROR: probability is ill-defined. Your probability weights should total 1.0")
                    print ("Currently, it totals:",probabilityTotalCheck)
                    print ("Production in question: ", self.alternations)
        else:
            choice = random.randint(0, len(weights)-1)
            return self.alternations[weights[choice]].evaluate()



class Alternate:

    #This class stores the option and it's probability (probability should be a decimal up to 2 decimal points)
    def __init__ (self, content, probability):
        self.content = content
        self.probability = probability

    def __repr__ (self):
        return str(self.content) + " @ " + str(self.probability)

    #This function returns the content created by the result
    def evaluate (self):
        if type(self.content) == list:
            return self.content
        elif isinstance(self.content, Optional) or isinstance(self.content, Repeat) or isinstance(self.content, Alternation):
            return self.content.evaluate()
        else:
            return self.content



class Repeat:

    #This class will store the string that is to be repeated
    def __init__ (self, content, min=0, max=5):
        self.content = content
        self.min = min
        self.max = max

    def __repr__ (self):
        return "{ " + str(self.content) + " }"

    #This class will return the content created by the repeated value
    def evaluate (self):

        repeat = []
        rep = []
        number = random.randint(self.min,self.max)
        if isinstance(self.content, Optional) or isinstance(self.content, Repeat) or isinstance(self.content, Alternation):
            repeat.extend(self.content.evaluate())
            rep = repeat.copy()
        else:
            repeat = self.content.copy()
            rep = repeat.copy()
        for i in range(number):
            #print("B", repeat,number) #before
            repeat.extend(rep)
            #print("A", repeat) #after
        for i in range(len(repeat)):
            if isinstance(repeat[i], Optional) or isinstance(repeat[i], Repeat) or isinstance(repeat[i], Alternation):
                #print("R:",repeat[i])
                repeat[i] = repeat[i].evaluate()
                #print("R2:",repeat[i])
        return repeat




class Optional:

    #This class will store the string that is optional in the production (for example ["hello"] represents optional in an ebnf grammar)
    def __init__ (self, content):
        self.content = content

    def __repr__ (self):
        return "[ " + str(self.content) + " ]"

    #This function will return the content created by the optional value
    def evaluate (self):
        choice = random.randint(0,1)

        if choice == 1:
            if type(self.content) == list:
                #note: deal with case that the name of a non-terminal is returned in generateSentence()
                return self.content
            elif isinstance(self.content, Optional) or isinstance(self.content, Repeat) or isinstance(self.content, Alternation):
                return self.content.evaluate()
            else:
                return self.content
        else:
            return ""



class CFGrammar:

    #This will hold the essentials of the grammar
    #non_terminals will hold all of the non_terminals of the grammar
    #terminals will hold all of the terminals of the grammar, as well as the type of the value
    #start_symbol will hold the starting production/symbol in the grammar
    #productions will hold a dictionary that uses the LHS of the productions and maps them to the linked lists

    def __init__ (self, non_terminals, terminals, start_symbol, productions):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.start_symbol = start_symbol
        self.productions = self.storeProductions(productions)
        self.output = []

    def storeProductions (self, productions):
        productionDict = {}

        for production in productions:
            productionDict[production.LHS] = production

        return productionDict

    #recursively go through productions starting at start symbol
    def genRandSentence (self, prod):
        sequence = self.productions[prod].evaluate()
        #print("SEQUENCE", sequence)

        for item in sequence:
            if isinstance(item, list):
                for i in item:
                    if i in self.non_terminals:
                        self.genRandSentence(i)
                    else:
                        self.output.append(i)
            else:
                if item in self.non_terminals:
                    self.genRandSentence(item)
                else:
                    self.output.append(item)







#Context Sensitive code below
#Author: Hamid Yuksel
class SensitiveProduction:

    #this will take a string as the LHS and a string as the RHS
    def __init__ (self, LHS, RHS):
        self.LHS = LHS
        self.RHS = RHS

    def get (self):
        l = [self.LHS, " ::= ",self.RHS]
        return l

    #This function will be used to evaluate a single production
    def evaluate (self):
        output = []
        for prod in self.RHS:
            #print("PROD:",prod)
            if type(prod) == list:
                subOutput = []
                for subProd in prod:
                    if type(subProd) == Optional or type(subProd) == Repeat or type(subProd) == Alternation:
                        val = subProd.evaluate()
                        subOutput.append(val)
                    else:
                        val = subProd
                        subOutput.append(val)
                output.append(subOutput)
            elif isinstance(prod, Optional) or isinstance(prod, Repeat) or isinstance(prod, Alternation):
                val = prod.evaluate()
                #print("VAL",val)
                output.append(val)
            else:
                val = prod
                output.append(val)

        return output


#Author: Hamid Yuksel   
class CSGrammar:

    #This will hold the essentials of a context sensitive grammar
    #non_terminals will hold all of the non_terminals of the grammar
    #terminals will hold all of the terminals of the grammar, as well as the type of the value
    #start_symbol will hold the starting production/symbol in the grammar
    #productions will hold a dictionary that uses the LHS and RHS of the production

    def __init__ (self, non_terminals, terminals, start_symbol, productions):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.start_symbol = start_symbol
        self.productions = productions
        self.output = []
        self.finalOutput = []


    def genRandSentence (self, prod):
        if type(self.maybeEvaluate(prod)[0]) == list:
            prod = prod[0].copy()
        #print("PROD",prod)

        validProds = self.matchSublists(prod) #first find the possible matches (replacements)
        if len(validProds) > 0: #if there are some, we can keep producing
            chosenProd = self.getRandomMatch(validProds)
            #print("BEFORE: ", prod)
            prod = self.replaceSequence(chosenProd)
            #print("AFTER: ", prod)
            prod = self.genRandSentence(prod)
        else: #else it's all terminals
            self.output.extend(prod)


    def replaceSequence (self, chosenProd):#replace part of the prod with the appropriate production rule
        replace = ''
        start = chosenProd[2]
        end = chosenProd[3]
        flatReplace = []
        for i in self.productions:
            if i.LHS == chosenProd[0]:
                #print(i.LHS, "->",i.RHS)
                replace = i.RHS.copy()
                replace = self.maybeEvaluate(replace)

        #print("2",chosenProd[1][start:end+1])
        #print("3Before",replace)
        for i in replace: #flatten the list (no more 2d arrays)
            if type(i) == list:
                for j in i:
                    flatReplace.append(j)
            else:
                flatReplace.append(i)

        if type(replace[0]) == list:
            replace = replace [0]
        #print("REP",chosenProd[1][start:end+1], "with",flatReplace)
        chosenProd[1][start:end+1] = flatReplace

        return chosenProd[1]


    def getRandomMatch (self, validProds): #pick a random matching from production
        if len(validProds) > 1:
            choice = random.randint(0,len(validProds)-1)
            return validProds[choice]
        else:
            #print(validProds)
            return validProds[0]


    def matchSublists (self, prod):#prod given as a list
        validProds = []
        counter = 0
        for i in self.productions: #match sublist to list and eventually pick best choice
            counter += 1
            sublength = len(i.LHS)
            length = len(prod)

            for j in range(length-sublength+1):#matching the list to any sublists in the larger list
                #print(i.LHS,"<>", prod[j:j+sublength])
                if isinstance(prod[j:j+sublength], Alternation):
                    prod[j:j+sublength] = prod[j:j+sublength].evaluate()
                if i.LHS == prod[j:j+sublength]:
                    validProds.append([i.LHS, prod, j,j+sublength-1, counter])#include range too of the substring if repeats, and counter

        return validProds


    def maybeEvaluate (self, prod): #recursively evaluate if possible
        for i in range(len(prod)):
            if isinstance(prod[i], Alternation) or isinstance(prod[i], Repeat) or isinstance(prod[i], Optional):
                prod[i] = self.maybeEvaluate(prod[i].evaluate())

        return prod

class Output:

    def __init__(self, grammarOutput): #creates output object
        self.gOutput = grammarOutput
        self.finalString = ""

    
    def addChar(self, out): #taking new char as parameter and appending to final string     
        if type(out) == list:
            for i in out:
                self.addChar(i) 
        elif type(out) == str: #adding string chars directly
            try:
                if type(int(self.finalString[-1:])) == int: 
                    self.finalString += " " + out + " "
            except: 
                self.finalString += out + " "
        elif type(out) == float:
            try:
                if type(int(self.finalString[-1:])) == int: 
                    self.finalString += " " + str(out) + " "
            except:
                self.finalString += str(out) + " "
        elif type(out) == int: #adding ints to list as well         
            self.finalString += str(out)

    def returnString(self): #return final string
        for i in self.gOutput:
            self.addChar(i)
        return self.finalString


#EXCEPTIONS
#Author: Hamid Yuksel
class ProbabilitySumError(Exception):
   """Raised when the probability weights do not total 1"""
   pass
