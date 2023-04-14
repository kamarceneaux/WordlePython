import random


class Wordle:

    def __init__(self, words: list[str]):
        self.words = words
        self.guess_attempts = 5
        self.current_answer = []
        self.correct_answer = " "
        self.correct_answer_arr = None

    def selectWord(self) -> str:
        """
        Selects a word from our list contain words and returns
        :return:
        """
        self.correct_answer = random.choice(self.words)

        self.correct_answer_arr = list(self.correct_answer)
