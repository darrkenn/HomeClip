package controllers

import (
	"HomeClip/models"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func EditFolder(c *gin.Context, db *gorm.DB) {
	name := c.PostForm("name")
	id := c.PostForm("id")
	//parentId := c.PostForm("parentId")
	colour := c.PostForm("colour")

	num, err := strconv.ParseUint(id, 10, 64)
	if err != nil {
		fmt.Println(err)
	}
	folderId := uint(num)

	var folder models.Folder
	db.First(&folder, folderId)

	folder.Name = name
	folder.Colour = colour

	db.Save(&folder)

	c.Header("HX-Redirect", c.Request.Referer())
	c.Status(http.StatusOK)
}
