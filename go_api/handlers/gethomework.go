package handlers

import (
	"database/sql"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func GetHomeworkHandler(c *gin.Context) {
	db, ok := c.MustGet("db").(*sql.DB)
	if !ok {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to get database connection from context"})
		return
	}

	idStr := c.Query("id")
	id, err := strconv.Atoi(idStr)
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid ID format"})
		return
	}

	query := fmt.Sprintf("SELECT id, homework_id, submission_required, start_date, end_date, creation_date FROM homework_list ORDER BY id DESC LIMIT %d", id)
	rows, err := db.Query(query)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Error executing query"})
		return
	}
	defer rows.Close()

	var results []map[string]interface{}
	for rows.Next() {
		var id, homeworkID int
		var submissionRequired, startDate, endDate, creationDate string
		err = rows.Scan(&id, &homeworkID, &submissionRequired, &startDate, &endDate, &creationDate)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Error scanning database results"})
			return
		}
		result := map[string]interface{}{
			"id":                  id,
			"homework_id":         homeworkID,
			"submission_required": submissionRequired,
			"start_date":          startDate,
			"end_date":            endDate,
			"creation_date":       creationDate,
		}
		results = append(results, result)
	}

	c.JSON(http.StatusOK, gin.H{"data": results})
}
