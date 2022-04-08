import os
import re
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
  res = f.with_name(name + '.result.txt')
  out = dst / f'{name}.html'
  os.system(f"""{bat} {
    res} {
    json / f'{name}.dbs.json'} {
    json / f'{name}.task.json'} -fo {
    out} > {
    dst / f'{name}.txt'}""")
  result = open(res).readlines()
  result[-1:-1] = [line for line in open(out) if re.match(r'Route\s+Length\s*:', line)]
  open(res, 'w').writelines(result)
