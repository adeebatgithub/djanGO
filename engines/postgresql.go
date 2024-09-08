package dbengines

import (
    "fmt"
    "gorm.io/driver/postgres"
    "gorm.io/gorm"
    "log"
)

func PostgreSQL(settings map[string]string) {
    var err error

    // Configure the database connection
    dsn := fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%s sslmode=%s",
	settings["host"],
	settings["user"],
	settings["password"],
	settings["dbname"],
	settings["port"],
	settings["sslmode"],
	)
    DB, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})
    if err != nil {
        log.Fatalf("Error connecting to the database: %v", err)
    }

    log.Println("Database connection established")
}