package handlers

import (
	"homeworkGun/utils"
	"net/http"

	"github.com/gin-gonic/gin"
)

// Adapt for Gin
func UserProfileHandler(c *gin.Context) {
	r := c.Request

	err := utils.TokenValid(r)
	if err != nil {
		c.AbortWithStatusJSON(http.StatusUnauthorized, gin.H{"error": "Unauthorized"})
		return
	}

	c.JSON(http.StatusOK, gin.H{"message": "User profile accessed successfully"})
}
