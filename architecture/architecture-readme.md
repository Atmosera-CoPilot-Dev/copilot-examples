# Simple Prompt to create Network Timing Diagram

With a source file in scope in Copilot chat, yuo can simple type:

`make me a mermaid diagram for this`

We were pretty vague about what we wanted here, and for my try it used a network timing diagram. To be more explicit we could say:

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


# Mermaid Architecture Diagram Results

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

