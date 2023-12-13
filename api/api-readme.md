# Summary 

This is a demo of prompts from CoPilot chat that will show how to iteratively make better prompts through better requirements. This would be an example of few-shot prompting where we give Copilot a few examples of what we want to do and it will try to figure out the rest.

## Requirements

Build a simple  python command-line utility that will fetch the current temperature at a given lat/long. You can find the Free Weather API at https://open-meteo.com/. Lat and Long are command line parameters.

We want to be able to run the utility from the command-line and get the current temperature in Austin, TX like: 

`python3 weather.py 45.4215 -75.6972`

# Try 1

```
Write me a function that uses api.open-meteo.com to get the weather. The input to the script should take the lat and long and return the current temperature and time. Be sure to handle errors if the lat and long is not specified within range as well had handling any HTTP errors. Use the api.open-meteo.com API
```

# Try 2

The first try doesn't tell the AI engine that we want to the parameters for the API to be taken from the command line, so we can start from scratch again with (new sentence added at the end):

```
Write me a function that uses api.open-meteo.com to get the weather. The input to the script should take the lat and long and return the current temperature and time. Be sure to handle errors if the lat and long is not specified within range as well had handling any HTTP errors. Use the api.open-meteo.com API. i need to run the script from command line where lat and long are command line parameters
```

# Try 3

We didn't tell Copilot anything about the API parameters or the schema of the response, so let's try again with that info:

```
Write me a function that uses api.open-meteo.com to get the weather. The input to the script should take the lat and long and return the current temperature and time. Be sure to handle errors if the lat and long is not specified within range as well had handling any HTTP errors. Use the api.open-meteo.com API. i need to run the script from command line where lat and long are command line parameters. Here's an example of the API call with parameters and a sample response:

$ curl "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

{
  "current": {
    "time": "2022-01-01T15:00"
    "temperature_2m": 2.4,
    "wind_speed_10m": 11.9,
  },
  "hourly": {
    "time": ["2022-07-01T00:00","2022-07-01T01:00", ...]
    "wind_speed_10m": [3.16,3.02,3.3,3.14,3.2,2.95, ...],
    "temperature_2m": [13.7,13.3,12.8,12.3,11.8, ...],
    "relative_humidity_2m": [82,83,86,85,88,88,84,76, ...],
  }
}

```

Now we've given Copilot clear enough requirements about how we want to run the program, what the parameters might be and what the schema response will look like. Note that requirements were not given on how to parse, what parts of the model to parse, or how to respond in the utility program - Copilot simply devised the most likely code given the information available.

```
% python3 weather.py 30.264980 -97.746597
Temperature: 14.6, Time: 2023-12-10T21:45
```

# Try 4 - Adding unit tests.

Assuming the app is basically working, we can add some unit test in multiple ways. One way is to prompt at the bottom the `weather.py` file with:

`# Unit test run with pytest to check if the function works properly`

# Some basic error checking

At this point we should have basic cmd-line utility running that returns the current temperature and time of temp on the cmd-line.
However we have not tested error handling for bad or missing parameters, such as:

`python3 weather.py`
`python3 weather.py foo bar`
`python3 weather.py 10000 900000`

Here we need to be a bit more precise, for example placing comments like:

`# Check that the latitude and longitude are floats and also not null`
`# Check that the latitude and longitude are within valid range`

# Installing the application and running it on the command line

To install the application, you can run:

`pip3 install -r requirements.txt`

To run the application, you can run:

`python3 weather.py 30.264980 -97.746597`

# Running the tests

To run the tests, you can run:

`pytest weather.py`

# Running the linter

To run the linter, you can run:

`flake8`

# Running the type checker

To run the type checker, you can run:

`mypy weather.py`


# References

* Tips on using Copilot Prompts: https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/
* Zero vs One vs Few Shot prompting: https://www.hatica.io/blog/prompt-engineering-with-github-copilot/

