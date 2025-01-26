package main

import (
	"os"

	routes "auth-service/routes"

	"github.com/gin-gonic/gin"
)

// ------ Run the application by running the serever----------

func main() {
	port := os.Getenv("PORT")

	if port == "" {
		port = "8005"
	}

	router := gin.New()
	router.Use(gin.Logger())
	routes.UserRoutes(router)

	router.Run(":" + port)
}
