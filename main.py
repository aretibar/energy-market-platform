from src.config import load_settings

settings = load_settings()
print("Key loaded:", settings.eia_api_key is not None)
