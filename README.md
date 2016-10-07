# LBsessions
Sessions from LanBilling and history connects.
Работа с сессиями из LanBilling. Поиск активного абонента, просмотр попыток подключения.
Необходимо прописать параметры доступа к базе радиуса в base/__init__.py

import MySQLdb

billing_db_conf = {
    'host': 'localhost',
    'user': 'radius',
    'passwd': 'pass',
    'db': 'radius',
    'charset': 'utf8'
}

