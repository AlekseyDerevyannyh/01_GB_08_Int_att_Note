from datetime import datetime
import time

from model import note

if __name__ == '__main__':
    current_time = datetime.now()
    time.sleep(2)
    current_time_2 = datetime.now()
    time.sleep(2)
    notes = []
    notes.append(note.Note(2, 'second note', 'My second note', str(datetime.now())))
    notes.append(note.Note(1, 'first note', 'My first note', str(current_time)))
    notes.append(note.Note(3, 'third note', 'My third note', str(current_time_2)))
    notes.sort()
    for note in notes:
        print(note)
