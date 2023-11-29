## Todo App
Erstelle eine Todo App, im templates Folder findest Du das HTML Markup dass Du für die Anwendung benötigst.
Folgende Funktionalität soll die ToDo Anwendung enthalten:

1. Erstellen eines ToDos
2. ToDos anzeigen
3. Status eines ToDos ändern von "open" zu "in progess"
4. Status ändern von "in progress" zu "finished"
5. Löschen eines ToDos

Die einzelenen ToDos sollen in einer MYSQL Datenbank gespeichert werden inkl. deren Zustand.

Erstelle Dir ein Repository in Deinem Github Account und übertrage den Code dorthin.
Achte darauf, dass Du die Inhalte des VENV nicht mit in Dein Repo überträgst.

## Backlog
- Adapt template to support looping ✅
- Implement routes for DELETE, START and DELETE ✅
- Use placerholder data ✅
- Integrate FastAPI and  Pydantic ✅
- Implement DELETE Funktion ❌
- Implement Status Update Support ❌
- Implement .env (dotenv) File Support ❌
- Implement mySQL-Database Integration (momentan nur database.py) ❌
- Add comments to source code, update Readme.md ❌
- Implement Userdata Script ❌
- Implement CloudFormation Template ❌
- Test on EC2 ❌

## Ressourcen
Wir erstellen eine Server-Anwendung die auf uvicorn basiert.
Wir erstellen verschiedene Routen die mit FastAPI implementiert werden.
Wir benutzen Jinja2 als Templating Engine um HTML Dateien aus einem Verzeichnis namens templates zu laden, und dort bestimmte Variablen zu ersetzen bzw. Bedingungen auszuführen.
Wir benutzen Pydantic als Datenmodell für die Liste der Todo items, die ID jedes items wird mittels uuid4() generiert.
Wir verwenden SQLAlchemy für das Speichern innerhalb einer Datenbank.

- [Frontend Intro](https://docs.google.com/presentation/d/1YoxRv7m7NmFjPQwffTqlgyJt0wIOvlMiX2XDnBZWjbY) 
- [Fastapi tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Jinja2 loops](https://ttl255.com/jinja2-tutorial-part-2-loops-and-conditionals/#loops)
- [To use forms, first install python-multipart. pip install python-multipart](https://fastapi.tiangolo.com/tutorial/request-forms/)
- [pydantic data model](https://docs.pydantic.dev/latest/examples/secrets/)
- [pydantic BaseModel](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic UUID](https://docs.pydantic.dev/2.0/usage/types/uuids/)
- [UUID Example](https://docs.pydantic.dev/latest/concepts/fields/)
- [Jinja2 loop.index](https://jinja.palletsprojects.com/en/3.0.x/templates/)
- [Remove elements from List](https://www.geeksforgeeks.org/how-to-remove-an-item-from-the-list-in-python/)
- [Python enum](https://www.geeksforgeeks.org/enum-in-python/)
- [Python enum value attribute](https://docs.python.org/3/howto/enum.html)
- [SQLAlchemy QuickStart](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [SQLAlchemy Reference](https://docs.sqlalchemy.org/en/20/orm/)
- [Understanding SQLAlchemy](https://dev.to/ajipelumi/understanding-sqlalchemy-orm-and-sqlalchemy-core-3nm5)

## Benutzung (unter GitBash)

python -m venv env

danach environment aktivieren mittels:

source env/Scripts/activate

pip install -r requirements.txt

mysql -u root -p < sql-scripts/01-prepare-db.sql

cd src
uvicorn main:app --reload

Alternativ (innerhalb des src Unterverzeichnis):
python main.py

### Zusatzaufgabe
Deploye Deine Anwendung auf einer EC2 Instanz inkl. Datenbank.
