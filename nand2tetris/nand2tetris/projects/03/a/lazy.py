from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
clip_msg = ''
for i in range(16):
    clip_msg += (f'DMux8Way(in=in[{i}], sel=sel, a=a[{i}], b=b[{i}], c=c[{i}], d=d[{i}], e=e[{i}], f=f[{i}], g=g[{i}], h=h[{i}]);\n')
r.clipboard_append(clip_msg)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()
print(clip_msg)