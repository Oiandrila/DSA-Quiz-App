from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root=Tk()
root.title("DSA")
root.iconbitmap('test.ico')
root.attributes('-fullscreen',True)

frame = LabelFrame(root,padx=50,pady=50)
frame.pack(padx=100,pady=100)

my_label0 = Label(frame,text='Click "Start" to start the test')
my_label0.pack()

answers=[]
correct_ans=['O(log n)','Stack','Merge Sort','O(n²)','Heap']
score = 0

#QUES 1
def start():
    root.withdraw()   # .destroy() WILL COMPLETELY KILL THE APP, RATHER USE .withdraw() to hide and .deiconify() to get back to the prev window
    top1 = Toplevel()
    top1.title("Question 1")
    frame1 = LabelFrame(top1, padx=50, pady=50)
    frame1.grid(row=0,column=0,padx=10, pady=10)
    my_label1 = Label(frame1, text='1. What is the time complexity of searching an element in a balanced binary search tree (BST)?')
    my_label1.pack()
    Options=[
        #("text","mode")
        ("","dummy"),
        ("O(n)","O(n)"),
        ("O(log n)","O(log n)"),
        (" O(n log n)"," O(n log n)"),
        ("O(1)","O(1)")
    ]
    select1 = StringVar()
    select1.set("dummy")
    for text, mode in Options:
        if mode != "dummy":
            Radiobutton(frame1,text=text,variable=select1,value=mode).pack(anchor=W)


    #QUES 2
    def save1():
        if len(answers)>0:
            answers[0]=select1.get()
        else:
            answers.append(select1.get())
        top1.withdraw()  # .destroy() WILL COMPLETELY KILL THE APP, RATHER USE .withdraw() to hide and .deiconify() to get back to the prev window
        top2 = Toplevel()
        top2.title("Question 2")
        frame2 = LabelFrame(top2, padx=50, pady=50)
        frame2.grid(row=0, column=0, padx=10, pady=10)
        my_label2 = Label(frame2,text='2. Which data structure is used for implementing recursion?')
        my_label2.pack()
        Options = [
            # ("text","mode")
            ("", "dummy"),
            ("Queue", "Queue"),
            ("Stack", "Stack"),
            ("Linked List", " Linked List"),
            ("Tree", "Tree")
        ]
        select2 = StringVar()
        select2.set("dummy")
        for text, mode in Options:
            if mode != "dummy":
                Radiobutton(frame2, text=text, variable=select2, value=mode).pack(anchor=W)


        # QUES 3
        def save2():
            if len(answers) > 1:
                answers[1] = select2.get()
            else:
                answers.append(select2.get())
            top2.withdraw()  # .destroy() WILL COMPLETELY KILL THE APP, RATHER USE .withdraw() to hide and .deiconify() to get back to the prev window
            top3 = Toplevel()
            top3.title("Question 3")
            frame3 = LabelFrame(top3, padx=50, pady=50)
            frame3.grid(row=0, column=0, padx=10, pady=10)
            my_label3 = Label(frame3, text='Which of the following sorting algorithms has the best average-case time complexity?')
            my_label3.pack()
            Options = [
                # ("text","mode")
                ("", "dummy"),
                ("Bubble Sort", "Bubble Sort"),
                ("Merge Sort", "Merge Sort"),
                ("Selection Sort", "Selection Sort"),
                ("Insertion Sort", "Insertion Sort")
            ]
            select3 = StringVar()
            select3.set("dummy")
            for text, mode in Options:
                if mode != "dummy":
                    Radiobutton(frame3, text=text, variable=select3, value=mode).pack(anchor=W)


            #Ques 4
            def save3():
                if len(answers) > 2:
                    answers[2] = select3.get()
                else:
                    answers.append(select3.get())
                top3.withdraw()  # .destroy() WILL COMPLETELY KILL THE APP, RATHER USE .withdraw() to hide and .deiconify() to get back to the prev window
                top4 = Toplevel()
                top4.title("Question 4")
                frame4 = LabelFrame(top4, padx=50, pady=50)
                frame4.grid(row=0, column=0, padx=10, pady=10)
                my_label4 = Label(frame4,text='4. What is the worst-case time complexity of Quick Sort?')
                my_label4.pack()
                Options = [
                    # ("text","mode")
                    ("", "dummy"),
                    ("O (n log n)", "O (n log n)"),
                    ("O(n²)", "O(n²)"),
                    ("O(log n)", "O(log n)"),
                    ("O(n)", "O(n)")
                ]
                select4 = StringVar()
                select4.set("dummy")
                for text, mode in Options:
                    if mode != "dummy":
                        Radiobutton(frame4, text=text, variable=select4, value=mode).pack(anchor=W)


                #QUES 5
                def save4():
                    if len(answers) > 3:
                        answers[3] = select4.get()
                    else:
                        answers.append(select4.get())
                    top4.withdraw()  # .destroy() WILL COMPLETELY KILL THE APP, RATHER USE .withdraw() to hide and .deiconify() to get back to the prev window
                    top5 = Toplevel()
                    top5.title("Question 5")
                    frame5 = LabelFrame(top5, padx=50, pady=50)
                    frame5.grid(row=0, column=0, padx=10, pady=10)
                    my_label5 = Label(frame5, text='5. Which data structure is best suited for implementing a priority queue?')
                    my_label5.pack()
                    Options = [
                        # ("text","mode")
                        ("", "dummy"),
                        ("Stack", "Stack"),
                        ("Queue", "Queue"),
                        ("Heap", "Heap"),
                        ("Hash Table", "Hash Table")
                    ]
                    select5 = StringVar()
                    select5.set("dummy")
                    for text, mode in Options:
                        if mode != "dummy":
                            Radiobutton(frame5, text=text, variable=select5, value=mode).pack(anchor=W)
                    def submit():
                        if len(answers) > 4:
                            answers[4] = select5.get()
                        else:
                            answers.append(select5.get())  #  Store last answer

                        #  CALCULATE SCORE
                        score = 0
                        for i in range(len(correct_ans)):
                            if i < len(answers) and answers[i] == correct_ans[i]:
                                score += 1

                        #  SHOW FINAL SCORE
                        messagebox.showinfo("Score", f"You scored {score} out of {len(correct_ans)}")
                        root.destroy()
                    def back5():
                        top4.deiconify()
                        top5.withdraw()
                    submit_btn = Button(top5, text="Submit", command=submit).grid(row=1, column=3)
                    back_btn = Button(top5, text="Back", command=back5).grid(row=1, column=1)

                def back4():
                    top3.deiconify()
                    top4.withdraw()

                save_btn = Button(top4, text="Save & Next", command=save4).grid(row=1, column=3)
                back_btn = Button(top4, text="Back", command=back4).grid(row=1, column=1)

            def back3():
                top2.deiconify()
                top3.withdraw()

            save_btn = Button(top3, text="Save & Next", command=save3).grid(row=1, column=3)
            back_btn = Button(top3, text="Back", command=back3).grid(row=1, column=1)

        def back2():
            top1.deiconify()
            top2.withdraw()

        save_btn = Button(top2, text="Save & Next", command=save2).grid(row=1, column=3)
        back_btn = Button(top2, text="Back", command=back2).grid(row=1, column=1)
    #1st screen back disabled
    save_btn = Button(top1,text="Save & Next",command=save1).grid(row=1,column=3)
    back_btn = Button(top1, text="Back", state=DISABLED).grid(row=1, column=1)

myButton = Button(frame,text="Start",command=start)
myButton.pack()
root.mainloop()