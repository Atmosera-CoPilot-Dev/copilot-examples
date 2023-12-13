# Summary

This module shows a couple of examples of generating regular expressions from code comments as prompts, generating a function to test if a pattern follows the regexp and finally some examples of running a unit test.
We'll just a basic JavaScript app to show this functionality.

# TODO: Sample prompts

## Staring from Copilot Chat
``` 
Write me a javascript function that will check is an email address is a valid format using regexp. Make the regexp a global variable. 
Also include unit tests with both invalid and valid email addresses and proper comments on how to run the unit tests
```

## Alternatively, we could start from a comment in the code editor:

```
// Global regular expression for email validation
```

```
// Function that checks if an email address is valid. Returns true if valid, false otherwise.
```

```
// Unit tests for isEmail function.  
```

Alternatively, use `/test`` in a Copilot prompt.

We can repeat this process for verifying a phone number is valid as well for practice.

## Alternative for generating tests

If you open inline chat and prompt with `/tests` and hit enter, it will generate tests for you (typically in a separate file)

## Running the app tests

To run `app.js` in the root of this folder, run `npm test` from the command line.

# References

* Seeing your first suggestion: https://docs.github.com/en/copilot/using-github-copilot/getting-started-with-github-copilot#seeing-your-first-suggestion-1
* Introducing Copilot Chat: https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat-in-your-ide#asking-your-first-question-1