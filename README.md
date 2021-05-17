# A Probability-based Random String Generator 🐙

### Navigation

Inside the `src` folder: 
- GrammarTools.py `source code`
- simple_grammar_test.py `testing on CFG source code`
- CSG_test.py `testing on CSG source code`


Inside the `documentation` folder: 
- GrammarTools markdown #documentation, but you can just scroll down it's all included below
- 4tb3finalposter pdf #project poster

Inside the `Plan` folder, it will have: 
- description folder
- resources markdown
- schedule markdown
- work division markdown

Inside the `Description` folder are the markdown files for:
- research question
- testing methodology
- doc methodology
- insight to be gained.

<br/>
<br/>

# Grammar Tools Documentation

![alt text](https://www.poemhunter.com/i/poem_images/974/the-octopus.jpg "Logo Title Text 1")

1. [ Purpose ](#purpose)
2. [ Sequence Wrappers ](#sequencewrappers)
3. [ Productions ](#productions)
4. [ Modeling a Grammar ](#modelingagrammar)
5. [ Example ](#example)

<a name="purpose"></a>
## Purpose

`GrammarTools` is a library created in python that is used to make it simple for users to represent grammars, and use our library to generate random sentences based on these grammars. The main use of this sentence generator would be to test parsers for a language, by taking the sentences as input.

`GrammarTools` gives users the option to model both context-free grammars and context-sensitive grammars and use these models to generate random typed sentences in an intuitive way.

<a name="sequencewrappers"></a>
## Sequence Wrappers

Our library has a variety of wrappers, and gives the user the option to represent an entire grammar including a start symbol, terminals, non-terminals and a list of productions. The library can also be used to model a single production.

Productions are modeled as a list of production objects. These objects include the basics of grammars: repetition of a sequence, alternative options, and optional sequences.

Each wrapper also comes with an `evaluate()` function for testing purposes, as well as a unique `__repr__()` function for accuracy when testing.

### Repetition

Sequences that can be repeated by the grammar are represented in the `Repeat` object. For example `{ "abcd" }` would be represented as:

``` python
    abcd = Repeat(["abcd"])
```

The `Repeat` object takes the value to be repeated (wrapped in a list) as it's first parameter. The `Repeat` object also has two optional parameters, min and max. These are the minimum and maximum times the sequence can be repeated. If the user does not pass in the min or max parameter they are set to 0 and 5 respectively.

Pythons' dynamic typing allows us to support multiple types to be included in the repeat sequence. The value to be repeated can be a string value, an integer, a double, another sequence wrapper or any combination of these. For example:

``` python
    value = Repeat(Optional(["hello"]))
```

is a valid representation, as well as:

``` python
    value = Repeat(["abcd", 1, Optional(["hello"])])
```

Each of our wrappers comes with an `evaluate()` function that can be used for testing. For example, let's use the object from above:

``` python
    abcd = Repeat(["abcd"])
    abcd.evaluate() #returns ['abcd', 'abcd', 'abcd']
```

### Optional

Sequences that can occur 0 or 1 times in the grammar are represented in the `Optional` object. For example, `[ "abcd" ]` would be represented as:

``` python
    abcd = Optional(["abcd"])
```

Just like our `Repetition` object, pythons' dynamic typing allows us to wrap another object from `GrammarTools` in an `Optional` wrapper. Also, we can wrap a list of multiple types just like when we use `Repetition`. The `Optional` wrapper only takes one parameter, the sequence that is optional.

``` python
    value = Optional(Repeat(["hello"]))
```

This would be a representation of the EBNF sequence `[ { "hello" } ]`

For testing, we can use our `evaluate()` function on the object to ensure the sequence wrapper is working correctly. For example, let's use the example above:

``` python
    value = Optional(Repeat(["hello"])
    value.evaluate() #could return [] or ['hello', 'hello']
```
### Alternation

Alternations represent choice in a grammar. The `Alternation` object takes a list of `Alternate` objects as it's only parameter, and uses the probabilities of each option to evaluate the sequence. 

Each alternate option in the alternations is represented by an `Alternate` object. This is a wrapper similar to the above objects, except it has two fields: `content` and `probability`. The `content` field can contain one of the above wrappers, or a list of the sequence (the list can contain any type! --> for example ["ok"] and ["hello", 1, 3] are both valid). The `probability` field contains a float up to two decimal places to represent the percentage.

For example, we can have `"a" | "b"` and each option would have a percentage attached. If we wanted to attach the percentages 60% and 40% respectively, we would represent the options by creating an `Alternation` object, which takes a list of `Alternate` objects as a parameter.

``` python
    Alternation([Alternate(["a"], 0.6), Alternate(["b"], 0.4)])
```

The `Alternate` object can also take another object as the `content` field. For example, the sequence `"a" | { "b" }` with percentages 40% and 60% respectively would be represented by:

``` python
    Alternation([Alternate(["a"], 0.4), Alternate(Repeat(["b"], 0.6)])
```

We can also use the `evaluate()` function on our alternate object for testing purposes. Since our `Alternation` object has to deal with probabilities, we use a weighted random choice to pick the outcome of the `Alternation` sequence. For an example, we used the following block of code to test the accuracy of our weighted probabilities:

``` python
    test = Alternation([Alternate(["d"], 0.33), Alternate(Repeat(["e"]), 0.33), Alternate(["f"], 0.33)])
    d, e, f = 0, 0, 0

    for i in range (10000):
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
```

<a name="productions"></a>
## Productions

Our implementation now supports two different types of productions. The first production object is called `Production`, and it is used in our `Grammar` class which represents a context-free grammar. The second production object is called `SensitiveProduction` and it is used in our `CSGrammar` class which represents our context-sensitive grammars.

### The Production object

We can model productions using a list of sequence wrappers. The `Production` class takes two parameters, the non-terminal it represents as the LHS and a list of the sequence wrappers as the RHS of the production.

For example, the production `A -> "a" | { "b" } | [ "c" ]` with percentages 40% , 30% and 30% respectively would be modeled like so:

``` python
    prod = Production("A", [Alternation(Alternate(["a"], 0.4), Alternate(Repeat(["b"]), 0.3), Alternate(Optional(["c"]), 0.3))])
```

An example of a production with a sequence of possibilities would be the production `A -> "a" { "a" } [ "b" ]`. This would be represented like so:

``` python
    prod = Production("A", [["a"], Repeat(["a"]), Optional(["b"])])
```

Each `Production` object also comes with an `evaluate` function, just like each of our sequence wrappers. This function returns whatever sentence the single production it was used on produces. For example, we can use the production above:

``` python
    prod = Production("A", ["a", Repeat(["a"]), Optional(["b"])])
    print (prod.evaluate()) #prints 'a a a a b'
```

Each `Production` object also comes with a unique `__repr__()` function, which returns the production modeled in EBNF form. For example:

``` python
    prod = Production("A", [["a"], Repeat(["a", 1]), Optional(["b", 2])])
    print (prod) #prints `A ::= a { a } [ b ]`
```

### The SensitiveProduction object

The `SensitiveProduction` object is used to represent productions in a context-sensitive grammar. Since a production in a context-sensitive grammar can match a sequence instead of just a one-word non-terminal (for example, `A a B -> a C d`), representing the production is a bit trickier.

The LHS of the production is represented by a list of non-terminals and terminals. For example,

``` python
    sensitive_production_lhs = ["a", "A", "c"]
```

The RHS of the production is represented the same way as our `Production` class - using a list to represent the sequence that the production generates. For example:

``` python
    sensitive_production_rhs = ["a", "b", "A", "c"]
```

Similarly to the `Production` object, you can use extra brackets for nesting. For example, if the rhs was modelled like this:

``` python
    sensitive_production_rhs = ["a", ["b, "A"], "c"]
```

it would produce a different output when evaluated. The `SensitiveProduction` class also has an `evaluate()` function for testing purposes. An example of it being used can be found be below:

``` python
    prod = SensitiveProduction(["a", "A", "c"], [["a", ["b", "A"]], "c"])
    print (prod.evaluate())

    prod = SensitiveProduction(["a", "A", "c"], ["a", "a", Repeat(["a"])])
    print (prod.evaluate())

    #sample output
    [['a', ['b', 'A']], 'c']
    ['a', 'a', ['a', 'a']]
```

<a name="modelingagrammar"></a>
## Modelling a Grammar

We can model two different types of grammars, context-sensitive grammars as well as context-free grammars. Context-free grammars are modeled by the `CFGrammar` class and context-sensitive grammars are modeled by the `CSGrammar` class.

### The CFGrammar class

The `CFGrammar ` object is what we use to generate our random sentences. The constructor takes 5 arguments:

* A list of non-terminal information
* A list of terminal information
* A start symbol
* A list of productions

An example of defining a grammar is shown below:

``` python
    grammar = CFGrammar(non_terminals, terminals, start_symbol, productions)
```

##### Non-Terminals (1st Param)

The non-terminal information is simply a list of each non-terminal in string form. For example:

``` python
    non_terminals = ["first", "second", "third"]
```

##### Terminal Information

The terminal information is simply a list of each terminal in string form. For example:

``` python
    terminals = ["a", "b", "c", "d"]
```

##### Start Symbol (3rd Param)

The start symbol is simply the first production we will start at when generating the random sentence, and it is in string form. For example:

``` python
    start_symbol = "first"
```

##### Productions (4th Param)

In the above section we went over how to create a production using our `Production` type, and this parameter simple contains a list of the productions. For example, assuming production\_one, production\_two and production\_three are of the type `Production`:

``` python
    productions = [production_one, production_two, production_three]
```

### The CSGrammar class

The `CSGrammar` class is used to model context-sensitive grammars. The parameters it takes when instantiated are the same as the above `CFGrammar` class.

However, there are two important distinctions between the `CSGrammar` class and the `CFGrammar` class. 

The `CSGGrammar` class only takes productions modeled by the `SensitiveProduction` object, whereas `CFGrammar` takes productions modeled by the `Production` object.

``` python
    prod = SensitiveProduction(["a", "A", "c"], [["a", ["b", "A"]], "c"])
```

As well, the `start_symbol` for `CSGrammar` must be wrapped in a list.

``` python
    start_symbol = "first"
```

#### Generating Random Sentences

The purpose of modeling grammars using our classes `CFGrammar` and `CSGrammar` is to generate random sentences with the extensions our project provides (probability and typing).

We made our own algorithms to generate these sentences from the modeled grammar and for both objects you can generate sentences using the same function: `genRandSentence()`

The function `genRandSentence()` takes one parameter --> the production you would like to start producing a sentence at. For most users, you would start producing from the start symbol. An example of the process of generating a sentence is below:

``` python
    grammar = CSGrammar(non_terminals, terminals, start_symbol, prods)
    grammar.genRandSentence(start_symbol)
```

Once the sentence is generated, the output can be found in the object variable `output` corresponding to the grammar object. For example:

``` python
    print (grammar.output)
```

would print the generated sentence in list form.

#### Output 

The Output class is was designed to improve readibility and to create useful output type for `grammar.output`. Where `grammar.output` may maintain the original types, it may be confusing due to nested lists as well weakly typed programs may struggle to interpret the output. Therefore, the Output returns a clean string with included whitespace.

To use output, a new output object is to be created with `grammar.output` as the parameter. The command `.returnString()` will return the output all converted to strings. Therefore, 

``` python
    Output(grammar.output).returnStrings()
```

can be used to convert any grammaroutput to all strings. 

<a name="example"></a>
# Example Poetry Grammar

Here is a grammar that generates 'poetry'. Of course, it faces the same challenges of turning a formal language (English) into a rigorous one.

``` python
    start_symbol = "S"
    terminals = ["dog", "cat", "clouds", "sun", "earth", "monsoon"]
    non_terminals = ["NP", "VP", "PN", "ART", "VERB", "NOUN", "ADJ", "PREP"]

    production_S_lhs = "S"
    production_S_rhs = ["NP", "VP"]
    production_S = Production(production_S_lhs, production_S_rhs)

    production_NP_lhs = "NP"
    production_NP_rhs = [Alternation([Alternate(["ART", "NOUN"], 0.2), Alternate(["ART", "ADJ", "NOUN"], 0.5), Alternate(["PN"], 0.3)])]
    production_NP = Production(production_NP_lhs, production_NP_rhs)

    production_VP_lhs = "VP"
    production_VP_rhs = [Alternation([Alternate(["VERB", "NP"], 0.2), Alternate(Repeat(["VERB", "PREP", "NP"]), 0.8)])]
    production_VP = Production(production_VP_lhs, production_VP_rhs)

    production_PN_lhs = "PN"
    production_PN_rhs = [Alternation([Alternate("Siberia", 0.4), Alternate("El Dorado", 0.2), Alternate("Earth", 0.4)])]
    production_PN = Production(production_PN_lhs, production_PN_rhs)

    production_ART_lhs = "ART"
    production_ART_rhs = [Alternation([Alternate("a", 0.4), Alternate("the", 0.6)])]
    production_ART = Production(production_ART_lhs, production_ART_rhs)

    production_VERB_lhs = "VERB"
    production_VERB_rhs = [Alternation([Alternate("smiles", 0.4), Alternate("sings", 0.1), Alternate("reprimands", 0.1), Alternate("reviles", 0.1), Alternate("revolves", 0.1), Alternate("resides", 0.1), Alternate("relaxes", 0.1)])]
    production_VERB = Production(production_VERB_lhs, production_VERB_rhs)

    production_NOUN_lhs = "NOUN"
    production_NOUN_rhs = [Alternation([Alternate("monster", 0.1), Alternate("flower", 0.1), Alternate("pizza", 0.1), Alternate("dog", 0.1), Alternate("cat", 0.1), Alternate("ocean", 0.1), Alternate("sun", 0.1), Alternate("crevace", 0.1), Alternate("tsunami", 0.1), Alternate("volcano", 0.1)])]
    production_NOUN = Production(production_NOUN_lhs, production_NOUN_rhs)

    production_ADJ_lhs = "ADJ"
    production_ADJ_rhs = [Alternation([Alternate("green", 0.1), Alternate("mean", 0.1), Alternate("lean", 0.1), Alternate("rough", 0.1), Alternate("soft", 0.1), Alternate("bright", 0.1), Alternate("dark", 0.1), Alternate("mellow", 0.1), Alternate("fiery", 0.1), Alternate("mystic", 0.1)])]
    production_ADJ = Production(production_ADJ_lhs, production_ADJ_rhs)

    production_PREP_lhs = "PREP"
    production_PREP_rhs = [Alternation([Alternate("about", 0.1), Alternate("above", 0.1), Alternate("across", 0.1), Alternate("after", 0.1), Alternate("against", 0.1), Alternate("before", 0.1), Alternate("along", 0.1), Alternate("by", 0.1), Alternate("like", 0.1), Alternate("at", 0.1)])]
    production_PREP = Production(production_PREP_lhs, production_PREP_rhs)

    productions = [production_S, production_NP, production_VP, production_PN, production_ART, production_VERB, production_NOUN, production_ADJ, production_PREP]

    grammar = CFGrammar(non_terminals, terminals, start_symbol, productions)
    grammar.genRandSentence(start_symbol)

    print (grammar.output)
 ```

### Some fun poetry

Here are some random poetry we generated:

Untitled 1.

    a ocean reviles at the mellow volcano
    reprimands by Earth
    relaxes at the dark flower
    relaxes like Earth
    smiles above

Untitled 2.

    a bright flower
    smiles against
    the tsunami
    
Untitled 3.

    the rough tsunami,
    the ocean smiles before a ocean reviles above El Dorado
    smiles against a green crevace

Untitled 4.

    a bright volcano
    resides before the fiery ocean

Untitled 5.

    the flower
    the fiery dog revolves above the flower
    
    
Untitled 6.

    sneezes like
    the tsunami smiles above
