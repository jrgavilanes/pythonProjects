# Create python environment

```bash
python -m venv venv

# Windows 
venv/Script/activate.bat
# Linux 
. venv/bin/activate

pip install -r requirements.txt

# Prior.
pip freeze > requirements.txt
```

# Launch Tests

```bash
janrax@JANRAX-HOME MINGW64 ~/PycharmProjects/pythonProjects/01-base (master)
$ pytest -v -s
========================== test session starts =========================
platform win32 -- Python 3.9.1, pytest-7.1.2, pluggy-1.0.0 -- 
c:\users\janrax\pycharmprojects\pythonprojects\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\janrax\PycharmProjects\pythonProjects\01-base
collected 1 item

test_main_integration.py::test_main PASSED      
```
