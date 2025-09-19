from modules.lfi import *


# * --------------
# * LFI CHECKER
# * --------------

url = init()
operating_system, testing_file = os_checker(target_url=url)
lfi_checker(target_url=url, target_os=operating_system, default_file=testing_file)


# * --------------
# * DIRECTORY CHECKER
# * --------------

