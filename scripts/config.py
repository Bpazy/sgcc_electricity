from yaml import load, FullLoader

f = open('config/config.yaml')
cfg = load(f, Loader=FullLoader)
f.close()
