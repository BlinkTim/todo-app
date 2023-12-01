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
- Adapt template to support looping/conditionals ✅
- Implement routes for DELETE, START and DELETE ✅
- Use placerholder data ✅
- Integrate FastAPI ✅
- Implement DELETE function ✅
- Implement Status Update Support ✅
- Implement .env (dotenv) File Support (db, host, port) ⌛
- Implement mySQL-Database Integration ✅
- Rework print() statements to use Python logging ✅
- Add more/better logging messages ❌
- Add comments to source code ❌
- update Readme.md ⌛
- Bugfix: Delete does not work if item is not finished ❌
- Finish Userdata Script ✅
   * Also use venv in userdata script ✅
   * Test locally under WSL/Ubuntu (apt instead of yum) ✅
   * Test standalone on EC2 (Amazon Linux: yum instead of apt) ✅
- Create a setup script that executes everthing needed ❌
- Implement CloudFormation Template (Security Group) ✅
   * CloudFormation via CLI
- Create s3 bucket ✅
- add unit tests ❌
- pip freeze ❌
- Extend CloudFormation to use RDS/Aurora instead of mySQL? ❌
- Add regression tests for all main routes ❌
- Use artillery/faker to stress test the todo app ❌

## Ressourcen
Wir erstellen eine Server-Anwendung die auf uvicorn (ASGI) basiert.
Wir erstellen verschiedene Routen (Endpoints) die mit FastAPI implementiert werden.
Wir benutzen Formulare innerhalb der HTML Datei um Daten an Python zu senden.
Wir benutzen Jinja2 als Templating Engine um HTML Dateien aus einem Verzeichnis namens templates zu laden, und dort bestimmte Variablen zu ersetzen bzw. Bedingungen/Schleifen auszuführen.
Wir benutzen Pydantic als Datenmodell für die Liste der Todo items, die ID jedes items ist ein Integer (autoincrement).
Wir verwenden SQLAlchemy für das Speichern innerhalb einer Datenbank (ORM).
Wir haben ein SQL-Script erstellt für die Erstellung der Datenbank und des nötigen Users mit den entsprechenden Rechten.
Wir haben eine requirements.txt erstellt die die Abhängigkeiten enthält für unsere Anwendung.
Diese sollten innerhalb eines Python venv installiert werden.

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
- [Python LOGGING](https://docs.python.org/3/howto/logging.html)

## Benutzung (unter GitBash)

 python -m venv  env

 danach environment  aktivieren mittels:

 source env/Scripts/activate

pip install -r requirements.txt

mysql -u root -p < sql-scripts/01-prepare-db.sql

 cd src
 uvicorn main:app --reload

Alternativ (innerhalb des src Unterverzeichnis):
python main.py

### Zusatzaufgabe
Deploye Deine Anwendung auf einer EC2 Instanz inkl. Datenbank.
