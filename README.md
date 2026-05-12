# 🎹 Sky Piano Autoclicker

**Автоматический проигрыватель песен для Sky: Children of the Light**

[![GitHub license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Python-3.9+-yellow)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Arch-blue)](https://archlinux.org)

---

## ❄️ Описание

Этот скрипт читает ноты из файлов `.txt` или `.json` (любого формата из Sky: Children of the Light) и автоматически играет их в игре через эмуляцию клавиатуры.

**Особенности:**
- 🎵 Поддержка всех форматов песен Sky (`songNotes`, `notes`, `columns+breakpoints`)
- 🖥️ Работает на **Wayland** (Hyprland) и X11
- 📊 Живой прогресс-бар и анимированный таймер
- 🎨 Красивый терминальный интерфейс с цветами
- 🐙 Встроенная реклама проектов `web-pentest`

---
## 📦 Установка

```bash
git clone https://github.com/web-pentest/sky-piano-autoclicker.git
cd sky-piano-autoclicker
chmod +x clicker.py
```
### Зависимости (Arch Linux)

```bash
sudo pacman -S python xdotool
pip install --break-system-packages pynput
```
### Зависимости (Debian/Ubuntu)

```bash
sudo apt install python3 python3-pip xdotool
pip install pynput
```
## 🎮 Как использовать

1. Положи файлы с песнями в папку `songs/`
2. Запусти скрипт:
   ```bash
   python3 clicker.py
   ```
3. Выбери песню из списка
4. Переключись в окно игры Sky
5. Слушай музыку!

---
## 🗂️ Формат файлов

**Текстовый файл (`.txt`)** — каждая строка: название ноты
**JSON файл (`.json`)** — любой формат Sky (`songNotes`, `notes`, `columns+breakpoints`)

---
## 🛠️ Раскладка клавиш

| Нота | Клавиша |
|------|---------|
| 1Key0 | y |
| 1Key1 | u |
| 1Key2 | i |
| 1Key3 | o |
| 1Key4 | p |
| 1Key5 | h |
| 1Key6 | j |
| 1Key7 | k |
| 1Key8 | l |
| 1Key9 | b |
| 1Key10 | c |
| 1Key11 | m |
| 1Key12 | t |
| 1Key13 | r |
| 1Key14 | n |

---
## 🐙 Автор

**web-pentest** — [GitHub](https://github.com/web-pentest)

## 📜 Лицензия

MIT — свободно используй и модифицируй.

---

⭐ Поставь звезду, если проект полезен!
