from datetime import datetime

class Note:
    """Logic note definition"""
    def __init__(self,title,content,date):
        self.title = title
        self.content = content
        self.date = date
    
    # Getter
    @property
    def title(self):
        return self._title
    # Setter
    def title(self,new_title):
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Note's title must be a string or not equal to a empty string")
        self._title = new_title
    

    # Getter
    @property
    def content(self):
        return self._content
    # Setter
    def content(self,new_content):
        if not isinstance(new_content, str) or not new_content.strip():
            raise ValueError("Note's content must be a string or not equal to a empty string")
        self._content = new_content


    # Getter
    @property
    def date(self):
        return self._date
    # Setter
    def date(self,new_date):
        actual_date = datetime.now().strftime("%d/%m/%Y") 
        self._date = new_date