# Summary

This module shows a simple SQL Injection in python and using Copilot to ask a recommendation on how to fix it.

## Prompts

* Simply ask: `what security problems are there in this file?`
* In order to sanitize the input, highlight the query statement in the editor and ask: `sanitize this input`

Additionally, you can ask for a STRIDE security review on the file to look for other vulnerabilities and suggestions. 

# Exercises

* Use `/fix` to fix the security vulnerability.
* Ask Copilot how you would exploit this code?
* Ask Copilot to create a Pull Request description for the fix.

# References

* Security Prompts for Copilot: https://github.com/austimkelly/blog/blob/main/doc/security_prompts_for_copilot.md
* SQL Injection: https://owasp.org/www-community/attacks/SQL_Injection
