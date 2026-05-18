#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║                     🎹 SKY PIANO AUTOCLICKER 🎹                  ║
║           Воспроизведение песен из файлов (JSON/TXT)            ║
╚══════════════════════════════════════════════════════════════════╝
"""

import time
import json
import os
import subprocess
import sys
import threading

# ==================== ТВОЯ РАСКЛАДКА (Sky) ====================
KEY_MAP = {
    "1Key0": "y", "1Key1": "u", "1Key2": "i", "1Key3": "o", "1Key4": "p",
    "1Key5": "h", "1Key6": "j", "1Key7": "k", "1Key8": "l", "1Key9": "b",
    "1Key10": "c", "1Key11": "m", "1Key12": "t", "1Key13": "r", "1Key14": "n"
}
# =============================================================

CYAN = '\033[96m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

def print_banner():
    os.system('clear')
    print(f"""
{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════════╗
║                     🎹 SKY PIANO AUTOCLICKER 🎹                  ║
║           Воспроизведение песен из файлов (JSON/TXT)            ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
    """)
    print(f"{BOLD}{MAGENTA}🐙 GitHub:{RESET} {CYAN}https://github.com/web-pentest{RESET}")
    print(f"{BOLD}{YELLOW}❄️  Проекты:{RESET} {GREEN}DarkVPN • TSandCode • PHPNoFluff • SNOWRECON{RESET}\n")

def print_progress_bar(current, total, bar_length=30):
    """Рисует красивый прогресс-бар"""
    percent = current / total
    filled = int(bar_length * percent)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f"\r{BOLD}{GREEN}[{bar}]{RESET} {BOLD}{GREEN}{int(percent * 100)}%{RESET} ({current}/{total})", end='', flush=True)

def send_key(key):
    subprocess.run(['xdotool', 'keydown', key])
    time.sleep(0.02)
    subprocess.run(['xdotool', 'keyup', key])

def find_notes(data):
    if isinstance(data, list):
        if any(isinstance(i, dict) and 'time' in i and 'key' in i for i in data):
            return data
        for item in data:
            res = find_notes(item)
            if res:
                return res
    elif isinstance(data, dict):
        for key in ['songNotes', 'notes', 'events', 'data']:
            if key in data and isinstance(data[key], list):
                notes = find_notes(data[key])
                if notes:
                    return notes
        for val in data.values():
            res = find_notes(val)
            if res:
                return res
    return None

def play_song(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
    except Exception as e:
        print(f"{RED}❌ Ошибка чтения файла {file_path}: {e}{RESET}")
        return

    notes = find_notes(raw_data)
    if not notes:
        print(f"{RED}❌ Не найдены ноты в файле {file_path}{RESET}")
        return

    total_notes = len(notes)
    total_time_ms = max((n.get('time', 0) for n in notes), default=0)
    total_seconds = total_time_ms / 1000.0

    print(f"\n{GREEN}🎵 Песня:{RESET} {YELLOW}{os.path.basename(file_path)}{RESET}")
    print(f"{GREEN}🎼 Нот:{RESET} {YELLOW}{total_notes}{RESET}")
    print(f"{GREEN}⏱️  Длительность:{RESET} {YELLOW}{total_seconds:.1f} сек{RESET}")
    print(f"{YELLOW}⏳ 5 секунд до старта...{RESET}")

    for i in range(5, 0, -1):
        print(f"\r   Старт через {i}... ", end='', flush=True)
        time.sleep(1)
    print(f"\r{GREEN}▶️ ИГРАЮ!{RESET} (жми Ctrl+C для остановки)\n")

    start_time = time.time()
    played_notes = 0

    def progress_updater():
        nonlocal played_notes
        while time.time() - start_time < total_seconds:
            elapsed = time.time() - start_time
            progress = min(elapsed / total_seconds, 1.0)
            print_progress_bar(progress, 1.0)
            time.sleep(0.2)
        print_progress_bar(1.0, 1.0)
        print()

    progress_thread = threading.Thread(target=progress_updater, daemon=True)
    progress_thread.start()

    try:
        for note in notes:
            if 'time' not in note:
                continue
            target_time = note['time'] / 1000.0
            while (time.time() - start_time) < target_time:
                time.sleep(0.001)
            key_val = str(note.get('key', ''))
            if not key_val.startswith('1Key') and key_val.isdigit():
                key_val = f"1Key{key_val}"
            key = KEY_MAP.get(key_val)
            if key:
                send_key(key)
            played_notes += 1
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}⏹ Воспроизведение остановлено пользователем.{RESET}")
        return

    print(f"\n{GREEN}✅ Воспроизведение завершено!{RESET}\n")

def main():
    while True:
        files = []
        for f in os.listdir('.'):
            if f.endswith(('.txt', '.json')):
                files.append(f)
        if os.path.isdir('songs'):
            for f in os.listdir('songs'):
                if f.endswith(('.txt', '.json')):
                    files.append(os.path.join('songs', f))

        if not files:
            print(f"{RED}❌ Нет .txt или .json файлов с песнями!{RESET}")
            break

        print(f"\n{BOLD}{CYAN}📁 Доступные песни:{RESET}")
        for i, filename in enumerate(files, 1):
            short = os.path.basename(filename)
            print(f"  {BOLD}{i}.{RESET} {short}")
        print(f"  {BOLD}{RED}0. Выход{RESET}")

        try:
            choice = input(f"\n{BOLD}{CYAN}🎤 Выбери номер: {RESET}")
            if choice == '0':
                print(f"\n{GREEN}❄️ Спасибо за использование! 🐙 github.com/web-pentest{RESET}\n")
                break

            idx = int(choice) - 1
            if 0 <= idx < len(files):
                play_song(files[idx])
            else:
                print(f"{RED}⚠️ Неверный номер.{RESET}")
        except ValueError:
            print(f"{RED}⚠️ Введи число.{RESET}")
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Выход.{RESET}")
            break

if __name__ == "__main__":
    print_banner()
    main()
