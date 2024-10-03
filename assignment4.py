import argparse
import nltk
from nltk.tree import Tree
#nltk.download('large_grammars')

from model.recognizer import recognize
from model.parser import parse, count

GRAMMAR_PATH = './data/atis-grammar-cnf.cfg'


def main():
    parser = argparse.ArgumentParser(
        description='CKY algorithm'
    )

    parser.add_argument(
        '--structural', dest='structural',
        help='Derive sentences with structural ambiguity',
        action='store_true'
    )

    parser.add_argument(
        '--recognizer', dest='recognizer',
        help='Execute CKY for word recognition',
        action='store_true'
    )

    parser.add_argument(
        '--parser', dest='parser',
        help='Execute CKY for parsing',
        action='store_true'
    )

    parser.add_argument(
        '--count', dest='count',
        help='Compute number of parse trees from chart without \
              actually computing the trees (Extra Credit)',
        action='store_true'
    )

    args = parser.parse_args()

    # load the grammar
    grammar = nltk.data.load(GRAMMAR_PATH)
    # load the raw sentences
    s = nltk.data.load("grammars/large_grammars/atis_sentences.txt", "auto")
    # extract the test sentences
    t = nltk.parse.util.extract_test_sentences(s)

    if args.structural:
        # Devise at least two sentences that exhibit structural ambiguity
        # Print the syntactic trees
        # Sentence 1: "The old man the boats."
        tree1_1 = Tree.fromstring('(S (NP (DT The) (JJ old)) (VP (VBP man) (NP (DT the) (NNS boats))))')
        tree1_2 = Tree.fromstring('(S (NP (DT The) (JJ old) (NN man)) (VP (VBZ the) (NNS boats)))')

        # Sentence 2: "Visiting relatives can be annoying."
        tree2_1 = Tree.fromstring(
            '(S (VP (VBG Visiting) (NP (NNS relatives))) (VP (MD can) (VP (VB be) (JJ annoying))))')
        tree2_2 = Tree.fromstring('(S (NP (VBG Visiting) (NNS relatives)) (VP (MD can) (VP (VB be) (JJ annoying))))')

        print("Structural Ambiguity Example 1.1:")
        tree1_1.draw()
        print("Structural Ambiguity Example 1.2:")
        tree1_2.draw()
        print("\nStructural Ambiguity Example 2.1:")
        tree2_1.draw()
        print("\nStructural Ambiguity Example 2.2:")
        tree2_2.draw()


    elif args.recognizer:
        # Implement the CKY algorithm in model/recognizer.py and use it as a recognizer
        # Provide a list of grammatical and ungrammatical sentences and test the recognizer

        grammatical_sentences = ["please show me all flights from montreal to las vegas .",
                                 "please book a one way coach fare from chicago to indianapolis on united flight two ninety two next wednesday .",
                                 "please tell me the round trip cost for these flights .",
                                 "count the number of flights between nine a.m. and twelve noon .",
                                 "what is the flying time from .",
                                 "i 'd like the cheapest round trip ticket from minneapolis to san diego arriving in san diego before seven p.m .",
                                 "what is the cheapest first class ticket available flying from new york to miami one way but also round trip .",
                                 "what flights leave boston to pittsburgh .",
                                 "what is the cheapest one way flight from phoenix to san diego that arrives in the morning on thursday june second .",
                                 "i want to leave before noon ."]
        ungrammatical_sentences = [
            "can i have the fare .",
            "what is e w r .",
            "i 'd like an afternoon flight .",
            "i 'd like to leave on a saturday .",
            "i need an american airlines flight number from chicago to philadelphia departing six p.m .",
            "please show me all flights from ontario to salt lake city leaving monday morning .",
            "Find me flight from Washington to Denver leaving at eight in morning .",
            "i would like to leave on thursday morning may fifth before six a.m .",
            "i need a first class round trip airfare from detroit to saint petersburg .",
            "How much does cost a round trip ticket from Atlanta to Las Vegas ?"]

        print("Testing Grammatical Sentences:")

        for sent in grammatical_sentences:
            result = recognize(grammar, nltk.word_tokenize(sent))
            print(f"{sent}: {result}")

        print("\nTesting Ungrammatical Sentences:")
        for sent in ungrammatical_sentences:
            result = recognize(grammar, nltk.word_tokenize(sent))
            print(f"{sent}: {result}")
    elif args.parser:
        # Extend CKY recognizer into a parser in model/parser.py
        # Provide the list of ATIS test sentences with tab-separated numbers of parse trees
        # Choose an ATIS test sentence with a number of parses p such that 1 < p < 5 and provide pictures of its parses

        chosen_sent = t[2][0]
        print("Sentence: ", chosen_sent)
        print("S#\t\t Predicted\t\tLabeled")
        for idx, (sentence, label) in enumerate(t):
            trees = parse(grammar, sentence)
            print(f"{idx}\t {len(trees)}\t \t{label}")

        selected_tree = parse(grammar, chosen_sent)

        print("\nSelected Sentence:")
        print(" ".join(chosen_sent))
        print("\nNumber of Parses: {}".format(len(selected_tree)))
        print("\nParse Trees:")
        for tree in selected_tree:
            print(tree)
            tree.draw()

    elif args.count:
        # Compute the number of parse trees for an entry A ∈ Ch(i, k) from the chart with backpointers
        # Use model/parser.py to compute the number of parse trees without actually computing the parse tree

        print("S#\t\t Predicted\t\tLabeled")
        for idx, (sentence, label) in enumerate(t):
            num_tree = count(grammar, sentence)
            print(f"{idx}\t {num_tree}\t \t{label}")


if __name__ == "__main__":
    main()
