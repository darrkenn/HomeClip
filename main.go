package main

import (
	"HomeClip/controllers"
	"HomeClip/models"
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"log"
	_ "modernc.org/sqlite"
	"net/http"
	"os"
	"strconv"
)

func main() {
	fmt.Println("Starting homeclip!")
	//Load .env and setup database
	envErr := godotenv.Load()
	if envErr != nil {
		fmt.Println("Cant get .env")
		log.Fatal(envErr)
	}
	dbLocation := os.Getenv("DATABASE")
	db := databaseSetup(dbLocation)

	//Setup of router and html/static files
	r := gin.Default()
	r.LoadHTMLGlob("templates/*")
	r.Static("/static", "./static")

	//Api endpoints and page setup
	loadApi(r, db)
	loadPages(r, db)

	runErr := r.Run(":3119")
	if runErr != nil {
		log.Fatal(runErr)
		return
	}
}

func loadApi(r *gin.Engine, db *gorm.DB) {
	//Pure html
	r.GET("/api/html/navbar", func(c *gin.Context) {
		c.HTML(http.StatusOK, "navbar.gohtml", nil)
	})
	r.GET("/api/html/newlink", func(c *gin.Context) {
		id := c.Query("id")
		var parent uint
		if id != "" {
			num, err := strconv.ParseUint(id, 10, 64)
			if err != nil {
				fmt.Println(err)
			}
			parent = uint(num)
		} else {
			parent = 0
		}

		c.HTML(http.StatusOK, "newlink.gohtml", gin.H{
			"parentId": parent,
		})
	})
	r.GET("/api/html/newfolder", func(c *gin.Context) {
		id := c.Query("id")
		var parent uint
		if id != "" {
			num, err := strconv.ParseUint(id, 10, 64)
			if err != nil {
				fmt.Println(err)
			}
			parent = uint(num)
		} else {
			parent = 0
		}
		c.HTML(http.StatusOK, "newfolder.gohtml", gin.H{
			"parentId": parent,
		})
	})
	r.GET("/api/html/clear", func(c *gin.Context) {
		c.HTML(http.StatusOK, "", nil)
	})

	//Links
	r.GET("/api/links/toplinks", func(c *gin.Context) {
		var links []models.Link
		result := db.Limit(5).Order("clicks desc").Find(&links)
		if result.Error != nil {
			log.Fatal("Cant get links: ", result.Error)
		}
		c.HTML(http.StatusOK, "links.gohtml", gin.H{
			"links": links,
		})
	})
	r.POST("/api/links/addlink", func(c *gin.Context) {
		controllers.NewLink(c, db)
	})
	r.POST("/api/links/delete/:linkid", func(c *gin.Context) {
		controllers.DeleteLink(c, db)
	})
	//Folders
	r.GET("/api/folders/:purpose/:parentid", func(c *gin.Context) {
		purpose := c.Param("purpose")
		parentId := c.Param("parentid")

		var folders []models.Folder
		result := db.Preload("Links").Preload("Children.Links").Preload("Children.Children").Where("parent_id = ?", parentId).Find(&folders)
		if result.Error != nil {
			fmt.Println("Cant get folders: ", result.Error)
		}

		if purpose == "nav" {
			c.HTML(http.StatusOK, "navfolders.gohtml", gin.H{
				"folders": folders,
			})
		}
		if purpose == "view" {
			c.HTML(http.StatusOK, "folderview.gohtml", gin.H{
				"folders": folders,
			})
		}
	})
	r.POST("/api/folders/newFolder", func(c *gin.Context) {
		controllers.NewFolder(c, db)
	})
}

func loadPages(r *gin.Engine, db *gorm.DB) {
	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "homepage.html", nil)
	})
	r.GET("/search", func(c *gin.Context) {
		c.HTML(http.StatusOK, "search.html", nil)
	})
	r.GET("/folders", func(c *gin.Context) {
		id := c.Query("id")
		var folderId uint
		var folder models.Folder
		var name string
		var parentId *uint

		if id != "" && id != "0" {
			num, err := strconv.ParseUint(id, 10, 64)
			if err != nil {
				fmt.Println(err)
			}
			folderId = uint(num)
			result := db.Where("id = ?", folderId).First(&folder)
			if result.Error != nil {
				fmt.Println(result.Error)
			}
			name = folder.Name
			parentId = folder.ParentId
		} else {
			folderId = 0
			name = "Root"
			parentId = nil
		}

		c.HTML(http.StatusOK, "folders.gohtml", gin.H{
			"FolderId": folderId,
			"Name":     name,
			"ParentId": parentId,
		})
	})
}

func databaseSetup(dbLocation string) *gorm.DB {
	db, dbErr := gorm.Open(sqlite.Open(dbLocation), &gorm.Config{})
	if dbErr != nil {
		fmt.Println(dbLocation)
		log.Fatal("Cant open db: ", dbErr)
	}

	migrateErr := db.AutoMigrate(&models.Folder{}, &models.Link{})
	if migrateErr != nil {
		log.Fatal("Cant migrate: ", migrateErr)
	}

	return db
}
