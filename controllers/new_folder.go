package controllers

import (
	"HomeClip/models"
	"fmt"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
	"strconv"
)

func NewFolder(c *gin.Context, db *gorm.DB) {
	name := c.PostForm("name")
	colour := c.PostForm("colour")
	parentId := c.PostForm("parentId")

	var parent uint
	if parentId != "" {
		num, err := strconv.ParseUint(parentId, 10, 64)
		if err != nil {
			fmt.Println(err)
		}
		parent = uint(num)
	} else {
		parent = 0
	}

	newFolder := models.Folder{
		Name:     name,
		Colour:   colour,
		ParentId: &parent,
	}

	result := db.Create(&newFolder)
	if result.Error != nil {
		fmt.Println("Cant create: ", result.Error)
		return
	}
	currentUrl := fmt.Sprintf("?id=%s", parentId)
	c.Header("HX-REDIRECT", currentUrl)
}
