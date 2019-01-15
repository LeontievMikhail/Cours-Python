"""
На предыдущей неделе вы разработали клиентское сетевое приложение — клиента для сервера метрик, который умеет отправлять и получать всевозможные метрики.
Пришло время финального задания — нужно реализовать серверную часть самостоятельно.
Как обычно вам необходимо разработать программу в одном файле-модуле, который вы загрузите на проверку обычным способом.
Сервер должен соответствовать протоколу, который был описан в задании к предыдущей неделе. Он должен уметь принимать от клиентов команды put и get, разбирать их, и формировать ответ согласно протоколу.
По запросу put требуется сохранять метрики в структурах данных в памяти процесса. По запросу get сервер обязан отдавать данные в правильной последовательности.
На верхнем уровне вашего модуля должна быть объявлена функция run_server(host, port) — она принимает адрес и порт, на которых должен быть запущен сервер.
Для проверки правильности решения мы воспользуемся своей реализацией клиента и будем отправлять на ваш сервер put и get запросы, ожидая в ответ правильные данные от сервера (согласно объявленному протоколу).
Все запросы будут выполняться с таймаутом — сервер должен отвечать за приемлемое время.
Сервер должен быть готов к неправильным командам со стороны клиента и отдавать клиенту ошибку в формате, оговоренном в протоколе. В таком случае работа сервера не должна завершаться аварийно.
На последней неделе мы с вами разбирали пример tcp-сервера на asyncio:
import asyncio
class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())
loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8181
)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
Данный код создает tcp-соединение для адрса 127.0.0.1:8181 и слушает все входящие запросы.
При подключении клиента будет создан новый экземпляр класса ClientServerProtocol, а при поступлении новых данных вызовется метод этого объекта - data_received. Внутри asyncio.Protocol спрятана вся магия обработки запросов через корутины,
остается реализовать протокол взаимодействия между клиентом и сервером.
Этот код может использоваться как основа для реализации сервера. Это не обязательное требование. Для реализации задачи вы можете использовать любые вызовы из стандартной библиотеки Python 3.
 Сервер должен обрабатывать запросы от нескольких клиентов одновременно.
В процессе разработки сервера для тестирования работоспособности вы можете использовать клиент, написанный на предыдущей неделе.
Давайте еще раз посмотрим на текстовый протокол в действии при использовании утилиты telnet:
$: telnet 127.0.0.1 8888
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
> get test_key
< ok
<
> got test_key
< error
< wrong command
<
> put test_key 12.0 1503319740
< ok
<
> put test_key 13.0 1503319739
< ok
<
> get test_key
< ok
< test_key 13.0 1503319739
< test_key 12.0 1503319740
<
> put another_key 10 1503319739
< ok
<
> get *
< ok
< test_key 13.0 1503319739
< test_key 12.0 1503319740
< another_key 10.0 1503319739
<
"""

import asyncio

storage = {}


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def process_data(self, data):
        if data[0:3] == "put":
            comm, key, value, timestamp = data.split()
            if key not in storage:
                storage[key] = []
            storage[key].append((int(timestamp), float(value)))
            resp = "ok\n\n"
        elif data[0:3] == "get":
            comm, key = data.split()
            resp = "ok\n"
            if key != "*":
                if key in storage:
                    for metric in storage[key]:
                        resp += key + ' ' + str(metric[1]) + ' ' + str(metric[0]) + "\n"
            else:
                for key in storage:
                    for metric in storage[key]:
                        resp += key + ' ' + str(metric[1]) + ' ' + str(metric[0]) + "\n"
            resp += "\n"
        else:
            resp = "error\nwrong command\n\n"

        return resp


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


# run_server("127.0.0.1", 8888)

"""
Решение:
Ниже наша реализация сервера для приема метрик. Код приложения разбит на классы Storage, Parser и Executor, также есть класс, который реализует asyncio-сервер. Storage инкапсулирует в себе методы для работы с хранилищем и сами метрики, в нашем случае мы просто сохраняем их в словарь, лежащий в памяти, однако класс легко расширить и добавить персистентность. Parser разбирает наш текстовый протокол при получении информации из сокета и формирует корректный запрос при отправке данных. Executor получает разобранные команды и отправляет соответствующие запросы в Storage.
Разбив логику приложения на несколько классов, мы можем легко модифицировать программу и добавлять новую функциональность. Также намного легче воспринимать и отлаживать код, который выполняет конкретную задачу, а не делает всё сразу. Надеемся, вы тоже постарались разбить свою реализацию на функциональные блоки с помощью классов и функций.
import asyncio
class Storage:
    #Класс для хранения метрик в памяти процесса
    def __init__(self):
        # используем словарь для хранения метрик
        self._data = {}
    def put(self, key, value, timestamp):
        if key not in self._data:
            self._data[key] = {}
        self._data[key][timestamp] = value
    def get(self, key):
        data = self._data
        # вовзращаем нужную метрику если это не *
        if key != "*":
            data = {
                key: data.get(key, {})
            }

        # для простоты мы храним метрики в обычном словаре и сортируем значения
        # при каждом запросе, в реальном приложении следует выбрать другую
        # структуру данных
        result = {}
        for key, timestamp_data in data.items():
            result[key] = sorted(timestamp_data.items())
        return result
class ParseError(ValueError):
    pass
class Parser:
    #Класс для реализации протокола

    def encode(self, responses):
        #Преобразование ответа сервера в строку для передачи в сокет
        rows = []
        for response in responses:
            if not response:
                continue
            for key, values in response.items():
                for timestamp, value in values:
                    rows.append(f"{key} {value} {timestamp}")
        result = "ok\n"
        if rows:
            result += "\n".join(rows) + "\n"
        return result + "\n"
    def decode(self, data):
        #Разбор команды для дальнейшего выполнения. Возвращает список команд для выполнения
        parts = data.split("\n")
        commands = []
        for part in parts:
            if not part:
                continue
            try:
                method, params = part.strip().split(" ", 1)
                if method == "put":
                    key, value, timestamp = params.split()
                    commands.append(
                        (method, key, float(value), int(timestamp))
                    )
                elif method == "get":
                    key = params
                    commands.append(
                        (method, key)
                    )
                else:
                    raise ValueError("unknown method")
            except ValueError:
                raise ParseError("wrong command")
        return commands
class ExecutorError(Exception):
    pass
class Executor:
    #Класс Executor реализует метод run, который знает как выполнять команды сервера

    def __init__(self, storage):
        self.storage = storage
    def run(self, method, *params):
        if method == "put":
            return self.storage.put(*params)
        elif method == "get":
            return self.storage.get(*params)
        else:
            raise ExecutorError("Unsupported method")
class EchoServerClientProtocol(asyncio.Protocol):
    #Класс для реализции сервера при помощи asyncio

    # Обратите внимание на то, что storage является атрибутом класса
    # Объект self.storage для всех экземмпляров класса EchoServerClientProtocol
    # будет являться одним и тем же объектом для хранения метрик.
    storage = Storage()
    def __init__(self):
        super().__init__()
        self.parser = Parser()
        self.executor = Executor(self.storage)
        self._buffer = b''
    def process_data(self, data):
        #Обработка входной команды сервера

        # разбираем сообщения при помощи self.parser
        commands = self.parser.decode(data)
        # выполняем команды и запоминаем результаты выполнения
        responses = []
        for command in commands:
            resp = self.executor.run(*command)
            responses.append(resp)
        # преобразовываем команды в строку
        return self.parser.encode(responses)
    def connection_made(self, transport):
        self.transport = transport
    def data_received(self, data):
        #Метод data_received вызывается при получении данных в сокете
        self._buffer += data
        try:
            decoded_data = self._buffer.decode()
        except UnicodeDecodeError:
            return

        # ждем данных, если команда не завершена символом \n
        if not decoded_data.endswith('\n'):
            return

        self._buffer = b''
        try:
            # обрабатываем поступивший запрос
            resp = self.process_data(decoded_data)
        except (ParseError, ExecutorError) as err:
            # формируем ошибку, в случае ожидаемых исключений
            self.transport.write(f"error\n{err}\n\n".encode())
            return
        # формируем успешный ответ
        self.transport.write(resp.encode())
if __name__ == "__main__":
    # запуск сервера для тестирования
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        EchoServerClientProtocol,
        '127.0.0.1', 8888
    )
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
"""

"""Мое решение для одного клиента:
def run_server(host, port):
	with socket.socket() as sock:
		sock.bind((host, port))
		sock.listen()
		while True:
			conn, attr = sock.accept()
			with conn:
				while True:
					item = conn.recv(1024)
					if not item:
						break
					item = item.decode("utf8")
					if item[0:3] == "put":
						comm, key, value, timestamp = item.split()
						if key not in data:
							data[key] = []
						data[key].append((int(timestamp), float(value)))
						conn.send("ok\n\n".encode("utf8"))
					elif item[0:3] == "get":
						comm, key = item.split()
						answer = "ok\n"
						if key != "*":
							for metric in data[key]:
								answer += key + ' ' + str(metric[1]) + ' ' + str(metric[0]) + "\n"
						else:
							for key in data:
								for metric in data[key]:
									answer += key + ' ' + str(metric[1]) + ' ' + str(metric[0]) + "\n"
						answer += "\n"
						conn.send(answer.encode("utf8"))
					else:
						conn.send("error\nwrong command\n\n".encode("utf8"))
#run_server("127.0.0.1", 8888)
"""






