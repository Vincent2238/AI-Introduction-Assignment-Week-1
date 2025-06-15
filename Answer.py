# CryptoBuddy - Your AI-powered Financial Sidekick! 🌟

# Sample crypto database
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

# Chatbot greeting
def greet():
    print("👋 Hey there! I’m CryptoBuddy—your AI-powered financial sidekick!")
    print("Ask me anything about crypto trends or sustainability 💰🌱")

# Chatbot logic
def respond_to_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 Try {coin}! It's eco-friendly with a high sustainability score of {crypto_db[coin]['sustainability_score']*10:.0f}/10.")

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        print(f"📈 The following coins are trending up: {', '.join(trending)}")

    elif "long-term" in user_query or "best to buy" in user_query:
        candidates = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"
                      and crypto_db[coin]["market_cap"] in ["medium", "high"]
                      and crypto_db[coin]["sustainability_score"] >= 0.7]
        if candidates:
            print(f"🚀 For long-term growth, consider: {', '.join(candidates)}")
        else:
            print("🤔 Hmm, no coin matches all long-term growth criteria right now.")

    elif "disclaimer" in user_query:
        print("⚠️ Crypto is risky—always do your own research before investing!")

    else:
        print("🤖 Sorry, I didn’t quite catch that. Try asking about 'sustainable' or 'trending' coins!")

# Chat loop
def start_chat():
    greet()
    while True:
        user_query = input("\nYou: ")
        if user_query.lower() in ["exit", "quit", "bye"]:
            print("👋 Bye for now! Stay smart and safe with your crypto choices!")
            break
        respond_to_query(user_query)

# Run the bot
if __name__ == "__main__":
    start_chat()

