#!/usr/bin/env python3

import os
import socket


# Função para obter o IP do computador
def get_current_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f'Erro ao obter o IP: {e}')
        return None


DEV_DEFAULTS = {
    'MODE': 'DEVELOPMENT',
    'DEBUG': 'True',
}


def _write_env_file(ip):
    # Cria o arquivo .env se ele não existir
    if not os.path.isfile('.env'):
        with open('.env', 'w', encoding='utf-8') as new_file:
            for key, value in DEV_DEFAULTS.items():
                new_file.write(f'{key}={value}\n')
            new_file.write(f'MY_IP={ip}\n')
        return

    with open('.env', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    existing_keys = {
        line.split('=', 1)[0].strip() for line in lines if '=' in line and not line.lstrip().startswith('#')
    }

    with open('.env', 'w', encoding='utf-8') as file:
        for line in lines:
            if not line.startswith('MY_IP='):
                file.write(line)

        if lines and not lines[-1].endswith('\n'):
            file.write('\n')

        for key, value in DEV_DEFAULTS.items():
            if key not in existing_keys:
                file.write(f'{key}={value}\n')

        file.write(f'MY_IP={ip}\n')


# Função para atualizar o arquivo .env com o novo IP
def update_env_file(ip):
    try:
        _write_env_file(ip)
        print(f'IP atualizado no arquivo .env: MY_IP={ip}')
    except Exception as e:
        print(f'Erro ao atualizar o arquivo .env: {e}')


# Função principal
def main():
    ip = get_current_ip()
    if ip:
        update_env_file(ip)


if __name__ == '__main__':
    main()
