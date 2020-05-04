# Project Proposal Plan

This is the project proposal plan for group 8 as part of CS 4TB3: Syntax-Based Tools and Compilers.

### Authors
Chen Chen 

Kael Boseland

Hamid Yuksel

## Description

### Research Question

#### What: 
Create a grammar-based random sentence generator. After being given a grammar `G`, be able to create a random sentence `s`, or a set of sentences `S`,  based off of `G`.


##### However there are two extensions to be added:

• Add probabilities for alternatives in productions

• Context information to make the output from the grammar G well-typed


#### Why:
To create random sentences to be used for testing. Specifically, testing a parser or a natural language processor.


#### Related Works:
Although we have found works on randomly generating sentences, they have been for fixed grammars.
Some included grammar-based sentence generation, though the grammars it accepts are very specific.
As well, none of the related works found included well-typing nor probabilities for productions with alternatives.


### Documentation Methodology

#### Report Format

We will be writting a wiki article for the specifications of the grammer generator loosely following the Volere format for software specifications. This is because we feel Volere does a better job at highlighting the most important areas of this project such as the needs, requirements and issues.

#### Sections

Key Sections of the report will be broken down into:

- Needs: Address the goal of the project and what we hope to accomplish. Define the scope of the project.
- Requirements: Functional and non-functional requirements to successfully meet our project needs.
- Issues: Issues and roadblocks along the way as well as current remaining issues and future risks to address.
- Definitions: A glossary of terms referenced in the report that is relevant to the project. 

#### Code Documentation

Since we will be using python as our language of choice for implementing the generator we will be using Pydocs format to comment the code for clarity.

#### Instructions

The instructions of the grammar parser will be located in the main readme that is stored in the repo of project. This is to make the instructions immedietely available to the user when they first access the repository. 



### Testing Methodology

#### Unit Tests

For each aspect of our project, we will need to create unit test suites to make sure that everything is running smoothly. For example, we will need a test suite to make sure our application can parse a grammar that the user passes in. We will need another test suite to make sure the application can parse the grammar and store the non-terminals, terminals and productions in our own defined objects. Next, we will need another test suite to make sure our appliction can use the grammar passed in to generate valid sentences. As we go, we may break down these issues further and make more test suites for each breakdown.

#### Integration Testing

Once we have a working model, we will want to add more testing to ensure the model is working properly. For this, we will keep an updated test suite to make sure that after each change/improvement we make the code still works with the existing sections and can pass our tests without any issues.

#### Functional Tests

Lastly, we will need functional tests that work at a higher level to ensure our product is outputting the correct results based on the inputs. At a high level, we will create functional tests where we will pass in a grammar and have our program output sentences, and we will check their validitity by running them through a parser for the language we passed into our program.



### Insight to be Gained

#### On Grammars and their implementation
The basis for this project involves an understanding of grammars and how they are implemented.
As such, it will involve learning a lot of tools commonly used to express grammars, including python, Go, and Lisp to name a few.
As well, we hope to learn about how to make tools that allow a user to freely express different grammars.    


#### On probability and its implementation
An understanding of probability will also come into play as we try to implement our probability extension on productions.
We should allow for the project to be liberal in how a user wants to express the probability for a production.
As such, programming tools involving the implementation of probability equations will also be learned.  


#### On typing and its compiler implementation
We will also have to make use of well-typing strategies, in order to ensure the program we output maintains well-typing.
To accomplish this we probably will have to learn about compiler design in order to make important decisions on achieving well-typing, while also preserving optimality.
This will provide us with a better understanding of typing, as well as its implementation in softare.


#### On artistry and poetry generation
Since the potential to generate random sentences, it could be a fun to figure out how to support "poetry". This would require learning more about poetry, 
such as its various structures and forms.


## Division of Work

### Individual Areas of Focus

#### Testing:

- Unit testing: ensure general functionality of generator
- Edge case testing: ensure special cases are covered

Person Responsible: Chen Chen

#### Project management

- Team lead: assure team is meeting deadlines
- Distribution of work: allocate work between team members 

Person Responsible: Hamid Yuksel

#### Research:

- Development side: research into libraries, packages, tools 
- Theory side: research into grammars, languages, compilers

Person Responsible: Kael Boseland 

### Group Responsibilities

#### Development:

- Contributing to code for the overall project
- Will be modified during the development process to more accurately address our need
 
#### Documentation:

- Readme on how to use the grammer generator
- Comments and docs for debugging and explanation

#### Poster:

- Design the poster and choose appropriate visuals to present data
- Compile data/examples from the parser and present them graphically
- Write up explanations explaining the project and its functionality


## Weekly Schedule

Our group plans to follow an agile development environment to ensure we complete our project cohesively and in a 
timely manner. 

### Weekly Meetings

The first idea we have is to have weekly in-person meetings where we will collaborate on our shared work which will consist of the design, development and testing of our project. These weekly meetings will take place on Thursdays between 3 to 6pm.

### Weekly Conference Calls

The second idea we have is to conference calls every week on Mondays to discuss our progress on the tasks this week. These calls do not have to be too in depth, mostly to touch on any issues that we are facing and to make sure everyone is on the same page for the project. We decided on conference calls because it is much more organized than communicating over text messages.

## Resources

Below are the resources found that may help with our project. 
This list will be continuously updated through the progress of the project.
All resources are linked as citation.

### Textbooks
1. [Compilers: Principles, Techniques & Tools](http://ce.sharif.edu/courses/94-95/1/ce414-2/resources/root/Text%20Books/Compiler%20Design/Alfred%20V.%20Aho,%20Monica%20S.%20Lam,%20Ravi%20Sethi,%20Jeffrey%20D.%20Ullman-Compilers%20-%20Principles,%20Techniques,%20and%20Tools-Pearson_Addison%20Wesley%20(2006).pdf)
2. [Programming Languages: Application and Interpretation](http://cs.brown.edu/courses/cs173/2012/book/)
3. [Parsing techniques: A Practical Guide](https://dickgrune.com/Books/PTAPG_2nd_Edition/)
4. [Survery of the State of the Art in Natural Language Generation](https://arxiv.org/pdf/1703.09902.pdf)


### Manuals
1. [Python Grammar](https://docs.python.org/3/reference/grammar.html)
2. [Intro to Grammars and Parsing Techniques](https://homepages.cwi.nl/~storm/teaching/sc1112/intro-parsing.pdf)
3. [Parsing in Python](https://tomassetti.me/parsing-in-python/)
4. [SimpleParse Grammars](http://simpleparse.sourceforge.net/simpleparse_grammars.html)
5. [Intro to Programming languages/Grammars](https://en.wikibooks.org/wiki/Introduction_to_Programming_Languages/Grammars)


### Articles
1. [Parsing CFGs using Lark](https://dexterritory.online/posts/parsing-context-free-grammars-using-lark/)
2. [Generating random sentence from a CFG](https://eli.thegreenplace.net/2010/01/28/generating-random-sentences-from-a-context-free-grammar)
3. [An Explanation of the Link Parser Output](https://www.link.cs.cmu.edu/link/explain-output.html)
4. [Parsec: direct style monadic parser combinators for the real world](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/parsec-paper-letter.pdf)
5. [Parsing Inputs](https://www.fuzzingbook.org/html/Parser.html)



### Software
1. [NLTK](https://www.nltk.org/)
2. [grammar-based-sentence-generator](https://github.com/hrs/grammar-based-sentence-generator)
3. [grammar](https://github.com/joshlf/grammar)
4. [sentence-generator](https://github.com/powellcj12/sentence-generator)
5. [sentenceGenerator](https://github.com/shrutika-dasgupta/SentenceGenerator)
6. [grammar_js](https://github.com/joshlf/grammar_js)
7. [prose](https://github.com/jdkato/prose)
8. [NLP-Python](https://github.com/susanli2016/NLP-with-Python)



### Videos
1. [CFG Using NLP](https://www.youtube.com/watch?v=b4nbE-pG_TM)
2. [Human Lanaguage Sentences](https://www.youtube.com/watch?v=luiUK4tMjy8)
3. [NLP in Python](https://www.youtube.com/watch?v=xvqsFTUsOmc)










