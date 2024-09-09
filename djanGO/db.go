package djanGO

import (
    "djanGO/djanGO/dbengines"
    "djanGO/djanGO_project"
)


func DBEngine() {
    dbengines.PostgreSQL(djanGO_project.DATABASE)
}


