package models

type Link struct {
	Id       uint   `gorm:"primaryKey;autoIncrement" json:"id"`
	Url      string `json:"url"`
	Name     string `json:"name"`
	Clicks   uint   `gorm:"default:0" json:"clicks"`
	FolderId *uint  `json:"folderId"`
	TagId    *uint  `json:"tagId"`
	Tag      *Tag   `gorm:"foreignKey:TagId;constraint:OnUpdate:CASCADE,OnDelete:SET NULL;" json:"tag"`
}
