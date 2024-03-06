package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	get_documents_path()
	router := gin.Default()
	router.GET("/get-advice", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "Streaming the returned content...",
		})
	})
	router.Run("127.0.0.1:2333") // listen and serve on 127.0.0.1:8080
}
