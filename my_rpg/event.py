class Event:
    def __init__(self, EventID: int, EventType = "A", EventName = "未知的活動名稱"):
        self.id = EventID
        self.type = EventType
        self.name = EventName

    def __str__(self):
        tag_map = {
            'A': "限時活動",
            'B': '常駐活動',
            'C': '抽獎活動',
            'D': '限定抽獎',
            'E': '慶典活動'
        }
        tag = tag_map.get(self.type)
        return f'{tag} - {self.name} ({self.type}{self.id})'