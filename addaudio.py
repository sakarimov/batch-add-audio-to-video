from os import listdir
import subprocess
from random import choice, sample


# change these to your liking
video_dir = "path/to/video"
audio_dir = "path/to/audio"
output_dir = "path/to/output"


# function for filtering files based on extension
# output = list
def saring_file(directory, extension):
    # file list of directory
    file_list = listdir(f"{directory}")
    the_files = []
    for i in file_list:
        the_files.append(f'{i}')
        sorted_files = [f for f in the_files if (str(f))[-3:] == f"{extension}"]
    return sorted_files

# for the subrocess to be running the " " in directory path must be converted to "\ "
conv_video_dir = video_dir.replace(" ", "\ ")
conv_audio_dir = audio_dir.replace(" ", "\ ")
conv_output_dir = output_dir.replace(" ", "\ ")
# video and audio files variables
video_files = saring_file(directory = video_dir, extension = "mp4")
audio_files = saring_file(directory = audio_dir, extension = "mp3")

# the looping process
for i in video_files:
    randmusic = choice(audio_files)
    print([i, randmusic])
    subprocess.run(f'ffmpeg -i {conv_video_dir}/{i} -i {conv_audio_dir}/{randmusic} -c copy -map 0:v:0? -map 1:a:0 -shortest {conv_output_dir}/{i}', shell=True, check=True, encoding='utf-8')
    subprocess.run(f'rm {conv_video_dir}/{i}', shell=True, check=True, encoding='utf-8')
