# this-catplanet-does-not-exist

Telegram-бот, генерирующий "кото-планеты": берёт изображение кота, оборачивает его на 3D-сферу (Mayavi/VTK) и отдаёт анимированный GIF вращающейся планеты.

## Структура проекта

```
bot.py                        # Точка входа — Telegram-бот (python-telegram-bot, async)
model/
  generator.py                # Генерация изображения (сейчас заглушка)
  smooth_borders.py           # Сглаживание границ изображения для бесшовной текстуры
  transform_to_planet.py      # Маппинг изображения на сферу + рендер GIF через ffmpeg
  train.py                    # Скрипт обучения GAN (PyTorch + absl-py flags)
  train.ipynb                 # Ноутбук с полным пайплайном обучения (JAX/Flax)
  train_config.json           # Конфигурация обучения
  weights/
    generator.pms             # Предобученные веса генератора
  input1.jpg, input2.jpg      # Примеры входных изображений
```

## Запуск

```bash
make install-dev   # установить зависимости (включая dev)
```

Для бота нужен файл `.env` с переменной `BOT_TOKEN`:
```
BOT_TOKEN=<telegram-bot-token>
```

```bash
python bot.py
```

## Make-команды

- `make install` — установить зависимости
- `make install-dev` — установить зависимости + dev (ruff)
- `make fmt` — форматирование кода (ruff format)
- `make lint` — проверка кода (ruff check)
- `make lint-fix` — проверка + автоисправление

## Команды бота

- `/start` — приветствие
- `/random_cat` — сгенерировать кото-планету

## Зависимости

Управляются через Poetry (`pyproject.toml`).

- **python-telegram-bot** >= 20.0 — async Telegram API
- **python-dotenv** — загрузка `.env`
- **PyTorch / torchvision** — нейросеть генератора
- **Mayavi / VTK** — 3D-рендеринг сферы
- **matplotlib, Pillow, numpy** — обработка изображений
- **ffmpeg** — системная зависимость для сборки GIF из кадров
- **ruff** (dev) — линтер и форматтер

## Соглашения

- Python 3.10+
- Код бота — async/await
- Линтинг и форматирование — ruff (конфигурация в `pyproject.toml`)
- Веса модели хранятся в `model/weights/`
- Генерируемые файлы (gif, mp4, tmp*) не коммитятся — см. `.gitignore`
