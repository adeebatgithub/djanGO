package djanGO

import (
	"github.com/gin-gonic/gin"
	"djanGO/djanGO_project"
)

func Urls(router *gin.Engine) {
	djanGO_project.UrlPatterns(router)
}	