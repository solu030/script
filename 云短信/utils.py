import random
import re
from tencentConfig import REGEX_MOBILE

def get_codes():
    seeds = '0123456789'
    code_list = []
    for i in range(4):
        code_list.append(random.choice(seeds))
    return ''.join(code_list)

def check_mobile(mobile):
    # REGEX_MOBILE = r'^1[358]\d{9}$|^147\d{8}$|^199\d{8}$'
    if re.match(REGEX_MOBILE, mobile):
        return True
    return False

if __name__ == '__main__':
    print(check_mobile('19936548569'))