from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
import config
from dialogflow import DialogFlow


bot = SimpleLongPollBot(tokens=config.TOKEN, group_id=config.GROUP_ID)
df = DialogFlow()


@bot.message_handler()
def echo(event: SimpleBotEvent) -> str:
    answer = df.get_answer(event.object.object.message.text)
    return answer


bot.run_forever()
