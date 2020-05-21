import yaml



def global_config(config_file):
	with open(config_file, 'r') as stream:
		try:
			return yaml.safe_load(stream)
		except yaml.YAMLError as exc:
			print(exc)



if __name__ == '__main__':
	config_file = "config.yml"
	global_config(config_file)