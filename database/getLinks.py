class Link:
    def __init__(self,id, title, link):
        self.id = id
        self.title = title
        self.link = link
    def to_dict(self):
        return {"id": self.id, "title": self.title, "link": self.link}

def final_links(links):
    results = []
    for row in links:
        id = row[0]
        title = row[1]
        link = row[2]
        results.append(Link(id,title, link).to_dict())
    return results