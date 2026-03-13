# FRC Scouting Application

Scouting app for frc

Domain Address: [scoutingfrc.com](https://www.scoutingfrc.com)

## Requirements

Defined by Gavin

1. Balls scored
2. Rough percentage made
3. Climb
4. Auto path
5. Trench y n
6. Pick up spot?
7. Shoot on move
8. Storage capacity

## Installation

Used to use `pip` as package manager, moved to `uv` <br>
[docs.astral.sh/uv/guides/migration/pip-to-project/#migrating-to-a-uv-project](https://docs.astral.sh/uv/guides/migration/pip-to-project/#migrating-to-a-uv-project) <br>
[notes.abgup.com/software/package-managers/python/](https://notes.abgup.com/software/package-managers/python/)

1. Clone the repo locally:
```bash
$ git clone https://github.com/ab12gu/scoutingfrc
$ cd scoutingfrc
```

2. Activate virtual env
```bash
# Unix
$ source .venv/bin/activate

# Windows via Powershell
$ .venv/Scripts/activate.ps1
```

3. Install project dependencies
```bash
$ uv sync
```

## Deploy

Local deploy, run:
```
$ python manage.py runserver <port number>
```

## Architecture

Languages:
- Frontend: `HTML/CSS`
- Backend: `Python`
- DB: `SQL`

Libraries/structure: 
- Web Framework: `Django`
- Backend DB: `Postgresql`

Hosting websites
- Hosting Platform: `Render`
- DB Host: `Subabase`
