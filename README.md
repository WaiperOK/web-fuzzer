# Fuzzing Tool

## Overview

This fuzzing tool is designed to generate random input data and send it to a specified URL to test applications for vulnerabilities. It helps identify potential weaknesses in how applications handle unexpected or malformed input.

## Features

- Generates random strings with a mix of letters, digits, and punctuation.
- Sends a specified number of requests to the target URL.
- Allows customization of the parameter name to fuzz.
- Displays status codes for each request to help identify potential issues.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Install the required `requests` library:

   ```bash
   pip install requests
