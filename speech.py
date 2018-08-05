import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()
i = input("Hello. Welcome to Conference Scribe. \nTo Start your recording please press 'Enter' ")

try:
    print ("Your recording has been started: ")
    print ("Say 'Good Bye'  to stop the recording")

    with m as source:
        r.adjust_for_ambient_noise (source)
    while True:
        with m as source:
            audio = r.listen (source)
            try:
                value = r.recognize_google (audio)
                if str is bytes:
                    result = u"{}".format (value).encode ("utf-8")
                else:
                    result = "{}".format (value)
                    if(result=="goodbye"):
                        break
                with open ("record.txt", "a") as f:
                    f.write (result + ".")
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass
            except KeyboardInterrupt:
                pass
except KeyboardInterrupt:
    pass


print("You Recoding has been Stopped")