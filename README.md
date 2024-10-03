# NLP_CKY-Parsing-and-Word-Recognition

# CKY Parsing and Word Recognition

## Project Overview

This project implements the **CKY algorithm** for parsing and word recognition using a context-free grammar (CFG). The CFG is provided from the Airline Travel Information System (ATIS) dataset. The project is structured into three main tasks: recognizing sentences that are in the language of the CFG, parsing sentences to generate parse trees, and resolving structural ambiguities. An additional bonus task focuses on optimizing the computation of parse trees.

## Tasks

### 1. **Structural Ambiguity** [20 pts]
   - Provide two sentences that exhibit **structural ambiguity**.
   - Use **syntactic trees** to illustrate at least two different analyses for each sentence.
   - Implement the flag `--structural` to visualize the syntactic trees using the NLTK `Tree` class.

### 2. **Word Recognition (CKY Recognizer)** [50 pts]
   - Implement the **CKY algorithm** in `recognizer.py` to recognize whether a sentence is in the language of the CFG.
   - Provide a list of at least 10 **grammatical** and 10 **ungrammatical** test sentences.
   - Test your CKY recognizer using the flag `--recognizer` to ensure it works correctly on the test sentences.

### 3. **Parsing with Backpointers (CKY Parser)** [30 pts]
   - Extend the CKY recognizer into a **CKY parser** by adding backpointers in `parser.py`.
   - Implement functionality to extract all possible **parse trees** from the backpointers in the CKY chart.
   - Test the parser on the ATIS dataset, outputting the number of possible parse trees for each sentence.
   - Visualize the parse trees for a selected ATIS test sentence that has between 2 and 4 possible parses using the NLTK `Tree.draw()` method.

### 4. **Bonus Task** [10 pts]
   - Implement a more efficient way to **count the number of parse trees** for a given entry in the CKY chart without actually computing the trees.
   - Compare the efficiency of this approach to the original solution that generates all trees.

## Files

- `assignment4.py`: The main script for running the CKY algorithm and handling different flags (`--structural`, `--recognizer`, `--parser`, `--count`).
- `atis-grammar-cnf.cfg`: The context-free grammar for the ATIS dataset in Chomsky Normal Form (CNF).
- `parser.py`: Implementation of the CKY parsing algorithm with backpointers to extract parse trees.
- `recognizer.py`: Implementation of the CKY algorithm as a sentence recognizer.
- `utils.py`: Helper functions for the project.

## How to Run

1. Install dependencies (if necessary):
   ```bash
   pip install nltk
   ```

2. **Run the CKY Recognizer**:
   ```bash
   python assignment4.py --recognizer
   ```

3. **Run the CKY Parser**:
   ```bash
   python assignment4.py --parser
   ```

4. **Visualize Structural Ambiguity**:
   ```bash
   python assignment4.py --structural
   ```

5. **Count the Number of Parse Trees (Bonus)**:
   ```bash
   python assignment4.py --count
   ```

## Results and Discussion

- **Structural Ambiguity**: The ambiguity in syntactic structure was demonstrated using two sentences with multiple parse trees, showing different analyses of the same sentence.
- **CKY Recognition**: The CKY recognizer correctly identified whether input sentences were valid according to the ATIS grammar.
- **CKY Parsing**: The CKY parser successfully generated all valid parse trees for a given input sentence and visualized them.
- **Efficiency Improvement**: The optimized approach for counting parse trees without generating them was compared against the full tree generation method.
