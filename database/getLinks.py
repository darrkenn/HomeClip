class Link:
    def __init__(self,id, title, link, tag, folder):
        self.id = id
        self.title = title
        self.link = link
        self.tag = tag
        self.folder = folder
    def to_dict(self):
        return {"id": self.id, "title": self.title, "link": self.link, "tag": self.tag, "folder": self.folder}

def final_links(links):
    results = []
    for row in links:
        id = row[0]
        title = row[1]
        link = row[2]
        tag = row[3]
        folder = row[4]
        results.append(Link(id,title, link, tag, folder).to_dict())
    return results