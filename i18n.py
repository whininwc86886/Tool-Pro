import json
import os
from typing import Dict

class I18N:
    def __init__(self):
        self.locale_data = {}
        self.current_lang = 'zh_CN'

    def load_language(self, lang: str):
        lang_file = os.path.join('languages', f'{lang}.json')
        try:
            with open(lang_file, 'r', encoding='utf-8') as f:
                self.locale_data = json.load(f)
                self.current_lang = lang
        except FileNotFoundError:
            self.locale_data = {}

    def translate(self, key: str) -> str:
        return self.locale_data.get(key, key)

# 创建全局实例
i18n = I18N()

# 简化调用方式
def _(key: str) -> str:
    return i18n.translate(key)