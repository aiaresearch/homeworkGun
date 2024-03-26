package main

import (
	"homeworkGun/db_operation"
	"homeworkGun/handlers"
	"homeworkGun/middleware"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
	_ "github.com/lib/pq"
)

func CORSMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
		c.Writer.Header().Set("Access-Control-Allow-Credentials", "true")
		c.Writer.Header().Set("Access-Control-Allow-Headers", "Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, accept, origin, Cache-Control, X-Requested-With")
		c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS, GET, PUT")

		if c.Request.Method == "OPTIONS" {
			c.AbortWithStatus(http.StatusNoContent)
			return
		}

		c.Next()
	}
}

func main() {
	check_config()

	r := gin.Default()
	db := db_operation.ConnectToDB()

	// Register the CORS middleware globally
	r.Use(CORSMiddleware())

	r.Use(func(c *gin.Context) {
		db_operation.SetDBToContext(c, db)
		c.Next()
	})
	r.GET("/crud", db_operation.QueryHandler)

	r.POST("/login", handlers.LoginHandler)
	r.POST("/register", handlers.RegisterHandler)

	r.POST("/create", handlers.CreateHomework)
	r.POST("/submit", handlers.SubmitHomework)

	authGroup := r.Group("/").Use(middleware.TokenAuthMiddleware())
	authGroup.GET("/user", handlers.UserProfileHandler)

	r.GET("/students", handlers.GetStudentsByClass)
	r.GET("/needsub", handlers.GetNeedSub)
	r.GET("/gethomework", handlers.GetHomeworkHandler)
	r.GET("/subhist", handlers.SubHistHandler)

	log.Fatal(r.Run("0.0.0.0:1145")) // listen and serve on 0.0.0.0:1145
}
