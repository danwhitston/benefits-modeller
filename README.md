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

The rules, expressed in the newly defined language, can be found at [./src/rules.ben](./src/rules.ben).

The test cases, expressed in the newly defined language, can be found at [./src/tests.ben](./src/tests.ben).


### 3. Create a parser to parse the benefit rule language

The parser generator ANTLR 4 was used to generate the language parser.

The lexer and parser definition is in [./BENEFIT_LANGUAGE.g4](./BENEFIT_LANGUAGE.g4)

To generate a parser from the grammar defined by the two files, run the following:

```sh
antlr4 -o ./lib/ BENEFIT_LANGUAGE.g4
javac ./lib/BENEFIT_LANGUAGE*.java
grun ./lib/BENEFIT_LANGUAGE file -gui
# Paste SAMPLE_BENEFIT_RULES.ben into the command line
# Press Ctrl-D
# Explore the GUI representation of the parse tree
```

### 4. Create a runner that takes language code and sample data

## Installation

## Usage

## Contributing

This is not currently open to outside contributions.

## License

See [./LICENSE](./LICENSE).
