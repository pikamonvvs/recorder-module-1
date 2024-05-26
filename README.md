# Recorder Module 1

Recorder Module 1 is a Python application designed for recording live streams from various platforms. It supports multiple platforms, customizable settings, and detailed logging using `loguru`.

Recorder Module 1 is a remake based on "[auqhjjqdo/LiveRecorder](https://github.com/auqhjjqdo/LiveRecorder)", aiming to provide functionality through an argument interface.

## Features

- Supports multiple live streaming platforms
- Customizable recording settings including interval, format, output path, and more
- Detailed logging with `loguru`
- Async-based architecture for efficient performance

## Supported Platforms

- Bilibili
- Douyu
- Huya
- Douyin
- Youtube
- Twitch
- Niconico
- Twitcasting
- Afreeca
- Pandalive
- Bigolive
- Pixivsketch

## Requirements

- Python 3.7+
- anyio
- argparse
- asyncio
- ffmpeg-python
- httpx
- httpx-socks
- loguru
- streamlink

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/recorder-module-1.git
    ```

2. Navigate to the project directory:
    ```sh
    cd recorder-module-1
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application with the necessary arguments:
    ```sh
    python main.py <platform> <id> [options]
    ```

### Arguments

- `<platform>`: The name of the platform (required)
- `<id>`: The ID of the user (required)

### Options

- `-n, --name`: Specify a name
- `-i, --interval`: Set interval time in seconds
- `-f, --format`: Set the output format
- `-o, --output`: Specify the output file path
- `-p, --proxy`: Set the proxy server
- `-c, --cookies`: Set the cookies file path

### Example
```sh
python main.py Afreeca ecvhao -n "woowakgood" -i 10 -f ts -o "output"
```

## Configuration

Recorder Module 1 can be configured using command line arguments. For advanced configurations, you can modify the source code or extend the functionality as needed.

## Logging

The application uses `loguru` for logging. By default, logs are stored in the `logs` directory and rotated daily with a retention period of 3 days.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue on GitHub.