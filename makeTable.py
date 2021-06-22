def make_table(rows,labels=None,centered=False):

    returnTabe = ''

    colsCount = len(rows[0]) 
    rowsCount = len(rows)

    ##################### Find Longest Word ###############################

    largestLength = 0
    for x in range(rowsCount):
        for y in range(colsCount):
            element = rows[x][y] = str(rows[x][y])
            if len(element) > largestLength:
                largestLength = len(element)
    
    cellLength = largestLength+2

    ############# Header/Footer Padding ####################

    tCount = colsCount - 1
    middlPartheader = ''
    middlePartFooter = ''
    if labels:
        BottomPartLabel = ''
        
    for t in range(tCount):
        middlPartheader += cellLength*'─'
        middlePartFooter += cellLength*'─'
        middlPartheader += '┬'
        middlePartFooter += '┴'
        if labels:
            BottomPartLabel += cellLength*'─'
            BottomPartLabel += '┼'

    middlPartheader += cellLength*'─'
    middlePartFooter += cellLength*'─'
    if labels: BottomPartLabel += cellLength*'─'

    headerLine = f"┌{middlPartheader}┐"
    footerLine = f"└{middlePartFooter}┘"
    returnTabe += headerLine+'\n'

    ################### Labels Padding ######################

    if labels:
        for label in labels:        
            labelIndex = labels.index(label)
            padding = cellLength - len(label)

            if centered == True:
                lpadLen = padding//2
                rpadLen = padding-lpadLen
                paddedCell = f"│{lpadLen*' '}{label}{rpadLen*' '}"

                if labelIndex==len(labels)-1:
                    paddedCell += "│"

            else:
                paddedCell = f"│{' '}{label}{(padding-1)*' '}"
                if labelIndex==len(labels)-1:
                    paddedCell += "│"

            returnTabe += paddedCell

        middleLine = f"├{BottomPartLabel}┤"

        returnTabe += "\n"+middleLine+"\n"

    ################### Content Padding #####################

    for x in range(rowsCount):
        for y in range(colsCount):
            cellValue = rows[x][y]
            wlen = len(cellValue)
            
            #for centered
            padding = cellLength - wlen
            if centered == True:
                lpadLen = padding//2
                rpadLen = padding-lpadLen
                paddedCell = f"│{lpadLen*' '}{cellValue}{rpadLen*' '}"
                if y==colsCount-1:
                    paddedCell += "│"
            else:
                paddedCell = f"│{' '}{cellValue}{(padding-1)*' '}"
                if y==colsCount-1:
                    paddedCell += "│"

            returnTabe += paddedCell

        returnTabe += '\n'

#################### Returning Table #################

    returnTabe += footerLine
    return returnTabe