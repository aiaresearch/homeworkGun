package db_operation

import (
	"database/sql"
	"log"

	"github.com/gin-gonic/gin"
)

func QueryHandler(c *gin.Context) {
	db, ok := c.MustGet("db").(*sql.DB)
	if !ok {
		c.JSON(500, gin.H{"error": "Failed to get database connection from context"})
		return
	}

	// Query from first table
	rows1, err := db.Query("SELECT name, id, class FROM students")
	if err != nil {
		log.Println(err)
		c.JSON(500, gin.H{"error": "Error executing query on studentsData"})
		return
	}
	defer rows1.Close()

	var studentsData []map[string]interface{}
	for rows1.Next() {
		var students_name, students_id, students_class string
		if err := rows1.Scan(&students_name, &students_id, &students_class); err != nil {
			log.Println(err)
			continue
		}
		studentsData = append(studentsData, map[string]interface{}{"name": students_name, "id": students_id, "class": students_class})
	}

	// Query from second table
	rows2, err := db.Query("SELECT id, subject, time FROM submission")
	if err != nil {
		log.Println(err)
		c.JSON(500, gin.H{"error": "Error executing query on SubmissionData"})
		return
	}
	defer rows2.Close()

	var submissionData []map[string]interface{}
	for rows2.Next() {
		var submission_id, submission_subject, submission_time string
		if err := rows2.Scan(&submission_id, &submission_subject, &submission_time); err != nil {
			log.Println(err)
			continue
		}
		submissionData = append(submissionData, map[string]interface{}{"id": submission_id, "subject": submission_subject, "time": submission_time})
	}

	// Aggregate and respond with JSON
	c.JSON(200, gin.H{
		"students":   studentsData,
		"submission": submissionData,
	})
}
