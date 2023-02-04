"""모든 설정값은 이곳에서 수정되고 참조되어야합니다."""

from discord import Intents

class Config:
    token: str = "token" # 봇의 토큰
    guild_id: int = 0 # 길드 아이디
    prefix: str = "!" # 봇의 접두사

    def intents() -> Intents:
        """봇의 권한을 반환합니다."""
        return Intents.all()
