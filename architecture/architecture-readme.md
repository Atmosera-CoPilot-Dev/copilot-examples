# Summary

This is a simple example of how we can use Copilot to generate reference architecture diagrams such as Network Timing diagram. We will create the format using [Mermaid](https://mermaid.live/).

We will run through the prompts even though the results are posted below. You should try this on your own code base or other unfamiliar code!

# Simple Prompt to create Network Timing Diagram

With a source file in scope in Copilot chat, you can simple type:

`make me a mermaid diagram for this`

We were pretty vague about what we wanted here, and for my try it created a network timing diagram. To be more explicit we could say:

`create a network timing diagram in mermaid format for weather.py`

By using the [weather.py](../api/weather.py) example, we can get network timing diagram like the one below. The mermaid result looks like this:

```
sequenceDiagram
    participant User
    participant Function as get_weather
    participant API as Open-Meteo API
    User->>Function: get_weather(lat, lon)
    Note over Function: Check lat, lon type and range
    alt Invalid lat, lon
        Function-->>User: Error: Latitude and longitude must be floats or Error: Latitude must be between -90 and 90 and longitude must be between -180 and 180.
    else Valid lat, lon
        Function->>API: GET request
        alt Successful request
            API-->>Function: JSON response
            Note over Function: Parse JSON and extract temperature and time
            Function-->>User: temperature, time
        else Unsuccessful request
            Function-->>User: HTTP error occurred or An error occurred
        end
    end
```


# Adding Mermaid Diagrams to Markdown

You can simply edit mermaid diagrams in Github markdown by adding `mermaid` right after the first three backticks. For example, the following markdown:

````
```mermaid
``````

## Diagram Display In Markdown

```mermaid
sequenceDiagram
    participant User
    participant Function as get_weather
    participant API as Open-Meteo API
    User->>Function: get_weather(lat, lon)
    Note over Function: Check lat, lon type and range
    alt Invalid lat, lon
        Function-->>User: Error: Latitude and longitude must be floats or Error: Latitude must be between -90 and 90 and longitude must be between -180 and 180.
    else Valid lat, lon
        Function->>API: GET request
        alt Successful request
            API-->>Function: JSON response
            Note over Function: Parse JSON and extract temperature and time
            Function-->>User: temperature, time
        else Unsuccessful request
            Function-->>User: HTTP error occurred or An error occurred
        end
    end
``````

## Creating a System Diagram

Alternatively we can specify diagram type,

`make me a system architecture resource diagram for weather.py in Mermaid format`

```mermaid
graph LR
    A[User] -- Input: Latitude, Longitude --> B[weather.py]
    B -- GET Request --> C[Open-Meteo API]
    C -- JSON Response --> B
    B -- Output: Temperature, Time --> A
```

# References

* Include diagrams in your markdown with Mermaid: https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/
* Mermaid Markdown viewer for VS Code: https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid
* Mermaid Live Editor: https://mermaid.live/
* Mermaid Documentation: https://mermaid-js.github.io/mermaid/#/

