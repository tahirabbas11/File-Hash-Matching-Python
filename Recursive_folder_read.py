import os               #used for file paths
import sys              #accept command line arguments
import hashlib          #generate hash 

compromised="compromised"
original="original"
walk_dir = compromised
#walk_dir = sys.argv[1]   #it is taking parametre from command line

print('walk_dir = ' + walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    list_file_path = os.path.join(root, 'my-directory-list.txt')

    with open(list_file_path, 'wb') as list_file:  #write file in binary

        for filename in files:
            compromised_file_path = os.path.join(root, filename)
            original_file_path= compromised_file_path.replace(compromised,original)
            try:
                compromised_md5= hashlib.md5(open(compromised_file_path,'r').read().encode('utf-8'))
                original_md5= hashlib.md5(open(original_file_path,'r').read().encode('utf-8'))

                if(compromised_md5 != original_md5):
                    print("[#] file is modified \t%s",compromised_file_path) # %s for string
            except(Exception):
                print('[#] newly created file detected: \t%s' , compromised_file_path)
