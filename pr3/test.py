import unittest
from main import Chat_bot

class CheckAnswerTest(unittest.TestCase):
    chat_bot = Chat_bot()

# фраза, которая заканчивает беседу
    def test1(self):
        result = self.chat_bot.reply('пока')
        self.assertEqual(result, False)

# любая фраза
    def test2(self):
        result = self.chat_bot.reply('привет')
        self.assertEqual(result, True)

# добавление новой фразы (ввод: любой, но не "-")
    def test3(self):
        result = self.chat_bot.learn('аа')
        self.assertEqual(result, True)

# отказ добавления новой фразы (ввод: "-")
    def test4(self):
        result = self.chat_bot.learn('аа')
        self.assertEqual(result, False)