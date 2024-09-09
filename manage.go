package manage

import (
	"djanGO/djanGO"
	"fmt"
	"os"
)

func main() {
	args := os.Args
	switch args[1] {
	case "runserver":
		djanGO.RunServer()
	default:
		fmt.Println("Unknown command: ", args[1])
	}
}