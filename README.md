# 🚀 Cisco DHCP & VLAN Config Generator

Script em Python para geração automática de configurações de **DHCP** e **VLAN** para roteadores e switches Cisco.  
Gera comandos prontos para **copiar e colar em produção**, reduzindo erro humano e acelerando deploy de rede.

Projeto desenvolvido 100% sem uso de inteligência artificial — focado em lógica, estudo e prática em automação de redes.

---

## 📌 Funcionalidades

- Geração automática de configuração DHCP
- Criação de VLANs padronizadas
- Saída formatada para CLI Cisco
- Redução de erro humano
- Script pronto para ambiente real
- Estrutura simples e extensível

---

## 🛠 Tecnologias

- Python 3.x
- Automação de redes
- Conceitos de Cisco IOS

---

## ▶️ Como usar

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/seurepositorio.git
```

2. Entre na pasta:

```bash
cd seurepositorio
```

3. Execute o script:

```bash
python script.py
```

4. Preencha os parâmetros solicitados  
5. Copie a saída gerada e aplique no equipamento Cisco

---

## 📷 Exemplo de saída

```bash
ip dhcp pool VLAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 8.8.8.8

vlan 10
 name USERS
```

---

## 🎯 Objetivo do projeto

Este projeto foi criado para praticar:

- Automação de redes
- Padronização de configuração
- Eficiência operacional
- Scripts aplicáveis em produção

---

## 🔮 Próximas melhorias

- Interface gráfica ou web
- Validação de entrada de dados
- Suporte a múltiplas VLANs em lote
- Exportação para arquivo
- Integração com ferramentas de automação

---

## 👨‍💻 Autor

Desenvolvido por **[seu nome aqui]**  
Foco em automação e engenharia de redes.

---

## 📄 Licença

Livre para uso educacional e melhoria.
