# Публикация langchain-xbaza на PyPI

## Подготовка

1. **Установить необходимые инструменты:**
```bash
pip install build twine
```

2. **Создать аккаунт на PyPI:**
   - Перейти на https://pypi.org/account/register/
   - Создать аккаунт
   - Сохранить credentials

3. **Создать аккаунт на TestPyPI (для тестирования):**
   - Перейти на https://test.pypi.org/account/register/
   - Создать аккаунт

## Сборка пакета

```bash
# Перейти в директорию пакета
cd langchain_xbaza

# Собрать пакет
python -m build

# Проверить пакет
twine check dist/*
```

## Тестовая публикация (TestPyPI)

```bash
# Загрузить на TestPyPI
twine upload --repository testpypi dist/*

# Установить с TestPyPI для проверки
pip install --index-url https://test.pypi.org/simple/ langchain-xbaza
```

## Официальная публикация

```bash
# Загрузить на PyPI
twine upload dist/*

# Установить пакет
pip install langchain-xbaza
```

## Обновление версии

1. Обновить версию в `pyproject.toml` и `__init__.py`
2. Обновить CHANGELOG.md
3. Собрать и опубликовать новую версию

## Проверка после публикации

```bash
# Установить пакет
pip install langchain-xbaza

# Проверить импорт
python -c "from langchain_xbaza import XbazaJobsTool; print('OK')"
```

## Полезные ссылки

- [PyPI](https://pypi.org/)
- [TestPyPI](https://test.pypi.org/)
- [Python Packaging Guide](https://packaging.python.org/)

