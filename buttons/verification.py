from nextcord import ButtonStyle, Interaction
from nextcord.ui import View, Button, button
from sys import exc_info


class verification(View):
    def __init__(self):
        super().__init__(timeout=None)

    @button(label="Подтвердить", row=0, style=ButtonStyle.green, custom_id=f'verification')
    async def verification_button(self, btn: Button, interaction: Interaction):
        try:
            if interaction.response.is_done() is False:
                await interaction.response.send_message(f"Ты уже прошел верефикацию...",
                                                        ephemeral=True)
            elif interaction.response.is_done() is True:
                await interaction.followup.send(f"Ты уже прошел верефикацию...",
                                                ephemeral=True)
        except Exception as error:
            print(error, f'\nat line {exc_info()[2].tb_lineno}')
            if interaction.response.is_done() is False:
                await interaction.response.send_message(f"Произошла неизвестная ошибка...",
                                                        ephemeral=True)
            elif interaction.response.is_done() is True:
                await interaction.followup.send(f"Произошла неизвестная ошибка...",
                                                ephemeral=True)
