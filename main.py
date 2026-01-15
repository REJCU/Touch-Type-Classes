from sentence_choice import DisplayList
from engine import TypeEngine
import random

sentence_categories = {
    "HIGH_FREQUENCY": [
        "The quick brown fox jumps over the lazy dog",
        "She said that it was time to go home now",
        "They went to the park to play with a ball",
        "You should try to eat some good food today",
    ],
    "HOME_ROW_BASIC_FINGER_MOVEMENT": [
        "Ask the lad to add a sash to the dress",
        "All fall as the tall glass falls to the floor",
        "Dad said to add salt to the fat fish",
        "She sells shells by the side of the sea",
    ],
    "RHYTHMIC_SENTENCES": [
        "Work hard and play soft for a long life",
        "Keep your eyes on the road and your hands on the wheel",
        "Every small step leads to a very large leap",
        "Light the fire and stay warm in the cold night",
    ],
}

def main():
    x = DisplayList()
    sentence_list = x.result
    sentence = random.choice(sentence_list)
    print(f"Randomly chosen was: {sentence}")
    ui.py()
    # print(sentence_list)
    
    TypeEngine(text)

# UI.py gets the inputs



main()
