class Contact:
    """
    Represents a single CRM contact.
    This is our OOP class — every contact is an object with these attributes.
    """

    def __init__(self, name, email, phone, company):
        self.name = name
        self.email = email
        self.phone = phone
        self.company = company

    def __str__(self):
        return (
            f"Name    : {self.name}\n"
            f"Email   : {self.email}\n"
            f"Phone   : {self.phone}\n"
            f"Company : {self.company}"
        )
