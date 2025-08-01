# Simple OSINT Recon MCP Tool

A comprehensive Open Source Intelligence (OSINT) reconnaissance tool built as a Model Context Protocol (MCP) server. This tool provides various reconnaissance capabilities including IP scanning, BSSID lookups, username tracking, and more.

## 🚀 Features

- **IP Port Scanner**: Scan IP addresses for open ports within specified ranges
- **Wigle BSSID Lookup**: Query Wigle database for wireless network information
- **Username Tracker**: Track usernames across multiple platforms and services
- **TCP Port Listener**: Set up listeners on specified ports for network monitoring
- **Phishing Detector**: Analyze URLs for potential phishing threats
- **Image Metadata Extractor**: Extract EXIF and metadata from uploaded images

## 📋 Prerequisites

- Python 3.8 or higher
- UV package manager (recommended) or pip
- Internet connection for OSINT queries
- Valid API keys for external services (where applicable)

## 🛠️ Installation

### Method 1: Using UV (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/simple-osint-recon-mcp-tool.git
cd simple-osint-recon-mcp-tool

# Install dependencies with UV
uv sync

# Install in development mode
uv pip install -e .
```

### Method 2: Using pip

```bash
# Clone the repository
git clone https://github.com/yourusername/simple-osint-recon-mcp-tool.git
cd simple-osint-recon-mcp-tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## 🚀 Usage

### Running as MCP Server

#### Development Mode
```bash
# Using UV
uv run dev mcp main.py

# Or directly with Python
python -m mcp main.py
```

#### Production Mode
```bash
# Using UV
uv run mcp main.py

# Or with Python
python main.py
```

### Integration with Claude Desktop

To use this tool with Claude Desktop, add the following configuration to your Claude Desktop settings:

1. Open Claude Desktop settings
2. Navigate to the MCP servers section
3. Add the following configuration:

```json
{
  "mcpServers": {
    "simple-osint-recon": {
      "command": "uv",
      "args": ["run", "mcp", "main.py"],
      "cwd": "/path/to/simple-osint-recon-mcp-tool"
    }
  }
}
```

Or if using Python directly:

```json
{
  "mcpServers": {
    "simple-osint-recon": {
      "command": "python",
      "args": ["main.py"],
      "cwd": "/path/to/simple-osint-recon-mcp-tool"
    }
  }
}
```

### Running with Claude API

You can also integrate this tool with Claude via the Anthropic API by running it as an MCP server and connecting it to your Claude application.

## 🔧 Tool Functions

### 1. IP Scanner
Scan IP addresses for open ports within a specified range.

**Parameters:**
- `ip_address`: Target IP address to scan
- `start_port`: Starting port number
- `end_port`: Ending port number

**Example Usage:**
```
Scan IP 192.168.1.1 from port 80 to 443
```

### 2. Wigle BSSID Lookup
Query the Wigle database for wireless network information using BSSID.

**Parameters:**
- `bssid`: MAC address of the wireless access point

**Example Usage:**
```
Look up BSSID AA:BB:CC:DD:EE:FF
```

### 3. Username Tracker
Track usernames across multiple platforms and social media services.

**Parameters:**
- `username`: Username to search for

**Example Usage:**
```
Track username "johndoe123" across platforms
```

### 4. TCP Port Listener
Set up a TCP listener on a specified port for network monitoring.

**Parameters:**
- `port`: Port number to listen on
- `host`: Host address (default: localhost)
- `buffer_size`: Buffer size for data reception

**Example Usage:**
```
Listen on port 8080 with host localhost and buffer size 1024
```

### 5. Phishing Detector
Analyze URLs for potential phishing threats and malicious content.

**Parameters:**
- `url`: URL to analyze

**Example Usage:**
```
Check if https://suspicious-site.com is a phishing site
```

### 6. Image Metadata Extractor
Extract EXIF data and metadata from uploaded images.

**Parameters:**
- `image`: Image file (binary data)

**Example Usage:**
```
Extract metadata from uploaded image file
```

## 🔐 Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

```env
# Wigle API Configuration
WIGLE_API_USERNAME=your_wigle_username
WIGLE_API_PASSWORD=your_wigle_password

# Additional API keys for external services
OTHER_API_KEY=your_api_key_here
```

### Configuration File

You can also use a `config.json` file for additional settings:

```json
{
  "timeout": 30,
  "max_threads": 10,
  "default_ports": [22, 23, 53, 80, 110, 143, 443, 993, 995],
  "log_level": "INFO"
}
```

## 📁 Project Structure

```
simple-osint-recon-mcp-tool/
├── main.py                 # Main MCP server entry point
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── README.md              # This file
├── .env.example           # Environment variables template
├── config.json            # Configuration settings
├── tools/                 # Individual tool modules
│   ├── __init__.py
│   ├── ip_scanner.py
│   ├── wigle_tool.py
│   ├── username_tracker.py
│   ├── tcp_listener.py
│   ├── phishing_detector.py
│   └── metadata_extractor.py
├── models/                # ML models and data
│   └── phishing_detector_model.pkl
└── logs/                  # Log files
    └── osint_tool.log
```

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**: Ensure the port you're trying to use isn't occupied by another service
2. **API key errors**: Verify your API keys are correctly set in the `.env` file
3. **Permission denied**: Run with appropriate permissions for network operations
4. **Module not found**: Ensure all dependencies are installed correctly

### Debug Mode

Run the tool with debug logging:

```bash
uv run dev mcp main.py --debug
```

### Logs

Check the log files in the `logs/` directory for detailed error information.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is intended for educational and authorized security testing purposes only. Users are responsible for ensuring they have proper authorization before scanning or analyzing any systems, networks, or services. The authors are not responsible for any misuse of this tool.

## 🔗 Useful Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Claude Desktop Integration Guide](https://docs.anthropic.com/)
- [Wigle API Documentation](https://wigle.net/api)
- [OSINT Best Practices](https://github.com/jivoi/awesome-osint)

## 📞 Support

Email - imashanilupul@gmail.com

---

**Happy OSINT Hunting! 🕵️‍♂️**
