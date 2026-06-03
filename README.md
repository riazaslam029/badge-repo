# badge-repo

Small Python CLI utilities for quick text tasks.

## Features

- `greet`: print a greeting
- `wordcount`: count words in text or a file
- `slugify`: make a URL-friendly slug
- `hash`: compute sha256 for text or a file

## Usage

Run via Python module:

```bash
python -m badge_cli greet Riaza
python -m badge_cli wordcount --text "Hello world"
python -m badge_cli slugify --text "Hello, GitHub!"
python -m badge_cli hash --text "demo"
```

Sample output:

```text
Hello, Riaza!
2
hello-github
2a97516c354b68848cdbd8f54a226a0a55b21ed138e207ad6c5cbb9c00aa5aea
```

Use stdin for larger input:

```bash
type README.md | python -m badge_cli wordcount
```

## Project layout

```
badge_cli/
	__init__.py
	__main__.py
```

## Tests

Run tests with the standard library:

```bash
python -m unittest
```
