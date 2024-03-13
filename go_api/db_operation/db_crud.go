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
	rows1, err := db.Query("SELECT id, name, class, student_id, school_id FROM students_list")
	if err != nil {
		log.Println(err)
		c.JSON(500, gin.H{"error": "Error executing query on students_listData"})
		return
	}
	defer rows1.Close()

	var students_listData []map[string]interface{}
	for rows1.Next() {
		var students_id, students_name, students_class, students_student_id, students_school_id string
		if err := rows1.Scan(&students_id, &students_name, &students_class, &students_student_id, &students_school_id); err != nil {
			log.Println(err)
			continue
		}
		students_listData = append(students_listData, map[string]interface{}{"id": students_id, "name": students_name, "class": students_class, "student_id": students_student_id, "school_id": students_school_id})
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
		"students":   students_listData,
		"submission": submissionData,
	})
}
