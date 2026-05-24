import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ================== TOKEN ==================
TOKEN = "8981227915:AAGt_Aimvc1UZQRJw9jt_5lAXMyq3AVR9T4"

bot = telebot.TeleBot(TOKEN)

# ================== MENUS ==================

def main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("🛒 Tech", callback_data="cat_tech"))
    markup.add(InlineKeyboardButton("📦 Fournisseur", callback_data="cat_fournisseur"))
    markup.add(InlineKeyboardButton("❓ Support", callback_data="support"))
    return markup

def tech_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📱 iPhone / Samsung", callback_data="tech_phones"))
    markup.add(InlineKeyboardButton("💻 Ordinateurs & Laptops", callback_data="tech_laptops"))
    markup.add(InlineKeyboardButton("🎧 AirPods & Casques", callback_data="tech_audio"))
    markup.add(InlineKeyboardButton("🔌 Accessoires Tech", callback_data="tech_access"))
    markup.add(InlineKeyboardButton("🔙 Retour", callback_data="back_main"))
    return markup

def fournisseur_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("📦 Grossiste Téléphones", callback_data="four_phones"))
    markup.add(InlineKeyboardButton("🖥 Grossiste Informatique", callback_data="four_pc"))
    markup.add(InlineKeyboardButton("📡 Accessoires en gros", callback_data="four_access"))
    markup.add(InlineKeyboardButton("🔙 Retour", callback_data="back_main"))
    return markup

# ================== START ==================

@bot.message_handler(commands=['start'])
def start(message):
    text = """
🔥 **Bienvenue sur Le Shop UHQ !**

Choisis ta catégorie :
    """
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu())

# ================== CALLBACKS ==================

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    data = call.data

    if data == "cat_tech":
        bot.edit_message_text("🛒 **Catégorie Tech**", chat_id, call.message.message_id, 
                            reply_markup=tech_menu(), parse_mode="Markdown")
    
    elif data == "cat_fournisseur":
        bot.edit_message_text("📦 **Catégorie Fournisseur**", chat_id, call.message.message_id, 
                            reply_markup=fournisseur_menu(), parse_mode="Markdown")
    
    elif data == "back_main":
        bot.edit_message_text("🔥 **Menu Principal**", chat_id, call.message.message_id, 
                            reply_markup=main_menu(), parse_mode="Markdown")
    
    elif data.startswith("tech_") or data.startswith("four_"):
        bot.answer_callback_query(call.id, "✅ Sélectionné")
        bot.send_message(chat_id, f"Tu as sélectionné : **{data}**\n\nContacte le support pour le prix et paiement (@UHQ_7500).", parse_mode="Markdown")
    
    elif data == "support":
        bot.send_message(chat_id, "🆘 **Support** :\n@UHQ_7500")

# ================== LANCEMENT ==================
if __name__ == "__main__":
    print("🤖 Bot démarré avec succès...")
    bot.infinity_polling(none_stop=True)
