# encoding = UTF-8

"""

"""
import os
import sys
import configparser


class ConfigTest:
    def __init__(self, section, config_file):
        self.section = section
        self.load_config(self.section, config_file)
        self.flag = True
        self.secret_key = ""
        self.admin_name = ""

    def load_config(self, section, config_file):
        if not os.path.exists(config_file):
            raise Exception("%s File not Exists." % config_file)
        config = configparser.ConfigParser()
        # 한글이 들어갈 경우 인코딩 값 역시 설정을 해줘야 오류가 안난다~
        config.read(config_file, encoding='utf-8')

        self.secret_key = config.get(section, "SECRET_KEY")
        self.admin_name = config.get(section, "ADMIN_NAME")


def main(section, config_file):
    print("Main Run")
    ct = ConfigTest(section, config_file)
    print(ct.admin_name)
    print(ct.secret_key)


def usage():
    print("Usage : python %s {Section} {config_file}" % sys.argv[0])


if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     usage()
    #     sys.exit(1)
    # vArg1 = sys.argv[1]     # Section
    # vArg2 = sys.argv[2]     # config_file

    vArg1 = "DEFAULT"
    vArg2 = "config.ini"
    main(vArg1, vArg2)
