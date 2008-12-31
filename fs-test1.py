import Tkinter as Tk

root = Tk.Tk()

def onevent(ev):
    print 'b:',ev.type,ev.num

def onwheel(ev):
    print 'w:',ev.type,ev.num


def keyhandler(ev):
    print 'k:',ev.type,ev.keysym,ev.num,ev.keycode

def anyhandler(ev):
    print 'a:',ev.type,ev.keysym,ev.num



def quithandler(ev):
    root.quit()

#root.bind("<Any-KeyRelease>",anyhandler)
root.bind("<Button>",onevent)
root.bind("<MouseWheel>",onwheel)
root.bind("<Key>",keyhandler)
root.bind('q',quithandler)

root.mainloop()
