import os
from typing import Dict, Union, Optional
from config import config


def register_resource_plugins(mcp):
    db_host = config.DB_HOST
    db_name = config.DB_NAME

    @mcp.resource(uri=f"mysql://{db_host}/{db_name}")
    def db_connector() -> Dict[str, Union[object, callable]]:
        """
        注册数据库连接资源。
        
        :return: 包含创建的数据库连接和关闭连接方法的字典。
        """
        from resources.mysql import create_connection, close_connection
        
        conn = create_connection()
        
        return {
            'connection': conn,
            'close': lambda: close_connection(conn)
        }