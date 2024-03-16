package models

import "time"

type SubmitItem struct {
	ID         int       `json:"id" gorm:"primary_key"`
	SchoolID   string    `json:"school_id"`
	SubjectID  int       `json:"subject_id"`
	HomeworkID int       `json:"homework_id"`
	SubmitTime time.Time `json:"submit_time"`
}
