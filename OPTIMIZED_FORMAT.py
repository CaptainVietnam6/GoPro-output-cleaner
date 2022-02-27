import os
sc=0
while True:
    if os.path.exists(f"./GoPro{sc}.mp4")==True:
        sc+=1
    if os.path.exists(f"./GoPro{sc}.mp4")==False:
        break
for f in os.listdir("./"):
    if f.endswith(".MP4"):
        os.rename(f, f"GoPro{sc}.mp4")
        sc+=1
    elif f.endswith(".WAV")or f.endswith(".THM")or f.endswith(".LRV"):
        os.remove(f)