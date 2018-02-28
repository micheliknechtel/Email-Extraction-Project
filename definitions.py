
patternUrl      = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
patternSender   = 'From: \"([^\"]*)\"'
patternReceiver = 'To: \"([^\"]*)\"'
patternEmail    = r'[\w\.-]+@[\w\.-]+'
    
FROM = "From: "
TO   = "To: "
    
sender   = []
receiver = []
email    = []
urls     = []
