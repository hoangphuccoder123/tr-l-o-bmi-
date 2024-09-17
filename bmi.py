import speech_recognition as sr
from gtts import gTTS
import os

# Hàm để nhận giọng nói tiếng Việt từ micro
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Vui lòng nói (ngôn ngữ: tiếng Việt)...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Sử dụng Google Speech Recognition để nhận diện giọng nói
            print("Đang nhận diện giọng nói...")
            text = recognizer.recognize_google(audio, language="vi-VN")
            print(f"Bạn đã nói: {text}")
            return text
        except sr.UnknownValueError:
            print("Không nhận diện được giọng nói!")
        except sr.RequestError:
            print("Lỗi khi kết nối đến Google API.")
        return None

# Hàm tính BMI dựa trên cân nặng và chiều cao
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Hàm chuyển văn bản thành giọng nói
def text_to_speech(text):
    tts = gTTS(text=text, lang='vi')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3") 

# Chạy chương trình
if __name__ == "__main__":
    # Nhận cân nặng từ giọng nói
    print("Nhập cân nặng của bạn (kg):")
    weight_text = recognize_speech_from_mic()
    weight = float(weight_text) if weight_text else None

    # Nhận chiều cao từ giọng nói
    print("Nhập chiều cao của bạn (mét):")
    height_text = recognize_speech_from_mic()
    height = float(height_text) if height_text else None

    if weight and height:
        # Tính BMI
        bmi = calculate_bmi(weight, height)
        result = f"Chỉ số BMI của bạn là {bmi:.2f}"
        print(result)

        # Đọc kết quả bằng giọng nói
        text_to_speech(result)