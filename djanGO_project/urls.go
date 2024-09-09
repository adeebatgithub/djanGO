package djanGO_project

import (
	"github.com/gin-gonic/gin"
	"djanGO/djanGO_app"
)

func UrlPatterns(router *gin.Engine) {
	djanGO_app.UrlPatterns(router)
}