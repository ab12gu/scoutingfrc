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

1. Clone the repo locally:

```
git clone https://github.com/ab12gu/scoutingfrc
cd scoutingfrc
```

2. Install project dependencies
```
pip install -r requirements.txt
```

3. Start virtual environment
```
source ./.venv/bin/activate
```

## Deploy

Local deploy, run:
```
python manage.py runserver
```

Ensure you are keeping the requirements.txt most up-to-date:
```
pip freeze > requirements.txt
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
