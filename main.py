from datetime import datetime
import uuid
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

filename = str(uuid.uuid4())
print(os.path.join(BASE_DIR+"/video_down",filename))