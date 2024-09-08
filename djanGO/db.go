package djanGO

import (
    "djanGO/djanGO/dbengines"
)

func DBEngine() {
    db := make(map[string]string)
    db["host"] = "localhost"
    db["dbname"] = "postgres"
    db["port"] = "5432"
    db["user"] = "postgres"
    db["password"] = "root"
    db["sslmode"] = "disable"


    dbengines.PostgreSQL(db)
}


