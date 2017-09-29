



def main():
    chart = readChart()
    chart = buySeat(chart)
    saveChart(chart)

def printChart(chart):
    mid = len(chart) * 3  # mid point for printing header
    print(" " * (mid-3), "Price chart")
    print(" ", mid , "column")
    
    print(" " * 3, end="")      #print column numbers
    for i in range(len(chart[0])) :
        print("%5d" % (i+1), end="")
    print()
    print("Row ", "=" * len(chart) * 6)
    
    for i in range(len(chart)): #print data
        print("%2d" %(i+1), "|", end="")
        for col in chart[i]:
            if col != 'X' and col != '-' :
                print("%5s" % ("$"+col), end="")    # %5s everything prints within 5 spaces. 
            else :
                print("%5s" % col, end="")
        print()
    print()
    
def readChart():
    chart = []
    fileReadSuccess = False #bc did not read file yet
    while not fileReadSuccess :
        fname = input("Enter file name of hit Enter for default lab5input.txt: ")
        if len(fname) == 0 : fname = DEFAULT_FILE
             ####short way of writing simple if
        try:
            with open (fname) as infile :   #### open can raise exception here
                row = infile.readline().rstrip().split()
                if len(row) == 0:
                    raise IOError ("Empty input file")  #### raising exception here
                while (len(row) != 0) :
                    chart.append(row)
                    row = infile.readline().rstrip().split()
                fileReadSuccess = True      #### stop loop
        except IOError as err:
            print(str(err))
            #### will either print "Empty  input file",
            #### or print "No such file or directory" from open()
    printChart(chart)
    return chart

def buySeat(chart):
    print("Available seats are shown with price")
    seatSold = []
    total = 0
    
    validSeats = False
    while not validSeats :
        try :       # get number of seats
            num = int(input("Number of seats: ")) # int can raise exception
            if num < 1 or num > len(chart) * len(chart[0] :
                raise valueError ("Not a valid number of seats")  ####raising exception
            validSeats = True
        except valueError as e :
            print(str(e))
    i = 1
    while(i <= num) :
        try : ####buy seats
            prompt = "Enter row, col for set " + str(i) + ": "
            (row,col) = [int(val) - 1 for val in input(prompt).split('.')]   ####exception here
        if chart[row][col] != '-' and chart[row][col] != 'X' :   #### exception here
            total += int(chart[row][col)
            chart[row][col] = 'X'
            seatSold.append((row+1, col+1))
            i += 1
        else :
            print("Sorry, that seat is not available.")
    except IndexError:
        print("Invalid row or column")
    except ValueError:
        print("Row and column must be numbers")
    print("\nYour total: $", total, sep="")
    print("Your", num, "seat(s) at", end=" ")
    for seat in seatSold:
        orubt(seat, end=" ")
    print("are marked with 'X'")
    printChart(chart)
    return chart

def saveChart():
    fname = input("Enter file name or hit Enter for default lab5input.txt: ")
    if len(fname) == 0 : fname = DEFAULT_FILE
    
    with open(fname, "w") as outfile:
        for row in chart:
            for col in row:
                if col == 'X' :
                    col = '-'
            outfile.write("%-3s" % col)
        outfile.write("\n")
    print(fname, "updated")