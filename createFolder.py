import os
import datetime

today = datetime.datetime.today().strftime("%Y%m%d")

# folder_path = r"C:\Users\cs2u56\Downloads" + today
folder_path = os.path.join(r"C:\Users\phongnl\Downloads", today)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
else:
    print(f"Folder {today} Exist !")