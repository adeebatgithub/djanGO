package testApp

import (
	"net/http"
	"github.com/gin-gonic/gin"
)


func IndexView(context *gin.Context) {
	context.HTML(http.StatusOK, "index.html", nil)
}