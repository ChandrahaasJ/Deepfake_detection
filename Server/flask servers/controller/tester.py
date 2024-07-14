import moviepy.editor

def extractaudio(path):
    video=moviepy.editor.VideoFileClip(path)
    audio=video.audio
    audio.write_audiofile("D:/Projects/Deepfake_detection/extracted audios/extracted_audio.wav")
    return "Uploaded successfully"

extractaudio("C:/Users/niran/Videos/2024-04-22 00-10-08.mkv")