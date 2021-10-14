import re
import time
from datetime import date
import os
import json
import sys
import config


class Patterns:
    question = r'\[(\d\d):(\d\d):(\d\d)] Вопрос от (\S+) ID \d+: (.+)'
    answer = r'\[(\d\d):(\d\d):(\d\d)] От \S+ для (\S+): (.+)'


class Parser:
    lines = None

    def __init__(self, filename: str) -> None:
        self.lines = self.getLines(filename)
    
    def getLines(self, filename: str) -> list:
        with open(filename, 'r', encoding='windows-1251') as f:
            try:
                return re.split('\n\n', f.read())
            except:
                return ['']

    def printLine(self) -> None:
        for line in self.lines:
            print(line)
        #print(self.lines[35])

    def parseLines(self):
        database = []
        for key, line in enumerate(self.lines):
            if re.match(Patterns.question, line):
                q_hours, q_minutes, q_secons, q_nickname, q_text = re.findall(Patterns.question, line)[0] #префикс q обозначает что это переменная вопроса
                q_time_tuple = (2017, 11, 12, int(q_hours), int(q_minutes), int(q_secons), 2, 317, 0)
                next_line = key + 1
                answers = []
                while key + 100 != next_line:
                    try:
                        if re.match(Patterns.answer, self.lines[next_line]):
                            a_hours, a_minutes, a_secons, a_nickname, a_text = re.findall(Patterns.answer, self.lines[next_line])[0] #префикс a обозначает что это переменная ответа
                            if a_nickname == q_nickname:
                                a_time_tuple = (2017, 11, 12, int(a_hours), int(a_minutes), int(a_secons), 2, 317, 0)
                                if time.mktime(a_time_tuple) < time.mktime(q_time_tuple) + 121:
                                    answers.append(a_text)
                        if re.match(Patterns.question, self.lines[next_line]):
                            _, _, _, q_nickname_hot, _ = re.findall(Patterns.question, line)[0] # суфикс hot значит что это хотфикс
                            if q_nickname_hot == q_nickname:
                                break
                    except:
                        pass
                    next_line = next_line + 1
                if len(answers) != 0:
                    database.append({'question': q_text, 'answers': answers})
        return database


class Chlogs:
    database = []
    files = None

    def __init__(self, directory) -> None:
        self.files = self.getChatlogs(directory)

    def getChatlogs(self, directory):
        files = os.listdir(directory)
        return list(filter(lambda x: x.endswith('.txt'), files))

    def addToDatabase(self, list):
        for obj in list:
            self.database.append(obj)

    def writeDatabase(self):
        with open('db.json', 'w+', encoding='utf-8') as f:
            f.write(json.dumps(self.database, indent=4))
        return True

    def parse(self):
        start_time = time.time()
        for key, file in enumerate(self.files):
            p = Parser(config.PATH_TO_CHLOGS+'\\'+file)
            self.addToDatabase(p.parseLines())
            sys.stdout.write('\033[K' + f"[PROGRESS]: {key}/{len(self.files)} File: {file}" + '\r')
            print()
        if self.writeDatabase():
            print(f'[DONE]: {len(self.database)} questions parsed! Completed in {time.time() - start_time} seconds.')
    

c = Chlogs(config.PATH_TO_CHLOGS)
c.parse()