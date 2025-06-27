import mysql.connector
from mysql.connector import Error
from config import config

def create_connection():
    """
    创建到MySQL数据库的连接。
    
    :return: 成功时返回数据库连接对象，失败时返回None。
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=config.MYSQL_HOST,
            user=config.MYSQL_USER,
            passwd=config.MYSQL_PASSWORD,
            database=config.MYSQL_DATABASE,
            port=int(config.MYSQL_PORT)
        )
        if connection.is_connected():
            print("成功连接到 MySQL 数据库")
    except Error as e:
        print(f"连接数据库失败: {e}")
    return connection

def close_connection(connection):
    """
    关闭数据库连接。
    
    :param connection: 要关闭的数据库连接对象
    """
    if connection and connection.is_connected():
        connection.close()
        print("数据库连接已关闭")