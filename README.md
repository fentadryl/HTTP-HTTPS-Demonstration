# HTTP vs HTTPS Packet Inspection Demo

This project demonstrates the difference between **HTTP** and **HTTPS** using two simple Python web servers and Wireshark.

The HTTP server sends a message in plaintext, which means the message can be viewed directly in a packet capture. The HTTPS server sends the same message through TLS encryption, which means Wireshark can see the network traffic but cannot read the message contents directly.

This project is intended for beginner-friendly cybersecurity, networking, and encryption practice.

---

## What This Project Shows

This demo shows how:

- HTTP sends data without encryption
- HTTPS protects data using TLS encryption
- Wireshark can reveal plaintext HTTP traffic
- Wireshark shows HTTPS traffic as encrypted TLS data
- RSA keys and self-signed certificates can be generated with OpenSSL
- Python can be used to run simple web servers

The message used in both demos is:

```text
SUPER SECRET DO NOT LEAK!!!
```

With HTTP, this message is visible in Wireshark.

With HTTPS, this message is encrypted in Wireshark.

---

## Files in This Project

```text
.
├── README.md
├── http_simple_server.py
└── https_simple_server.py
```

You will also generate these files yourself when setting up HTTPS:

```text
server.key
server.crt
```

### `http_simple_server.py`

Runs a basic unencrypted HTTP server on port `8080`.

### `https_simple_server.py`

Runs a basic HTTPS server on port `8443` using a private key and certificate.

### `server.key`

The RSA private key used by the HTTPS server.

### `server.crt`

The self-signed certificate used by the HTTPS server.

---

## Requirements

You need:

- Python 3
- OpenSSL
- Wireshark
- A terminal or command prompt

This project was originally demonstrated on Kali Linux, but it can also work on other Linux distributions, macOS, or Windows with the correct tools installed.

---

## Part 1: Run the HTTP Server

Open a terminal in the project folder and run:

```bash
python http_simple_server.py
```

Depending on your system, you may need to use:

```bash
python3 http_simple_server.py
```

Expected output:

```text
Server running on port 8080...
```

The server is now waiting for requests.

---

## Test the HTTP Server

Open a second terminal and run:

```bash
curl http://localhost:8080
```

Expected output:

```text
SUPER SECRET DO NOT LEAK!!!
```

This proves that the HTTP server is working.

---

## View HTTP Traffic in Wireshark

1. Open Wireshark.
2. Start capturing on the loopback interface.
   - On Linux, this is usually called `lo`.
   - If you are testing over a real network, choose your active network adapter instead.
3. Run the curl command again:

```bash
curl http://localhost:8080
```

4. In Wireshark, use this display filter:

```text
http
```

5. Click the HTTP packet.
6. Look inside the packet details or packet bytes.

You should be able to see:

```text
SUPER SECRET DO NOT LEAK!!!
```

This shows that HTTP traffic is not encrypted.

---

## Part 2: Generate an RSA Key and Certificate

Before running the HTTPS server, generate a private key and certificate.

Run this command to create the RSA private key:

```bash
openssl genpkey -algorithm RSA -out server.key
```

This creates:

```text
server.key
```

Now generate a self-signed certificate:

```bash
openssl req -new -x509 -key server.key -out server.crt -days 365 -subj "/CN=localhost"
```

This creates:

```text
server.crt
```

The HTTPS server needs both files to start.

---

## Part 3: Run the HTTPS Server

Make sure `server.key` and `server.crt` are in the same folder as `https_simple_server.py`.

Then run:

```bash
python https_simple_server.py
```

Or:

```bash
python3 https_simple_server.py
```

Expected output:

```text
HTTPS server running on port 8443...
```

You may also see a warning like this:

```text
DeprecationWarning: ssl.wrap_socket() is deprecated
```

That warning is okay for this simple classroom demonstration. The server can still run.

---

## Test the HTTPS Server

Open another terminal and run:

```bash
curl --cacert server.crt https://localhost:8443
```

Expected output:

```text
SUPER SECRET DO NOT LEAK!!!
```

The `--cacert server.crt` option tells curl to trust the self-signed certificate you created.

---

## View HTTPS Traffic in Wireshark

1. Open Wireshark.
2. Capture traffic on the loopback interface, usually `lo` on Linux.
3. Run:

```bash
curl --cacert server.crt https://localhost:8443
```

4. In Wireshark, use one of these display filters:

```text
tls
```

or:

```text
tlsv1.3
```

You should see TLS packets such as:

```text
Client Hello
Server Hello
Application Data
```

Unlike the HTTP demo, you should not be able to read:

```text
SUPER SECRET DO NOT LEAK!!!
```

inside the packet contents.

Instead, the data appears encrypted.

---
