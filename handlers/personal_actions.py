from aiogram import types
from dispatcher import dp
import config
import re
from bot import BotDB

@dp.message_handler(commands = "start")
async def start(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)

    await message.bot.send_message(message.from_user.id, "Добро пожаловать!")

@dp.message_handler(commands = ("add", "a"), commands_prefix = "/!")
async def start(message: types.Message):
    cmd_variants = (('/spent', '/s', '!spent', '!s'), ('/earned', '/e', '!earned', '!e'))
    # operation = '-' if message.text.startswith(cmd_variants[0]) else '+'

    description = message.text
    # for i in cmd_variants:
    #     for j in i:
    #         value = value.replace(j, '').strip()

    if(len(description)):
        # x = re.findall(r"\d+(?:.\d+)?", value)
        # if(len(x)):
        #     value = float(x[0].replace(',', '.'))

            BotDB.add_record(message.from_user.id, description)

            await message.reply("✅ Запись успешно внесена!")
            
    else:
        await message.reply("Напечатайте объявление!")

# @dp.message_handler(commands = ("history", "h"), commands_prefix = "/!")
# async def start(message: types.Message):
#     cmd_variants = ('/history', '/h', '!history', '!h')
#     within_als = {
#         "day": ('today', 'day', 'сегодня', 'день'),
#         "month": ('month', 'месяц'),
#         "year": ('year', 'год'),
#     }

#     cmd = message.text
#     for r in cmd_variants:
#         cmd = cmd.replace(r, '').strip()

#     within = 'day'
#     if(len(cmd)):
#         for k in within_als:
#             for als in within_als[k]:
#                 if(als == cmd):
#                     within = k

#     records = BotDB.get_records(message.from_user.id, within)

#     if(len(records)):
#         answer = f"🕘 История операций за {within_als[within][-1]}\n\n"

#         for r in records:
#             answer += "<b>" + ("➖ Расход" if not r[2] else "➕ Доход") + "</b>"
#             answer += f" - {r[3]}"
#             answer += f" <i>({r[4]})</i>\n"

#         await message.reply(answer)
#     else:
#         await message.reply("Записей не обнаружено!")