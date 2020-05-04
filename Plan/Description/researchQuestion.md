Research Question
-----------------

### What: 
Create a grammar-based random sentence generator. After being given a grammar `G`, be able to create a random sentence `s`, or a set of sentences `S`,  based off of `G`.

##### However there are two extensions to be added:

• Add probabilities for alternatives in productions

• Context information to make the output from the grammar G well-typed

-------

### Why:
To create random sentences to be used for testing. Specifically, testing a parser or a natural language processor.

-------

### Related Works:
Although we have found works on randomly generating sentences, they have been for fixed grammars.
Some included grammar-based sentence generation, though the grammars it accepts are very specific.
As well, none of the related works found included well-typing nor probabilities for productions with alternatives.
