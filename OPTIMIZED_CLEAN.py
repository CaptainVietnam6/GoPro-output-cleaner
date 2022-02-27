import os
n=0
d=f"./GoPro{n}.mp4"
l=(".WAV",".THM",".LRV")
while True:
    if os.path.exists(d)==True:
        n+=1
    else:
        break
for f in os.listdir("./"):
    if f.endswith(".MP4"):
        os.rename(f,f"GoPro{n}.mp4")
        n+=1
    elif f.endswith(l):
        os.remove(f)