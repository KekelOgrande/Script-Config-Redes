🚀 Cisco DHCP & VLAN Config Generator

Script em Python para geração automática de configurações de DHCP e VLAN para roteadores e switches Cisco.
O objetivo é produzir configurações prontas para copiar e colar em produção, reduzindo erro humano e acelerando deploy de rede.

Projeto desenvolvido 100% sem uso de inteligência artificial — focado em lógica, estudo e prática em automação de redes.

📌 Funcionalidades

Geração automática de configuração DHCP

Criação de VLANs padronizadas

Saída formatada para CLI Cisco

Redução de erro humano em configuração manual

Script pronto para uso em ambiente real

Estrutura simples e extensível

🛠 Tecnologias

Python 3.x

CLI / Automação de redes

Conceitos de Cisco IOS

▶️ Como usar

Clone o repositório:

git clone https://github.com/seuusuario/seurepositorio.git


Entre na pasta:

cd seurepositorio


Execute o script:

python script.py


Preencha os parâmetros solicitados

Copie a saída gerada e aplique no equipamento Cisco

📷 Exemplo de saída
ip dhcp pool VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8

vlan 10
 name USERS


(exemplo ilustrativo)

🎯 Objetivo do projeto

Este projeto foi criado como prática de:

Automação de redes

Padronização de configuração

Eficiência operacional

Desenvolvimento de scripts aplicáveis em produção

🔮 Próximas melhorias

Interface gráfica ou web

Validação de entrada de dados

Suporte a múltiplas VLANs em lote

Exportação para arquivo

Integração com ferramentas de automação

👨‍💻 Autor

Desenvolvido por [seu nome aqui]
Estudante / Profissional de redes focado em automação.

📄 Licença

Este projeto é livre para uso educacional e melhoria.
