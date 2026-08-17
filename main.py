import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters, CommandHandler

# ১. জেমিনি এপিআই কী সেটআপ
GEMINI_API_KEY = "AQ.Ab8RN6IG6tkEktvODDbz3t-T9H599j-LVkuZkKTlyHSCb9a57Q"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# স্টার্ট কমান্ড হ্যান্ডলার
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("হ্যালো নূর ভাই! আমি আপনার টেলিগ্রাম এআই বট। আমাকে যেকোনো প্রশ্ন করতে পারেন!")

# মেসেজ হ্যান্ডলার ফাংশন
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_text = update.message.text
        response = model.generate_content(user_text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("দুঃখিত, কোনো সমস্যা হয়েছে। আবার চেষ্টা করুন।")

# ৩. বট রান করা
if __name__ == '__main__':
    BOT_TOKEN = "8714503275:AAH16SOBBR2-67H1KmNkLO07MRENFKTOt6w"
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot is running...")
    app.run_polling()
