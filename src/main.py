import time
from src.utils.constants import Constants
from src.scraping.scraping import ScrapingMethods
from src.HTTP_HELPER.http_helper import HTTPHelper
from src.store.text_store_helper import TextAppend


def convert_data_to_dict():
    data = ScrapingMethods.get_data_by_class_name(
        f'{Constants.ELECTION_API_URL}/pradesh-2/district-parsa?lng=eng',
        "widget clearfix")[2]
    names = ScrapingMethods.extract_data_by_regex(str(data), 'class=\"nominee-name\" style=\"color:#000;\">', '<')
    votes = ScrapingMethods.extract_data_by_regex(str(data), '=\"vote-count font-md p-0\">', '<')
    candidate_type = ScrapingMethods.clean_candidate_type(data)
    candidate_list = []
    for i in range(len(names)):
        candidate_list.append({"name": names[i], "votes": votes[i], "candidate_type": candidate_type[i]})
    return votes, candidate_list


def main():
    while True:
        h = convert_data_to_dict()
        votes = h[0]
        print(votes)
        stored_votes = TextAppend.read_text_append()
        print(stored_votes)
        if stored_votes != str(votes):
            TextAppend.write_text_append(str(votes))
            HTTPHelper.post_to_telegram_bot(Constants.TELEGRAM_URL, h[1])
            print("Sent")
        print("Not Sent")
        time.sleep(30)


if __name__ == "__main__":
    main()
