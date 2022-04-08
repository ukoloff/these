import os
from pathlib import Path

root = Path(__file__).parents[1]
src = root / 'pcglns'
json = root / 'json'
dst = root / 'html'
bat = Path(__file__).parent / 'j2gtsp.bat'
dst.mkdir(exist_ok=True)

for f in src.glob('*.pcglns'):
  name = f.stem
  print(name, end=' ', flush=True)
  os.system(f"""{bat} {
    f.with_name(name + '.result.txt')} {
    json / f'{name}.dbs.json'} {
    json / f'{name}.task.json'} -fo {
    dst / f'{name}.html'} > {
    dst / f'{name}.txt'}""")

