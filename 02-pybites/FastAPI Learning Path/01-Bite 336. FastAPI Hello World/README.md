# Arranca servidor

    uvicorn main:app --host "0.0.0.0" --port 8000 --reload


# Testea endpoints ( httppie )

```bash
(venv) janrax@janrax-matebook:~/Code/pythonProjects$ http localhost:8000
HTTP/1.1 200 OK
content-length: 65
content-type: application/json
date: Fri, 15 Jul 2022 18:19:11 GMT
server: uvicorn

{
    "message": "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"
}



```



