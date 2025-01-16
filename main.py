import tkinter as tk
from datetime import datetime
from tkinter import *
import re
from math import sqrt

current_time = datetime.now()
class Main(tk.Tk):
   def __init__(self):
       super().__init__()


       self.title("A.I. Ryan")
       self.geometry("500x500")
       self.configure(bg="black")


       self.background = tk.Frame(self, bg="black")
       self.background.pack(fill=tk.BOTH, expand=True)


       self.title_label = Label(self.background, text="A.I. Ryan 1.0", font=("Impact", 50, "bold"), fg="#D3FFCE", bg="black")
       self.title_label.pack(pady=20)


       self.textfield = Text(self.background, font=("Arial", 12), fg="#A9E37C", bg="darkgray", height=7, width=60)
       self.textfield.pack(pady=10)


       self.submit_button = Button(self.background, text="Submit", command=self.action_performed)
       self.submit_button.pack(pady=10)


       self.aimessage = Label(self.background,text="Hello There! My name's A.I. Ryan. How may I assist you today?",
                              fg="#A9E37C", bg="black", font=("Arial",16),wraplength=475)
       self.aimessage.pack(pady=20)
   def action_performed(self):
       text = self.textfield.get("1.0", "end-1c")
       self.checkGreeting(text)
       self.checkInquiry(text)
       self.checkMath(text)
   def checkGreeting(self, text):
       # Greetings - Positive, Negative, and Neutral Greeting Responses:
       positive_greeting_keywords = ["good", "fine", "great", "excellent", "awesome", "amazing", "splendid", "spectacular", "rad", "sick"]
       negative_greeting_keywords = ["bad", "awful", "terrible", "horrible", "disastrous", "catastrophic", "shit", "garbage", "sad", "depressing"]
       neutral_greeting_keywords = ["alright", "okay", "eh", "meh"]
       # Questions - of a particular categorical set:
       greeting_questions = ["hello", "hi", "howdy", "hey"]
       # Your logic to check for greetings here
       for keyword in positive_greeting_keywords:
           if keyword in text.lower():
               print("That's great to hear! How can I help you today?")
               return

       for keyword in negative_greeting_keywords:
           if keyword in text.lower():
               print("I'm sorry to hear that. How can I assist you?")
               return

       for keyword in neutral_greeting_keywords:
           if keyword in text.lower().removesuffix("!").removesuffix("?").removesuffix(",").removesuffix(".").strip():
              print("Wonderful! How can I assist you?")


       for keyword in greeting_questions:
           if keyword in text.lower().removesuffix("!").removesuffix("?").removesuffix(",").removesuffix(".").strip():
               print("Greetings, human! How can I help you today?")
               return


   def checkInquiry(self, text) :
       #Inquiry Library
       greeting_inquiry_questions = ["whats up","what's up","how are you","hows life","how's life","how is life","how's it going","hows it going","how is it going",
                                   "how do you do","how are you doing","how you doing","how's everything","hows everything","how is everything"]
       weather_inquiry = ["weather"]
       time_inquiry = ["time"]
       date_inquiry = ["date"]


       # logic for inquiries
       for keyword in greeting_inquiry_questions:
           if keyword in text.lower().removesuffix("!").removesuffix("?").removesuffix(",").removesuffix(".").strip():
               print("I'm doing absolutely wonderful! Thank you so much for asking! How can I help you today?")
               return


       for keyword in weather_inquiry:
           if keyword in text.lower().removesuffix("!").removesuffix("?").removesuffix(",").removesuffix(".").strip():
               print("The weather is currently 7°C, with a little bit of sunshine. Is there anything else I can help you with?")
               return


       for keyword in time_inquiry:
           if keyword in text.lower().strip().removesuffix("!").removesuffix("?").removesuffix(",").removesuffix("."):
               print("The time is currently " + current_time.strftime("%H:%M:%S") + ". Is there anything else I can help you with?")
               return


       for keyword in date_inquiry:
           if keyword in text.lower().removesuffix("!").removesuffix("?").removesuffix(",").removesuffix(".").strip():
               print("The date is currently " + current_time.strftime("%m/%d/%Y") + ". Is there anything else I can help you with?")
               return

   def checkMath(self, text):
       math_keywords = ["calculate", "math", "solve", "find", "what is", "what's"]

       for keyword in math_keywords:
           if keyword in text.lower().strip("!?.,"):
               numbers = re.findall(r'\b\d+\b', text)
               if numbers:
                   numbers = [int(num) for num in numbers]
                   print("Numeric values in the input:", numbers)
                   if "+" in text:
                       result = sum(numbers)
                       print("Sum of numeric values:", result)
                   elif "-" in text:
                       result = numbers[0] - sum(numbers[1:])
                       print("Difference of numeric values:", result)
                   elif "*" in text:
                       result = 1
                       for num in numbers:
                           result *= num
                       print("Multiplication of numeric values:", result)
                   elif "/" in text:
                       result = numbers[0]
                       for num in numbers[1:]:
                           if num != 0:
                               result /= num
                               print("Division of numeric values:", result)
                           else:
                               print("Error, cannot divide by zero. Please try again.")
                               return
                   elif "^" in text or "power of" in text:
                       result = numbers[0] ** numbers[1]
                       print("Power of numeric values:", result)
                   elif "sqrt" in text or "square root" in text or "√" in text:
                       result = sqrt(numbers[0])
                       print("Square root of numeric value: ", result)
                   elif "%" in text or "modulus" in text or "remainder of" in text:
                       result = numbers[0] % sum(numbers[1:])
                       print("Remainder of numeric values: ", result)
                   return
               else:
                   print("No numeric values found within the input. Please try again.")
                   return

if __name__ == "__main__":
   app = Main()
   app.mainloop()
