from datetime import datetime

from langchain_core.tools import tool


@tool
def get_current_date() -> str:
    """Retorna la fecha y hora actual en formato ISO 8601."""
    return datetime.now().isoformat()
