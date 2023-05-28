import config_wl as cfg
from configReader import configReader
class configReader_WL(configReader):

    @staticmethod
    def get_setting(name):
        cfg_new = cfg.config_settings
        return cfg_new[name]

    @staticmethod
    def get_setting_all():
        cfg_new = cfg.config_settings
        return(cfg_new)