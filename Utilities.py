class Pattern():
    Url      = 'http[s]?://(?:[[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    Sender   = 'From: \"([^\"]*)\"'
    Receiver = 'To: \"([^\"]*)\"'
    Email    = r'[\w\.-]+@[\w\.-]+'
    Name     = '"([^"]*)"'

class Definition():
    FROM = "From: "
    TO   = "To: "




