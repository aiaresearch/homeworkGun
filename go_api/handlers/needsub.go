package handlers

import (
	"database/sql"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func GetNeedSub(c *gin.Context) {
	db, ok := c.MustGet("db").(*sql.DB)
	if !ok {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to get database connection from context"})
		return
	}

	homeworkID := c.Query("homeworkid")
	var submissionRequired string

	err := db.QueryRow("SELECT submission_required FROM homework_list WHERE homework_id = $1", homeworkID).Scan(&submissionRequired)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to query submission_required"})
		return
	}

	submissionIDs := strings.Split(submissionRequired, "#")
	c.JSON(http.StatusOK, gin.H{"Need2BSub": submissionIDs})
}
