package controllers

import (
	"HomeClip/models"
	"fmt"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func DeleteLink(c *gin.Context, db *gorm.DB) {
	linkid := c.Param("linkid")

	linkDeleteErr := db.Where("Id = ?", linkid).Delete(&models.Link{})
	if linkDeleteErr.Error != nil {
		fmt.Println("Cant delete link: ", linkDeleteErr.Error)
	}
	fmt.Println("Deleted link")

}
