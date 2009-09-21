

import Tkinter as Tk


def get_root():
    root = Tk.Tk()
    root.bind('<Key>',handle_keys)
    b1 = Tk.Button(root)
    b1['text'] = 'toggle'
    b1['command'] = toggle_fs
    b1.pack({"side": "left"})

    return root

def handle_keys(ev):
    
    key = ev.keysym.lower()

    if key == 'tab':
        toggle_fs_req()
    if key == 'q':
        root.quit()
    if key == 'escape':
        root.quit()



def toggle_fs_req():

    global toggle_fs_requested

    toggle_fs_requested = True
    root.quit()

    




fs = 0
toggle_fs_requested = False

def toggle_fs():

    global fs

    if fs:

        fs = 0
        root.wm_state( 'normal' )
        root.grab_release()
        root.geometry("%dx%d+0+0" % (400,300))
        root.wm_overrideredirect(0)

    else:
        fs = 1
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()

        root.wm_overrideredirect( 1 )
        root.wm_geometry("%dx%d+0+0" % (w, h))

        #root.grab_set_global()
        root.focus_set()
        root.tkraise()
        


#toggle_fs()

while (1==1):
    root.mainloop()
    if not toggle_fs_requested:
        break
    else:
        toggle_fs_requested = False
        toggle_fs()
