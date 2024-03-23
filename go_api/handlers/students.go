package handlers

import (
	"database/sql"
	"net/http"

	"github.com/gin-gonic/gin"
)

func GetStudentsByClass(c *gin.Context) {
	classValue := c.Query("class")

	db, ok := c.MustGet("db").(*sql.DB)
	if !ok {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to get database connection from context"})
		return
	}

	query := "SELECT name, school_id FROM students_list WHERE class = $1"
	rows, err := db.Query(query, classValue)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Error executing query"})
		return
	}
	defer rows.Close()

	var results []map[string]interface{}
	for rows.Next() {
		var name string
		var schoolID int
		if err := rows.Scan(&name, &schoolID); err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Error scanning rows"})
			return
		}
		result := map[string]interface{}{"name": name, "school_id": schoolID}
		results = append(results, result)
	}

	c.JSON(http.StatusOK, gin.H{"students": results})
}
