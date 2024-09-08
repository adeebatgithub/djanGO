package djanGO

import (
    "encoding/json"
    "os"
    "path/filepath"
)

type Settings struct {
    Port string
    Database struct {
        Host     string
        Port     int
        User     string
        Password string
        DBName   string
    }
}

func LoadSettings() (*Settings, error) {
    jsonPath, error := filepath.Abs(filepath.Join("djanGO", "settings.json"))
    if error != nil {
        println(error)
    }
    file, err := os.Open(jsonPath)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    config := &Settings{}
    decoder := json.NewDecoder(file)
    err = decoder.Decode(config)
    if err != nil {
        return nil, err
    }

    return config, nil
}
