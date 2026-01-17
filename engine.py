import time

class TypeEngine:
    def __init__(self, text):
        self.target = text
        self.current_input = ""
        self.start_time = None
        self.end_time = None
        self.total_keystroke = 0

    def process_key(self, char):
        if self.start_time is None:
            self.start_time = time.time()

        if char == "BACKSPACE":
            if len(self.current_input) > 0:
                self.current_input = self.current_input[:-1]
        else:
            self.current_input += char
            self.total_keystroke += 1
