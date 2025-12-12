#Made by Gl1tch : https://github.com/Gl1tch404x

import os
import json
import time
import random
import threading
import requests
from colorama import Fore, Style, init

init(autoreset=True)

PURPLE = Fore.MAGENTA
BRIGHT_PURPLE = Fore.MAGENTA + Style.BRIGHT
RESET = Style.RESET_ALL
TOKENS_FILE = "tokens.txt"

os.system('cls' if os.name == 'nt' else 'clear')

class DiscordRaider:
    def __init__(self):
        self.tokens = []
        self.load_tokens()
        
    def load_tokens(self):
        try:
            if os.path.exists(TOKENS_FILE):
                with open(TOKENS_FILE, 'r') as f:
                    self.tokens = [line.strip() for line in f if line.strip()]
                print(f"{PURPLE}[+] Loaded {len(self.tokens)} tokens from {TOKENS_FILE}")
        except Exception as e:
            print(f"{PURPLE}[!] Error loading tokens: {str(e)}")
            self.tokens = []
            
    def save_tokens(self):
        pass

    def add_token(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.display_logo()
            token = input(f"{PURPLE}Enter token to add: {RESET}").strip()
            if not token:
                print(f"{PURPLE}[!] No token entered.")
                time.sleep(2)
                return
            if token in self.tokens:
                print(f"{PURPLE}[!] Token already exists in the list.")
                time.sleep(2)
                return
            if len(token) >= 59:
                self.tokens.append(token)
                self.save_tokens()
                print(f"{PURPLE}[+] Token added successfully!")
            else:
                print(f"{PURPLE}[!] Invalid token format! Token must be at least 59 characters.")
            time.sleep(2)
        except Exception as e:
            print(f"{PURPLE}[!] Error adding token: {str(e)}")
            time.sleep(2)

    def list_tokens(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_logo()

        if not self.tokens:
            print(f"{PURPLE}[!] No tokens available.")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        print(f"{PURPLE}Checking token validity...{RESET}")
        
        valid_tokens = []
        invalid_tokens = []
        
        for token in self.tokens:
            if self.check_token_validity(token):
                valid_tokens.append(token)
            else:
                invalid_tokens.append(token)
        
        with open("token_status.txt", "w") as f:
            f.write("===== VALID TOKENS =====\n")
            for token in valid_tokens:
                f.write(f"{token}\n")
            
            f.write("\n===== INVALID TOKENS =====\n")
            for token in invalid_tokens:
                f.write(f"{token}\n")
        
        print(f"{PURPLE}Tokens saved to token_status.txt{RESET}")
        print(f"{Fore.GREEN}Valid tokens: {len(valid_tokens)}{RESET}")
        print(f"{Fore.RED}Invalid tokens: {len(invalid_tokens)}{RESET}")
        
        print(f"\n{PURPLE}Options:{RESET}")
        print(f"{PURPLE}1. Remove Specific Token{RESET}")
        print(f"{PURPLE}2. Remove All Invalid Tokens{RESET}")
        print(f"{PURPLE}3. Back to Main Menu{RESET}")
        
        choice = input(f"\n{BRIGHT_PURPLE}Choice: {RESET}")
        
        if choice == "1":
            self.remove_token()
        elif choice == "2":
            for token in invalid_tokens:
                if token in self.tokens:
                    self.tokens.remove(token)
            self.save_tokens()
            print(f"{Fore.GREEN}[+] Removed {len(invalid_tokens)} invalid tokens.{RESET}")
            time.sleep(2)
        elif choice == "3":
            return
        else:
            print(f"{PURPLE}[!] Invalid choice.{RESET}")
            time.sleep(1)
    
    def check_token_validity(self, token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        
        try:
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            return r.status_code == 200
        except:
            return False
    
    def remove_token(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_logo()

        if not self.tokens:
            print(f"{PURPLE}[!] No tokens available to remove.")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        print(f"{PURPLE}Available tokens:{RESET}")
        for i, token in enumerate(self.tokens):
            masked_token = token[:10] + '*' * (len(token) - 15) + token[-5:]
            print(f"{PURPLE}{i+1}. {masked_token}{RESET}")

        choice = input(f"{PURPLE}Enter token number to remove (or 'all' to remove all): {RESET}")

        if choice.lower() == 'all':
            self.tokens = []
            self.save_tokens()
            print(f"{PURPLE}[+] All tokens removed successfully.")
        else:
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.tokens):
                    removed = self.tokens.pop(index)
                    self.save_tokens()
                    masked_token = removed[:10] + '*' * (len(removed) - 15) + removed[-5:]
                    print(f"{PURPLE}[+] Removed token: {masked_token}")
                else:
                    print(f"{PURPLE}[!] Invalid token number.")
            except ValueError:
                print(f"{PURPLE}[!] Please enter a valid number or 'all'.")

        input(f"{PURPLE}Press Enter to continue...{RESET}")

    def display_logo(self):
        logo = f"""
        {PURPLE}
  ________.__  ____  __         .__           ___________           .__          
 /  _____/|  |/_   |/  |_  ____ |  |__ ___  __\__    ___/___   ____ |  |   ______
/   \  ___|  | |   \   __\/ ___\|  |  \\  \/  / |    | /  _ \ /  _ \|  |  /  ___/
\    \_\  \  |_|   ||  | \  \___|   Y  \>    <  |    |(  <_> |  <_> )  |__\___ \ 
 \______  /____/___||__|  \___  >___|  /__/\_ \ |____| \____/ \____/|____/____  >
        \/                    \/     \/      \/                               \/          
         {PURPLE}               

{PURPLE}Discord Raider | Made by: Glitched Tools{RESET}
"""
        print(logo)

    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_logo()
        
        print(f"{PURPLE}Tokens: {len(self.tokens)}")
        print(f"{PURPLE}Add Token [AT]")

        menu = f"""
{PURPLE}Options:
{PURPLE}1. Raid Server
{PURPLE}2. Custom Status
{PURPLE}3. Onliner
{PURPLE}4. Nickname Changer
{PURPLE}0. Exit

{BRIGHT_PURPLE}Choice: {RESET}"""

        choice = input(menu).upper()

        if choice == "1":
            self.raid_server()
        elif choice == "2":
            self.custom_status()
        elif choice == "3":
            self.onliner()
        elif choice == "4":
            self.nickname_changer()
        elif choice == "AT":
            self.add_token()
        elif choice == "0":
            self.exit_program()
        else:
            print(f"{PURPLE}[!] Invalid choice. Please try again.{RESET}")
            time.sleep(2)

    def raid_server(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_logo()

        if not self.tokens:
            print(f"{PURPLE}[!] No tokens available. Please add tokens first.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        guild_id = input(f"{PURPLE}Enter server (guild) ID: {RESET}")
        channel_id = input(f"{PURPLE}Enter channel ID: {RESET}")
        message = input(f"{PURPLE}Enter message to spam: {RESET}")

        try:
            num_tokens = int(input(f"{PURPLE}Enter number of tokens to use (max {len(self.tokens)}): {RESET}"))
            if num_tokens > len(self.tokens):
                num_tokens = len(self.tokens)
                print(f"{PURPLE}[!] Using maximum available tokens: {num_tokens}{RESET}")

            num_threads = int(input(f"{PURPLE}Enter number of threads: {RESET}"))

            if num_threads < 1:
                num_threads = 1
                print(f"{PURPLE}[!] Using minimum thread count: 1{RESET}")

            message_count = int(input(f"{PURPLE}Enter number of messages per token: {RESET}"))

            if message_count < 1:
                message_count = 1
                print(f"{PURPLE}[!] Setting message count to 1{RESET}")
        except ValueError:
            print(f"{PURPLE}[!] Invalid input. Please enter numbers.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        selected_tokens = self.tokens[:num_tokens]

        total_messages_sent = 0
        total_errors = 0
        status_lock = threading.Lock()
        
        def raid_thread(token, thread_id):
            nonlocal total_messages_sent, total_errors
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }

            url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

            for i in range(message_count):
                payload = {'content': message}

                try:
                    r = requests.post(url, headers=headers, json=payload)
                    if r.status_code == 200 or r.status_code == 204:
                        with status_lock:
                            total_messages_sent += 1
                            print(f"\r{PURPLE}Messages sent successfully: {total_messages_sent}  |  Messages Failed to send: {total_errors}{RESET}", end="")
                    else:
                        with status_lock:
                            total_errors += 1
                            print(f"\r{PURPLE}Messages sent successfully: {total_messages_sent}  |  Messages Failed to send: {total_errors}{RESET}", end="")
                        if r.status_code == 429:
                            try:
                                retry_after = r.json().get('retry_after', 0.1)
                                time.sleep(min(retry_after, 0.5))
                            except:
                                time.sleep(0.1)
                except Exception as e:
                    with status_lock:
                        total_errors += 1
                        print(f"\r{PURPLE}Messages sent successfully: {total_messages_sent}  |  Messages Failed to send: {total_errors}{RESET}", end="")

        print(f"{BRIGHT_PURPLE}[+] Starting raid with {num_tokens} tokens and {num_threads} threads...{RESET}")

        threads = []
        thread_counter = 0

        for token in selected_tokens:
            for _ in range(num_threads):
                thread_counter += 1
                t = threading.Thread(target=raid_thread, args=(token, thread_counter))
                threads.append(t)
                t.start()

        for t in threads:
            t.join()
            
        print()
        print(f"{BRIGHT_PURPLE}[+] Raid completed!{RESET}")
        print(f"{PURPLE}Messages sent successfully: {total_messages_sent}  |  Messages Failed to send: {total_errors}{RESET}")
        input(f"{PURPLE}Press Enter to continue...{RESET}")

    def custom_status(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_logo()

        if not self.tokens:
            print(f"{PURPLE}[!] No tokens available. Please add tokens first.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        status_text = input(f"{PURPLE}Enter custom status text: {RESET}")

        if not status_text:
            print(f"{PURPLE}[!] No status text provided.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        try:
            num_tokens = int(input(f"{PURPLE}Enter number of tokens to use (max {len(self.tokens)}): {RESET}"))
            if num_tokens > len(self.tokens):
                num_tokens = len(self.tokens)
                print(f"{PURPLE}[!] Using maximum available tokens: {num_tokens}{RESET}")
        except ValueError:
            print(f"{PURPLE}[!] Invalid input. Please enter a number.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        selected_tokens = self.tokens[:num_tokens]

        print(f"{BRIGHT_PURPLE}[+] Setting custom status for {num_tokens} tokens...{RESET}")

        def set_status(token, index):
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }

            url = 'https://discord.com/api/v9/users/@me/settings'

            payload = {
                'custom_status': {
                    'text': status_text
                }
            }

            try:
                r = requests.patch(url, headers=headers, json=payload)
                if r.status_code == 200:
                    print(f"{PURPLE}[+] Status set successfully!{RESET}")
                else:
                    print(f"{PURPLE}[!] Failed to set status. Status: {r.status_code}{RESET}")
            except Exception as e:
                print(f"{PURPLE}[!] Error: {str(e)}{RESET}")

        threads = []
        for i, token in enumerate(selected_tokens):
            t = threading.Thread(target=set_status, args=(token, i))
            threads.append(t)
            t.start()
            time.sleep(0.2)

        for t in threads:
            t.join()

        print(f"{BRIGHT_PURPLE}[+] Custom status operation completed!{RESET}")
        input(f"{PURPLE}Press Enter to continue...{RESET}")

    def onliner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_logo()

        if not self.tokens:
            print(f"{PURPLE}[!] No tokens available. Please add tokens first.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        try:
            num_tokens = int(input(f"{PURPLE}Enter number of tokens to use (max {len(self.tokens)}): {RESET}"))
            if num_tokens > len(self.tokens):
                num_tokens = len(self.tokens)
                print(f"{PURPLE}[!] Using maximum available tokens: {num_tokens}{RESET}")
        except ValueError:
            print(f"{PURPLE}[!] Invalid input. Please enter a number.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        selected_tokens = self.tokens[:num_tokens]
        
        print(f"{BRIGHT_PURPLE}[+] Setting {num_tokens} tokens online...{RESET}")
        online_count = 0

        def set_online(token):
            nonlocal online_count
            try:
                ws_url = "wss://gateway.discord.gg/?v=9&encoding=json"
                ws_headers = {
                    'Origin': 'https://discord.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
                }
                
                session_id = ''.join(random.choice('0123456789abcdef') for _ in range(32))
                payload = {
                    'op': 2,
                    'd': {
                        'token': token,
                        'properties': {
                            'os': 'windows',
                            'browser': 'chrome',
                            'device': ''
                        },
                        'presence': {
                            'status': 'online',
                            'since': 0,
                            'activities': [],
                            'afk': False
                        }
                    }
                }
                
                try:
                    headers = {
                        'Authorization': token,
                        'Content-Type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
                    }
                    
                    r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
                    if r.status_code == 200:
                        online_count += 1
                        print(f"{PURPLE}[+] Token set to online. Token {online_count}/{len(selected_tokens)}{RESET}")
                    else:
                        print(f"{PURPLE}[!] Invalid token or token is locked.{RESET}")
                except Exception as e:
                    print(f"{PURPLE}[!] Error checking token: {str(e)}{RESET}")
            except Exception as e:
                print(f"{PURPLE}[!] Error: {str(e)}{RESET}")

        threads = []
        for token in selected_tokens:
            t = threading.Thread(target=set_online, args=(token,))
            threads.append(t)
            t.start()
            time.sleep(0.5)

        for t in threads:
            t.join()

        print(f"{BRIGHT_PURPLE}[+] Online operation completed! {online_count}/{len(selected_tokens)} tokens set to online.{RESET}")
        input(f"{PURPLE}Press Enter to continue...{RESET}")

    def nickname_changer(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_logo()

        if not self.tokens:
            print(f"{PURPLE}[!] No tokens available. Please add tokens first.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        guild_id = input(f"{PURPLE}Enter server (guild) ID: {RESET}")
        nickname = input(f"{PURPLE}Enter nickname to set: {RESET}")

        if not guild_id or not nickname:
            print(f"{PURPLE}[!] Server ID and nickname are required.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        try:
            num_tokens = int(input(f"{PURPLE}Enter number of tokens to use (max {len(self.tokens)}): {RESET}"))
            if num_tokens > len(self.tokens):
                num_tokens = len(self.tokens)
                print(f"{PURPLE}[!] Using maximum available tokens: {num_tokens}{RESET}")
        except ValueError:
            print(f"{PURPLE}[!] Invalid input. Please enter a number.{RESET}")
            input(f"{PURPLE}Press Enter to continue...{RESET}")
            return

        selected_tokens = self.tokens[:num_tokens]
        
        print(f"{BRIGHT_PURPLE}[+] Setting nickname for {num_tokens} tokens...{RESET}")
        success_count = 0

        def change_nickname(token):
            nonlocal success_count
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
            }

            url = f'https://discord.com/api/v9/guilds/{guild_id}/members/@me'
            payload = {'nick': nickname}

            try:
                r = requests.patch(url, headers=headers, json=payload)
                if r.status_code == 200 or r.status_code == 204:
                    success_count += 1
                    print(f"{PURPLE}[+] Nickname changed successfully! {success_count}/{len(selected_tokens)}{RESET}")
                else:
                    print(f"{PURPLE}[!] Failed to change nickname. Status: {r.status_code}{RESET}")
            except Exception as e:
                print(f"{PURPLE}[!] Error: {str(e)}{RESET}")

        threads = []
        for token in selected_tokens:
            t = threading.Thread(target=change_nickname, args=(token,))
            threads.append(t)
            t.start()
            time.sleep(0.5)

        for t in threads:
            t.join()

        print(f"{BRIGHT_PURPLE}[+] Nickname change operation completed! {success_count}/{len(selected_tokens)} nicknames changed.{RESET}")
        input(f"{PURPLE}Press Enter to continue...{RESET}")

    def exit_program(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{BRIGHT_PURPLE}Thanks for using Discord Raider!")
        exit()

def main():
    raider = DiscordRaider()
    while True:
        raider.display_menu()

if __name__ == "__main__":
    main()
