import os
for file in os.listdir("./"):
    if file.endswith(".WAV") or file.endswith(".THM") or file.endswith(".LRV"):
        os.remove(file)