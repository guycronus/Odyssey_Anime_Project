# Anime Odyssey Hub

## Overview
Anime Odyssey Hub is a suite of interconnected Telegram bots designed to enhance the experience for anime enthusiasts. These bots provide features like real-time news updates, trivia games, SFW anime-style art generation, community discussions, and merchandise deal alerts. Built with Python and Telegram's Bot API, this project aims to create a profitable, automated ecosystem with passive income through premium subscriptions, affiliate marketing, and in-app purchases.

The project is structured as an "army" of bots that cross-promote each other, fostering user engagement and scalability. It's inspired by the goal of generating sustainable income to replace traditional work, allowing more time for personal projects like programming DΞS☥INY.

### Bots in the Suite
- **@OdysseySpark**: Delivers daily anime news, release updates, and personalized subscriptions to specific series or genres.
- **@OdysseyQuest**: Offers anime-themed trivia quizzes, challenges, and leaderboards for solo or group play.
- **@OdysseyCanvas**: Generates safe-for-work (SFW) anime-style art based on user prompts, with built-in filters to ensure appropriateness.
- **@OdysseyClan**: Builds communities for anime fans with moderated discussions, fan art sharing, and role-playing features.
- **@OdysseyBazaar**: Curates deals on anime merchandise from platforms like Amazon and Right Stuf Anime, with affiliate links for monetization.

## Features
- **Automation**: Bots use APIs (e.g., MyAnimeList, Amazon Associates) and schedulers for real-time updates and notifications.
- **Monetization**:
  - Freemium model with premium subscriptions ($7–$15/month) for exclusive features.
  - Affiliate commissions from streaming services (e.g., Crunchyroll) and merch sales.
  - In-app purchases via Telegram Stars.
- **Cross-Promotion**: Each bot advertises the others to drive user retention and growth.
- **Security**: Environment variables for sensitive data (e.g., bot tokens) via `.env` files.
- **Scalability**: Shared backend database (SQLite) for user data across bots.

## Tech Stack
- **Language**: Python 3.12
- **Key Libraries**:
  - `python-telegram-bot`: For Telegram API integration.
  - `requests`: For fetching data from external APIs.
  - `apscheduler`: For scheduling tasks like daily broadcasts.
  - `python-dotenv`: For managing environment variables.
- **Database**: SQLite for user subscriptions and preferences.
- **Hosting**: Heroku (prototype) or AWS for production.
- **APIs**: MyAnimeList (via Jikan), Amazon Associates, Stable Diffusion (for art generation in @OdysseyCanvas).

## Installation
1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/anime-odyssey-hub.git
   cd anime-odyssey-hub
   ```

2. **Set Up Virtual Environment**:
   ```
   python -m venv venv
   ```
   - Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux).

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   - Create a `.env` file in the root directory:
     ```
     ODYSSEYSPARK_BOT_TOKEN=your_spark_token_here
     # Add tokens for other bots as you build them
     ```
   - Obtain tokens from Telegram's BotFather.

5. **Initialize Database**:
   - Run the bot scripts to auto-create SQLite databases (e.g., `odyssey_spark.db`).

## Usage
1. **Run a Bot** (e.g., @OdysseySpark):
   ```
   cd spark
   python bot.py
   ```
   - Interact via Telegram: Send `/start` to @OdysseySpark for onboarding.

2. **Commands** (Example for @OdysseySpark):
   - `/start`: Welcome and instructions.
   - `/news`: Fetch latest anime news.
   - `/subscribe <anime>`: Get alerts for a specific series.
   - `/premium`: Info on premium features.
   - `/promote`: Discover other Odyssey bots.

3. **Deployment**:
   - Deploy to Heroku: Create an app, set config vars (e.g., bot tokens), and push the code.
   - Use webhooks for production (update script to `self.app.run_webhook(...)`).

4. **Monetization Setup**:
   - Join affiliate programs (e.g., Amazon Associates, Crunchyroll Affiliates).
   - Integrate Telegram Payments for subscriptions (add to script using `telegram.ext.PreCheckoutQueryHandler`).

## Project Structure
```
anime-odyssey-hub/
├── common/             # Shared code (e.g., database utils)
├── spark/              # @OdysseySpark bot
│   └── bot.py
├── quest/              # @OdysseyQuest bot (WIP)
├── canvas/             # @OdysseyCanvas bot (WIP)
├── clan/               # @OdysseyClan bot (WIP)
├── bazaar/             # @OdysseyBazaar bot (WIP)
├── .env                # Environment variables (gitignore'd)
├── requirements.txt    # Dependencies
├── README.md           # This file
└── .gitignore          # Ignore venv, .env, etc.
```

## Contributing
Contributions are welcome! Focus on adding features like premium integrations or new bot functionalities. Please:
1. Fork the repo.
2. Create a feature branch (`git checkout -b feature/xyz`).
3. Commit changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature/xyz`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact
For questions or collaborations, reach out via GitHub Issues or Telegram (@Vulcanguile).

---
