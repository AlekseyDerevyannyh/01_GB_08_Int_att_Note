class Note:
    def __init__(self, id_note, title, msg, date_modified):
        self.__id_note = id_note
        self.__title = title
        self.__msg = msg
        self.__date_modified = date_modified

    def __str__(self):
        return 'ID: ' + self.__id_note + '. Title: ' + self.__title + '. Message: ' + \
            self.__msg + '. Date modified: ' + self.__date_modified
