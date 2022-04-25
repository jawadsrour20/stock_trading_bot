from enum import Enum

class DiscordMessage(Enum):

    HELLO = 0
    BYE = 1


discord_messages = {
    DiscordMessage.HELLO: "hello",
    DiscordMessage.BYE: "bye",
}

