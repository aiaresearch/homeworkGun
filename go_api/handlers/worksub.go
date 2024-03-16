package handlers

import (
	"database/sql"
	"homeworkGun/models"
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

func SubmitHomework(c *gin.Context) {
	db, ok := c.MustGet("db").(*sql.DB)
	if !ok {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to get database connection from context"})
		return
	}

	var item models.SubmitItem
	if err := c.BindJSON(&item); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	item.SubmitTime = time.Now()

	_, err := db.Exec("INSERT INTO submit_list (school_id, subject_id, homework_id, submit_time) VALUES ($1, $2, $3, $4)",
		item.SchoolID, item.SubjectID, item.HomeworkID, item.SubmitTime)
	if err != nil {
		log.Printf("Failed to insert submit item into database: %v", err)
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to insert submit item into database"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"status": "success"})

}
