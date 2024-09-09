package djanGO

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"djanGO/djanGO_project"
)

func RunServer() {
	router := gin.Default()

	Urls(router)

	router.LoadHTMLGlob("templates/*")
	DBEngine()

	fmt.Println("djanGO development server")
	fmt.Println("Server is started at 127.0.0.1:" + djanGO_project.PORT)

	error := router.Run(":" + djanGO_project.PORT)
	if error != nil{
		panic(error)
	}
}
