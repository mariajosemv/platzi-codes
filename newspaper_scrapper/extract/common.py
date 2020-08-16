import yaml


__config = None


def config():
	global __config

	if not __config:
		with open('config.yaml', mode='r') as f:
			__config = yaml.safe_load(f)
	return __config

#if __name__ == '__main__':
	#print('  ' *20)
	#print(f"config(): {config()}")
	#print('  ' *20)
	#print(f"config()['news_sites]['eluniversal']: {config()['news_sites']['eluniversal']}")
	#print('  ' *20)
	#print(f"config()['news_sites'].keys(): {config()['news_sites'].keys()}")
	#print('  ' *20)
	#print(f"config()['news_sites'].values(): {config()['news_sites'].values()}")