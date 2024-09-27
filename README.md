# Custom Color Print and Input Utility

This project provides a customizable utility for printing colored, styled text directly in the terminal.

It builds upon the popular [termcolor](https://github.com/termcolor/termcolor) library and extends its capabilities to allow for simpler and dynamic styling options, including inline colorization and formatting.

## Features

- **Customizable Colored Prints**: Easily print styled text with options for bold, underline, and different foreground/background color combinations.
- **Colored Input Prompts**: Accept user input with colored and styled prompts, enhancing terminal interaction.
- **Inline Colorization**: Style specific parts of your text using a special format within the print message itself.
- **Error, Warning, and Info Messages**: Predefined formats for error, warning, and informational messages to streamline logging and debugging.
- **Exception Messages**: Predefined formats for exceptions that prints an error message with basic exception details.
- **Multiline Input**: Customizable multiline input prompts for collecting multiple lines of text.

## Installation

You can install **pyColorPrint** via pip. This will also install **termcolor** as a dependency:
```bash
pip install pyColorPrint
```

## Usage
This project leverages the [termcolor](https://github.com/termcolor/termcolor) library for its core functionalities, allowing for easy color and style customization in the terminal. If you need more detailed functionalities, such as more advanced styling or color schemes, please check out the termcolor project.

### Basic Custom Print and Input
`print_custom` and `input_custom`, allows for dynamic, styled text output by specifying foreground colors, background colors, bold, and underline attributes.

```python
# Example: Print a message in green text, with a yellow background, and bold.
print_custom("Hello, World!", text_color="green", on_color="on_yellow", bold=True)
```

### Inline Customization
The `print_custom` and `input_custom` functions support inline text color and style customization within a single string using special tags.

```python
# Example:
# 'Hello!' will be green
# 'John' will be bold, underlined & red on grey
# 'birthday' will be bold green
# 'Feb 29' will be bold, & magenta on yellow

msg = ("<cyan:Hello!> My name is <bold_ul_red_on_grey:John>."
       "My <bold_green:birthday> is on <bold_magenta_on_yellow:Feb 29>!")
print_custom(msg)
```
**IMPORTANT: bold_ and ul_ always need to be in front of colors**

### Predefined Print & Input Functions
You can suffix print or input with any of the colors. E.g. `print_red`, `print_magenta`, `input_green`, etc.

#### Errors, Info, Warning, and Done
For convenience, I have also added `print_error`, `print_info`, `print_warning` and `print_done` that add symbols to differentiate the output.
```python
print_error("This is an error message")
print_info("This is info")
print_warning("This is a warning")
print_done("Task completed successfully")
```
Output:

> ${\color{red}❌ This\ is\ an\ error\ message}$
> 
> ${\color{#00BFFF}⚡ This\ is\ info}$
>
> ${\color{#FF7E00}⚠ This\ is\ a\ warning}$
>
> ${\color{00FF00}✅ Task\ completed\ successfully}$


#### Exceptions
The `print_exception` function accepts the exception object and prints an error message with the ExceptionClass and Exception message, and not print the traceback to keep the output clean.
```python
# Example: print_exception()
try:
    x = 1/0
except Exception as e:
    print_exception(e)
```
Output: 

> ${\color{red}❌ ZeroDivisionError: division by zero}$

### Multiline Input
`multiline_input` lets you collect multiple lines of input (including any new lines) until an end signal is provided (default: q!).
```python
# Example: Collect multiline input from the user
text = multiline_input("Please enter the description:", end_signal="q!")
print("You entered:\n", text)
```
Output:

> ${\color{#00BFFF}Please\ enter\ the\ description:}$
>
> ${\color{#FF7E00}Enter\ multi\-line\ text\ (to\ finish,\ in\ an\ empty\ line\ type\ '\color{#FF1493}q!\color{#FF7E00}'\ and\ hit\ enter)}$:
>
> This is the user's input
>
> 
>
> The above empty line will be retained
> 
> The next line will end input
> 
> q!

## Supported Colors and Attributes

#### Text Colors
- `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, and `grey`

#### Background Colors
- `on_green`, `on_yellow`, `on_blue`, `on_magenta`, `on_cyan`, `on_white`, and `on_grey`

#### Attributes
- `bold`, `underline`

#### Inline Tags
Use inline tags to change the format of parts of your message dynamically. Example: `<bold_red:Hello>` will print "Hello" in bold red.

```python
msg = "<bold_green:Success!> The operation completed <ul_blue:without issues>."
print_custom(msg)
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements, bug fixes, or new features.

1. Fork the repository.
2. Create your feature branch: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Open a pull request.

## Acknowledgments
Special thanks to the creators of the [**termcolor**](https://github.com/termcolor/termcolor) project for providing the foundation upon which this utility is built. Please check the project for more advanced styling and color schemes.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/roamingsaint/pyColorPrint/blob/main/LICENSE) file for details.
