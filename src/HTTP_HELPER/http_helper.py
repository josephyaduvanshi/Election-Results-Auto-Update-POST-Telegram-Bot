import requests
from src.utils.constants import Constants


class HTTPHelper:
    @staticmethod
    def post_to_telegram_bot(url: str, data: list):
        try:
            txt = \
                f'''
𝐄𝐥𝐞𝐜𝐭𝐢𝐨𝐧 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐨𝐧𝐬𝐭𝐢𝐭𝐮𝐞𝐧𝐜𝐲 : 𝟐 (𝟏)\n
𝗖𝗮𝗻𝗱𝗶𝗱𝗮𝘁𝗲 𝗡𝗮𝗺𝗲: <b>{data[0]['name']}</b>
𝗩𝗼𝘁𝗲 𝗖𝗼𝘂𝗻𝘁: <b>{data[0]['votes']}</b>
𝗣𝗮𝗿𝘁𝘆: <b>{data[0]['candidate_type']}</b>\n
𝗖𝗮𝗻𝗱𝗶𝗱𝗮𝘁𝗲 𝗡𝗮𝗺𝗲: <b>{data[1]['name']}</b>
𝗩𝗼𝘁𝗲 𝗖𝗼𝘂𝗻𝘁: <b>{data[1]['votes']}</b>
𝗣𝗮𝗿𝘁𝘆: <b>{data[1]['candidate_type']}</b>\n
𝗖𝗮𝗻𝗱𝗶𝗱𝗮𝘁𝗲 𝗡𝗮𝗺𝗲: <b>{data[2]['name']}</b>
𝗩𝗼𝘁𝗲 𝗖𝗼𝘂𝗻𝘁: <b>{data[2]['votes']}</b>
𝗣𝗮𝗿𝘁𝘆: <b>{data[2]['candidate_type']}</b>\n
𝗖𝗮𝗻𝗱𝗶𝗱𝗮𝘁𝗲 𝗡𝗮𝗺𝗲: <b>{data[3]['name']}</b>
𝗩𝗼𝘁𝗲 𝗖𝗼𝘂𝗻𝘁: <b>{data[3]['votes']}</b>
𝗣𝗮𝗿𝘁𝘆: <b>{data[3]['candidate_type']}</b>\n
𝗖𝗮𝗻𝗱𝗶𝗱𝗮𝘁𝗲 𝗡𝗮𝗺𝗲: <b>{data[4]['name']}</b>
𝗩𝗼𝘁𝗲 𝗖𝗼𝘂𝗻𝘁: <b>{data[4]['votes']}</b>
𝗣𝗮𝗿𝘁𝘆: <b>{data[4]['candidate_type']}</b>\n
𝗖𝗮𝗻𝗱𝗶𝗱𝗮𝘁𝗲 𝗡𝗮𝗺𝗲: <b>{data[5]['name']}</b>
𝗩𝗼𝘁𝗲 𝗖𝗼𝘂𝗻𝘁: <b>{data[5]['votes']}</b>
𝗣𝗮𝗿𝘁𝘆: <b>{data[5]['candidate_type']}</b>\n
𝗖𝗮𝗻𝗱𝗶𝗱𝗮𝘁𝗲 𝗡𝗮𝗺𝗲: <b>{data[6]['name']}</b>
𝗩𝗼𝘁𝗲 𝗖𝗼𝘂𝗻𝘁: <b>{data[6]['votes']}</b>
𝗣𝗮𝗿𝘁𝘆: <b>{data[6]['candidate_type']}</b>\n
𝗖𝗮𝗻𝗱𝗶𝗱𝗮𝘁𝗲 𝗡𝗮𝗺𝗲: <b>{data[7]['name']}</b>
𝗩𝗼𝘁𝗲 𝗖𝗼𝘂𝗻𝘁: <b>{data[7]['votes']}</b>
𝗣𝗮𝗿𝘁𝘆: <b>{data[7]['candidate_type']}</b>\n
𝗖𝗮𝗻𝗱𝗶𝗱𝗮𝘁𝗲 𝗡𝗮𝗺𝗲: <b>{data[8]['name']}</b>
𝗩𝗼𝘁𝗲 𝗖𝗼𝘂𝗻𝘁: <b>{data[8]['votes']}</b>
𝗣𝗮𝗿𝘁𝘆: <b>{data[8]['candidate_type']}</b>\n'''
            response = requests.post(url, json={"chat_id": f"{Constants.TELEGRAM_CHAT_ID}", "text": f"{txt}",
                                                "parse_mode": "HTML"})
            return response.json()
        except Exception as e:
            print(e)
