package models

// User is the model that governs all notes objects retrived or inserted into the DB
type User struct {
	Full_name     *string `json:"full_name" validate:"required,min=2,max=100"`
	Email         *string `json:"email" validate:"email,required"`
	Password      *string `json:"password" validate:"required,min=6""`
	Token         *string `json:"token"`
	Refresh_token *string `json:"refresh_token"`
}
