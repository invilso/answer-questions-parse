# Answer Questions Parser
## Установка:
Клонируем репозиторий:
```
git clone https://github.com/invilso/banlist-tool-fastapi.git
```
Переходим в директорию:
```
cd banlist-tool-fastapi
```
Активируем виртуальное окружение:
```
Linux:
source env/bin/activate 

Windows CMD:
cd env/Scripts
activate.bat

Windows PS:
& .\env\Scripts\Activate.ps1
```
Редактируем путь к чатлогам в config.py.
```
PATH_TO_CHLOGS = 'path\\vot\\tak'
```
Запускаем парсер, на выходе получаем файл db.json в папке со скриптом:
```
python parser.py
```

Питоновская модель данных json файла, можете использовать для Pydantic:
```
class ModelItem(BaseModel):
    question: str
    answers: List[str]


class Model(BaseModel):
    __root__: List[ModelItem]
```