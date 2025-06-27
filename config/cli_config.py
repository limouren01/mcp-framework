#config/cli_config.py
import argparse

def load_cli_config():
    parser = argparse.ArgumentParser(description="Override config via command line.")
    parser.add_argument("--db_host", help="Database host")
    parser.add_argument("--db_user", help="Database user")
    parser.add_argument("--db_password", help="Database password")
    parser.add_argument("--db_name", help="Database name")
    parser.add_argument("--db_port", type=int, help="Database port")
    parser.add_argument("--mcp_allowwrite", help="MCP allow write flag")
    parser.add_argument("--mcp_rootdir", help="MCP root directory")
    
    args = parser.parse_args()
    return {k.upper(): v for k, v in vars(args).items() if v is not None}