import configparser
import paramiko
import msvcrt
import assets.basics as basics
import assets.listserver as listserver
import assets.addserver as addserver

config = configparser.ConfigParser()
config.read('./config/config.ini')

b = basics
l = listserver
a = addserver

def get_config_host():
    map = {}
    map['host'] = config['remote-server']['host']
    map['port'] = int(config['remote-server']['port'])
    map['username'] = config['remote-server']['username']
    map['password'] = config['remote-server']['password']
    map['nginxpath'] = config['remote-server']['nginxpath']
    
    return map

def get_nginx_config(server):
    b.cleanup()
    print("Getting nginx config from server\nPlease wait...", end="")
    
    ssh = paramiko.SSHClient() 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server['host'], username=server['username'], password=server['password'], port=server['port'])
    sftp = ssh.open_sftp()
    sftp.get(f"{server['nginxpath']}/nginx.conf", './temp/nginx.conf')
    sftp.close()
    ssh.close()
    
    select_what_to_do()

def select_what_to_do():
    b.cleanup()
    print("What do you want to do?\n1. Get Config\n2. List Server\n3. Add Server\n4. Remove Server\n5. Push Changes\n6.(Q) Exit\n\n> ", sep="", end="")
    user_input = msvcrt.getch().decode("utf-8").lower()
    try: 
        match user_input:
            case "1":
                # Get Config
                get_nginx_config(auth)
            case "2":
                # List Server
                l.list_nginx_config()
                select_what_to_do()
            case "3":
                # Add Server
                a.add_server()
                select_what_to_do()
            case "4":
                print("Remove Server")
            case "5":
                print("Push Changes")
            case "6" | "q":
                exit()
            case _:
                select_what_to_do()
    except Exception as e:
        select_what_to_do()
        print("Something went wrong", e)

auth = get_config_host()
select_what_to_do()

