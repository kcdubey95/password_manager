from tkinter import *
from tkinter import messagebox
window = Tk()


def save():
    file = open("password.txt", "a")
    web = website_name.get()
    emaildata = emailid.get()
    passw = pass_word.get()
    if len(web)==0 or len( passw):
        messagebox.askokcancel(title='Please Fill the data', message='Fild is blank')
    else:
        is_ok=messagebox.askokcancel(title=web, message=f" website{web}\n password {passw}\n emailid {emaildata}")
        if is_ok:
           l = f"{web}|{emaildata}|{passw}\n"
           file.write(l)
           file.close()


def generatepass():
    import random
    import array

    # maximum length of password needed
    # this can be changed to suit your password length
    MAX_LEN = 12

    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but
    # we want a 12-character password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined
    # list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # traverse the temporary password array and append the chars
    # to form the password
    password = ""
    for x in temp_pass_list:
        password = password + x

    # print out password
    pass_word.delete(0, END)
    pass_word.insert(0, password)

window.title('Password Manger')
window.config(padx=20, pady=20)
canvas = Canvas(height=200, width=200)
myimg = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=myimg)
canvas.grid(column=1, row=0)
# lable
websitname = Label(text="Website Name")
email = Label(text="Email id")
password = Label(text="Password")
websitname.grid(column=0, row=1)
email.grid(column=0, row=2)
password.grid(column=0, row=3)
# input box
website_name = Entry(width=35)
website_name.focus()
website_name.grid(column=1, row=1)
emailid = Entry(width=35)
emailid.grid(column=1, row=2)
emailid.insert(0, 'Kc@kc.com')
pass_word = Entry(width=21)
pass_word.grid(column=1, row=3, columnspan=2)

# button
genpass = Button(text="Generate", width=15, command=generatepass)
genpass.grid(row=3, column=3)

add = Button(text="Save", width=25, command=save)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()
