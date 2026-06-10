# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: HealthLog
def validate_required(value, field_name):
    if value is None or (isinstance(value, str) and not value.strip()):
        raise ValueError(f"Field '{field_name}' cannot be empty.")
    return True

def validate_identifier(identifier, prefix=""):
    if identifier is None:
        raise ValueError("Identifier cannot be None.")
    clean_id = str(identifier).strip()
    if not clean_id or len(clean_id) > 64:
        raise ValueError(f"Invalid identifier length or format for '{identifier}'.")
    if prefix and not clean_id.startswith(prefix):
        raise ValueError(f"Identifier must start with '{prefix}'.")
    return True

def validate_short_text(text, max_length=100, min_length=1):
    if text is None:
        raise ValueError("Text cannot be None.")
    clean_text = str(text).strip()
    if len(clean_text) < min_length or len(clean_text) > max_length:
        raise ValueError(f"Text length must be between {min_length} and {max_length}.")
    return True

def validate_positive_number(value, field_name):
    try:
        num = float(value)
        if num <= 0:
            raise ValueError(f"{field_name} must be a positive number.")
        return num
    except (ValueError, TypeError):
        raise ValueError(f"{field_name} must be a valid number.")

def validate_date(date_str, format="%Y-%m-%d"):
    if not date_str:
        raise ValueError("Date cannot be empty.")
    try:
        from datetime import datetime
        datetime.strptime(str(date_str).strip(), format)
        return True
    except ValueError:
        raise ValueError(f"Invalid date format. Expected: {format}")

def validate_email(email):
    if not email or "@" not in email or "." not in email:
        raise ValueError("Invalid email address.")
    local, domain = email.rsplit("@", 1)
    if len(local) > 64 or len(domain) > 255:
        raise ValueError("Email parts too long.")
    return True

def validate_phone(phone):
    if not phone:
        raise ValueError("Phone cannot be empty.")
    clean_phone = str(phone).replace("-", "").replace(" ", "").replace("+", "")
    if len(clean_phone) < 10 or len(clean_phone) > 15:
        raise ValueError("Invalid phone number length.")
    return True
