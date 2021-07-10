from os import environ

from dotenv import load_dotenv


load_dotenv()


config = {
    'chart': {
        'url': environ.get('CHART_URL'),
        'start': int(environ.get('CHART_START')),
        'end': int(environ.get('CHART_END'))
    },
    'vk': {
        'user': environ.get('VK_USER'),
        'password': environ.get('VK_PASSWORD'),
        'playlist': environ.get('VK_PLAYLIST')
    }
}
