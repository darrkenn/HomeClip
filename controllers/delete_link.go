package controllers

import (
	"HomeClip/models"
	"fmt"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func DeleteLink(c *gin.Context, db *gorm.DB) {
	linkid := c.Param("linkid")
	tagid := c.Param("tagid")

	linkDeleteErr := db.Where("Id = ?", linkid).Delete(&models.Link{})
	if linkDeleteErr.Error != nil {
		fmt.Println("Cant delete link: ", linkDeleteErr.Error)
	}
	fmt.Println("Deleted link")
	if tagid != "nil" {
		checkTag(db, tagid)
	}
}

func checkTag(db *gorm.DB, tagid string) {
	var count int64
	db.Model(&models.Link{}).Where("TagId = ?", tagid).Count(&count)
	if count == 0 {
		tagDeleteErr := db.Where("Id = ?", tagid).Delete(&models.Tag{})
		if tagDeleteErr.Error != nil {
			fmt.Println("Cant delete tag: ", tagDeleteErr.Error)
		}
	}
}
