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
	if _, err := os.Stat(configFilePath); os.IsNotExist(err) {
		if _, err := os.Create(configFilePath); err != nil {
			fmt.Println("Error creating file:", err)
			return
		}
		fmt.Println("未检测到 config.toml 文件，已为你自动生成，路径为：", configFilePath)
	} else {
		// File exists
		fmt.Println(configFilePath)
	}
}
