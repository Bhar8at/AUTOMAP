import json
from types import SimpleNamespace as Bunch
import os


def get_config_from_json(json_file):
    """
    Get the config from a json file
    :param json_file:
    :return: config(namespace) or config(dictionary)
    """
    # parse the configurations from the config json file provided
    print("[DEBUG] The json file is being opened ", json_file)
    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)

    print("[DEBUG] config_dict = ", config_dict)
    # convert the dictionary to a namespace using bunch lib
    config = Bunch(**config_dict)
    print("[DEBUG] config = ", config)
    return config, config_dict


def process_config(json_file):
    config, _ = get_config_from_json(json_file)
    print("[DEBUG] Recieved config from json")
    print("config = ", config)
    print("config_dict = ", _)
    config.summary_dir = os.path.join("experiments", config.exp_name, "summary/")
    config.checkpoint_dir = os.path.join("experiments", config.exp_name, "checkpoint/")
    config.graph_file = os.path.join("experiments", config.exp_name, "checkpoint/","loss_training.p")
    return config
