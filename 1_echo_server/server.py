import socket
import logging
import os

# Настройки логирования (5)
logging.basicConfig(
    format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
    handlers=[logging.FileHandler("server.log"), logging.StreamHandler()],
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

sock = socket.socket()
# 4
port_input = input("Введите номер порта для сервера -> ")
ip_input = input("Введите IP для сервера -> ")

port = int(input("Введите номер порта для проверки -> "))

#username = str(input('Введите username: '))
password = str(input('Введите password'))

auth_result, username = self.database.user_auth(client_ip, user_password)

        # Если авторизация прошла успешно
        if auth_result == 1:
            logger.info(f"Клиент {client_ip} -> авторизация прошла успешно")
            data = {"result": True, "body": {"username": username}}
            if client_ip not in self.authenticated_list:
                self.authenticated_list.append(client_ip)
                self.ip2username_dict[client_ip] = username
                logging.info(f"Добавили клиента {client_ip} в список авторизации")
        # Если авторизация не удалась, но пользователь с таким ip существует
        elif auth_result == 0:
            logger.info(f"Клиент {client_ip} -> авторизация не удалась")
            data = {"result": False, "description": "wrong auth"}
        # Если пользователя с таким ip не существует, то необходима регистрация
        else:
            logger.info(
                f"Клиент {client_ip} -> необходима предварительная регистрация в системе"
            )
            data = {"result": False, "description": "registration required"}
            if client_ip not in self.reg_list:
                self.reg_list.append(client_ip)
                logging.info(f"Добавили клиента {client_ip} в список регистрации")

        self.send_message(conn, data, client_ip)
        logger.info(f"Клиент {client_ip}. Отправили данные о результате авторизации")

        # Если была успешная авторизация - принимаем последующие сообщения от пользователя
        if auth_result == 1:
            self.message_logic(conn, client_ip)

# 6
sock.bind((ip_input, int(port_input)))
sock.listen(1)
conn, addr = sock.accept()
print(addr)
try:
	sock2 = socket.socket()
	sock2.bind(('', port))
	sock2.close()
	print(f'Порт {port} свободен')
except OSError:
	print(f'Порт {port} занят')

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	logging.info(f"Передача данных ")
	conn.send(data)

print(msg)

conn.close()
