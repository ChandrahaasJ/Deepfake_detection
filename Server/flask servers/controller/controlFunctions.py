import moviepy.editor
import cv2
import numpy as np
import os
import instagram

def cleardir(path):
    for img in os.listdir(path):
        os.remove(os.path.join(path,img))


def extractaudio(path):
    video=moviepy.editor.VideoFileClip(path)
    audio=video.audio
    cleardir("D:/Projects/Deepfake_detection/extracted audios")
    save_path="D:/Projects/Deepfake_detection/extracted audios/extracted_audio.wav"
    audio.write_audiofile(save_path)
    save_path

def extractframes(path):
    savedir="D:/Projects/Deepfake_detection/flask servers/controller/savedframes"
    cleardir(savedir)
    frame_count=0

    video=cv2.VideoCapture(path)

    if not video.isOpened():
        return "error while opening the video"
    
    while True:
        success,frame=video.read()
        if not success:
            break
        else:
            frame_path=os.path.join(savedir,f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path,frame)

            frame_count+=1


# def process_video_dl(video_path):
#     cap = cv2.VideoCapture(video_path)
#     frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fps = cap.get(cv2.CAP_PROP_FPS)

#     output_filename = os.path.join(app.config['OUTPUT_FOLDER'], os.path.basename(video_path))
#     out = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Preprocess frame for prediction
#         image = cv2.resize(frame, (224, 224))
#         image = np.expand_dims(image, axis=0)
#         image = preprocess_input(image)

#         # Predict class labels
#         # preds = model.predict(image)
#         # max_index = np.argmax(preds[0])
#         # predicted_class = class_labels[max_index]

#         # # Annotate frame with prediction
#         # cv2.putText(frame, f'Prediction: {predicted_class}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2,
#         #             cv2.LINE_AA)
#         # out.write(frame)

#     cap.release()
#     out.release()

#     return output_filename