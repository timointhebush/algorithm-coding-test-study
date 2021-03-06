class Node:
    def __init__(self):
        self.count = 1
        self.child = {}

class Tree:
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        node = self.root
        for w in word:
            if w in node.child:
                node = node.child[w]
                node.count += 1
            else:
                node.child[w] = Node()
                node = node.child[w]

    def getCount(self, partOfQuery):
        node = self.root
        if partOfQuery == "?":
            count  = 0
            for value in self.root.child.values():
                count += value.count
            return count
        for q in partOfQuery:
            if q in node.child:
                node = node.child[q]
            else:
                return 0
        return node.count

def solution(words, queries):
    answer = []
    forwardTrees, reverseTrees = {}, {}
    for word in words:
        n = len(word)
        if n in forwardTrees:
            forwardTree, reverseTree = forwardTrees[n], reverseTrees[n]
            forwardTree.addWord(word)
            reverseTree.addWord(word[::-1])
        else:
            forwardTree, reverseTree = Tree(), Tree()
            forwardTree.addWord(word)
            reverseTree.addWord(word[::-1])
            forwardTrees[n], reverseTrees[n] = forwardTree, reverseTree
    for query in queries:
        n = len(query)
        if n in forwardTrees:
            if query[0] != "?": # 정방향
                splitedQuery = query.split("?")[0]
                answer.append(forwardTrees[n].getCount(splitedQuery))
            else:
                if query[n-1] == "?":
                    splitedQuery = "?"
                else:
                    splitedQuery = query.split("?")[-1]
                answer.append(reverseTrees[n].getCount(splitedQuery[::-1]))
        else:
            answer.append(0)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
    