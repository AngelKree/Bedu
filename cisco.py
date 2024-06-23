from netmiko import ConnectHandler 

from getpass import getpass 

 

def backup_switch(host, username, password, enable_password): 

    try: 

        # Configuración del dispositivo 

        device = { 

            'device_type': 'cisco_ios', 

            'host': host, 

            'username': username, 

            'password': password, 

            'secret': enable_password, 

        } 

 

        # Conexión al dispositivo 

        connection = ConnectHandler(**device) 

         

        # Entrar en modo enable 

        connection.enable() 

         

        # Ejecutar comando para obtener la configuración 
 running_config = connection.send_command("show running-config") 

         

        # Guardar la configuración en un archivo 

        with open(f"backup_{host}.txt", "w") as backup_file: 

            backup_file.write(running_config) 

         

        print(f"Backup completed for switch {host}") 

         

        # Cerrar la conexión 

        connection.disconnect() 
 except Exception as e: 

        print(f"Failed to backup switch {host}: {e}") 

 

# Solicitar credenciales al usuario 

username = input("Enter your SSH username: ") 

password = getpass("Enter your SSH password: ") 

enable_password = getpass("Enter your enable password: ") 

 # Datos de los switches 

switches = [ 

    '192.168.1.1', 

    '192.168.1.2', 

] 

 

# Realizar el respaldo de cada switch 

for host in switches: 

    backup_switch(host, username, password, enable_password) 