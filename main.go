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
	loadPages(r)

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
		c.HTML(http.StatusOK, "newlink.html", nil)
	})
	r.GET("/api/html/clear", func(c *gin.Context) {
		c.HTML(http.StatusOK, "", nil)
	})

	//Links
	r.GET("/api/links/toplinks", func(c *gin.Context) {
		var links []models.Link
		result := db.Preload("Tag").Limit(5).Order("clicks desc").Find(&links)
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
	r.POST("/api/links/delete/:linkid/:tagid", func(c *gin.Context) {
		controllers.DeleteLink(c, db)
	})
}

func loadPages(r *gin.Engine) {
	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "homepage.html", nil)
	})
	r.GET("/search", func(c *gin.Context) {
		c.HTML(http.StatusOK, "search", nil)
	})
}

func databaseSetup(dbLocation string) *gorm.DB {
	db, dbErr := gorm.Open(sqlite.Open(dbLocation), &gorm.Config{})
	if dbErr != nil {
		fmt.Println(dbLocation)
		log.Fatal("Cant open db: ", dbErr)
	}

	migrateErr := db.AutoMigrate(&models.Folder{}, &models.Link{}, models.Tag{})
	if migrateErr != nil {
		log.Fatal("Cant migrate: ", migrateErr)
	}

	return db
}
