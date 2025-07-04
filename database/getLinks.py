class Link:
    def __init__(self,id, title, link, tag):
        self.id = id
        self.title = title
        self.link = link
        self.tag = tag
    def to_dict(self):
        return {"id": self.id, "title": self.title, "link": self.link, "tag": self.tag}

def final_links(links):
    results = []
    for row in links:
        id = row[0]
        title = row[1]
        link = row[2]
        tag = row[3]
        results.append(Link(id,title, link, tag).to_dict())
    return results