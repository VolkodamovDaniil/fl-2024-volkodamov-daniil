from lr1_parser import LR1Parser
from grammar import Grammar

def test_expression():
    grammar = Grammar([['^', 'E$'],
                       ['E', 'E+T'], 
                       ['E', 'T'], 
                       ['T', 'T*F'],
                       ['T', 'F'],
                       ['F', '(E)'],   
                       ['F', 'i']])
    
    parser = LR1Parser()
    parser.fit(grammar)

    words = ['i', 'i+(i+i)', '(i+i)*', 'i+i', '(i+i)*i+', 'i*i*i', 'i+i+i', '(i+i))']
    result = []

    for word in words:
        if parser.predict(word):
            result.append('Yes')
        else:
            result.append('No')

    excepted = ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No']

    for i in range(len(result)):
        if (result[i] != excepted[i]):
            print("Expression test failed", i)
    else:
        print("Expression tests ended.")

def run_tests():
    test_expression()

run_tests()