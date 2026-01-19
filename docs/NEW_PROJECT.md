# New Python Project – Quick Start 🚀

Diese Anleitung beschreibt den **Standard-Workflow**, um aus dem Repository
`python-starter-kit` ein neues Python-Projekt zu erstellen.

Ziel: **schnell starten, sauber bleiben, ohne Overhead**.

---

## 1. Neues Repository erstellen (GitHub)

**Empfohlener Weg:** `python-starter-kit` als **Template** verwenden.

1. Öffne `python-starter-kit` auf GitHub
2. Klicke auf **Use this template**
3. Vergib einen neuen Repository-Namen
4. Public oder Private wählen
5. Repository erstellen

➡️ Das neue Projekt hat eine **eigene Git-History**.

---

## 2. Repository klonen

```bash
git clone https://github.com/<USER>/<PROJECT_NAME>.git
cd <PROJECT_NAME>
```

---

## Python-Version festlegen (pyenv)

```bash
pyenv local 3.14.2
python --version
```

Hinweis: Falls bereits eine .python-version existiert, wird sie automatisch verwendet.

---

## 4. Virtuelle Umgebung erstellen

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

---

## 5. Dependencies installieren (pip-tools)

```bash
pip install pip-tools
pip-compile requirements.in
pip-compile requirements-dev.in
pip-sync requirements.txt requirements-dev.txt
```

---

## 6. Package-Namen anpassen

Das Template enthält ein Beispiel-Package unter src/my_project.

### Beispiel

Projektname: cool_app

```bash
mv src/my_project src/cool_app
```

Danach **alle Imports und Tests anpassen**.

Suchen:
```bash
grep -R "my_project" -n .
```

Ersetzen durch:
```bash
cool_app
```

---

## 7. Package lokal installieren (editable)

Damit Tests, Notebooks und Tools dein Package finden:

```bash
pip install -e .
```

---

## 8. Qualität prüfen

```bash
ruff format .
ruff check .
pytest
```

✔️ Alles grün → Projekt ist startklar.

---

## 9. README aktualisieren

Passe in README.md mindestens an:

- Projektname
- Kurzbeschreibung
- ggf. besondere Abhängigkeiten

---

## 10. Initial Commit

```bash
git add -A
git commit -m "Initialize project from python-starter-kit"
git push
```

## 🎉 Fertig

Du hast jetzt:

- ein sauberes Python-Projekt (src/-Layout)
- reproduzierbare Dependencies
- konsistentes Formatting & Linting
- eine klare Lern- und Projektstruktur

**Regel für den Alltag**
- Code → src/
- Tests → tests/
- Experimente → notebooks/

Viel Erfolg und Spaß beim Entwickeln 🚀