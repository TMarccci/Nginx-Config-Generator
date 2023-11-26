import os
import assets.basics as basics
import crossplane
import msvcrt

b = basics

def list_nginx_config():
    if check_if_nginx_config_exists():
        servers = parse_nginx_config()

        index = 0
        inlist = True
        while inlist:
            server = servers[index]
            b.cleanup()
            print("\nCurrent Server:", index + 1, "/", len(servers), "\n")
            
            list_server_data(parse_server_data(server))
            
            print("\n\nPress N to go to next, B to go back, or Q to quit:\n> ", end="")
            
            user_input = msvcrt.getch().decode("utf-8").lower()    
            if user_input == "n":
                if index != len(servers) - 1:
                    index += 1
            elif user_input == "b":
                if index != 0:
                    index -= 1
            elif user_input == "q":
                inlist = False
    else:
        print("No config found. Please get config first.")
        
def check_if_nginx_config_exists():
    if os.path.isfile('./temp/nginx.conf'):
        return True
    else:
        return False
 
def parse_nginx_config():
    payload = crossplane.parse('./temp/nginx.conf')
    parsed = payload['config'][0]['parsed']
    
    # Find HTTP Directive
    http = {}
    for i in range(len(parsed)):
        if parsed[i]['directive'] == 'http':
            http = parsed[i]
            
    # Find Server Directives
    servers = []
    for i in range(len(http['block'])):
        if http['block'][i]['directive'] == 'server':
            servers.append(http['block'][i])
            
    return servers

def parse_server_data(server):
    # Find listen
    listen = ''
    for i in range(len(server['block'])):
        if server['block'][i]['directive'] == 'listen':
            listen = server['block'][i]['args']
            
    # Find server_name
    server_name = ''
    for i in range(len(server['block'])):
        if server['block'][i]['directive'] == 'server_name':
            server_name = server['block'][i]['args']
            
    # Find access log
    access_log = ''
    for i in range(len(server['block'])):
        if server['block'][i]['directive'] == 'access_log':
            access_log = server['block'][i]['args'][0]
    
    ssl_certificate = ''
    ssl_certificate_key = ''
    if "443" or "ssl" or "https" in listen:
        # Find ssl_certificate
        for i in range(len(server['block'])):
            if server['block'][i]['directive'] == 'ssl_certificate':
                ssl_certificate = server['block'][i]['args'][0]
                
        # Find ssl_certificate_key
        for i in range(len(server['block'])):
            if server['block'][i]['directive'] == 'ssl_certificate_key':
                ssl_certificate_key = server['block'][i]['args'][0]
        
    # Find location
    location = ''
    for i in range(len(server['block'])):
        if server['block'][i]['directive'] == 'location':
            location = server['block'][i]['args'][0]
            
    # Find root
    root = ''
    for i in range(len(server['block'])):
        if server['block'][i]['directive'] == 'location':
            for j in range(len(server['block'][i]['block'])):
                if server['block'][i]['block'][j]['directive'] == 'root':
                    root = server['block'][i]['block'][j]['args'][0]
            
    # Find index
    index = ''
    for i in range(len(server['block'])):
        if server['block'][i]['directive'] == 'location':
            for j in range(len(server['block'][i]['block'])):
                if server['block'][i]['block'][j]['directive'] == 'index':
                    index = server['block'][i]['block'][j]['args'][0]
            
    # Find proxy_pass
    proxy_pass = ''       
    for i in range(len(server['block'])):
        if server['block'][i]['directive'] == 'location':
            for j in range(len(server['block'][i]['block'])):
                if server['block'][i]['block'][j]['directive'] == 'proxy_pass':
                    proxy_pass = server['block'][i]['block'][j]['args'][0]
                    
    return listen, server_name, access_log, ssl_certificate, ssl_certificate_key, location, root, index, proxy_pass 
    
def list_server_data(server):
    listen, server_name, access_log, ssl_certificate, ssl_certificate_key, location, root, index, proxy_pass = server
    
    # If one value is empty dont print
    if listen != '':
        print("Listen Port:\t", " ".join(listen))   
    if server_name != '':
        print("Server Name:\t", " ".join(server_name))
    if access_log != '':    
        print("Access Log:\t", access_log)
    if ssl_certificate != '':
        print("SSL Certificate:\t", ssl_certificate)
    if ssl_certificate_key != '':
        print("SSL Certificate Key:\t", ssl_certificate_key)
    if location != '':
        print("Location:\t", location)
    if root != '':
        print("\tRoot:\t", root)
    if index != '':
        print("\tIndex:\t", index)
    if proxy_pass != '':
        print("\tProxy Pass:\t", proxy_pass)