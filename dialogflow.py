from google.cloud import dialogflow_v2beta1 as dialogflow


class DialogFlow:
    def __init__(self):
        self.DIALOGFLOW_PROJECT_ID = 'chatbot-egdk'
        self.DIALOGFLOW_LANGUAGE_CODE = 'ru'
        self.SESSION_ID = 'me'
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(
            self.DIALOGFLOW_PROJECT_ID, self.SESSION_ID)

    def get_answer(self, text_to_be_analyzed):
        text_input = dialogflow.types.TextInput(
            text=text_to_be_analyzed,
            language_code=self.DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = self.session_client.detect_intent(
            session=self.session,
            query_input=query_input)
        return response.query_result.fulfillment_text
