package main

import (
	"homeworkGun/db_operation"

	"github.com/gin-gonic/gin"
)

func main() {
	check_config()

	r := gin.Default()
	db := db_operation.ConnectToDB()
	r.Use(func(c *gin.Context) {
		db_operation.SetDBToContext(c, db)
		c.Next()
	})
	r.GET("/crud", db_operation.QueryHandler)
	r.Run("0.0.0.0:1145") // listen and serve on 0.0.0.0:1145
}
