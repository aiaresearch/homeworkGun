package utils

import (
	"database/sql"
	"errors"
	"homeworkGun/models"
	"net/http"
	"time"

	"github.com/golang-jwt/jwt"
	"golang.org/x/crypto/bcrypt"
)

var jwtKey = []byte("your_secret_key")

type Claims struct {
	Account string `json:"account"`
	jwt.StandardClaims
}

func LoginUser(account, passwd string, db *sql.DB) (string, error) {
	var dbPasswd string
	err := db.QueryRow(`SELECT passwd FROM platform_users WHERE account = $1`, account).Scan(&dbPasswd)
	if err != nil {
		return "", err
	}

	if err := bcrypt.CompareHashAndPassword([]byte(dbPasswd), []byte(passwd)); err != nil {
		return "", errors.New("invalid login credentials")
	}

	expirationTime := time.Now().Add(30 * time.Minute)
	claims := &Claims{
		Account: account,
		StandardClaims: jwt.StandardClaims{
			ExpiresAt: expirationTime.Unix(),
		},
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	tokenString, err := token.SignedString(jwtKey)
	if err != nil {
		return "", err
	}

	return tokenString, nil
}

func RegisterUser(user models.User, db *sql.DB) error {
	hashedPasswd, err := bcrypt.GenerateFromPassword([]byte(user.Passwd), bcrypt.DefaultCost)
	if err != nil {
		return err
	}

	_, err = db.Exec(`INSERT INTO platform_users (account, passwd) VALUES ($1, $2)`, user.Account, string(hashedPasswd))
	return err
}

func TokenValid(req *http.Request) error {
	tokenString := req.Header.Get("Authorization")
	claims := &Claims{}

	token, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (interface{}, error) {
		return jwtKey, nil
	})

	if err != nil || !token.Valid {
		return errors.New("invalid token")
	}

	return nil
}
