# copilot-examples
Code snippets and examples demonstrating GH Copilot functionality. This content is complimentary to the [Copilot for Developers (Intermediate) Workshop](https://github.com/services/github-copilot-for-developers-intermediate ).

## Branches

* `main` - This is the starting point with _incomplete_ examples. There are **TODO** comments in each of the example module readme files.
* `completed-exercises` - These is the completed exercises with working code examples. 

### Note on variety of results

Generative AI, by definition, can yield very different results based on session content and variations in how questions are asked. Do not expect to get identical results as `completed-exercises`, even with the same prompts!

# Installation

1. Clone the repository:

`git clone git@github.com:Atmosera-CoPilot-Dev/copilot-examples.git`

2. Switch to the `start-labs`` branch:

`git checkout start-labs`
`git pull`

3. Open up the `copilot-repository` folder in VS Code.

4. Command line utilities used in the apps:

You can install these on the fly if you have `brew` (macOS) or `choco` (Windows) installed. 

* Python3 (with pip3)
* sqlite
* Go
* Docker
* npm

5. Mermaid VS Code extensions:

* Markdown Preview Mermaid Support extension for VS Code [installation](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) - This is to render and view visual architecture-diagrams-as-code in markdown.

6. We will also use Damn Vulnerable Web App for an exercise: https://github.com/digininja/DVWA

`git clone https://github.com/digininja/DVWA.git`

Add this repository to your VS Code workspace.

# Pre-requisites

You will need basic knowledge of Git, GitHub, and working with the terminal. Additionally you will need:

1. Visual Studio Code installed - [Download](https://code.visualstudio.com/download) VS Code.
2. Copilot extension installed - [Download](https://code.visualstudio.com/docs/editor/github-copilot) GitHub Copilot extension for VS Code.
3. A Copilot enabled GitHub account - See [Quickstart for GitHub Copilot](https://docs.github.com/en/copilot/quickstart).

# Copilot Examples Content

Here's a quick rundown of the modules and a suggested order of presenting. Each module show a different aspect of software development, design and architecture. The modules are meant to be taught in order, but can really cherry picked as desired.

| Topic                                 | What we'll cover                                                                                       |
|---------------------------------------|-------------------------------------------------------------------------------------------------------|
| `.copilot_ignore`                     | See the .copilot_ignore file in the root of this repo. This is a file that Copilot will use to ignore certain files and directories. It's useful to know about this file as it can be used to ignore files that you don't want Copilot to suggest on. |
| Simple prompts in code editor         | See [development-q-and-a](./development-q-and-a/) - Here are just some simple prompts in Javascript comments to show how Copilot makes in editor suggestions. |
| Basic function and unit test building | See [regexp](./regexp/) - Here's we'll build a regular expression, a function to check if an input is a regexp match and some unit tests to verify the function works. |
| Rest API in a command-line utility     | See [api](./api/) - Here we'll use Copilot to build a simple API that returns the weather for a given latitude and longitude. This covers also just building a simple command-line utility. |
| Architecture Diagrams                  | See [architecture](./architecture/) - Here we'll use Copilot to build a simple architecture diagram using Mermaid. |
| Markdown                              | See [markdown](./markdown/) - Here we'll use Copilot to build a simple markdown document with a table of contents and some sections. |
| Code translation                      | See [translate-code](./translate-code/) - Here we'll use Copilot to translate some code from Python to Go. |
| SQL generation                        | See [sql](./sql/) - Here we'll use Copilot to build a simple SQL queries on a 3 table sqlite DB. |
| Security code review                  | See [security](./security/) - Here we have a python script that suffers from SQL injection. We'll ask Copilot if there are any vulnerabilities and it will suggest a fix. |
| Getting up to speed on a new code base | See [new-codebase](./new-codebase/) - Here we'll look at how you can use Copilot to get up to speed on a new code base. |
| Infrastructure as Code                | See [iac](./iac/) - Here we'll use Copilot to build some boilerplate infrastructure as code using Docker to wrap a Python Flask hello world app. It should run on port 5001. |


