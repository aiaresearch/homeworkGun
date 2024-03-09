package main

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
)

func get_documents_path() {
	var docPath string
	if runtime.GOOS == "windows" {
		docPath = os.Getenv("USERPROFILE") + "\\Documents"
	} else {
		docPath = os.Getenv("HOME") + "/Documents"
	}

	// Path to the config.toml file
	configFilePath := filepath.Join(docPath, "config.toml")

	// Check if the config.toml file exists
	file, err := os.OpenFile(configFilePath, os.O_RDWR|os.O_CREATE|os.O_EXCL, 0666)
	if err != nil {
		if os.IsExist(err) {
			fmt.Println("Config file already exists:", configFilePath)
		} else {
			fmt.Println("Error creating file:", err)
		}
		return
	}
	defer file.Close()

	defaultContent := "[databases]\nhost = \"\" # 请在此处填写你的数据库地址（本地填写127.0.0.1）\ndatabase = \"\" # 请在此处填写你的数据库名称\nusername = \"\" # 请在此处填写你的数据库账号\npassword = \"\" # 请在此处填写你的数据库密码\n\n[apikeys]\nglm = \"\" # 填写 ChatGLM API key\n"

	if _, err := file.WriteString(defaultContent); err != nil {
		fmt.Println("Error writing to file:", err)
		return
	}

	fmt.Println("未检测到 config.toml 文件，已为你自动生成，路径为：", configFilePath)
}
