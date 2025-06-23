import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Porta {port} está aberta")
        else:
            print(f"Porta {port} está fechada")
        sock.close()
    except socket.error:
        print(f"Erro ao escanear porta {port}")

def main():
    print("=====================================")
    print(" 𓆂Տᑕᗩᑎ-ᑕՏ𓆃  https://youtube.com/@lrcreador?si=uGf_ewOVLWJZTXYy ") 
    print("        ")
    print(f"  Criado por: LorranC. Seja bem vindo {input('Digite seu nome ou apelido: ')}")
    print("=====================================")
    
    ip = input("Digite o endereço IP do servidor: ")
    porta_inicial = int(input("Digite a porta inicial: "))
    porta_final = int(input("Digite a porta final: "))

    for port in range(porta_inicial, porta_final + 1):
        scan_port(ip, port)

if __name__ == "__main__":
    main()