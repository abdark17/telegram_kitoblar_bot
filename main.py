from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = "7807683658:AAEVPGDFCP_DlHBCSO5pP-6ADQUo-VpsxGs"   # Token xavfsizlik uchun yashirilishi kerak
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# === GLOBAL BACK NAVIGATION STATE ===
user_state = {}

# =========================
# START
# =========================
@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton("📚 Кутубхона"))
    await msg.answer("👇🏻", reply_markup=kb)
    user_state[msg.from_user.id] = "main"


# =========================
# KUTUBXONA (5 bo‘lim)
# =========================
@dp.message_handler(lambda m: m.text == "📚 Кутубхона")
async def library(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(
        types.KeyboardButton("Ақида"),
        types.KeyboardButton("Фиқҳ"),
        types.KeyboardButton("Манҳаж"),
        types.KeyboardButton("Ҳадис"),
        types.KeyboardButton("Одоб")
    )
    await msg.answer("👇🏻", reply_markup=kb)
    user_state[msg.from_user.id] = "kutubxona"



# ============================================
# --- A Q I D A ---
# ============================================
aqida_buttons = [
    "Ла илаҳа иллаллоҳ калимаси шартлари",
    "Исломнинг икки шаҳодатини таҳқиқ қилиш билан боғлиқ ислом диёрининг калити",
    "Тўрт қоида шарҳи",
    "Олти асос шарҳи",
    "Исломни бузувчи амаллар",
    "Ақида дарслари силсиласи",
    "Қўрқув хавфнинг турлари",
    "Умид қилишнинг турлари",
    "Аллоҳдан ўзгага таваккул қилишлик",
    "Рағбат, Раҳбат ва хушуъ",
    "Тошлардан, дарахтлардан, қабрлардан барака талаб этиш ширк эканлиги ҳақида",
    "Солиҳ кишилар осорлари борасида ғулув кетиш ширкнинг келиб чиқишига сабабдир"
]

@dp.message_handler(lambda m: m.text == "Ақида")
async def aqida(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for b in aqida_buttons:
        kb.add(types.KeyboardButton(b))
    kb.add(types.KeyboardButton("⬅️ Ортга"))
    await msg.answer("👇🏻", reply_markup=kb)
    user_state[msg.from_user.id] = "aqida"


@dp.message_handler(lambda m: m.text in aqida_buttons)
async def aqida_files(msg: types.Message):

    pdf_paths = {
        aqida_buttons[0]: "pdf/Ла_илаҳа_иллаллоҳ_калимасининг_шартлари.pdf",
        aqida_buttons[1]: "pdf/ИСЛОМНИНГ_ИККИ_ШАҲОДАТИНИ_ТАҲҚИҚ_ҚИЛИШ_БИЛАН_БОҒЛИҚ_ИСЛОМ_ДИЁРИНИНГ.pdf",
        aqida_buttons[2]: "pdf/«ТЎРТ ҚОИДА» ШАРҲИ..pdf",
        aqida_buttons[3]: "pdf/«ОЛТИ АСОС» ШАРҲИ..pdf",
        aqida_buttons[4]: "pdf/Исломни бузувчи амаллар баёни.pdf",
        aqida_buttons[5]: "pdf/Ақида дарслари силсиласи..pdf",
        aqida_buttons[6]: "pdf/Қўрқув-хавфнинг турлари__.pdf",
        aqida_buttons[7]: "pdf/Умид қилишнинг турлари..pdf",
        aqida_buttons[8]: "pdf/Аллоҳдан_бошқасига_таваккул_қилишлик_ширк_экани_ҳақида.pdf",
        aqida_buttons[9]: "pdf/Рағбат, раҳбат ва хушуъ.pdf",
        aqida_buttons[10]: "pdf/Тошлардан_,_дарахтлардан_,_қабрлардан_барака_талаб_этиш_ширк_эканлиги.pdf",
        aqida_buttons[11]: "pdf/Солиҳ_кишиларнинг_осорлари_борасида_ғулув_кетиш_ширкнинг_келиб_чиқишига.pdf"
    }

    chosen = msg.text
    file_path = pdf_paths[chosen]

    caption = f"• {chosen}\n\n<i>Тайёрлади: Абу Умар</i>"

    try:
        with open(file_path, "rb") as pdf:
            await msg.answer_document(document=pdf, caption=caption, parse_mode="HTML")
    except:
        await msg.answer("⚠️ Fayl topilmadi.")



# ============================================
# --- F I Q H ---
# ============================================
fiqh_buttons = [
    "Таҳорат , намоз ва рўзага оид аҳкомлар",
    "Намозда қайтарилган ўтиришликнинг баъзи суратлари",
    "Намоздан кейинги зикрлар",
    "Соч ва бадан тукларига тегишли баъзи аҳкомлар",
    "Оқарган соч-соқолни бўяшликда баъзи аҳкомлар",
    "Рўзага оид аҳкомлар",
    "Фитр закоти",
    "УСУЛ ИЛМИДАН АСОСЛАР"
]

@dp.message_handler(lambda m: m.text == "Фиқҳ")
async def fiqh(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for b in fiqh_buttons:
        kb.add(types.KeyboardButton(b))
    kb.add(types.KeyboardButton("⬅️ Ортга"))
    await msg.answer("👇🏻", reply_markup=kb)
    user_state[msg.from_user.id] = "fiqh"


@dp.message_handler(lambda m: m.text in fiqh_buttons)
async def fiqh_files(msg: types.Message):

    pdf_paths = {
        fiqh_buttons[0]: "pdf/Таҳорат,_намоз_ва_рўзага_оид_аҳкомлар_.pdf",
        fiqh_buttons[1]: "pdf/Намозда_қайтарилган_ўтиришликнинг_баъзи_суратларига_мисоллар.pdf",
        fiqh_buttons[2]: "pdf/Namozdan keyingi zikrlar.pdf",
        fiqh_buttons[3]: "pdf/Соч_ва_бадан_тукларини_олиш_ёки_олмаслик_эътибори_билан_баъзи_аҳкомлар.pdf",
        fiqh_buttons[4]: "pdf/Оқарган_соч_соқолни_бўяшликнинг_ҳукмлари_.pdf",
        fiqh_buttons[5]: "pdf/Рўзага оил аҳкомлар.pdf",
        fiqh_buttons[6]: "pdf/Фитр_закоти.pdf",
        fiqh_buttons[7]: "pdf/УСУЛ ИЛМИДАН АСОСЛАР.pdf",
    }

    chosen = msg.text
    file_path = pdf_paths[chosen]
    caption = f"• {chosen}\n\n<i>Тайёрлади: Абу Умар</i>"

    try:
        with open(file_path, "rb") as pdf:
            await msg.answer_document(pdf, caption=caption, parse_mode="HTML")
    except:
        await msg.answer("⚠️ Fayl topilmadi.")



# ============================================
# --- M A N H A J ---
# ============================================
manhaj_buttons = [
    "Фитна вақтида лозим бўлган 5-амал",
    "Фитна қаршисида мусулмон кишининг вазифалари",
    "Қони харом бўлган 4-тоифа",
    "Жаҳмийлар ва ашарийлар қуръон хусусида ботил эътиқодларининг баёни",
    "Ҳукмдорнинг ҳақлари"
]

@dp.message_handler(lambda m: m.text == "Манҳаж")
async def manhaj(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for b in manhaj_buttons:
        kb.add(types.KeyboardButton(b))
    kb.add(types.KeyboardButton("⬅️ Ортга"))
    await msg.answer("👇🏻", reply_markup=kb)
    user_state[msg.from_user.id] = "manhaj"


@dp.message_handler(lambda m: m.text in manhaj_buttons)
async def manhaj_files(msg: types.Message):

    pdf_paths = {
        manhaj_buttons[0]: "pdf/Fitna vaqtida lozim bo'lgan 5 amal.pdf",
        manhaj_buttons[1]: "pdf/Фитна_қаршисида_мусулмон_кишининг_вазифалари.pdf",
        manhaj_buttons[2]: "pdf/Қони ҳаром бўлган тўрт тоифа.pdf",
        manhaj_buttons[3]: "pdf/Жаҳмийлар_ва_ашарийлар_Қуръон_ҳусусида_ботил_эътиқодларининг_баёни.pdf",
        manhaj_buttons[4]: "pdf/Ҳукмдорнинг ҳақлари_.pdf",
    }

    chosen = msg.text
    file_path = pdf_paths[chosen]
    caption = f"• {chosen}\n\n<i>Тайёрлади: Абу Умар</i>"

    try:
        with open(file_path, "rb") as pdf:
            await msg.answer_document(pdf, caption=caption, parse_mode="HTML")
    except:
        await msg.answer("⚠️ Fayl topilmadi.")



# ============================================
# --- H A D I S ---
# ============================================
@dp.message_handler(lambda m: m.text == "Ҳадис")
async def hadis(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(types.KeyboardButton("Қирқ ҳадиснинг муҳтасар шарх ҳадиснинг муҳтасар шархи"))
    kb.add(types.KeyboardButton("⬅️ Ортга"))
    await msg.answer("👇🏻", reply_markup=kb)
    user_state[msg.from_user.id] = "hadis"


@dp.message_handler(lambda m: m.text == "Қирқ ҳадиснинг муҳтасар шарх ҳадиснинг муҳтасар шархи")
async def hadis_file(msg: types.Message):

    chosen = msg.text
    caption = f"• {chosen}\n\n<i>Тайёрлади: Абу Умар</i>"

    try:
        with open("pdf/«ҚИРҚ_ҲАДИС»НИНГ_МУҲТАСАР_ШАРҲИ_.pdf", "rb") as pdf:
            await msg.answer_document(pdf, caption=caption, parse_mode="HTML")
    except:
        await msg.answer("⚠️ Fayl topilmadi.")



# ============================================
# --- O D O B ---
# ============================================
odob_buttons = [
    "Билим талабида 9 асос",
    "Савол қўйиш одоблари",
    "Илмнинг Фазилати"
]

@dp.message_handler(lambda m: m.text == "Одоб")
async def odob(msg: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for b in odob_buttons:
        kb.add(types.KeyboardButton(b))
    kb.add(types.KeyboardButton("⬅️ Ортга"))
    await msg.answer("👇🏻", reply_markup=kb)
    user_state[msg.from_user.id] = "odob"


@dp.message_handler(lambda m: m.text in odob_buttons)
async def odob_files(msg: types.Message):

    pdf_paths = {
        odob_buttons[0]: "pdf/Билим талабида 9 асос.pdf",
        odob_buttons[1]: "pdf/САВОЛ ҚЎЙИШ ОДОБЛАРИ.pdf",
        odob_buttons[2]: "pdf/Илмнинг фазилати.pdf",
    }

    chosen = msg.text
    file_path = pdf_paths[chosen]
    caption = f"• {chosen}\n\n<i>Тайёрлади: Абу Умар</i>"

    try:
        with open(file_path, "rb") as pdf:
            await msg.answer_document(pdf, caption=caption, parse_mode="HTML")
    except:
        await msg.answer("⚠️ Fayl topilmadi.")



# ============================================
# 🔙 ORTGA QAYTISH
# ============================================
@dp.message_handler(lambda m: m.text == "⬅️ Ортга")
async def back(msg: types.Message):

    state = user_state.get(msg.from_user.id, "main")

    if state in ["aqida", "fiqh", "manhaj", "hadis", "odob"]:
        await library(msg)

    elif state == "kutubxona":
        await start(msg)



# =========================
# RUN
# =========================
if __name__ == '__main__':
    executor.start_polling(dp)

