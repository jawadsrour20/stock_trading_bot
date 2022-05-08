from enum import Enum

class eDiscordMessage(Enum):

    HELLO = 0
    BYE = 1


discord_messages = {
    eDiscordMessage.HELLO: "hello",
    eDiscordMessage.BYE: "bye",
}

