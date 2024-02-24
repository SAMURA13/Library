from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Определение атрибутов настроек для подключения к базе данных
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

# Определение свойства для формирования URL для подключения к базе данных с использованием asyncpg(Асинхр)
    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
# Определение свойства для формирования URL для подключения к базе данных с использованием psycop(Синхр)
    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    # Инициализация настроек из файла .env
    model_config = SettingsConfigDict(env_file=".env")
    
# Создание экземпляра класса настроек
settings = Settings()