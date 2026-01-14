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


category_names = list(sentence_categories.keys())


class DisplayList():
    def __init__(self):
        self.display_sentence()
        self.get_choice()

    def display_sentence(self):
        for i, name in enumerate(category_names):
            print(f"{i + 1}---{name}")

# Get user's choice
    def get_choice(self):
        try:
            choice_index = int(input(">>> ")) - 1
            if not 0 <= choice_index < len(category_names):
                print("Invalid choice!")
                exit()
            chosen_category_name = category_names[choice_index]
            sentence_list = sentence_categories[chosen_category_name]
            print(sentence_list)
            return sentence_list
        except (ValueError, IndexError):
            print("Invalid input!")
            exit()
