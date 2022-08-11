from datetime import datetime
from hm import urok

now = datetime.now()


while urok() == now:
    print("Lesson time")
    break



