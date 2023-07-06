import os
import openai
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time

openai.api_key = "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"

#setting all the emotions that the ai can feel
emotionsstring = ""
emotions = {"Happy": "Happy_Face.jpg", "Sad": "Sad_Face.jpg", "Angry": "Angry_Face.jpg", "Neutral": "Neutral_Face.jpg"}
for emotion in emotions:  
    emotionsstring = emotionsstring + emotion + ", "
emotionsstring = emotionsstring[:-2]


#welcome message
print("Welcome to the Emotion Chatbot")
print("Your ai has access to these emotions: " + emotionsstring)
print("To quit the program type quit")

while True:
    
    user = input()
    if user == "quit":
        break
    user_message = " you have 3 emotions" + emotionsstring + " choose the emotion that you think the user wants you to feel followd by a period. then respond to the user with a message that uses that emotion. the format of you response should be Emotion: THE_EMOTION then a newline then ur respone This is the message from the user: " + user
    response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": 'Act Like a friend'},
                                {"role": "user", "content": user_message}
                    ])
    '''
     print("---------------------")
    print(response)
    print("---------------------")
    '''
   
    content = response["choices"][0]["message"]["content"]
    emotion = content.split(":")[0].strip()
    content = content.split(":")[1]
    print(emotion)
    image = mpimg.imread(emotions[emotion])
    

    #remove spaces
    
    print(content)
    plt.imshow(image)
    plt.show()
    # wait for a 2 seconds then delete plt
    time.sleep(2)
    plt.close()
    