# FRC Scouting Application

Scouting app for frc

Domain Address: [scoutingfrc.com](https://www.scoutingfrc.com)

## Architecture

Languages:
- Frontend: `HTML/CSS`
- Backend: `Python`
- DB: `SQL`

Libraries/structure: 
- Web Framework: `Django`
- Backend DB: `Postgresql`

Hosting websites
- Hosting Platform: [Render](https://render.com)
  - [https://render.com/docs/deploy-django](https://render.com/docs/deploy-django)
- DB Host: `Subabase`

NOTE: I don't have a [build script](https://render.com/docs/deploy-django#create-a-build-script) in github for render and just define them within render UI. 

## Google Sheets

The data is outputted into a Google Sheets, which makes it easier to human-analyze and syncs w/ google survey's output. If needed, we rely on google survey's to gather data. 

To connect the google sheets, you need to add a script to: [https://script.google.com/](https://script.google.com/).

## Installation

Used to use `pip` as package manager, moved to `uv` <br>
[docs.astral.sh/uv/guides/migration/pip-to-project/#migrating-to-a-uv-project](https://docs.astral.sh/uv/guides/migration/pip-to-project/#migrating-to-a-uv-project) <br>
[notes.abgup.com/software/package-managers/python/](https://notes.abgup.com/software/package-managers/python/)

1. Clone the repo locally:
```bash
$ git clone https://github.com/ab12gu/scoutingfrc
$ cd scoutingfrc
```

2. Request `.env` variable from me (Abhay) to add to root for `DJANGO_SECRET_KEY`

3. Activate virtual env
```bash
# Unix
$ source .venv/bin/activate

# Windows via Powershell
$ .venv/Scripts/activate.ps1
```

4. Install project dependencies
```bash
$ uv sync
```

## Deploy

Local deploy, run:
```
$ python manage.py runserver <port number>
```

## Requirements

Defined by Gavin

1. Team #
2. Match #
3. Balls scored
4. Rough percentage made
5. Climb
6. Auto path
7. Trench y n
8. Pick up spot?
9. Shoot on move
10. Storage capacity
