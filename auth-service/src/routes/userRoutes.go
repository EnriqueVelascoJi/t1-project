package routes

import (
	controller "auth-service/controllers"

	"github.com/gin-gonic/gin"
)

// ------ All endpoints ----------
func UserRoutes(incomingRoutes *gin.Engine) {
	incomingRoutes.POST("/users/signup", controller.SignUp())
	incomingRoutes.POST("/users/login", controller.Login())
}
