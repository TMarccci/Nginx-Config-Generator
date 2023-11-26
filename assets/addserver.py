import msvcrt
import assets.basics as basics

b = basics

def add_server():
    b.cleanup()
    print("What do you want to do?\n1. Create Local Resource Reverse Proxy\n2. Create Local Resource Reverse Proxy with SSL\n3. Create Local Resource Reverse Proxy Normal+SSL\n4. Create Remote Resource Reverse Proxy\n5. Create Remote Resource Reverse Proxy with SSL\n6. Create Remote Resource Reverse Proxy Normal+SSL\n7.(Q) Go Back\n\n> ", sep="", end="")
    user_input = msvcrt.getch().decode("utf-8").lower()  
    
    try:
        match user_input:
            case "1":
                create_local_resource_reverse_proxy()
            case "2":
                create_local_resource_reverse_proxy_with_ssl()
            case "3":
                create_local_resource_reverse_proxy_with_ssl(True)
            case "4":
                create_remote_resource_reverse_proxy()
            case "5":
                create_remote_resource_reverse_proxy_with_ssl()
            case "6":
                create_remote_resource_reverse_proxy_with_ssl(True)
            case "7" | "q":
                print("Going back...")
            case _:
                add_server()
    except Exception as e:
        print("Something went wrong", e)
        add_server()

def create_local_resource_reverse_proxy():
    # Get the necessary information from the user
    print("What is the listen port (default is 80): ", end="")
    listen = input() or "80"
    print("> What is the server name (domain name), separate with comma(,): ", end="")
    domain = input().split(",")
    print("> What is the access log file path (/etc/nginx/logs/xyz.log): ", end="")
    access_log = input()
    print("> What is the location (default is /): ", end="")
    location = input() or "/"
    print("> What is the root (default is /var/www/html): ", end="")
    root = input() or "/var/www/html"
    print("> What is the index (default is index.html): ", end="")
    index = input() or "index.html"
    
    print(listen, domain, access_log, location, root, index)
    
def create_local_resource_reverse_proxy_with_ssl(doNormalAlso):
    # Get the necessary information from the user
    print("What is the listen port (default is 443): ", end="")
    listen = input() or "443"
    print("> What is the server name (domain name), separate with comma(,): ", end="")
    domain = input().split(",")
    print("> What is the access log file path (/etc/nginx/logs/xyz.log): ", end="")
    access_log = input()
    print("> What is the location (default is /): ", end="")
    location = input() or "/"
    print("> What is the root (default is /var/www/html): ", end="")
    root = input() or "/var/www/html"
    print("> What is the index (default is index.html): ", end="")
    index = input() or "index.html"
    print("> What is the ssl certificate file path (/etc/nginx/ssl/xyz.pem): ", end="")
    ssl_certificate = input()
    print("> What is the ssl certificate key file path (/etc/nginx/ssl/xyz.key): ", end="")
    ssl_certificate_key = input()
    
    print(listen, domain, access_log, location, root, index, ssl_certificate, ssl_certificate_key)

def create_remote_resource_reverse_proxy():
    # Get the necessary information from the user
    print("What is the listen port (default is 80): ", end="")
    listen = input() or "80"
    print("> What is the server name (domain name), separate with comma(,): ", end="")
    domain = input().split(",")
    print("> What is the access log file path (/etc/nginx/logs/xyz.log): ", end="")
    access_log = input()
    print("> What is the location (default is /): ", end="")
    location = input() or "/"
    print("> What is the proxy pass (default is http://localhost:8080): ", end="")
    proxy_pass = input() or "http://localhost:8080"
    
    print(listen, domain, access_log, location, proxy_pass)

def create_remote_resource_reverse_proxy_with_ssl(doNormalAlso):
    # Get the necessary information from the user
    print("What is the listen port (default is 443): ", end="")
    listen = input() or "443"
    print("> What is the server name (domain name), separate with comma(,): ", end="")
    domain = input().split(",")
    print("> What is the access log file path (/etc/nginx/logs/xyz.log): ", end="")
    access_log = input()
    print("> What is the location (default is /): ", end="")
    location = input() or "/"
    print("> What is the proxy pass (default is http://localhost:8080): ", end="")
    proxy_pass = input() or "http://localhost:8080"
    print("> What is the ssl certificate file path (/etc/nginx/ssl/xyz.pem): ", end="")
    ssl_certificate = input()
    print("> What is the ssl certificate key file path (/etc/nginx/ssl/xyz.key): ", end="")
    ssl_certificate_key = input()
    
    print(listen, domain, access_log, location, proxy_pass, ssl_certificate, ssl_certificate_key)
    
