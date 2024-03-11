package models

type User struct {
	Account string `json:"account"`
	Passwd  string `json:"passwd"`
}
