import os
import telegram
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
import random
import datetime
import asyncio
import logging

# =============================================
# ⚙️ НАСТРОЙКИ - ЗАМЕНИ ЗДЕСЬ СВОИ ДАННЫЕ!
# =============================================

# 🔑 ЗАМЕНИ 'YOUR_BOT_TOKEN_HERE' на токен бота от @BotFather
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8240936265:AAEOVHklnIPXT1N7bMgQ6ZVvrg9CB9TRM5o')

# 👤 ЗАМЕНИ 5234287314 на свой Telegram ID (узнать можно у @userinfobot)
ADMIN_ID = int(os.environ.get('ADMIN_ID', '8240351121'))

# =============================================
# 🚀 ОСНОВНОЙ КОД (НЕ МЕНЯЙ)
# =============================================

# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Создаем необходимые файлы если их нет
def create_required_files():
    required_files = {
        'welcome.txt': 'Добро пожаловать!',
        'namebot.txt': 'Мой Бот',
        'photomenu.txt': 'https://t.me/paraIiza/4',
        'fast.txt': 'Привет!\nКак дела?\nЧто нового?'
    }

    for filename, content in required_files.items():
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)


# Создаем файлы при запуске
create_required_files()

# Списки для хранения данных
sh = []
state = []
pined_chats = []
usersat = []
chatsat = []
chats = []
chatsp = []
chatsv = []
time = []
timeat = []

# Создаем приложение
application = Application.builder().token(BOT_TOKEN).build()


# Команды
async def start_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        ad = await context.bot.get_chat(ADMIN_ID)
        m = ReplyKeyboardMarkup(
            [
                [
                    KeyboardButton(text='Help✞'),
                    KeyboardButton(text='Разработчик✞'),
                    KeyboardButton(text='Шаблоны✞')
                ]
            ], resize_keyboard=True
        )
        name = ad.first_name
        await context.bot.send_photo(
            ADMIN_ID,
            photo='https://t.me/paraIiza/4',
            caption=f'Добро пожаловать в место где тебя похоронят, {name}✞',
            reply_markup=m
        )


async def off_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text('Ща')
        if context.args:
            try:
                chat = int(context.args[0])
                if chat in chats:
                    chats.remove(chat)
                await update.message.reply_text("Все")
            except ValueError:
                await update.message.reply_text("Неверный формат ID чата")


async def offv_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text('Ща')
        if context.args:
            try:
                chat = int(context.args[0])
                if chat in chatsv:
                    chatsv.remove(chat)
                await update.message.reply_text("Все")
            except ValueError:
                await update.message.reply_text("Неверный формат ID чата")


async def offp_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text('Ща')
        if context.args:
            try:
                chat = int(context.args[0])
                if chat in chatsp:
                    chatsp.remove(chat)
                await update.message.reply_text("Все")
            except ValueError:
                await update.message.reply_text("Неверный формат ID чата")


async def timea_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        time.clear()
        if context.args:
            try:
                chat = int(context.args[0])
                time.append(chat)
                await update.message.reply_text(f'<b>Установлена задержка:</b><code>{context.args[0]}</code>',
                                                parse_mode='HTML')
            except ValueError:
                await update.message.reply_text("Неверный формат времени")


async def settingsa_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        helptxt = (
            '\n✞ /timea + time <b>- задержка на автоответчик</b>'
            '\n✞ /shap + text <b>- шапка на автоответчик</b>'
            '\n✞ /use + user id <b>- добавляет юзерка в список автоответчика</b>'
            '\n✞ /dob ( пропиши в конференции ) <b>- добавляет весь чат в автоответчик</b>'
        )
        await update.message.reply_text(helptxt, parse_mode='HTML')


async def shap_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        sh.clear()
        url = ' '.join(context.args)
        sh.append(url)
        await update.message.reply_text(f'<b>Установлен текст в автоответчике</b>:<code>{url}</code>',
                                        parse_mode='HTML')


async def dob_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        user = update.effective_chat.id
        chatsat.append(user)
        await update.message.reply_text('добавлен в список автоответчика\n Чтобы вырубить <code>/dbb</code>',
                                        parse_mode='HTML')


async def dbb_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        user = update.effective_chat.id
        if user in chatsat:
            chatsat.remove(user)
        await update.message.reply_text('deleted.')


async def uss_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        if context.args:
            try:
                user = int(context.args[0])
                if user in usersat:
                    usersat.remove(user)
                await update.message.reply_text('deleted.')
            except ValueError:
                await update.message.reply_text("Неверный формат ID пользователя")


async def use_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        if context.args:
            try:
                user = int(context.args[0])
                usersat.append(user)
                await update.message.reply_text(
                    f'добавлен в список автоответчика\n Чтобы вырубить <code>/uss {user}</code>', parse_mode='HTML')
            except ValueError:
                await update.message.reply_text("Неверный формат ID пользователя")


async def timeat_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        timeat.clear()
        if context.args:
            try:
                chat = int(context.args[0])
                timeat.append(chat)
                await update.message.reply_text(
                    f'<b>Установлена задержка в автоответчике:</b><code>{context.args[0]}</code>', parse_mode='HTML')
            except ValueError:
                await update.message.reply_text("Неверный формат времени")


async def ras_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        text = (
            '/pin + chat id + time + text message - <b>пинит ваш текст в конфе постоянно (нужна админка)</b>'
            '\n/welcome + text - <b>меняет ваше приветствие</b>'
            '\n/namea + text - <b>меняет имя вашего бота</b>'
        )
        await update.message.reply_text(text, parse_mode='HTML')


async def welcome_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        text = ' '.join(context.args)
        with open('welcome.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        await update.message.reply_text(f'Text to welcome: {text}')


async def namea_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        text = ' '.join(context.args)
        with open('namebot.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        await update.message.reply_text(f'NameBot: {text}')


async def pin_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        if len(context.args) >= 2:
            try:
                chat = int(context.args[0])
                delay = int(context.args[1])
                text_message = ' '.join(context.args[2:])
                pined_chats.append(chat)
                await update.message.reply_text(f'For off: <code>/poff {chat}</code>', parse_mode='HTML')

                # Запускаем пин в отдельной задаче
                asyncio.create_task(pin_loop(context.bot, chat, delay, text_message))
            except ValueError:
                await update.message.reply_text("Неверный формат ID чата или времени")


async def pin_loop(bot, chat, delay, text_message):
    while chat in pined_chats:
        try:
            message = await bot.send_message(chat, text_message)
            await bot.pin_chat_message(chat, message.message_id)
            await asyncio.sleep(delay)
        except Exception as e:
            print(f"Error in pin_loop: {e}")
            await asyncio.sleep(delay)


async def poff_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        if context.args:
            try:
                chat = int(context.args[0])
                if chat in pined_chats:
                    pined_chats.remove(chat)
                    await update.message.reply_text('Deleted.')
                else:
                    await update.message.reply_text('Chat dont appended to list... Clown.')
            except ValueError:
                await update.message.reply_text("Неверный формат ID чата")


async def help_button(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        if update.message.text == 'Help✞':
            try:
                name = open('namebot.txt', 'r', encoding='utf-8').readline()
            except:
                name = "Мой Бот"

            try:
                url = open('photomenu.txt', 'r').readline()
            except:
                url = 'https://t.me/paraIiza/4'

            helptxt = (
                f'{name} help:'
                '\n✞ /prl <b>+ chat id + название шаблона.txt + обращение</b>'
                '\n✞ /prlz <b>chat id + название шаблона.txt + ссылка на видео + обращение</b>'
                '\n✞ /prlzz <b>Все тоже самое что и видео, но ссылку отправлять на фото</b>'
                '\n✞ /id <b>для получения айди чата</b>'
                '\n✞ /fast <b>Для быстрого меню</b>'
                '\n✞ /timef + time <b>Для изменения задержки отправки сообщений</b>'
                '\n✞ /settingsa + time <b>для настроек автоответчика</b>'
                '\n✞ /ras - <b>Для просмотра функций с рассылкой</b>'
                '\n✞ <b>Нажмите кнопку " шаблоны " чтобы получить все файлы в ней </b> <b>Чтобы получить все файлы которые есть в папке с ботом ( для просмотра шаблонов )</b>'
                '\n✞ <b>!!!</b> <i>просто скиньте текстовик боту и он загрузит его к себе</i>'
                '\n✞ <b>!!!</b> <i>Нажмите /start если пропали кнопки</i> '
            )
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=url,
                caption=helptxt,
                parse_mode='HTML'
            )


async def templates_button(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID and update.message.text == 'Шаблоны✞':
        try:
            await context.bot.send_message(ADMIN_ID, 'Ща скину')
            ls = os.listdir()
            info = '<code>' + '\n\n'.join([str(elem) for elem in ls]) + "</code>"

            if len(info) > 4096:
                for x in range(0, len(info), 4096):
                    await context.bot.send_message(ADMIN_ID, info[x:x + 4096], parse_mode='HTML')
            else:
                await context.bot.send_message(ADMIN_ID, info, parse_mode='HTML')
        except Exception as e:
            await context.bot.send_message(ADMIN_ID, f'Ошибка: {e}')


async def developer_button(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID and update.message.text == 'Разработчик✞':
        await context.bot.send_photo(
            ADMIN_ID,
            'https://t.me/paraIiza/4',
            'Богоподобный [Paralizator](https://t.me/paraIizator) \n Лучшие боты только у него',
            parse_mode='Markdown'
        )


async def id_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        chat_id = update.effective_chat.id
        await context.bot.send_message(update.effective_chat.id, f'✞<b>CHAT ID:</b> <code>{chat_id}</code>',
                                       parse_mode='HTML')


async def prl_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        if len(context.args) >= 2:
            try:
                chat = int(context.args[0])
                sh = context.args[1]
                ob = ' '.join(context.args[2:])

                chats.append(chat)
                await context.bot.send_message(ADMIN_ID, f'Запущен!\nЧтобы вырубить <code>/off {chat}</code>',
                                               parse_mode='HTML')

                # Запускаем рассылку в отдельной задаче
                asyncio.create_task(prl_loop(context.bot, chat, sh, ob))
            except ValueError:
                await update.message.reply_text("Неверный формат ID чата")


async def prl_loop(bot, chat, sh, ob):
    while chat in chats:
        try:
            with open(f'{sh}', 'r', encoding='utf-8') as f:
                a = f.read()
                b = a.split('\n')
                if ob:
                    await bot.send_message(chat, str(ob + random.choice(b)))
                else:
                    await bot.send_message(chat, random.choice(b))

                if time:
                    await asyncio.sleep(int(time[0]))
                else:
                    await asyncio.sleep(1)
        except Exception as e:
            print(f"Error in prl_loop: {e}")
            if time:
                await asyncio.sleep(int(time[0]))
            else:
                await asyncio.sleep(1)


async def prlz_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        if len(context.args) >= 3:
            try:
                chat = int(context.args[0])
                sh = context.args[1]
                vid = context.args[2]
                ob = ' '.join(context.args[3:])

                chatsv.append(chat)
                await update.message.reply_text(f'Запущен. Чтобы вырубить <code>/offv {chat}</code>', parse_mode='HTML')

                asyncio.create_task(prlz_loop(context.bot, chat, sh, vid, ob))
            except ValueError:
                await update.message.reply_text("Неверный формат ID чата")


async def prlz_loop(bot, chat, sh, vid, ob):
    while chat in chatsv:
        try:
            with open(f'{sh}', 'r', encoding='utf-8') as f:
                a = f.read()
                b = a.split('\n')
                await bot.send_video(chat, video=vid, caption=(ob + random.choice(b)))

                if time:
                    await asyncio.sleep(int(time[0]))
                else:
                    await asyncio.sleep(1)
        except Exception as e:
            print(f"Error in prlz_loop: {e}")
            if time:
                await asyncio.sleep(int(time[0]))
            else:
                await asyncio.sleep(1)


async def prlzz_command(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        if len(context.args) >= 3:
            try:
                chat = int(context.args[0])
                sh = context.args[1]
                photo = context.args[2]
                ob = ' '.join(context.args[3:])

                chatsp.append(chat)
                await update.message.reply_text(f'Запущен. Чтобы вырубить <code>/offp {chat}</code>', parse_mode='HTML')

                asyncio.create_task(prlzz_loop(context.bot, chat, sh, photo, ob))
            except ValueError:
                await update.message.reply_text("Неверный формат ID чата")


async def prlzz_loop(bot, chat, sh, photo, ob):
    while chat in chatsp:
        try:
            with open(f'{sh}', 'r', encoding='utf-8') as f:
                a = f.read()
                b = a.split('\n')
                await bot.send_photo(chat, photo=photo, caption=(ob + random.choice(b)))

                if time:
                    await asyncio.sleep(int(time[0]))
                else:
                    await asyncio.sleep(1)
        except Exception as e:
            print(f"Error in prlzz_loop: {e}")
            if time:
                await asyncio.sleep(int(time[0]))
            else:
                await asyncio.sleep(1)


async def new_chat_members(update: Update, context: CallbackContext):
    if update.message.new_chat_members:
        mes = update.effective_chat
        ids = mes.id
        try:
            text = open('welcome.txt', 'r', encoding='utf-8').readline()
        except:
            text = "Добро пожаловать!"

        text1 = f'{text} {os.name} \nID: <code>{ids}</code>\nChat title: <code>{mes.title}</code>'
        await asyncio.sleep(1)

        try:
            photo = open('photomenu.txt', 'r').read()
        except:
            photo = 'https://t.me/paraIiza/4'

        await context.bot.send_photo(update.effective_chat.id, photo=photo, caption=text1, parse_mode='HTML')


async def document_handler(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        try:
            msg = await context.bot.send_message(update.effective_user.id, "Скачиваю...")
            file_id = update.message.document.file_id
            file = await context.bot.get_file(file_id)

            await file.download_to_drive(update.message.document.file_name)
            await context.bot.edit_message_text('Успешно скачал ✅', update.effective_chat.id, msg.message_id)
        except Exception as e:
            await context.bot.send_message(update.effective_user.id, f"Ошибка: {e}")


async def auto_reply(update: Update, context: CallbackContext):
    if (update.effective_user.id in usersat) or (
            update.effective_chat.id in chatsat and update.effective_user.id != ADMIN_ID):
        if timeat:
            await asyncio.sleep(int(timeat[0]))
        try:
            with open('fast.txt', 'r', encoding='utf-8') as f:
                a = f.read()
                a = a.split('\n')
                if sh:
                    await update.message.reply_text(str(sh[0] + random.choice(a)))
                else:
                    await update.message.reply_text(random.choice(a))
        except Exception as e:
            print(f"Auto-reply error: {e}")


# Регистрируем обработчики
def setup_handlers(app):
    # Команды
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("off", off_command))
    app.add_handler(CommandHandler("offv", offv_command))
    app.add_handler(CommandHandler("offp", offp_command))
    app.add_handler(CommandHandler("timea", timea_command))
    app.add_handler(CommandHandler("settingsa", settingsa_command))
    app.add_handler(CommandHandler("shap", shap_command))
    app.add_handler(CommandHandler("dob", dob_command))
    app.add_handler(CommandHandler("dbb", dbb_command))
    app.add_handler(CommandHandler("uss", uss_command))
    app.add_handler(CommandHandler("use", use_command))
    app.add_handler(CommandHandler("timeat", timeat_command))
    app.add_handler(CommandHandler("ras", ras_command))
    app.add_handler(CommandHandler("welcome", welcome_command))
    app.add_handler(CommandHandler("namea", namea_command))
    app.add_handler(CommandHandler("pin", pin_command))
    app.add_handler(CommandHandler("poff", poff_command))
    app.add_handler(CommandHandler("id", id_command))
    app.add_handler(CommandHandler("prl", prl_command))
    app.add_handler(CommandHandler("prlz", prlz_command))
    app.add_handler(CommandHandler("prlzz", prlzz_command))

    # Обработчики сообщений
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Help✞$'), help_button))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Шаблоны✞$'), templates_button))
    app.add_handler(MessageHandler(filters.TEXT & filters.Regex('^Разработчик✞$'), developer_button))
    app.add_handler(MessageHandler(filters.Document.ALL, document_handler))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_chat_members))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))


# Запуск бота
if __name__ == '__main__':
    print("🚀 Запуск бота на Railway...")
    print(f"🔑 Токен: {BOT_TOKEN}")
    print(f"👤 Админ ID: {ADMIN_ID}")
    setup_handlers(application)
    application.run_polling()