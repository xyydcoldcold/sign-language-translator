import cv2
import mediapipe as mp
import pyttsx3

# 初始化文字转语音
engine = pyttsx3.init()
def speak(text):
    print(f"SPEAK: {text}")
    engine.say(text)
    engine.runAndWait()


# 初始化 MediaPipe 手部模型
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# 打开摄像头
cap = cv2.VideoCapture(1)
detected = False  # 防止语音重复播放

while True:
    success, img = cap.read()
    if not success:
        break

    # 翻转镜像图像
    img = cv2.flip(img, 1)

    # 转换颜色空间
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # 示例：判断是否是“竖大拇指”的姿势（简单粗暴方式）
            thumb_tip = handLms.landmark[4]
            index_tip = handLms.landmark[8]

            if thumb_tip.y < index_tip.y and not detected:
                gesture_text = "Thumbs up"
                speak(gesture_text)
                detected = True
            elif thumb_tip.y > index_tip.y:
                detected = False  # 重置状态，允许再次触发

    cv2.imshow("Sign Language Recognition", img)

    # 按 'q' 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
