# Dict for various Partner Configurations
PARTNER_CONFIG = {
    "ACME": {
        "partner_code": "ACME",
        "delimiter": "|",
        "columns": {
            "MBI": "external_id",
            "FNAME": "first_name",
            "LNAME": "last_name",
            "DOB": "dob",
            "EMAIL": "email",
            "PHONE": "phone"
        },
        "dob_format": "%m/%d/%Y"
    },
    "BETTERCARE": {
        "partner_code": "BETTERCARE",
        "delimiter": ",",
        "columns": {
            "subscriber_id": "external_id",
            "first_name": "first_name",
            "last_name": "last_name",
            "date_of_birth": "dob",
            "email": "email",
            "phone": "phone"
        },
        "dob_format": "%d-%m-%Y"
        
    }
}
