from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///./example1.db", echo=True, future=True)
conn = engine.connect()

# Creación
conn.execute(text("""
CREATE TABLE IF NOT EXISTS users ( 
name varchar, 
age int
);
"""))

# Insertar
NAME = "optimus prime"
AGE = 200
result = conn.execute(text("INSERT INTO users VALUES (:name, :age)"), [{"name": NAME, "age": AGE}])
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
NAME = "cabro-nazi"
result = conn.execute(text("INSERT INTO users VALUES (:name, :age)"), [{"name": NAME, "age": AGE}])
conn.rollback()
