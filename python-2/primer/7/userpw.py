db = {}

def newuser():
    prompt = "login desired:"
    while True:
        name = input(prompt)
        if name in db:
            prompt = "name taken,try again: "
            continue
        else:
            break
    pwd = input("passwd:")
    db[name]= pwd 
    print("regeisted oK!\n")

def olduser():
    name = input("login:")
    pwd = input("passwd:")
    passwd = db.get(name)
    if passwd == pwd:
        print("welcome back," ,name)
    else:
        print("login incorrect")

def showmenu():
    prompt = """
  (n) new user login
  (l) exiting user login
  (q) quit
   enter choice : """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError,KeyboardInterrupt):
                choice = "q"
            print("\n you picked [%s]" % choice)
            if choice not in "nlq":
                print("invalid option, try again")
            else:
                chosen = True

        if choice == "q": done = True
        if choice == "n": newuser()
        if choice == "l": olduser()

if __name__ == "__main__":
    showmenu()
    

