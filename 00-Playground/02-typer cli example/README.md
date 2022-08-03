# Cli apps con typer

https://typer.tiangolo.com/

```bash
(venv) janrax@janrax-matebook: ../02-typer cli example$ python main.py --help
                                                                                           
 Usage: main.py [OPTIONS] COMMAND [ARGS]...                                                
                                                                                           
╭─ Options ───────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                 │
│ --show-completion             Show completion for the current shell, to copy it or      │
│                               customize the installation.                               │
│ --help                        Show this message and exit.                               │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────╮
│ check                                                                                   │
│ check-file                                                                              │
│ check-urls                                                                              │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
```

```bash
(venv) janrax@janrax-matebook: ../02-typer cli example$ python main.py check --help
                                                                                           
 Usage: main.py check [OPTIONS] URL                                                        
                                                                                           
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────╮
│ *    url      TEXT  [default: None] [required]                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────╮
│ --substring        TEXT  [default: None]                                                │
│ --help                   Show this message and exit.                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
```

```bash
(venv) janrax@janrax-matebook: ../02-typer cli example$ python main.py check-urls --help
                                                                                           
 Usage: main.py check-urls [OPTIONS] URLS...                                               
                                                                                           
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────╮
│ *    urls      URLS...  [default: None] [required]                                      │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────╮
│ --async-mode    --no-async-mode          [default: no-async-mode]                       │
│ --substring                        TEXT  [default: None]                                │
│ --help                                   Show this message and exit.                    │
╰─────────────────────────────────────────────────────────────────────────────────────────╯


```

```bash
(venv) janrax@janrax-matebook: ../02-typer cli example$ python main.py check-file --help
                                                                                           
 Usage: main.py check-file [OPTIONS] FILE                                                  
                                                                                           
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────╮
│ *    file      PATH  [default: None] [required]                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────╮
│ --async-mode    --no-async-mode          [default: no-async-mode]                       │
│ --substring                        TEXT  [default: None]                                │
│ --help                                   Show this message and exit.                    │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
```
