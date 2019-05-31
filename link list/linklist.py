class Node:
    def __init__(self,col=None, dataval=None,linkNode=None):
        self.dataval = dataval
        self.col = col
        self.linkNode = linkNode
class Head:
    def __init__(self,row, linkHead=None , linkNode=None):
        self.linkHead = linkHead
        self.linkNode = linkNode
        self.row = row
class LinkList:
    def __init__(self ,head,matris ):
        self.head = head
        self.matris = matris

    def rowHasNode (self,row):
        head = self.findHead(row)
        if head.linkNode is None :
            return False
        else :
            return True
            
    def findHead (self,row) :
        head = self.head
        while head is not None :
            if head.row == int(row) :
                return head
            else :
                head = head.linkHead
        return None 

    def getRowCols(self,row):
        listCol = []
        node = self.findHead(row).linkNode
        while node is not None :
            listCol.append(node.col)
            node = node.linkNode
        return listCol

    # get all first / second / third ...  row col
    def getColswithIndex(self,col):
        nodes = []
        node = 0
        for i in range(4):
            node = myLinkList.findNode(i,col)
            if node :
                nodes.append(i)
        return nodes

    def deleteAllNodes(self) :
        head = self.head
        while head is not None :
            head.linkNode = None
            head = head.linkHead
        print('all Node Deleted')

    def findNode(self,row,col):
        head = self.findHead(row) 
        if head is not None :
            node = head.linkNode
            while node is not None :
                if node.col == int(col):
                    return node
               
                node = node.linkNode
            
        return None

    def insert(self,row,col,data):
        node = self.findNode(row,col) 
        if node :
            node.dataval = data
            
        else:
            
            if self.rowHasNode(row) is True : 
                listCols = self.getRowCols(row)   
                prev = self.findHead(row) 
                next = None
                last = listCols[len(listCols)-1]
                for i in listCols : 

                    if int(last) == int(i) and int(i) < int(col)  :
                        prev = self.findNode(row,i) 
                        break 
                    
                    elif int(last) == int(i) and int(i) < int(col)  :
                        next = self.findNode(row,i) 
                        break 
                    
                    elif int(i) < int(col) : 
                        prev = self.findNode(row,i) 
                    
                    elif int(i) > int(col) :
                        next = self.findNode(row,i) 
                        break
   
                newNode = Node(col,data,next)
                prev.linkNode = newNode
                newNode.linkNode = next

            else :
                
                head = self.findHead(row)
                if head :
                    head.linkNode = Node(col,data)
                else : 
                    print('head not found')
    
    def showAll(self) :
        head = self.head 
        while head is not None :
            print('head row : '+f'{head.row} Nodes : ' , end = ' ')
            node = head.linkNode
            while node is not None :
                print(f'(col : {node.col} & data : {node.dataval})' , end = ' ')
                node = node.linkNode
            head = head.linkHead
            print('') 

    def transpose(self) :
        matris = self.matris 
        matris = transpose(matris) 
        self.makeNewLinkList(matris)
        print("transpose complete")

    def deleteAllHeads(self) :
        head = self.head
        head.linkHead = None

    def deleteAll(self) :
        self.deleteAllHeads
        self.deleteAllNodes
        print('all Nodes and Head deleted')

    def makeNewLinkList(self,matris) :
        self.deleteAll()
        print(matris)
        FirstHead = None
        index1 = 0 
        indexCol = 0 
        for line in matris :
            if index1 == 0 :
                myHead = Head(0)
                FirstHead = myHead  
                # if data == 1 new node and set col 
                index2 = 0
                indexCol = 0 
                for data in line :
                    if data == "1" and index2 == 0 : 
                        # config First Node
                        myHead.linkNode = Node(indexCol,data)
                        myNode = myHead.linkNode
                        index2 += 1
                    elif data == "1" : 
                        myNode.linkNode = Node(indexCol,data)
                        myNode = myNode.linkNode
                        index2 += 1
                    indexCol += 1
                index1 += 1

            else :
                # config Link Head
                myHead.linkHead = Head(index1)
                myHead = myHead.linkHead
                # if data == 1 new node and set col 
                index2 = 0
                indexCol = 0 
                for data in line :
                    if data == "1" and index2 == 0 :
                        # config First Node
                        myHead.linkNode = Node(indexCol,data)
                        myNode = myHead.linkNode
                        index2 += 1
                    elif data == "1" :
                        myNode.linkNode = Node(indexCol,data)
                        myNode = myNode.linkNode
                        index2 += 1
                    indexCol += 1
                index1 += 1
        self.head = FirstHead
        self.matris = matris

def transpose(matris) :
    r = []
    lenght = len(matris)
    for i in range(lenght):
        data = []
        for j in range(lenght):
            data.append(matris[j][i]) 

        r.append(data)
    return r
    


# Read From txt
file = open("hi.txt","r")
content = file.read()
s = content.split('\n')


print(s)
FirstHead = None
index1 = 0 
indexCol = 0 
for line in s :
    if index1 == 0 :
        myHead = Head(0)
        FirstHead = myHead  
        # if data == 1 new node and set col 
        index2 = 0
        indexCol = 0 
        for data in line :
            if data == "1" and index2 == 0 :
                # config First Node
                myHead.linkNode = Node(indexCol,data)
                myNode = myHead.linkNode
                index2 += 1
            elif data == "1" :
                myNode.linkNode = Node(indexCol,data)
                myNode = myNode.linkNode
                index2 += 1
            indexCol += 1
        index1 += 1

    else :
        # config Link Head
        myHead.linkHead = Head(index1)
        myHead = myHead.linkHead
        # if data == 1 new node and set col 
        index2 = 0
        indexCol = 0 
        for data in line :
            if data == "1" and index2 == 0 :
                # config First Node
                myHead.linkNode = Node(indexCol,data)
                myNode = myHead.linkNode
                index2 += 1
            elif data == "1" :
                myNode.linkNode = Node(indexCol,data)
                myNode = myNode.linkNode
                index2 += 1
            indexCol += 1
        index1 += 1
myLinkList = LinkList(FirstHead,s)

# End Insert To My Link List
   
myLinkList.showAll() 
myLinkList.makeNewLinkList(['0010', '1011', '0000', '1111']) 
 
 
print('------------------------')

print('Commands')
print('1.insert => insert row col data')
print('2.deleteNode => delete row col')
print('3.getNodeVal => node row col')
print('4.getHead => head row')
print('5.transposeMatris => transpos')
print('6.showMatris => show')
while True :
    print(':',end=' ')
    s = input('')
    myInput = s.split(' ')
    if myInput[0] == 'insert' : 
        myRow = myInput[1]
        myCol = myInput[2]
        myData = myInput[3]
        myLinkList.insert(myRow,myCol,myData)
        print('inserted')
    elif myInput[0] == 'delete' :
        pass
    elif myInput[0] == 'node' :
        print(myLinkList.findNode(f'{myInput[1]}', f'{myInput[2]}').dataval )
    elif myInput[0] == 'head' :
        print(myLinkList.findHead(f'{myInput[1]}'))
    elif myInput[0] == 'transpose' :
        myLinkList.transpose()
    elif myInput[0] == 'show' :
        myLinkList.showAll()
    else:
        print('wrong command')