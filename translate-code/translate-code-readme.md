This is an example of how you can use Copilot to translate code from one language to another. In this case, we'll translate from Python to Go.

## Prompts

First select [weather.py](../api/weather.py) and then run the following prompts:

* `Translate weather.py from Python to Go`
* `Expain how I would run this if I had never used Go before. Provide the results in markdown format`

## Results

* [weather.go)](./weather.go) - The working utility in Go.
* The install and run instructions below.
* We're going to run into string/date conversion issues with the AtoI function. For starters, we can just keep the date as a string since we don't need to manipulate it, so we ask Copilot:

```
translate weather.py to Go. Please treat the date as a string and don't do any date or time conversions.
```

# Installing Go and Running the App

To run Go code, you first need to install Go on your machine. Here are the steps:

Install Go: You can download Go from the official website: https://golang.org/dl/. Choose the distribution appropriate for your system. The website has installations for Linux, macOS, and Windows.

Verify the installation: Open a terminal and type go version. This should display the installed version of Go.

Run the Go code: Save the Go code in a file with a .go extension, for example main.go. To run the code, open a terminal, navigate to the directory containing your main.go file, and type go run main.go.

In the context of the weather program you've been given, you would need to pass latitude and longitude as command-line arguments. For example, if you want to get the weather for New York City (latitude 40.7128 and longitude -74.0060), you would run:

`go run weather.go 40.7128 -74.0060`

This will print the temperature and time for the specified location.

Remember, Go programs are typically organized into packages. A package consists of one or more .go source files in a single directory. The package main statement at the top of the file identifies the file as part of the main package. The main function is the entry point of the program. When the program is run, it starts by executing the function main.

Also, Go uses a different approach for error handling compared to languages like Python. Instead of exceptions, Go uses multiple return values to indicate errors. If a function can return an error, it's usually the last return value. If the error is not nil, an error occurred and you can handle it.

