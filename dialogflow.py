from google.cloud import dialogflow_v2beta1 as dialogflow
from google.protobuf.json_format import MessageToDict

from datetime import date


class DialogFlow:
    def __init__(self):
        self.DIALOGFLOW_PROJECT_ID = 'chatbot-egdk'
        self.DIALOGFLOW_LANGUAGE_CODE = 'ru'
        self.session_client = dialogflow.SessionsClient()

    def get_answer(self, user_id, text_to_be_analyzed):
        # Добавить возможность работы с utils и придумать способ их проходить.
        self.session = self.session_client.session_path(
            self.DIALOGFLOW_PROJECT_ID, user_id)
        text_input = dialogflow.types.TextInput(
            text=text_to_be_analyzed,
            language_code=self.DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = self.session_client.detect_intent(
            session=self.session,
            query_input=query_input)
        answer = response.query_result.fulfillment_text
        params = response.query_result.parameters
        intent_name = response.query_result.intent.display_name
        is_all_params = response.query_result.all_required_params_present
        if intent_name == 'KreditForm' and is_all_params:
            url = self.make_url(params.pb)
            answer += "\n\n" + url
        return answer

    def make_url(self, params):
        base = 'https://my.incognitocr.ru/#/loan-vk?'

        # phone-number
        number = ''.join(
            [n for n in str(params['phone-number']) if n.isdigit()])

        url = base + "phone=" + number + "&"

        # dates given like 2022-04-05T00:00:00+05:00
        delta_dates = MessageToDict(params['date-period'])
        start_date = self._get_date(delta_dates['startDate'])
        end_date = self._get_date(delta_dates['endDate'])
        delta = end_date - start_date
        count_days = str(delta.days)
        url += f"days={count_days}&"

        # birthday
        # TODO truble with birtday(почему-то год записан)
        birthday_string = MessageToDict(params['birthday'])
        birthday_date = self._get_date(birthday_string)
        birthday = birthday_date.strftime("%d.%m.%Y")
        url += f"birth_date={birthday}&"

        # sum
        data = MessageToDict(params['unit-currency'])
        amount = data['amount']
        url += f"sum={amount}"
        return url

    def _get_date(self, string):
        # parse strings like 2022-04-05T00:00:00+05:00
        row_date = string.split('T')[0].split('-')
        int_list_date = [int(el) for el in row_date]
        return date(*int_list_date)
