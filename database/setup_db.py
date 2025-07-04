import sqlite3

def setup_db():
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Tags (TagId INTEGER PRIMARY KEY, Tag TEXT UNIQUE NOT NULL, Favourite BOOLEAN NOT NULL DEFAULT FALSE)")
    c.execute("CREATE TABLE IF NOT EXISTS Folders (FolderId INTEGER PRIMARY KEY, Folder TEXT UNIQUE NOT NULL, Favourite BOOLEAN NOT NULL DEFAULT FALSE)")
    c.execute("""
              CREATE TABLE IF NOT EXISTS Links
              (
                  LinkId   INTEGER PRIMARY KEY AUTOINCREMENT,
                  Title    TEXT NOT NULL,
                  Link     TEXT NOT NULL,
                  TagId    INTEGER DEFAULT NULL,
                  FolderId INTEGER DEFAULT NULL,
                  Clicks INTEGER DEFAULT 0,
                  FOREIGN KEY (TagId) references Tags (TagId),
                  FOREIGN KEY (FolderId) references Folders (FolderId)
              )
              """
    )
    conn.commit()
    conn.close()
    print("Database setup complete")
