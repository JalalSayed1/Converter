from moviepy.editor import *
import os
import sys

# get all .mp4 files in the 'files' folder and put them in a list:
files_paths = [os.path.join('files', file) for file in os.listdir('files') if file.endswith('.mp4')]

# sort the list according to file size (from small to large)
files_paths.sort(key=os.path.getsize)

print('Files to found (sorted according to file size):')
      for file in files_paths:
    # print filename and size:
    print(f'    {file}')


for input_file_path in files_paths:
    # output file name is the same as input file name with .mp3 extension
    output_file_path = input_file_path[:-4] + ".mp3"

    # Load the video file
    video = VideoFileClip(input_file_path)

    # Extract the audio from the video and save it as an mp3 file
    audio = video.audio
    audio.write_audiofile(output_file_path)

    # Close the video and audio files
    video.close()
    audio.close()
