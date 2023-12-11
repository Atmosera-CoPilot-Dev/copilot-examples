package main

import (
    "encoding/json"
    "fmt"
    "net/http"
    "os"
    "strconv"
)

type WeatherData struct {
    Current struct {
        Temperature2m float64 `json:"temperature_2m"`
        Time          string  `json:"time"`
    } `json:"current"`
}

func getWeather(lat, lon float64) (float64, string, error) {
    resp, err := http.Get(fmt.Sprintf("https://api.open-meteo.com/v1/forecast?latitude=%f&longitude=%f&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m", lat, lon))
    if err != nil {
        return 0, "", err
    }
    defer resp.Body.Close()

    var data WeatherData
    err = json.NewDecoder(resp.Body).Decode(&data)
    if err != nil {
        return 0, "", err
    }

    return data.Current.Temperature2m, data.Current.Time, nil
}

func main() {
    if len(os.Args) != 3 {
        fmt.Println("Usage: go run weather.go [latitude] [longitude]")
        os.Exit(1)
    }

    lat, err := strconv.ParseFloat(os.Args[1], 64)
    if err != nil || lat < -90 || lat > 90 {
        fmt.Println("Error: Latitude must be a float between -90 and 90.")
        os.Exit(1)
    }

    lon, err := strconv.ParseFloat(os.Args[2], 64)
    if err != nil || lon < -180 || lon > 180 {
        fmt.Println("Error: Longitude must be a float between -180 and 180.")
        os.Exit(1)
    }

    temperature, time, err := getWeather(lat, lon)
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(1)
    }

    fmt.Printf("Temperature: %f, Time: %s\n", temperature, time)
}