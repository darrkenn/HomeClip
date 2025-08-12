package controllers

import (
	"HomeClip/models"
	"fmt"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
	"strconv"
)

func NewLink(c *gin.Context, db *gorm.DB) {
	name := c.PostForm("name")
	url := c.PostForm("link")
	folderId := c.PostForm("FolderId")
	colour := c.PostForm("colour")
	var folder uint
	if folderId != "" {
		num, err := strconv.ParseUint(folderId, 10, 64)
		if err != nil {
			fmt.Println(err)
		}
		folder = uint(num)
	}
	newLink := models.Link{
		Url:      url,
		Name:     name,
		FolderId: &folder,
		Colour:   colour,
	}
	result := db.Create(&newLink)
	if result.Error != nil {
		fmt.Println("Cant create: ", result.Error)
		return
	}

	currentUrl := fmt.Sprintf("?id=%s", folderId)
	c.Header("HX-REDIRECT", currentUrl)
}
