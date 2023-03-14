from moviepy.editor import *
import os
import sys

# Replace input_file_path and output_file_path with the paths to your input and output files
# get file name from cmd line:
input_file = sys.argv[1]
# check if file exists:
if not os.path.isfile(input_file):
    print("File does not exist")
    sys.exit(1)

# output file name is the same as input file name with .mp3 extension
output_file= input_file[:-4] + ".mp3"

# Load the video file
video = VideoFileClip(input_file)

# Extract the audio from the video and save it as an mp3 file
audio = video.audio
audio.write_audiofile(output_file)

# Close the video and audio files
video.close()
audio.close()
