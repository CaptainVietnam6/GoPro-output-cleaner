import os
suffix_count = 0
while True:
    if os.path.exists(f"./GoPro{suffix_count}.mp4") == True:
        suffix_count += 1
    if os.path.exists(f"./GoPro{suffix_count}.mp4") == False:
        break
for file in os.listdir("./"):
    if file.endswith(".MP4"):
        os.rename(file, f"GoPro{suffix_count}.mp4")
        suffix_count += 1