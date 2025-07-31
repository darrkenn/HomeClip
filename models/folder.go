package models

type Folder struct {
	Id       uint      `gorm:"primaryKey;autoIncrement"`
	Name     string    `gorm:"not null" json:"name"`
	Colour   string    `gorm:"not null; default:white"`
	ParentId *uint     `json:"parentId" gorm:"default:null"`
	Parent   *Folder   `gorm:"constraint:OnUpdate:CASCADE,OnDelete:SET NULL;default:null"`
	Children []*Folder `gorm:"foreignKey:ParentId;default:null" json:"children"`
	Links    []Link    `json:"links" gorm:"foreignKey:FolderId"`
}
