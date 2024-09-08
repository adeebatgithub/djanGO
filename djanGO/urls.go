package djanGO

import (
	"github.com/gin-gonic/gin"
	"djanGO/testApp"
)

func Urls(router *gin.Engine) {
	testApp.UrlPatterns(router)
}	