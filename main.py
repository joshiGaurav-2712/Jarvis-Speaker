import pyttsx3

if __name__=="__main__":
        print("Welcome to Jarvis Speaker created by Gaurav Joshi!")
        while True:
            #initialization
            engine=pyttsx3.init() 
            words=input("Enter what you want me to speak and write quit to exit:")
        
            if words=="quit":
                #testing
                engine.say("Good Bye friend. Thank you for using Jarvis Speaker created by Gaurav Joshi!")
                engine.runAndWait()
                break
          
            engine.say(f"{words}")
            engine.runAndWait()

        print("Program Successfully terminated!")  
        