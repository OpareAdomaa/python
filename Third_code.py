import random

#Quotes generation
Quotes = [
    "In the middle of difficulty lies opportunity. - Albert Einstein",
    "The only way to deal with this life meaningfully is to find your passion and give it your all.",
    "We suffer more often in imagination than in reality. - Seneca",
    "What you think, you become. What you feel, you attract. What you imagine, you create. - Buddha",
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "The wound is the place where the Light enters you. - Rumi",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "He who has a why to live can bear almost any how. - Friedrich Nietzsche"
]

choice = random.choice(Quotes)
print("The quote of the day is : \n")
print(choice)