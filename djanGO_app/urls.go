package djanGO_app

import "github.com/gin-gonic/gin"

func UrlPatterns(router *gin.Engine) {
	index := router.Group("/")
	{
		index.GET("/", IndexView)
	}
}