import requests
import random
import string
import time
from termcolor import colored
import os
from tqdm import tqdm

def clear_screen():
    """Membersihkan layar terminal berdasarkan OS"""
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_email(domain):
    """Menghasilkan email acak dengan domain yang ditentukan"""
    username_length = random.randint(5, 12)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(username_length))
    return f"{username}@{domain}"

def get_random_user_agent():
    """Menghasilkan user agent acak"""
    user_agents = [
        # Chrome di Windows
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        # Firefox di Windows
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        # Edge di Windows
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/133.0.2623.0',
        # Chrome di Mac
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
        # Safari di Mac
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
        # Chrome di Android
        'Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36',
        # Safari di iOS
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
    ]
    return random.choice(user_agents)

def print_banner():
    """Menampilkan banner profesional"""
    banner = """
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║           🔐 BANTAI PHISING ANJ 🔐               ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
    """
    print(colored(banner, 'cyan'))

def main():
    clear_screen()
    print_banner()
    
    # Input pengguna
    print(colored("\n[*] Konfigurasi Parameter Login", 'yellow'))
    print("=" * 50)
    
    domain = input(colored("[+] Masukkan domain email (default: gmail.com): ", 'green')) or "gmail.com"
    password = input(colored("[+] Masukkan password yang akan digunakan: ", 'green'))
    num_attempts = int(input(colored("[+] Masukkan jumlah percobaan login: ", 'green')))
    delay = float(input(colored("[+] Masukkan jeda antar percobaan (detik): ", 'green')) or "1")
    change_ua = input(colored("[+] Ganti user agent setiap percobaan? (y/n): ", 'green')).lower() == 'y'
    
    print("\n" + "=" * 50)
    print(colored(f"[*] Memulai {num_attempts} percobaan login dengan domain: {domain}", 'yellow'))
    if change_ua:
        print(colored("[*] User agent akan diganti untuk setiap percobaan", 'yellow'))
    print("=" * 50 + "\n")
    
    # Pengaturan sesi
    session = requests.Session()
    
    cookies = {
        'PHPSESSID': 'aefca73814a2fb6ba057757376a70fe8',
    }
    
    base_headers = {
        'accept': 'text/plain, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://cdmsk.kmmyai.biz.id',
        'referer': 'https://cdmsk.kmmyai.biz.id/index.php?gToken=verified',
        'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-requested-with': 'XMLHttpRequest',
    }
    
    # Membuat file log untuk menyimpan detail percobaan
    with open("login_attempts.log", "a") as log_file:
        log_file.write(f"\n\n=== Sesi baru dimulai pada {time.strftime('%Y-%m-%d %H:%M:%S')} ===\n")
    
    # Pelacakan hasil
    success_count = 0
    failure_count = 0
    
    # Progress bar
    progress_bar = tqdm(total=num_attempts, desc="Proses Bantai..", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}")
    
    # Menjalankan percobaan login
    for i in range(num_attempts):
        email = generate_random_email(domain)
        
        # Menggunakan user agent acak jika diminta
        current_headers = base_headers.copy()
        if change_ua or i == 0:  # Selalu gunakan random UA minimal sekali
            current_ua = get_random_user_agent()
            current_headers['user-agent'] = current_ua
        
        data = {
            'email': email,
            'sandi': password,
            'login': 'Facebook',
        }
        
        try:
            response = session.post(
                'https://cdmsk.kmmyai.biz.id/data.php',
                cookies=cookies,
                headers=current_headers,
                data=data,
                timeout=10
            )
            
            status = "Berhasil" if response.status_code == 200 else f"Gagal ({response.status_code})"
            result_color = "green" if response.status_code == 200 else "red"
            
            if response.status_code == 200:
                success_count += 1
            else:
                failure_count += 1
            
            # Memperbarui progress bar
            progress_bar.update(1)
            
            # Log hasil percobaan
            with open("login_attempts.log", "a") as log_file:
                log_file.write(f"[{time.strftime('%H:%M:%S')}] {email} - {status} - UA: {current_headers['user-agent'][:30]}...\n")
            
            # Menyimpan login yang berhasil ke file terpisah
            if response.status_code == 200:
                with open("successful_logins.txt", "a") as f:
                    f.write(f"{email}:{password}\n")
                    
        except Exception as e:
            progress_bar.update(1)
            failure_count += 1
            with open("login_attempts.log", "a") as log_file:
                log_file.write(f"[{time.strftime('%H:%M:%S')}] {email} - Error: {str(e)[:50]}\n")
        
        time.sleep(delay)
    
    progress_bar.close()
    
    # Laporan ringkasan
    print("\n" + "=" * 50)
    print(colored("[*] Ringkasan Percobaan Login", 'yellow'))
    print("=" * 50)
    print(colored(f"✓ Percobaan berhasil: {success_count}", 'green'))
    print(colored(f"✗ Percobaan gagal: {failure_count}", 'red'))
    print(colored(f"Total percobaan: {num_attempts}", 'cyan'))
    # print(colored(f"Log detail tersimpan di: login_attempts.log", 'cyan'))
    # if success_count > 0:
    #     print(colored(f"Login berhasil tersimpan di: successful_logins.txt", 'green'))
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\n\n[!] Operasi dibatalkan oleh pengguna.", 'yellow'))
    except Exception as e:
        print(colored(f"\n\n[!] Terjadi kesalahan: {e}", 'red'))
    finally:
        print(colored("\n[*] Program berakhir.", 'cyan'))
