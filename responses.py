import random

agents = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 'Fade', 'Harbor', 'Jett', 'KAY/O', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'Hello Agent!'

    if p_message == '!roulette':
        select_agent = random.choice(agents)
        print('Your Agent is:', select_agent)

    if p_message == '!help':
        return "`I am here to help!\nMy Commands are !hello and !roulette\n!hello - Simply Greets you with a hello back!\n!roulette - Picks a random Agent for you t play!`"

