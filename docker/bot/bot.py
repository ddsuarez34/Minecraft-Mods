import os
import asyncio
from discord.ext import commands
from mcrcon import MCRcon

# Read config from env
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
RCON_HOST     = os.environ.get("RCON_HOST", "mc-server")
RCON_PORT     = int(os.environ.get("RCON_PORT", 25575))
RCON_PASSWORD = os.environ["RCON_PASSWORD"]

# Prefix for your bot commands
bot = commands.Bot(command_prefix="!")

def run_rcon(cmd: str) -> str:
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        return mcr.command(cmd)

# A simple “say” command
@bot.command()
@commands.has_any_role("Admin","Moderator")
async def say(ctx, *, message: str):
    """!say <message> — broadcast chat from the bot."""
    resp = run_rcon(f"say [Discord] {message}")
    await ctx.send(f"✅ Sent to server chat.")

@bot.command()
@commands.has_role("Admin")
async def stop(ctx):
    """!stop — gracefully stop the MC server."""
    run_rcon("stop")
    await ctx.send("🛑 Server stopping…")

@bot.command()
async def status(ctx):
    """!status — check MC server status via RCON."""
    # For example, try a harmless command:
    try:
        run_rcon("list")
        await ctx.send("✅ Server is up and responding!")
    except Exception as e:
        await ctx.send(f"❌ Server isn’t responding: {e}")

# Run the bot
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
