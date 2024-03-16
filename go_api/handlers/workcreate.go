package handlers

import (
	"database/sql"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

type Homework struct {
	HomeworkID         int    `json:"homework_id"`
	SubmissionRequired string `json:"submission_required"`
	StartDate          string `json:"start_date"`
	EndDate            string `json:"end_date"`
}

func CreateHomework(c *gin.Context) {
	var newHomework Homework

	if err := c.BindJSON(&newHomework); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	db, ok := c.MustGet("db").(*sql.DB)
	if !ok {
		c.JSON(500, gin.H{"error": "Failed to get database connection from context"})
		return
	}

	// Manual parsing of date strings
	startDate, err := time.Parse("2006-01-02", newHomework.StartDate)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid start date format"})
		return
	}
	endDate, err := time.Parse("2006-01-02", newHomework.EndDate)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid end date format"})
		return
	}

	query := `INSERT INTO homework_list (homework_id, submission_required, start_date, end_date, creation_date) VALUES ($1, $2, $3, $4, NOW())`
	_, err = db.Exec(query, newHomework.HomeworkID, newHomework.SubmissionRequired, startDate, endDate)
	if err != nil {
		c.JSON(500, gin.H{"error": "Failed to insert new homework into database"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"status": "success"})
}
