try:
    _secrets = __import__("/secrets")
except ImportError:
    _secrets = __import__("/system/secrets")

# Copy contents of secrets to module scope
for k, v in _secrets.__dict__.items():
    if not k.startswith("__"):
        locals()[k] = v

del _secrets, k, v
