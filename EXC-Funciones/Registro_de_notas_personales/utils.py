from pathlib import Path

db = 'notas.db'
path = Path.joinpath(Path.cwd(),db)
print(path)