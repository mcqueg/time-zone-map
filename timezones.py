# Creator: Garrett McCue
# Filename:  timezones.py

from tkinter import *
from datetime import datetime
import pytz

### main():
window = Tk()
window.title("America's Big Ole Clock")

# add map image
background_image = PhotoImage(file='map.gif')
Label(window, image=background_image).grid(row=0, column=0, sticky=E)

# initiate label for the date and place it in the right spot
date_lbl = Label(window, font=('calibri', 30, 'bold'))
date_lbl.place(x=50, y=450)

# initiate and place labels(time) for all timezones
# EST
est_lbl = Label(window, font=('calibri', 20, 'bold'))
est_lbl.place(x=600, y=50)
# CST
cst_lbl = Label(window, font=('calibri', 20, 'bold'))
cst_lbl.place(x=450, y=475)
# MST
mst_lbl = Label(window, font=('calibri', 20, 'bold'))
mst_lbl.place(x=180, y=25)
# PST
pst_lbl = Label(window, font=('calibri', 20, 'bold'))
pst_lbl.place(x=0, y=390)

# get date and current time for each timezone called every second
def date_time():
    # gets date
    date_str = datetime.today().strftime("%B %d, %Y")
    date_lbl.config(text=date_str)

    # get timezones
    # EST
    time_est = datetime.now(pytz.timezone('America/New_York'))
    est_lbl.config(text='{}'.format(time_est.strftime("%I:%M:%S %p EST")))
    # CST
    time_cst = datetime.now(pytz.timezone('America/Chicago'))
    cst_lbl.config(text='{}'.format(time_cst.strftime("%I:%M:%S %p CST")))
    # MST
    time_mst = datetime.now(pytz.timezone('America/Denver'))
    mst_lbl.config(text='{}'.format(time_mst.strftime("%I:%M:%S %p MST")))
    # PST
    time_pst = datetime.now(pytz.timezone('America/Los_Angeles'))
    pst_lbl.config(text='{}'.format(time_pst.strftime("%I:%M:%S %p PST")))

    # recalls the date_time every second to update time
    pst_lbl.after(1000, date_time)


# call date()/time() to write to screen
# updates both every minute
date_time()

## run main loop
mainloop()
