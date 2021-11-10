import random, time

class Chat_bot:

    had_learnt = False

    def __init__(self):
        with open('ans.txt', encoding='UTF-8') as ansfile:
            self.answers = []
            for st in ansfile:
                st = st.replace('\n', '')
                self.answers.append(st.split('#'))

        with open('rep.txt', encoding='UTF-8') as repfile:
            self.replys = []
            for st in repfile:
                st = st.replace('\n', '')
                self.replys.append(st)

    def exit_proc(self):
        with open('ans.txt', 'w', encoding='UTF-8') as ansfile:
            for item in self.answers:
                it = str(item)[1:-1].replace("'","")
                ansfile.write(it)
                ansfile.write('\n')

        with open('rep.txt', 'w', encoding='UTF-8') as repfile:
            for item in self.replys:
                repfile.write(item)
                repfile.write('\n')

    def learn(self, an):
        new_phrase = input('Придумайте ответ или введите "-", чтобы не добавлять фразу :')
        if (new_phrase!='-'):
            self.replys.append(an)
            self.answers.append([input()])
            self.had_learnt = True
            print('Запомнил!')
        else:
            self.had_learnt = False
            print('Добавление новой фразы отменено')
        return self.had_learnt

    def reply(self, answer):
        game = True
        if answer in self.replys:
            index = self.replys.index(answer)
            print(random.choice(self.answers[index]))
            if answer == 'пока':
                if self.had_learnt:
                    self.exit_proc()
                game = False
        else:
            print('Не понимаю')
            self.learn(answer)
        time.sleep(0.5)
        return game


def main():
    gameloop = True

    chat_bot = Chat_bot()
    while gameloop:
        print('Вы: (для выхода напишите "пока")')
        rep = input().lower()
        gameloop = chat_bot.reply(rep)

if __name__ == '__main__':
    main()
