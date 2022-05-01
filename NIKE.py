import os

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("NIKE").keyx()
       __import__("NIKE").login()
   except Exception as a:
       exit(str(a))
