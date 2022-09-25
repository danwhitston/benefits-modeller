# A modelling engine for UK welfare benefit entitlement and household income

-- An MSc Computer Science project by Daniel Whitston, Birkbeck College, University of London

This repository contains code, examples, and documentation for a programmable modelling engine for UK welfare benefit entitlement. The project includes sufficient rules to demonstrate the engine's capabilities, but does not provide complete coverage of the welfare system.

The engine is written using a custom-created DSL called Ben. A grammar, parser, and runner for Ben are also included in the repo. Code written in Ben has the filename extension `.ben`.

## Development areas

The project is being developed in four distinct stages:

1. Create a sample set of benefit rules and test cases
2. Define a language for expressing benefit rules
3. Create a parser to parse the benefit rule language
4. Create a runner that takes language code and sample data

Each stage is documented below, with links to corresponding files.

### 1. Create a sample set of benefit rules and test cases

The sample set of benefit rules can be found at [./SAMPLE_BENEFIT_RULES.md](./SAMPLE_BENEFIT_RULES.md).

The sample test cases can be found at [./SAMPLE_TEST_CASES.md](./SAMPLE_TEST_CASES.md).

### 2. Define a language for expressing benefit rules

The informal language definition can be found at [./LANGUAGE_DERIVATION.md](./LANGUAGE_DERIVATION.md).

The rules, expressed in the newly defined language, can be found at [./src/SAMPLE_BENEFIT_RULES.ben](./src/SAMPLE_BENEFIT_RULES.ben).

The test cases, expressed in the newly defined language, can be found at [./src/tests.ben](./src/tests.ben).


### 3. Create a parser to parse the benefit rule language

The parser generator ANTLR 4 was used to generate the language parser.

The lexer and parser definition is in [./BENEFIT_LANGUAGE.g4](./BENEFIT_LANGUAGE.g4)

The Antlr-produced lexer, parser and base listener are in [./lib/](./lib/).

### 4. Create a runner that takes language code and sample data

The runner script is at [./src/ben_to_smtlib.py](./src/ben_to_smtlib.py).

Usage is like `python3 ben_to_smtlib.py SAMPLE_BENEFIT_RULES.ben`.

## Installation

First, download the code to your local environment. The code was developed using Windows Subsystem for Linux on a Windows machine, which means it has been tested and works on a current version of Ubuntu.

```sh
git clone git@github.com:Birkbeck/msc-computer-science-project-2021_22-danwhitston.git
```

For ease of development, the Antlr grammar was converted into a parser in Python, rather than the default Java. You'll need Python 3 and pip installed to use the Python parser. You'll also need to install the Antlr4 runtime library for Python:

```sh
pip install antlr4-python3-runtime
```

To run the Python script that uses the parser to translate code into SMT-LIB2, you'll need to install Z3 which is used as the provider of SMT-LIB2 solving:

```sh
pip install z3-solver
```

## Usage

There are several levels of use of the codebase in its current state of development

### Compiling the grammar definition

To recompile the grammar, e.g. if you update the parser or if you want to compile and explore the grammar using Java features such as `grun` GUI output, you'll need Java installed. You'll also need to install Antlr4 as detailed at <https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#unix>. Then, for example if you want to compile the grammar in Java and display a tree representation of some BEN code:

```sh
antlr4 -o ./lib/ BENEFIT_LANGUAGE.g4
javac ./lib/BENEFIT_LANGUAGE*.java
grun ./lib/BENEFIT_LANGUAGE file -gui
# Paste a BEN file, e.g. SAMPLE_BENEFIT_RULES.ben, into the command line
# Press Ctrl-D
# Explore the GUI representation of the parse tree
```

To recompile the grammar into a Python parser, use:

```sh
antlr4 -o ./lib/ -Dlanguage=Python3 -visitor -no-listener BENEFIT_LANGUAGE.g4
```

### Parsing BEN code and solving it in SMT-LIB2

BEN is the name of the Domain Specific Language that's been developed to represent benefit logic in this project. By parsing a BEN file with the grammar, we can determine if the basic structure meets the requirements of a BEN program. Once that's been done we can tie our own code in using the Listener pattern to traverse the created structure and convert each element into SMT-LIB2.

Both of these tasks are accomplished by running a single script, as follows:

```sh
cd src
python3 ben_to_smtlib.py SAMPLE_BENEFIT_RULES.ben
```

This assumes that both antlr4 and z3_solver are installed and accessible from the Python path.

## Contributing

This is not currently open to outside contributions.

## License

See [./LICENSE](./LICENSE).
