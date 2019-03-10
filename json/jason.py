import json

with  open('haksik.json', 'rb') as f:
  root = json.load(f)

  print(root)
