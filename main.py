from pathlib import Path

root=Path('files')

for i in range(10, 21):
  filename=str(i)+'.txt'
  filepath=root / Path(filename)
  filepath.touch()