When checking out a new code base, CoPilot will primarily focus on the selected editor window and then use any open files are supplemental input.

## How to use Copilot with a new code base

When checking out a new code base, CoPilot will primarily focus on the selected editor window and then use any open files are supplemental input.   If you have a file open that is not in the same directory as the selected editor window, CoPilot will not be able to use that file as input.  If you have a file open that is in the same directory as the selected editor window, CoPilot will use that file as input.  If you have multiple files open that are in the same directory as the selected editor window, CoPilot will use all of those files as input.

## Using @workrspace in the chat

@workspace - Ask a question about the files in your current workspace

When asking questions about large code bases, it's helpful to break up questions about code in smaller modules.
Eg: front end, styles, API, databases, authentication flows, or specific business logic.


## Example:

Check out the DVWA: https://github.com/digininja/DVWA

Open up file: login.php

Prompts:

* `Explaining the code in login.php`
* `Create a network timing diagram in mermaid format`
* `Update the diagram with a treat modeling assessment`
* `Provide a threat assessment in STRIDE format`
* `@workspace explain with this application does`
* `@workspace create a system architecture diagram in mermaid format`