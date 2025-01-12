# Speech Recognition 설치
import speech_recognition as sr
def make_folder_path(folder_type="Training", data_type="Voice_Data"):
    '''
    폴더까지의 주소를 리턴해주는 함수
    folder_type = "Training" # or 'Validation'
    data_type = "Origin" # or 'Labeling'
    '''
    sound_folder_path = f"/stt_data/{folder_type}/{data_type}/D02/"
    return sound_folder_path


def make_file_path(path=make_folder_path(), file_type="wav", j_folder_num="05",s_folder_no="01", file_no="0001"):
    '''
    파일까지의 주소를 리턴해주는 함수
    folder_no : "01"~"30"
    file_no : 각각 다름
    '''
    sound_file_folder = f"S0000{s_folder_no}"
    file_path = f"{path}/J{j_folder_num}/{sound_file_folder}/{file_no}.{file_type}"

    return file_path

# folder_path = make_folder_path()
# file_path = make_file_path()

r = sr.Recognizer()

# audio file 불러오기
file_path = make_file_path(s_folder_no='02')
audio_file = sr.AudioFile(file_path)

# print(audio_file)
with audio_file as source:
    audio = r.record(source)

print(r.recognize_google(audio, language='ko-KR'))