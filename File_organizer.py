import os
import shutil
import time

pic_path = '/home/garuda/Pictures'
video_path = '/home/garuda/Videos'
files_path = '/home/garuda/Documents'
audio_path = '/home/garuda/Music'

dir_path= '/home/garuda/Desktop/Mover'
img_list = ['.png','.jpg','.jpeg','.gif']
video_list = ['.mkv','.mp4']
audio_list = ['.avi','.mp3']
file_list = ['.doc','.pdf','.pptx','.txt']

while True:
    file_list = os.listdir(dir_path)
    if len(file_list)>0:
        file_name = file_list[0]
        file_path = dir_path + f'/{file_name}'

        for types in img_list:
            if types in file_name:
                #shutil.move(file_path, pic_path)
                os.system(f'mv {file_path} {pic_path}')
                break
        for types in video_list:
            if types in file_name:
                #shutil.move(file_path, video_path)
                os.system(f'mv {file_path} {video_path}')
                break
        for types in audio_list:
            if types in file_name:
                #shutil.move(file_path, audio_path)
                os.system(f'mv {file_path} {audio_path}')
                break
        for types in file_list:
            if types in file_name:
                #shutil.move(file_path, files_path)
                os.system(f'mv {file_path} {files_path}')
                break

        file_list = []
    else:
        pass
        