package djanGO

import (
	"fmt"
	"github.com/gin-gonic/gin"
)

func RunServer() {
	settings := getSettings()
	router := gin.Default()
	Urls(router)
	router.LoadHTMLGlob("templates/*")
	fmt.Println("djanGO development server")
	fmt.Println("Server is started at 127.0.0.1:" + settings.Port)
	error := router.Run(":" + settings.Port)
	if error != nil{
		panic(error)
	}
}

func getSettings() *Settings {
	settings, error := LoadSettings()
	if error != nil {
		panic(error)
	}
	return settings
}
