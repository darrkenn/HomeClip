package models

type Tag struct {
	Id   uint   `gorm:"primaryKey;autoIncrement"`
	Name string `gorm:"uniqueIndex;not null" json:"name"`
}
