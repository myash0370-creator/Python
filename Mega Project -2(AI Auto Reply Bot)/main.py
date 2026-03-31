import pyautogui
import time
import pyperclip
from google import genai


client = genai.Client(
    api_key="YOUR API KEY",)

def is_last_message_from_sender(chat_log, sender_name="Ashish Room"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2026] ")[-1]
    if sender_name in messages:
        return True 
    return False
    

# Step 1: Click on the chrome icon at coordinates (1207, 1044)
pyautogui.click(1207, 1044)

time.sleep(1)

while True:
    time.sleep(5)

    # Step 2: Drag to select text
    pyautogui.moveTo(734,1280)
    pyautogui.dragTo(187, 996, duration=2.0, button='right')

    # Step 3: Copy
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)

    pyautogui.click(718, 196)

    # Step 4: Get clipboard
    chat_history = pyperclip.paste()

    print(chat_history)
    print(is_last_message_from_sender(chat_history))

    if is_last_message_from_sender(chat_history):

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"""
You are a person named Naruto who speaks Hindi and English.
You are from India and you are a coder.
You analyze chat history and roast people in a funny way.
Output should be the next chat response (text message only).
Do not start like this [11:38, 30/3/2026] Ashish Room:

{chat_history}
"""
        )

        reply = response.text

        pyperclip.copy(reply)

        # Step 5: Click message box
        pyautogui.click(795, 1030)
        time.sleep(1)

        # Step 6: Paste
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Step 7: Send
        pyautogui.press('enter')