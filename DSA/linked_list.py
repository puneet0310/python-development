class Queue:
    def __init__(self):
        self.queue=[]
    def addq(self,v):
        self.queue.append(v)
    def deleteq(self):
        v =None
        if not self.isempty():
            v=self.queue[0]
            self.queue=self.queue[1:]
        return(v)
    def isempty(self):
        return(self.queue==[])
    def __str__(self):
        return(str(self.queue))
def BFS(AMat,v):
    (rows,cols)=AMat.shape
    visited={}
    for i in range (rows):
        visited[i]=False
        q=Queue()
        visited[v]=True
        q.addq(v)
        while(not q.isempty()):
            j=q.deleteq()
            for k in neighbours(AMat,j):
                if (not visited[k]):
                    visited[k]=True
                    q.addq
    return (visited) 
    