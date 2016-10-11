
queue = []
def enQ():
    queue.append(input("enter new string:").strip())
def deQ():
    if len(queue) == 0:
        print("empty queue\n")
    else:
        print('Removed![',repr(queue.pop()),']')
def viewQ():
    print(queue)

CMDS = {'e': enQ,'d':deQ,'v':viewQ}
def showmenu():
    pr="""
(E)nqueue
(D)enqueue
(V)iew
(Q)uit

 enter choice: """
    while True:
        while True:
            try:
                 choice = input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterpt,IndexError):
                 choice = "q"
            print("\nYou picked:[%s]" % choice)
            if choice not in "devq":
                 print("error,try again")
            else:
                 break
            if choice == "q":
                 break
        CMDS[choice]()
if __name__ == '__main__':
        showmenu()
                 
