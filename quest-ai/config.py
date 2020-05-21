import yaml

with open("config.yml", 'r') as stream:
	try:
		print(yaml.safe_load(stream))
	except yaml.YAMLError as exc:
		print(exc)

# regroup all configs
# use object