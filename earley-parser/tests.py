from earley import Earley
from grammar import Grammar

def test_equal_a_and_b():
    grammar = Grammar([['S', 'aSbS'], 
                       ['S', 'bSaS'],
                       ['S', '']])
    
    parcer = Earley('S')
    parcer.fit(grammar)

    words = ['ab', 'a', 'b', 'aabb', 'abbaba', 'aabbba', 'aaabbba', 'baba']
    result = []

    for word in words:
        if parcer.is_recognised(word):
            result.append('Yes')
        else:
            result.append('No')

    excepted = ['Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes']

    for i in range(len(result)):
        if (result[i] != excepted[i]):
            print("Equal test failed", i)
    else:
        print("Equal test passed")

def test_correct_parentheses():
    grammar = Grammar([['S', '(S)S'], 
                       ['S', '']])
    
    parser = Earley('S')
    parser.fit(grammar)

    words = ['()()', '(())', '())', ')', '(', '(()', '(()())()(())', '((()()())))']
    result = []

    for word in words:
        if parser.is_recognised(word):
            result.append('Yes')
        else:
            result.append('No')

    excepted = ['Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No']

    for i in range(len(result)):
        if (result[i] != excepted[i]):
            print("Correct parentheses test failed on word ", words[i])
    else:
        print("Correct parentheses test passed")

def run_tests():
    test_equal_a_and_b()
    test_correct_parentheses()

run_tests()