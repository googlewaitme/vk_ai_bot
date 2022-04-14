from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
import config
from dialogflow import DialogFlow


bot = SimpleLongPollBot(tokens=config.TOKEN, group_id=config.GROUP_ID)
df = DialogFlow()


@bot.message_handler()
def echo(event: SimpleBotEvent) -> str:
    # TODO нужно получать юзер id и передавать в get_answer
    user_id = event.object.object.message.from_id
    answer = df.get_answer(user_id, event.object.object.message.text)
    return answer


bot.run_forever()
