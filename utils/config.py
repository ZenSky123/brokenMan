import os
import json


def get_config_path():
    user_dir = os.path.expanduser('~')
    program_name = 'crack'
    config_filename = 'config.json'

    config_path = os.path.join(user_dir, program_name, config_filename)

    return config_path


def mkdir(path):
    parent_dir = os.path.dirname(path)
    if not os.path.exists(parent_dir):
        mkdir(parent_dir)
    if not os.path.exists(path):
        os.mkdir(path)


def save_config(config):
    config_path = get_config_path()
    mkdir(config_path)
    json.dump(config, open(config_path, 'w'))


def load_config():
    config_path = get_config_path()
    if not os.path.exists(config_path):
        return None
    else:
        return json.load(open(config_path))


def init_config():
    config_path = get_config_path()
    if os.path.exists(config_path):
        config = load_config()
        choose = input("Your configuration already exists. Do you want to rebuild it? (Y/n)")

        if choose not in ('Y', 'y'):
            return

        admin_username = input("Admin Username (default {}):".format(config['admin_username'])) or config[
            'admin_username']
        admin_password = input("Admin Password (default {}):".format(config['admin_password'])) or config[
            'admin_password']
        rule_181 = int(input("Rule for 181 (default {})".format(config['rule']['181'])) or config['rule']['181'])
        rule_182 = int(input("Rule for 182 (default {})".format(config['rule']['182'])) or config['rule']['182'])
        rule_183 = int(input("Rule for 183 (default {})".format(config['rule']['183'])) or config['rule']['183'])
        rule_184 = int(input("Rule for 184 (default {})".format(config['rule']['184'])) or config['rule']['184'])
        rule_185 = int(input("Rule for 185 (default {})".format(config['rule']['185'])) or config['rule']['185'])
        rule_186 = int(input("Rule for 186 (default {})".format(config['rule']['186'])) or config['rule']['186'])
        rule_187 = int(input("Rule for 187 (default {})".format(config['rule']['187'])) or config['rule']['187'])
        rule_188 = int(input("Rule for 188 (default {})".format(config['rule']['188'])) or config['rule']['188'])
    else:
        admin_username = input("Admin Username:")
        admin_password = input("Admin Password:")
        rule_181 = int(input("Rule for 181 :"))
        rule_182 = int(input("Rule for 182 :"))
        rule_183 = int(input("Rule for 183 :"))
        rule_184 = int(input("Rule for 184 :"))
        rule_185 = int(input("Rule for 185 :"))
        rule_186 = int(input("Rule for 186 :"))
        rule_187 = int(input("Rule for 187 :"))
        rule_188 = int(input("Rule for 188 :"))

    config = {
        "admin_username": admin_username,
        "admin_password": admin_password,
        "rule": {
            "181": rule_181,
            "182": rule_182,
            "183": rule_183,
            "184": rule_184,
            "185": rule_185,
            "186": rule_186,
            "187": rule_187,
            "188": rule_188,
        }
    }
    save_config(config)
    return config


config = load_config()
