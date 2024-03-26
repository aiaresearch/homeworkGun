package handlers

import (
	"database/sql"
	"net/http"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
)

type SubmitListEntry struct {
	ID         int       `json:"id"`
	SchoolID   string    `json:"school_id"`
	SubjectID  int       `json:"subject_id"`
	HomeworkID int       `json:"homework_id"`
	SubmitTime time.Time `json:"submit_time"`
}

func SubHistHandler(c *gin.Context) {
	nParam := c.Query("id")
	n, err := strconv.Atoi(nParam)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid parameter"})
		return
	}

	db, ok := c.MustGet("db").(*sql.DB)
	if !ok {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to get database connection from context"})
		return
	}

	query := `SELECT id, school_id, subject_id, homework_id, submit_time
	FROM submit_list
	ORDER BY id DESC
	LIMIT $1
	`
	rows, err := db.Query(query, n)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Query execution failed"})
		return
	}
	defer rows.Close()

	var entries []SubmitListEntry
	for rows.Next() {
		var e SubmitListEntry
		if err := rows.Scan(&e.ID, &e.SchoolID, &e.SubjectID, &e.HomeworkID, &e.SubmitTime); err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to parse query results"})
			return
		}
		entries = append(entries, e)
	}

	c.JSON(http.StatusOK, entries)
}
