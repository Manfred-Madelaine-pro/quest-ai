from front.front import *
from conf.global_config import *



class QuestAI:
	def __init__(self, conf={}):
		front_conf  = global_conf['front']
		back_conf   = global_conf['back']
	
		main_args = global_conf['main'].values()
		back_model = back.Model(*main_args, conf=back_conf)

		Front(back_model, *main_args, conf=front_conf) 	


if __name__ == '__main__':
	config_file = "conf/config.yml"
	global_conf = global_config(config_file)
	
	QuestAI(global_conf)
