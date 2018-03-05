#  Utilities.py
#  python
#
#  Created by Micheli Knechtel on 05/03/2018.
#  Copyright © 2018 Micheli Knechtel. All rights reserved.
# 
#   1) Description: class Pattern() 
#   Holds the regular expression patterns 
# 
#   2) Description: class Definition() 
#   Holds hard code values 

class Pattern():
    Url      = 'http[s]?://(?:[[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    Sender   = 'From: \"([^\"]*)\"'
    Receiver = 'To: \"([^\"]*)\"'
    Email    = r'[\w\.-]+@[\w\.-]+'
    Name     = '"([^"]*)"'

class Definition():
    FROM = "From: "
    TO   = "To: "




