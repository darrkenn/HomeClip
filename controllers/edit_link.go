package controllers

import (
	"HomeClip/models"
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func EditLink(c *gin.Context, db *gorm.DB) {
	name := c.PostForm("name")
	url := c.PostForm("link")
	id := c.PostForm("id")
	colour := c.PostForm("colour")

	num, err := strconv.ParseUint(id, 10, 64)
	if err != nil {
		fmt.Println(err)
	}
	linkId := uint(num)

	var link models.Link
	db.First(&link, linkId)

	link.Name = name
	link.Url = url
	link.Colour = colour

	db.Save(&link)

	c.Header("HX-Redirect", c.Request.Referer())
	c.Status(http.StatusOK)
}
