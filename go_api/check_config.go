package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func check_config() {
	// Set the filename
	filename := "config.toml"

	// Check if the file exists in the current directory
	if _, err := os.Stat(filename); os.IsNotExist(err) {
		// File does not exist, create it
		file, err := os.Create(filename)
		if err != nil {
			fmt.Println("Error creating file:", err)
			return
		}
		defer file.Close()

		// Write default content to the file
		defaultContent := "[databases]\nhost = \"\" # 请在此处填写你的数据库地址（本地填写127.0.0.1）\nport = \"\" # 请在此处填写你数据库端口（默认5432）\ndatabase = \"\" # 请在此处填写你的数据库名称\nusername = \"\" # 请在此处填写你的数据库账号\npassword = \"\" # 请在此处填写你的数据库密码\n\n[apikeys]\nglm = \"\" # 填写 ChatGLM API key\n"
		_, err = file.WriteString(defaultContent)
		if err != nil {
			fmt.Println("Error writing to file:", err)
			return
		}

		// Get the full path of the created file
		fullPath, err := filepath.Abs(filename)
		if err != nil {
			fmt.Println("Error getting full path:", err)
			return
		}

		fmt.Println("Config file created at:", fullPath, "Please modify the configuration file as described in the documentation, and then re-run the program.")
		os.Exit(0)
	} else {
		// File exists, continue with the rest of the program
		fmt.Println("Config file already exists, continuing...")
	}
}
