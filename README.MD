# Answer Questions Parser
## ���������:
��������� �����������:
```
git clone https://github.com/invilso/banlist-tool-fastapi.git
```
��������� � ����������:
```
cd banlist-tool-fastapi
```
���������� ����������� ���������:
```
Linux:
source env/bin/activate 

Windows CMD:
cd env/Scripts
activate.bat

Windows PS:
& .\env\Scripts\Activate.ps1
```
����������� ���� � �������� � config.py.
```
PATH_TO_CHLOGS = 'path\\vot\\tak'
```
��������� ������, �� ������ �������� ���� db.json � ����� �� ��������:
```
python parser.py
```

����������� ������ ������ json �����, ������ ������������ ��� Pydantic:
```
class ModelItem(BaseModel):
    question: str
    answers: List[str]


class Model(BaseModel):
    __root__: List[ModelItem]
```