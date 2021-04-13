class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd=False
        self.count=0
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self,string):
        node=self.root
        
        for c in string:
            if c not in node.children:
                node.children[c]=TrieNode()
            node.count+=1
            
            node=node.children[c]
            
        node.isEnd=True
        

    def search(self,string):
        node=self.root

        for c in string:
            if c not in node.children:
                return False
            node=node.children[c]
        return node.isEnd

    def walk(self):
        node=self.root
        count=0
        letters=""
        while len(node.children)==1 and not node.isEnd:
            count+=1
            for k,v in node.children.items():
                letters+=k
                node=v

        return letters

    def walk2(self,s):
        node=self.root
        count=0
        letters=""
        for l in s:
            if l in node.children:
                letters+=l
                node=node.children[l]
            else:
                break

        return letters


def longestPrefix(num,t):
    temp=t
    temp.insert(num)
    
    return t.walk()

def twilio(area_codes,phones):
    t=Trie()
    output=[]
    for i in area_codes:
        t.insert(i)

    for num in phones:
        output.append(t.walk2(num))

    return output



print(twilio(["213", "21358", "1234", "12"],["21349049", "1204539492", "123490485904"]))


