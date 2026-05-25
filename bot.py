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
    markup.add(InlineKeyboardButton("🔥 Tech SNAP SS06", callback_data="tech_snap"))
    markup.add(InlineKeyboardButton("🍔 Tech Uber Eats", callback_data="tech_ubereats"))
    markup.add(InlineKeyboardButton("🚗 Tech Uber", callback_data="tech_uber"))
    markup.add(InlineKeyboardButton("🍎 Tech Apple", callback_data="tech_apple"))
    markup.add(InlineKeyboardButton("🛒 Tech Amazone", callback_data="tech_amazon"))
    markup.add(InlineKeyboardButton("🔙 Retour", callback_data="back_main"))
    return markup

def fournisseur_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("🧨 Fournisseur mortiers", callback_data="four_mortiers"))
    markup.add(InlineKeyboardButton("⌚️ Fournisseur 1.1 montre Swatch X Ap", callback_data="four_swatches"))
    markup.add(InlineKeyboardButton("💎 Fournisseur sac et montre de luxe", callback_data="four_luxe"))
    markup.add(InlineKeyboardButton("👖 Fournisseur ensemble essentiels", callback_data="four_essentiels"))
    markup.add(InlineKeyboardButton("🔙 Retour", callback_data="back_main"))
    return markup

# ================== START ==================

@@bot.message_handler(commands=['start'])
def start(message):
    text = "🔥 **Bienvenue sur Le Shop UHQ !**\n\n" \
           "Nous sommes ravis de vous accueillir.\n" \
           "Vous trouverez ici une sélection de produits de qualité au meilleur prix.\n\n" \
           "🆘 SAV : @UHQ_7500\n\n" \
           "Choisis ta catégorie :"

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

    bot.answer_callback_query(call.id)

# ================== LANCEMENT ==================
if __name__ == "__main__":
    print("🤖 Bot UHQ démarré avec succès...")
    bot.infinity_polling(none_stop=True)
