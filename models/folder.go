package models

type Folder struct {
	Id       uint       `gorm:"primaryKey;autoIncrement"`
	Name     string     `gorm:"uniqueIndex;not null" json:"name"`
	ParentId *uint      `json:"parentId"`
	Parent   *Folder    `gorm:"constraint:OnUpdate:CASCADE,OnDelete:SET NULL;"`
	Children *[]*Folder `gorm:"foreignKey:ParentId" json:"children"`
	Links    *[]Link    `json:"links"`
}
