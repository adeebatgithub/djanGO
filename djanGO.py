import os, sys


def make_dir(name):
    try:
        os.mkdir(name)
        print("Directory created successfully; ", name)
    except FileExistsError:
        print("Directory already exists")
    except OSError as e:
        print(f"Error creating directory: {e}")


def make_file(name, content):
    with open(name, "w") as file:
        file.write(content)
    print("File created successfully; ", name)


def help():
    print(
        """
djanGO - A Gin project strusture
-----------------------------------------------
Usage:- djanGO.py [commands]
-----------------------------------------------
commands
    startproject [project-name]                     - create project structure
    installdb [project-name] [database(psql/mysql)] - install databes configration to project
                                                    - *currently psql is supported
"""
    )


def start_project(args):
    if not args:
        print("project name required")
        return
    base_dir = args[0]
    make_dir(base_dir)
    make_file(name=f"{base_dir}/manage.go", content=f"""
package main

import (
	"{base_dir}/djanGO"
	"fmt"
	"os"
)

func main() {{
	args := os.Args
	switch args[1] {{
	case "runserver":
		djanGO.RunServer()
	default:
		fmt.Println("Unknown command: ", args[1])
	}}
}}
""")
    make_file(name=f"{base_dir}/go.mod",
              content=f"""
module {base_dir}

go 1.23.1

require (
	github.com/gin-gonic/gin v1.10.0
	gorm.io/driver/postgres v1.5.9
	gorm.io/gorm v1.25.12
)

require (
	github.com/bytedance/sonic v1.11.6 // indirect
	github.com/bytedance/sonic/loader v0.1.1 // indirect
	github.com/cloudwego/base64x v0.1.4 // indirect
	github.com/cloudwego/iasm v0.2.0 // indirect
	github.com/gabriel-vasile/mimetype v1.4.3 // indirect
	github.com/gin-contrib/sse v0.1.0 // indirect
	github.com/go-playground/locales v0.14.1 // indirect
	github.com/go-playground/universal-translator v0.18.1 // indirect
	github.com/go-playground/validator/v10 v10.20.0 // indirect
	github.com/goccy/go-json v0.10.2 // indirect
	github.com/jackc/pgpassfile v1.0.0 // indirect
	github.com/jackc/pgservicefile v0.0.0-20221227161230-091c0ba34f0a // indirect
	github.com/jackc/pgx/v5 v5.5.5 // indirect
	github.com/jackc/puddle/v2 v2.2.1 // indirect
	github.com/jinzhu/inflection v1.0.0 // indirect
	github.com/jinzhu/now v1.1.5 // indirect
	github.com/json-iterator/go v1.1.12 // indirect
	github.com/klauspost/cpuid/v2 v2.2.7 // indirect
	github.com/kr/text v0.2.0 // indirect
	github.com/leodido/go-urn v1.4.0 // indirect
	github.com/mattn/go-isatty v0.0.20 // indirect
	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
	github.com/modern-go/reflect2 v1.0.2 // indirect
	github.com/pelletier/go-toml/v2 v2.2.2 // indirect
	github.com/rogpeppe/go-internal v1.12.0 // indirect
	github.com/twitchyliquid64/golang-asm v0.15.1 // indirect
	github.com/ugorji/go/codec v1.2.12 // indirect
	golang.org/x/arch v0.8.0 // indirect
	golang.org/x/crypto v0.23.0 // indirect
	golang.org/x/net v0.25.0 // indirect
	golang.org/x/sync v0.1.0 // indirect
	golang.org/x/sys v0.20.0 // indirect
	golang.org/x/text v0.15.0 // indirect
	google.golang.org/protobuf v1.34.1 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
)

"""
              )
    django_dir = f"{base_dir}/djanGO"
    make_dir(name=django_dir)
    make_file(
        name=f"{django_dir}/db.go",
        content=f"""
package djanGO

// database setting
"""
    )
    make_file(
        name=f"{django_dir}/runServer.go",
        content=f"""
package djanGO

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"{base_dir}/{base_dir}"
)

func RunServer() {{
	router := gin.Default()

	Urls(router)

	router.LoadHTMLGlob("templates/*")
	DBEngine()

	fmt.Println("djanGO development server")
	fmt.Println("Server is started at 127.0.0.1:" + {base_dir}.PORT)

	error := router.Run(":" + {base_dir}.PORT)
	if error != nil{{
		panic(error)
	}}
}}

"""
    )
    make_file(
        name=f"{django_dir}/urls.go",
        content=f"""
package djanGO

import (
	"github.com/gin-gonic/gin"
	"{base_dir}/{base_dir}"
)

func Urls(router *gin.Engine) {{
	{base_dir}.UrlPatterns(router)
}}
"""
    )
    root_dir = f"{base_dir}/{base_dir}"
    make_dir(name=root_dir)
    make_file(
        name=f"{root_dir}/settings.go",
        content=f"""
package {base_dir}

const PORT string = "8000"

var DATABASE = map[string]string{{
	"host": "localhost",
	"dbname": "postgres",
	"port": "5432",
	"user": "postgres",
	"password": "root",
}}
"""
    )
    make_file(
        name=f"{root_dir}/urls.go",
        content=f"""
package {base_dir}

import (
	"github.com/gin-gonic/gin"
	// "{base_dir}/appName"
)

func UrlPatterns(router *gin.Engine) {{
	// appName.UrlPatterns(router)
}}
"""
	)
    make_dir(
        name=f"{base_dir}/templates"
	)
    make_file(
        name=f"{base_dir}/templates/index.html",
        content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>djanGO</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Open Sans, sans-serif;
            text-align: center;
            background-color: #f0f8ff;
        }
        .container {
            max-width: 600px;
        }
        .main-text {
            font-size: 6em;
            font-weight: bold;
        }
        .sub-text {
            font-size: 1.5em;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="main-text">djan<span style="color:#00ADD8;">GO</span></div>
        <div class="sub-text">A Gin Project Structure</div>
    </div>
</body>
</html>
"""
    )
    print("project created successfully: ", base_dir)
    print(f"""
    - python djanGO.py installdb {base_dir} psql
    - cd {base_dir}
    - go mod tidy
    - go run manage.go runserver
          """)


def create_db(args):
    name = args[0]
    db = args[1]
    db_dir = f"{name}/djanGO/dbengines"
    if not os.path.exists(f"{name}/{name}/settings.go"):
        print("project not found: ", name)
        return
    if not os.path.exists(db_dir):
        make_dir(db_dir)
    if db.lower() == "psql" or db.lower() == "postgresql":
        make_file(
            name=f"{db_dir}/postgresql.go",
            content=f"""
package dbengines

import (
    "fmt"
    "gorm.io/driver/postgres"
    "gorm.io/gorm"
    "log"
)

var DB *gorm.DB

func PostgreSQL(database map[string]string) {{
    var err error

    // Configure the database connection
    dsn := fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%s sslmode=%s",
	database["host"],
	database["user"],
	database["password"],
	database["dbname"],
	database["port"],
	database["sslmode"],
	)
    DB, err = gorm.Open(postgres.Open(dsn), &gorm.Config{{}})
    if err != nil {{
        log.Fatalf("Error connecting to the database: %v", err)
    }}

    log.Println("Database connection established")
}}
"""
		)
        make_file(
            name=f"{name}/djanGO/db.go",
            content=f"""
package djanGO

import (
    "{name}/djanGO/dbengines"
    "{name}/{name}"
)


func DBEngine() {{
    dbengines.PostgreSQL({name}.DATABASE)
}}

"""
		)


if __name__ == "__main__":
    args = sys.argv[1:]
    
    if not args:
        help()
        quit()
    
    commands = {
        "startproject": start_project,
        "installdb": create_db
    }
    if args[0] in commands:
        commands[args[0]](args[1:])
    else:
        print("command not found: ", args[0])
        help()

