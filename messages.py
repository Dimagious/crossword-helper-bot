# coding=utf-8
# messages to parser.py
STATUS_CODE_ERROR = 'Ошибка, Код ответа: %s'
SUCCESS_CONNECTION = 'Удалось подключиться к сайту'
FAILED_CONNECTION = 'Не удалось подключиться к сайту'
NO_INPUT = 'Пользователь не ввел слово'
INPUT_PLEASE = 'Введите шаблон для поиска'
SEARCHING_BY_DESCRIPTION = 'Выполняется поиск по описанию'
SEARCHING_BY_MASK = 'Выполняется поиск по маске'
NO_RESULT_AFTER_SEARCH = 'К сожалению, я не знаю что это.\n' \
                         'Попробуй проверить правильность написания, либо давай помогу с другим вопросом'

# messages to bot.py
BY_MASK = 'По маске'
BY_DESCRIPTION = 'По описанию'
MASK_EXAMPLE = 'Введи слово, в котором пропущенные буквы замени на \'*\'.\n' \
               'Пример: п*ивет'
DESCRIPTION_EXAMPLE = 'Введи задание из кроссворда или его часть.\n' \
                      'Пример: рассказ Набокова'
CHOOSE = 'Пожалуйста, выбери как будем искать слово'
IF_NOTHING_CHOSEN = 'Меня создавали исключительно для помощи в поиске слов.\n' \
                    'Поэтому нажми /start и выбери как будем искать слово'
TRY_AGAIN = 'Если буду нужен ещё жми /start'
BYE = 'Был рад помочь! Всегда к твоим услугам по команде /start'
ERROR_LOGGING = 'Update "%s" caused error "%s"'
LOGGING = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
HELP = 'Привет! Я могу помочь тебе найти практически любое слово.\n' \
       'Нажми /start, чтобы я приступил к работе' \
