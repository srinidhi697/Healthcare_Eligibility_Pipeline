import pandas as pd
from datetime import datetime
import re
from config import PARTNER_CONFIG

# Checking the phone number format
def format_phone(phone):
    digits = re.sub(r"\D", "", str(phone))
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    return None

# processing the src file based on the partner config
def process_file(file_path, partner_key):
    config = PARTNER_CONFIG[partner_key]

    df = pd.read_csv(
        file_path,
        delimiter=config["delimiter"]
    )

    # Rename columns to standard schema
    df = df.rename(columns = config["columns"])

    # Required field validation
    df = df[df["external_id"].notna()]

    # Transformations as stated in the project requirements
    df["first_name"] = df["first_name"].str.title()
    df["last_name"] = df["last_name"].str.title()
    df["email"] = df["email"].str.lower()
    df["dob"] = pd.to_datetime(
        df["dob"],
        format=config["dob_format"],
        errors="coerce"
    ).dt.strftime("%Y-%m-%d")

    df["phone"] = df["phone"].apply(format_phone)
    df["partner_code"] = config["partner_code"]

    return df[
        ["external_id", "first_name", "last_name", "dob", "email", "phone", "partner_code"]
    ]