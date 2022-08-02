import time
from timeit import Timer

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine('postgresql://root:root@localhost:5432/janrax', echo=False, future=True)
conn = Session(engine)

# Creación
conn.execute(text("""
CREATE TABLE IF NOT EXISTS users (
name varchar, 
age int
);
"""))

# Borrado
conn.execute(text("""
DELETE FROM users;
"""))

# Insertar
NAME = "optimus prime"
AGE = 200
result = conn.execute(text("INSERT INTO users(name, age) VALUES (:name, :age)"), [{"name": NAME, "age": AGE}])
print(result)

# Insertar múltiples registros
NAME = "optimus prime"
AGE = 200
result = conn.execute(text("INSERT INTO users(name, age) VALUES (:name, :age)"),
                      [{"name": NAME, "age": AGE}, {"name": NAME, "age": AGE}])
print(result)

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

# Ejemplo insercción múltiple
personajes = []
for i in range(1000):
    personajes.append({"name": f"tio{i}", "age": 4567})

t = time.time()
result = conn.execute(text("INSERT INTO users(name, age) VALUES (:name, :age)"), personajes)
conn.commit()
print(f"Tarda: {round(time.time() - t, 2)} segundos")

# Rollback
NAME = "MALOTE"
conn.execute(text("INSERT INTO users(name, age) VALUES (:name, :age)"), [{"name": NAME, "age": AGE}])
conn.rollback()
