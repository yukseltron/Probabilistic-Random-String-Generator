Testing Methodology
-------------------

### Unit Tests

For each aspect of our project, we will need to create unit test suites to make sure that everything is running smoothly. For example, we will need a test suite to make sure our application can parse a grammar that the user passes in. We will need another test suite to make sure the application can parse the grammar and store the non-terminals, terminals and productions in our own defined objects. Next, we will need another test suite to make sure our appliction can use the grammar passed in to generate valid sentences. As we go, we may break down these issues further and make more test suites for each breakdown.

### Integration Testing

Once we have a working model, we will want to add more testing to ensure the model is working properly. For this, we will keep an updated test suite to make sure that after each change/improvement we make the code still works with the existing sections and can pass our tests without any issues.

### Functional Tests

Lastly, we will need functional tests that work at a higher level to ensure our product is outputting the correct results based on the inputs. At a high level, we will create functional tests where we will pass in a grammar and have our program output sentences, and we will check their validitity by running them through a parser for the language we passed into our program.