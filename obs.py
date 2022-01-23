import obfuscator
import os
import traceback
from sys import argv

import random

obs = obfuscator.obfuscator()

def main():
    print("**************")
    print("* OBFUSCATOR *")
    print("**************")
    
    try:
        if len(argv) == 2:
            path = argv[1]
            if not os.path.exists(path):
                print("[-] File not found!")
                exit(0)
            
            if not os.path.isfile(path) or not path.endswith('.py'):
                print("[-] Invalid file!")
                exit()
            
            with open(file=path, mode='r', encoding='utf-8', errors='ignore') as file:
                file_content = "\n"
                file_content += "{} = '{}'\n".format(random.randint(1, 51) * "_", random.randint(0, 100))
                
                for line in file.readlines():
                    file_content += line + "\n"
                    
                obfuscated_content = obs.obfuscate(file_content)
                
                if os.path.exists(f'{path.split(".")[0]}-obfuscated.py'):
                    backup = 0
                    while os.path.exists(f'{path.split(".")[0]}-obfuscated-{backup}.bkp'):
                        backup += 1
                    os.rename(f'{path.split(".")[0]}-obfuscated.py', f'{path.split(".")[0]}-obfuscated-{backup}.bkp')
                
            with open(file=f'{path.split(".")[0]}-obfuscated.py', encoding="utf-8", mode='w') as file:
                file.write(obfuscated_content)
                print("[+] Script has been obfuscated!")
        
        else:
            print(f'[!] Usage: py {argv[0]} <file>')
                
    except Exception as e:
        print(f'[!] Usage: py {argv[0]} <file>')
        #print(e)
        print(traceback.format_exc())
        
if __name__ == "__main__":
    main()