# Python Starter Kit

Minimaler, sauberer Python-Projekt-Starter für **Studium & Lernen**  
(geeignet als Template für neue Projekte).

**Ziele**
- reproduzierbares Setup
- klare Projektstruktur (`src/`-Layout)
- modernes Tooling ohne Overhead

---

## Features

- pyenv für Python-Versionen
- venv pro Projekt
- pip-tools für reproduzierbare Dependencies
- ruff für Linting & Formatting
- pytest für Tests
- JupyterLab für Notebooks

---

## Voraussetzungen

- Ubuntu Linux
- `pyenv` installiert
- Python ≥ 3.12

Empfohlen:
```bash
pyenv install 3.14.2
```

---

## 🚀 Projekt aufsetzen (Quickstart)
```bash
git clone https://github.com/<USER>/<PROJECT_NAME>.git
cd <PROJECT_NAME>

pyenv local 3.14.2

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

pip install pip-tools
pip-compile requirements.in
pip-compile requirements-dev.in
pip-sync requirements.txt requirements-dev.txt

pip install -e .
```

---

## 🧪 Tests & Qualität

```bash
ruff format .
ruff check .
pytest
```

---

## 📁 Projektstruktur

```bash
.
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── greetings.py
├── tests/
├── notebooks/
├── requirements.in
├── requirements-dev.in
├── pyproject.toml
└── README.md
```

### Regel
- produktiver Code → src/
- Experimente / Lernen → notebooks/

---

## 🔁 Neues Projekt aus diesem Template starten

Siehe: [docs/NEW_PROJECT.md](https://github.com/frahil003/python-starter-kit/blob/main/docs/NEW_PROJECT.md)

Kurzfassung:

1. Repo als GitHub Template verwenden
2. Package unter src/ umbenennen
3. Imports & Tests anpassen
4. Commit & loslegen 🚀

---

## 🧠 Design-Prinzipien

- Explizit statt magisch
- Ein Tool pro Aufgabe
- Lernfreundlich vor clever
- Produktionsnah, aber entspannt

---

## 📜 Lizenz

MIT