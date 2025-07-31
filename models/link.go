package models

type Link struct {
	Id       uint    `gorm:"primaryKey;autoIncrement" json:"id"`
	Url      string  `json:"url"`
	Name     string  `json:"name"`
	Clicks   uint    `gorm:"default:0" json:"clicks"`
	Colour   string  `gorm:"default:white"`
	FolderId *uint   `json:"folderId" gorm:"default:null"`
	Folder   *Folder `gorm:"foreignKey:FolderId;constraint:OnUpdate:CASCADE,OnDelete:SET NULL;default:null"`
}
