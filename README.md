<h1 align="center">Welcome to sc-tool 👋</h1>

> Decompress/compress Supercell game assets

### 🏠 [Homepage](https://github.com/PhoenixFire6879/sc-tool/blob/master/README.md)

## Prerequisites

- python 3.7

## Features
- decompress .csv or .sc from Clash Royale/ Brawl Stars
- compress .csv or .sc from Clash Royale/ Brawl Stars


## Usage

- decompression
    ```
    python main.py -d <file_path>
    ```
    or for multiple files
    ```
    python main.py -d <folder_path>
    ```
- compression
    ```
    python main.py -c <signature> <file_path>
    ```
    Supported signatures: LZMA, SC
    - How do you know what signature to use? Well it's simple: when you compress .sc files use SC signature and when you compress .csv use LZMA signature.

## To do
- add support for SCLZ signature
- add support for SIG signature

## Author

👤 **Phoenix**

* Github: [@PhoenixFire6879](https://github.com/PhoenixFire6879)
* Discord: PhoenixFire#6879
* Twitter: [@PhoenixBSArt](https://twitter.com/PhoenixBSArt)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/PhoenixFire6879/sc-tool/issues).

## Show your support

Give a ⭐️ if this project helped you!
