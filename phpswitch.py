"""
usage: phpswitch <version>
"""

#########################################################
# CONFIGURATION
#########################################################

PHP_DIR = r'C:\PHP'

#########################################################
# EXECUTION
#########################################################

import os
import sys

def get_composer_bat(version):
    return f"""
@echo off

rem Define the path to the other script
set "script_path=php C:\PHP\{version}\composer.phar"

rem Call the script with all arguments passed as-is
call %script_path% %*

exit /b 0
"""

def get_php_bat(version):
    return f"""
@echo off

rem Define the path to the other script
set "script_path=C:\PHP\{version}\php.exe"

rem Call the script with all arguments passed as-is
call "%script_path%" %*

exit /b 0
"""

def get_php_versions():
    files = os.listdir(PHP_DIR)
    folders = [f for f in files if os.path.isdir(os.path.join(PHP_DIR, f))]
    return folders

def main():
    # if no args, print help
    if len(sys.argv) < 2:
        print(__doc__)
        print('versions:')
        for v in get_php_versions():
            print(' - ' + v)
        return

    version = sys.argv[1]
    if version not in get_php_versions():
        print(f'Version {version} not found')
        return
    
    print('Dumping php.bat')
    with open(os.path.join(PHP_DIR, 'php.bat'), 'w', encoding='utf-8') as f:
        f.write(get_php_bat(version))
    
    print('Dumping composer.bat')
    with open(os.path.join(PHP_DIR, 'composer.bat'), 'w', encoding='utf-8') as f:
        f.write(get_composer_bat(version))
    
    print(f'PHP version switched to {version}')

    print(f'Testing PHP version')
    print('-' * 40)
    os.system('php -v')

if __name__ == '__main__':
    main()