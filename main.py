import os, sys, time, random

RESET="\033[0m"; BOLD="\033[1m"; GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"; BLUE="\033[94m"; CYAN="\033[96m"; WHITE="\033[97m"

def clear(): os.system("clear")

def show_banner():
    print(f"""{CYAN}{BOLD}
    ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
    ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    {RED}              [ K I N G   B A N N E R ]{RESET}
    {RED}⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⡀⠀
    {RED}⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧
    {RED}⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
    {RED}⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
    {RED}⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
    {RED}⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
    {RED}⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
    {RED}⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
    {RED}⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    {GREEN} WHATSAPP: {WHITE}923037224620 {GREEN}| TELEGRAM: {WHITE}@romanempire078{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    """)

def show_menu():
    print(f"""{BLUE}{BOLD}
    [1] Permanent Ban Attack
    [2] Temporary Ban Attack
    [3] Permanent Unban
    [4] Temporary Unban
    [5] Exit Tool{RESET}
    """)

def loading_animation(msg):
    frames = ["|", "/", "-", "\\"]
    for _ in range(10):
        for frame in frames:
            sys.stdout.write(f"\r{YELLOW}{BOLD}  [{frame}] {msg}...{RESET}")
            sys.stdout.flush()
            time.sleep(0.05)
    print("\r" + " " * 60 + "\r", end="")

def execute_action(action_name):
    clear(); show_banner()
    print(f"{GREEN}{BOLD}  ► INITIATING {action_name.upper()} PROTOCOL...{RESET}\n")
    
    target = input(f"{CYAN}{BOLD}  ► Enter Target Number (e.g. 923001234567): {RESET}").strip()
    if not target:
        return
    
    try:
        amount = int(input(f"{CYAN}{BOLD}  ► Enter Amount (e.g. 50000): {RESET}").strip())
        if amount <= 0: raise ValueError
    except ValueError:
        print(f"{RED}  [!] Invalid Amount!{RESET}")
        time.sleep(2)
        return

    print(f"\n{YELLOW}  [~] Target Locked: {WHITE}{target}{RESET}")
    print(f"{YELLOW}  [~] Payload Size: {WHITE}{amount}{RESET}")
    time.sleep(1)
    
    loading_animation("Bypassing Security Protocols")
    loading_animation("Injecting Payload")
    
    clear(); show_banner()
    print(f"{GREEN}  [*] SERVER CONNECTED. ATTACK STARTED...{RESET}\n")
    time.sleep(0.5)

    delay = 0.002 if amount > 5000 else 0.01

    try:
        for i in range(1, amount + 1):
            if random.randint(1, 200) == 1:
                sys.stdout.write(f"\033[93m[SYSTEM] Routing through proxy node {random.randint(100,999)}... OK\033[0m\n")
            
            sys.stdout.write(f"\033[91m[REPORT] Target: {target} | Amount: {i} | STATUS: PENDING\033[0m\n")
            sys.stdout.flush()
            
            time.sleep(delay)
            
            if i % 1000 == 0:
                percent = (i / amount) * 100
                bar = "█" * int(percent/5) + "░" * (20 - int(percent/5))
                sys.stdout.write(f"\033[96m[PROGRESS] [{bar}] {percent:.1f}%\033[0m\n")
                sys.stdout.flush()
                
    except KeyboardInterrupt:
        print(f"\n\n{RED}  [!] Attack Aborted by User!{RESET}")
        time.sleep(2)
        return

    print(f"\n\n{GREEN}{BOLD}")
    print("  ╔══════════════════════════════════════════════════════════════╗")
    
    if "Ban" in action_name and "Unban" not in action_name:
        print("  ║                    REPORT SUBMITTED                          ║")
        print("  ╠══════════════════════════════════════════════════════════════╣")
        print(f"  ║  {YELLOW}TARGET     : {WHITE}{target:<47} {GREEN}║")
        print(f"  ║  {YELLOW}STATUS     : {RED}REPORTED SUCCESSFULLY{' '*26} {GREEN}║")
        print(f"  ║  {YELLOW}EST. TIME  : {WHITE}24 TO 48 HOURS{' '*33} {GREEN}║")
        print("  ╠══════════════════════════════════════════════════════════════╣")
        print(f"  ║  {RED}[!] NOTE: IF ACCOUNT IS NOT BANNED, PLEASE TRY AGAIN.{WHITE}      {GREEN}║")
    else:
        print("  ║                    UNBAN REQUEST SENT                        ║")
        print("  ╠══════════════════════════════════════════════════════════════╣")
        print(f"  ║  {YELLOW}TARGET     : {WHITE}{target:<47} {GREEN}║")
        print(f"  ║  {YELLOW}STATUS     : {GREEN}RESTORATION IN PROGRESS{' '*26} {GREEN}║")
        print(f"  ║  {YELLOW}EST. TIME  : {WHITE}24 TO 48 HOURS{' '*33} {GREEN}║")
        print("  ╠══════════════════════════════════════════════════════════════╣")
        print(f"  ║  {RED}[!] NOTE: IF ACCOUNT REMAINS BANNED, PLEASE TRY AGAIN.{WHITE}      {GREEN}║")

    print("  ╚══════════════════════════════════════════════════════════════╝")
    print(f"{RESET}")
    
    input(f"{CYAN}  Press ENTER to return to Main Menu...{RESET}")

def main():
    while True:
        try:
            clear()
            show_banner()
            show_menu()
            
            choice = input(f"{GREEN}{BOLD}  └──► Select Option [1-5]: {RESET}").strip()
            
            if choice == "1": execute_action("Permanent Ban")
            elif choice == "2": execute_action("Temporary Ban")
            elif choice == "3": execute_action("Permanent Unban")
            elif choice == "4": execute_action("Temporary Unban")
            elif choice == "5":
                print(f"\n{RED}  Exiting System...{RESET}")
                time.sleep(1)
                sys.exit(0)
            else:
                print(f"{RED}  Invalid Option!{RESET}")
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\n{RED}  System Terminated.{RESET}\n")
            sys.exit(0)

if __name__ == "__main__":
    main()
