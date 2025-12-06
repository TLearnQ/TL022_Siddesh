import json, yaml

def normalize(x):
    if isinstance(x, dict): 
        return {k.lower(): normalize(v) for k, v in x.items()}
    if isinstance(x, list): 
        return [normalize(i) for i in x]
    return x

path = "test.json"
data = json.load(open(path,'r')) 
if path.endswith((".yml",".yaml")):
    yaml.safe_load(path)
else :
    json.load(open(path))
json.dump(normalize(data), open("output.json","w"), indent=2)