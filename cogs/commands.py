import nextcord
import requests

from nextcord.ext.commands.bot import Bot
from nextcord.embeds import Embed
from nextcord.ext import commands
from nextcord import Colour, Interaction
from nextcord.user import ClientUser
from sys import exc_info
from buttons.verification import verification
from os import environ

guilds = [int(environ.get('guild_id', None))]


class Buttons(commands.Cog):

    def __init__(self: ClientUser, client: Bot):
        self.bot = client

    @nextcord.slash_command(name='verification', description='Создание эмбеда с кнопкой для верификации',
                            guild_ids=guilds)
    async def verification(self, interaction: Interaction, channel: nextcord.abc.GuildChannel):
        try:
            channel = interaction.client.get_channel(channel.id)
            if channel is not None:
                verification_embed = Embed(title='Приветик, давай знакомиться!',
                              description='Мы не любим плохих роботов и поэтому нам нужна гарантия того, '
                                          'то Вы — человек! Нажмите на кнопку ниже, чтобы получить доступ к другим каналам!',
                              color=nextcord.Colour.from_rgb(48, 49, 53))
                verification_embed.set_image(url='https://i.imgur.com/Dkhme0q.png')
                await channel.send(embed=verification_embed, view=verification())
            else:
                await interaction.response.send_message('Error', ephemeral=True)
            if interaction.response.is_done() is False:
                await interaction.response.send_message(f"Сообщение с кнопками создан в канале {channel.mention}",
                                                        ephemeral=True)
            elif interaction.response.is_done() is True:
                await interaction.followup.send(f"Сообщение с кнопками создан в канале {channel.mention}",
                                                ephemeral=True)
        except Exception as error:
            print(error, f'\nat line {exc_info()[2].tb_lineno}')

    @nextcord.slash_command(name='cat', description='Рандомная пикча с котиком, лично для тебя', guild_ids=guilds)
    async def random_cat(self, interaction: Interaction):
        try:
            url = requests.get(url='https://some-random-api.ml/animal/cat').json()
            embed = Embed(color=Colour.from_rgb(47, 49, 54))
            embed.set_image(url=url['image'])
            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as error:
            print(error, f'\nat line {exc_info()[2].tb_lineno}')
            if interaction.response.is_done() is False:
                await interaction.response.send_message(f"Произошла неизвестная ошибка",
                                                        ephemeral=True)
            elif interaction.response.is_done() is True:
                await interaction.followup.send(f"Произошла неизвестная ошибка",
                                                ephemeral=True)


def setup(bot):
    bot.add_cog(Buttons(bot))
