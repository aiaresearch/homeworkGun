package get_config

import (
	"log"

	"github.com/BurntSushi/toml"
)

type Config struct {
	Databases Databases `toml:"databases"`
	Apikeys   Apikeys   `toml:"apikeys"`
}

type Databases struct {
	Database string `toml:"database"`
	Port     string `toml:"port"`
	Username string `toml:"username"`
	Password string `toml:"password"`
	Host     string `toml:"host"`
}

type Apikeys struct {
	Glm string `toml:"glm"`
}

var Cfg Config

// Initialize loading configuration
func InitConfig() {
	if _, err := toml.DecodeFile("config.toml", &Cfg); err != nil {
		log.Fatal(err)
	}
}

// 其他文件中的调用方式如下：
// Sample.调用 databases 中的 database
// config.Cfg.Databases.Database
// Sample.调用 apikeys 中的 glm
// config.Cfg.Apikeys.Glm
