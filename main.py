import os
Is_Finished = False

while not Is_Finished:
    File_Name = input("")
    x = File_Name.split() #String split by spacebar.
    # print(len(x))
    #print(x[-1]) #prints the value of the last element in the array
    if len(x) > 0:
        if x[0] == "cat":
            if x[-2] == ">":
                with open(x[-1], "w") as Test_Write:

                    Selected_Files = []
                    nothingness = []
                    for i in range(len(x)):
                        if i == 0 or i == len(x)-2 or i == len(x)-1:
                            nothingness.append(x[i])
                        else:
                            Selected_Files.append(x[i])

                    Final_Text = ""

                    for y in Selected_Files:
                        if os.path.exists(y):
                            with open(y, "r") as file_A:
                                file_A_contents = file_A.read()
                                Final_Text = file_A_contents

                            Final_Text += "\n"
                            print("The following text has been added to your text file named " + File_Name + ": \n" + Final_Text)
                            Test_Write.write(Final_Text)
                            Is_Finished = True

                        else:
                            print("One of the files you entered does not exist.")
                            Go = input("Try again? [Press Y to try again]")
                            if Go != "Y":
                                Is_Finished = True

            if len(x) == 2:
                if os.path.exists(x[1]):
                    with open(x[1], "r") as file_Read:
                        file_Read_contents = file_Read.read()
                        Final_Text = file_Read_contents
                    print(Final_Text)
                    Is_Finished = True
                else:
                    print("File does not exist.")
                    Go = input("Try again? [Press Y to try again]")
                    if Go != "Y":
                        Is_Finished = True
        else:
            print("Syntax Error")
            Is_Finished = True

    else:
        print("Syntax Error")
        Is_Finished = True
