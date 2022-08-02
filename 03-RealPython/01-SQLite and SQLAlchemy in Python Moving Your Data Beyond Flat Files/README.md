# SQLite and SQLAlchemy in Python Moving Your Data Beyond Flat Files

https://realpython.com/courses/sqlite-sqlalchemy-python/

All programs process data in one form or another, and many need to be able to save and retrieve that data from one
invocation to the next. Python, SQLite, and SQLAlchemy give your programs database functionality, allowing you to store
data in a single file without the need for a database server.

You can achieve similar results using flat files in any number of formats, including CSV, JSON, XML, and even custom
formats. Flat files are often human-readable text files—though they can also be binary data—with a structure that can be
parsed by a computer program. You’ll explore using SQL databases and flat files for data storage and manipulation and
learn how to decide which approach is right for your program.

In this video course, you’ll learn how to use:

    Flat files for data storage
    SQL to improve access to persistent data
    SQLite for data storage
    SQLAlchemy to work with data as Python objects

## Notas rápidas sobre sqlite

https://www.sqlite.org/cli.html

https://www.sqlite.org/docs.html

```sqlite
janrax@janrax-matebook:~/Escritorio$ ls -ltr ejemplo.db
ls: no se puede acceder a 'ejemplo.db': No existe el archivo o el directorio
janrax@janrax-matebook:~/Escritorio$ sqlite3 ejemplo.db
SQLite version 3.37.2 2022-01-06 13:25:41
Enter ".help" for usage hints.
sqlite> CREATE TABLE people (
   person_id INTEGER PRIMARY KEY AUTOINCREMENT,
   first_name text NOT NULL,
   last_name text NOT NULL
);
sqlite> insert into people(first_name, last_name) values ("juan", "ra");
sqlite> insert into people(first_name, last_name) values ("pedro", "ra");
sqlite> select * from people;
1|juan|ra
2|pedro|ra

sqlite> .mode column
sqlite> select * from people;
person_id  first_name  last_name
---------  ----------  ---------
1          juan        ra       
2          pedro       ra       

sqlite> .width 0 20 -30
sqlite> select * from people;
person_id  first_name                                 last_name
---------  --------------------  ------------------------------
1          juan                                              ra
2          pedro                                             ra
sqlite> .mode box
sqlite> select * from people;
┌───────────┬──────────────────────┬────────────────────────────────┐
│ person_id │      first_name      │           last_name            │
├───────────┼──────────────────────┼────────────────────────────────┤
│ 1         │ juan                 │                             ra │
│ 2         │ pedro                │                             ra │
└───────────┴──────────────────────┴────────────────────────────────┘
sqlite> .excel
sqlite> select * from people;
-- El resultado se abre en la hoja de calculo del sistema

sqlite> .mode json
sqlite> select * from people;
[{"person_id":1,"first_name":"juan","last_name":"ra"},
{"person_id":2,"first_name":"pedro","last_name":"ra"}]
sqlite> .mode insert
sqlite> select * from people;
INSERT INTO "table"(person_id,first_name,last_name) VALUES(1,'juan','ra');
INSERT INTO "table"(person_id,first_name,last_name) VALUES(2,'pedro','ra');
sqlite> .output salida.txt
sqlite> select * from people;
-- el resultado se almacena en el fichero salida.txt

-- salgo y vuelvo a abrir la base de datos
sqlite> .quit
janrax@janrax-matebook:~/Escritorio$ sqlite3 ejemplo.db
SQLite version 3.37.2 2022-01-06 13:25:41
Enter ".help" for usage hints.
sqlite> .tables
people
sqlite> .schema people
CREATE TABLE people (
   person_id INTEGER PRIMARY KEY AUTOINCREMENT,
   first_name text NOT NULL,
   last_name text NOT NULL
);
sqlite> .schema
CREATE TABLE people (
   person_id INTEGER PRIMARY KEY AUTOINCREMENT,
   first_name text NOT NULL,
   last_name text NOT NULL
);
CREATE TABLE sqlite_sequence(name,seq);
sqlite> .dump
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE people (
   person_id INTEGER PRIMARY KEY AUTOINCREMENT,
   first_name text NOT NULL,
   last_name text NOT NULL
);
INSERT INTO people VALUES(1,'juan','ra');
INSERT INTO people VALUES(2,'pedro','ra');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('people',2);
COMMIT;
sqlite> 
```

## Backup y restore

10. Converting An Entire Database To A Text File

Use the ".dump" command to convert the entire contents of a database into a single UTF-8 text file. This file can be
converted back into a database by piping it back into sqlite3.

A good way to make an archival copy of a database is this:

    $ sqlite3 ex1 .dump | gzip -c >ex1.dump.gz

This generates a file named ex1.dump.gz that contains everything you need to reconstruct the database at a later time,
or on another machine. To reconstruct the database, just type:

    $ zcat ex1.dump.gz | sqlite3 ex2

The text format is pure SQL so you can also use the .dump command to export an SQLite database into other popular SQL
database engines. Like this:

    $ createdb ex2
    $ sqlite3 ex1 .dump | psql ex2

## Claves foraneas

    sqlite> PRAGMA foreign_keys = ON;
    sqlite> create table employee ( id integer primary key autoincrement, salary int not null, people_id integer, foreign key (people_id) references people(person_id));
    sqlite> insert into employee ( salary, people_id ) values ( 1000, 9);
    Error: stepping, FOREIGN KEY constraint failed (19)

## Ejemplo básico python sqlarchemy

```python
from sqlalchemy import create_engine, text

# Si no existe el fichero, lo crea.
engine = create_engine("sqlite:///./example.db", echo=True, future=True)
conn = engine.connect()

# Creación
conn.execute(text("""
CREATE TABLE IF NOT EXISTS users ( 
id integer primary key autoincrement,
name varchar, 
age int
);
"""))

# Insertar
NAME = "optimus prime"
AGE = 200
result = conn.execute(text("INSERT INTO users(name, age) VALUES (:name, :age)"), [{"name": NAME, "age": AGE}])
print(result)

# Commit necesario
conn.commit()

# Insertar múltiples registros
NAME = "optimus prime"
AGE = 200
result = conn.execute(text("INSERT INTO users(name, age) VALUES (:name, :age)"),
                      [{"name": NAME, "age": AGE}, {"name": NAME, "age": AGE}])
print(result)

# Commit necesario
conn.commit()

# Seleccionar básico
result = conn.execute(text("SELECT * FROM users"))
for row in result:
    print(f"nombre: {row.name}")

# Seleccionar definido
result = conn.execute(text("SELECT name, age FROM users"))
for name, age in result:
    print(f'nombre: {name}, edad: {age}')

# Seleccionar diccionarios
result = conn.execute(text("SELECT name, age FROM users"))
for row in result.mappings():
    print(row)

# Rollback
NAME = "MALOTE"
result = conn.execute(text("INSERT INTO users(name, age) VALUES (:name, :age)"), [{"name": NAME, "age": AGE}])
conn.rollback()

```