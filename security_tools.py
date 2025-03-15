# tools/security_tools.py
import hashlib
import secrets
import string
from typing import Dict
from typing import Dict, Any

class SecurityTools:
    @staticmethod
    def generate_password(length: int = 16, special_chars: bool = True) -> str:
        """生成随机密码"""
        chars = string.ascii_letters + string.digits
        if special_chars:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        return ''.join(secrets.choice(chars) for _ in range(length))

    @staticmethod
    def password_strength(password: str) -> Dict[str, Any]:
        """检查密码强度"""
        strength = {
            'length': len(password) >= 12,
            'lowercase': any(c.islower() for c in password),
            'uppercase': any(c.isupper() for c in password),
            'digit': any(c.isdigit() for c in password),
            'special': any(c in string.punctuation for c in password)
        }
        score = sum(strength.values())
        return {
            'score': score,
            'strength': '弱' if score < 3 else '中' if score == 3 else '强',
            'details': strength
        }

    @staticmethod
    def file_hash(file_path: str, algorithm: str = 'sha256') -> str:
        """计算文件哈希值"""
        hasher = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()