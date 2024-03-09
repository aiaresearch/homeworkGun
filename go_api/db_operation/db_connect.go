package db_operation

import (
	"database/sql"
	"log"

	"github.com/gin-gonic/gin"
	_ "github.com/lib/pq"
)

func ConnectToDB() *sql.DB {
	connStr := " "
	// 在此处填写数据库相关信息
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	return db
}

func SetDBToContext(c *gin.Context, db *sql.DB) {
	c.Set("db", db)
}
