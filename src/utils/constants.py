from dotenv import load_dotenv
import os
from pathlib import Path


class Constants:
    load_dotenv()
    path = os.path.dirname(os.path.abspath(__file__))
    main_dir = Path(path).parent.parent
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
    ELECTION_API_URL = os.getenv('ELECTION_API_URL')
    TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
