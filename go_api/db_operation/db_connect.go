package db_operation

import (
	"database/sql"
	"fmt"
	"log"

	"homeworkGun/get_config"

	"github.com/gin-gonic/gin"
	_ "github.com/lib/pq"
)

func ConnectToDB() *sql.DB {
	get_config.InitConfig()

	connStr := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",
		get_config.Cfg.Databases.Host,
		get_config.Cfg.Databases.Port,
		get_config.Cfg.Databases.Username,
		get_config.Cfg.Databases.Password,
		get_config.Cfg.Databases.Database,
	)
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	return db
}

func SetDBToContext(c *gin.Context, db *sql.DB) {
	c.Set("db", db)
}
