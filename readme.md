# 🛠️ Discord Bot - Modular Cog-Based Setup

A powerful and modular Discord bot built using `discord.py`, designed to be scalable and easy to maintain. It includes a combination of slash commands, prefix commands, and event-based features.

---

## 🚀 Features

### ✅ Slash Commands
- `/ping`: Returns bot latency with a stylish embed.
- `/say <message>`: Bot will repeat your message. *(No need for quotes around the message!)*

### ✅ Prefix Commands
- `!say <message>`: Bot echoes your message (free-form string, no quotes required).
- `!ban <user>`: Bans a user from the server, with built-in error detection.

---

## 📁 Project Structure

```bash
.
├── bot.py              # Main bot launcher
├── .env                # Stores your bot token securely
├── cogs/               # Modular command and event files
│   ├── admin.py        # Ban command and other admin tools
│   ├── commands.py     # Say command and general commands
│   ├── crazy_shits.py  # Meme/random/fun commands
│   ├── events.py       # Event listeners like on_ready, on_message
│   ├── extra.py        # Additional features and utilities
│   ├── games.py        # Mini-games or gaming-related features
│   ├── greetings.py    # Welcome/greeting logic
│   ├── utility.py      # Ping and helper slash commands
└── README.md
---
```

## Requirements
Python 3.8+

discord.py 2.0+ (for slash commands support)

python-dotenv (for .env usage)

-------

```
Install all dependencies:

pip install -U discord.py python-dotenv
pip install discord
pip install discord.py
```

⚙️ Getting Started
Clone the repository.

Create a .env file in the root directory and add your bot token:

init

DISCORD_TOKEN=your_token_here
Run the bot:


---
> python bot.py
>🧠 Notes
>All commands are modularized using Cogs for better organization.
>Slash commands are registered with Discord automatically.
>Errors are handled gracefully with helpful responses.

---
Developer

Made by Abhi.

Feel free to contribute or report issues!
