from first import get_first
from grammar import Grammar

class Table:
    grm = Grammar
    entryOfGram = {}
    frst = {}

    def __init__(self, grammar):
        self.grm = grammar
        
    def checkValidity(self, state):
        if state[0][-1]=='.':
            return False
        return True

    def preProcessStates(self, states):
        state_list=[]
        for state in states:
            if self.checkValidity(state):
                state_list.append(''.join(state).replace(' ',''))

        if len(state_list)!=0:
            return(state_list)		

    def is_nonterminal(self, symbol):
        return symbol.isupper()

    def shiftPos(self, item):
        Item = ''.join(item).replace(' ','')
        listItem = list(Item)
        index = listItem.index('.')
        if len(listItem[index:]) != 1:
            return (Item[:index] + '' + Item[index+1] + '.' + Item[index+2:])
        return item

    def check(self, item, symbol):
        Item = ''.join(item).replace(' ','')
        listItem = list(Item)
        try:
            index = listItem.index('.')
            if symbol == listItem[index+1]:
                return True
            if ' ' == listItem[index+1]:
                return False
        except:
            return False
        
    def GOTO(self, item_I, symbol):
        item_J = []
        for i in item_I:
            if self.check(i, symbol):
                new = self.shiftPos(i)
                item_J.append(new)

        if len(item_J)==0:
            return([])

        return(self.findClosure([item_J]))

    def findProduction(self, nonterminal):
        if nonterminal == '$':
            return 1
        if nonterminal not in self.entryOfGram.keys():
            return 1
        return self.entryOfGram[nonterminal]

    def findTerminalsOf(self, gram):
        newList={}
        for rule in gram.rules:
            if rule.left not in newList.keys():
                newList[rule.left]=[''.join(rule.right)]
            else:
                newList[rule.left].append(''.join(rule.right))
        return newList


    def nextDotPos(self, item):
        Item=item.replace(' ','')
        listItem=list(Item)
        try:
            index=listItem.index('.')
            return listItem[index + 1]
        except:
            return '$'

    def followOf(self, item):
        Item=item.replace(' ','')
        listItem=list(Item)
        try:
            index = listItem.index('.')
            return listItem[index + 2]
        except IndexError:
            return '$'

    def findClosure(self, items):
        changed = True
        while (changed):
            changed = False
            for item in items:
                element = item[0]
                nextElem = self.nextDotPos(element)
                findPr = self.findProduction(nextElem)
                if findPr == 1:
                    pass
                else:				
                    for productions in findPr:
                        for sym in self.frst[self.followOf(element)]:
                            elem = [nextElem + '->.' + productions + '' + sym]
                            if elem not in items:
                                items.append(elem)
                                changed = True
        return items
                                
    def build_parsing_table(self):
        self.frst = get_first(self.grm)

        start_rule=f'{self.grm.rules[-1].left}->.{self.grm.rules[-1].right}'

        self.entryOfGram = self.findTerminalsOf(self.grm)

        closure=[self.findClosure([[start_rule]])]

        allSymbols = set()
        allSymbols |= self.grm.nonterminals
        allSymbols |= self.grm.terminals
        allSymbols.remove('$')
        allSymbols.remove('^')

        allItems = {}
        allStates = []
        new_item = True
        while new_item:
            new_item = False
            i = 1
            for item in closure:
                i += 1
                for sym in allSymbols:
                    if len(self.GOTO(item, sym)) != 0:
                        goto = self.GOTO(item, sym)
                        item_list = [[item] for sublist in goto for item in sublist]
                        if item_list not in closure:
                            index = 'I' + str(i)
                            if index not in allItems.keys():
                                allItems[index]=[sym]
                            else:
                                allItems[index].append(sym)	
                                
                            closure.append(item_list)
                            item_check = self.preProcessStates(item_list)
                            if (item_check):
                                allStates.append(item_list)
                            
                            new_item = True

        allStates.insert(0, self.findClosure([[start_rule]]))
        i = 0
        table={}

        for item in allStates:
            i += 1
            for num in item:
                dot_pos = list(num[0]).index('.') + 2
                if dot_pos < len(num[0]):
                    elem = list(num[0]).index('.') + 1
                    sym = list(num[0])[elem]
                    goto = self.GOTO(num, sym)
                    if goto in allStates:
                        index = allStates.index(goto)
                        last = list(num[0])[len(num[0]) - 1]
                        table[str(i - 1) + '+' + sym] = "shift " + str(index)
                else:
                    elem = list(num[0]).index('.')
                    if elem + 1 >= len(num[0]):
                        sym = ''
                    else:
                        sym = num[0][elem + 1]
                    table[str(i - 1) + '+' + sym] = "reduce "+ num[0][:elem]
        return table
    

        



