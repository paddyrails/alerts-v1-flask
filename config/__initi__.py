from config.settings import config_map

def get_config(env):
    return config_map.get(env, config_map('default'))