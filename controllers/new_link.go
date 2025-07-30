package controllers

import (
	"HomeClip/models"
	"errors"
	"fmt"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
	"net/http"
)

func NewLink(c *gin.Context, db *gorm.DB) {
	name := c.PostForm("name")
	url := c.PostForm("link")
	tagName := c.PostForm("tag")

	var tag models.Tag

	if tagName != "" {
		if whereErr := db.Where("name = ?", tagName).First(&tag).Error; whereErr != nil {
			if errors.Is(whereErr, gorm.ErrRecordNotFound) {
				tag = models.Tag{Name: tagName}
				if createErr := db.Create(&tag).Error; createErr != nil {
					c.JSON(http.StatusBadRequest, gin.H{"error": createErr})
					return
				}
			}
		}
	}

	newLink := models.Link{
		Url:   url,
		Name:  name,
		TagId: &tag.Id,
	}

	createErr := db.Create(&newLink)
	if createErr != nil {
		fmt.Println("Cant create: ", createErr)
		return
	}
}
