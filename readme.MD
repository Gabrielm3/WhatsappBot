# WhatsAppBot

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-3.x-green)

Este é um bot automatizado simples para WhatsApp Web, desenvolvido em Python usando a biblioteca Selenium. Ele permite automatizar o envio de mensagens para contatos e grupos do WhatsApp diretamente do seu navegador.

## Pré-requisitos

- Python 3.x
- Selenium
- Webdriver do Chrome

## Instalação

1. Clone este repositório:
```
git clone https://github.com/gabrielm3/WhatsAppBot.git
```
Navegue até o diretório do projeto:
```
cd WhatsAppBot
```
Instale as dependências:
```
pip install selenium
```

Faça o download do Webdriver do Chrome e coloque-o no diretório do projeto ou adicione o caminho para o executável nas variáveis de ambiente do sistema.

## Uso

Edite o arquivo `main.py` para personalizar as mensagens e os contatos que deseja enviar.

Execute o script principal:

```
python main.py
```

O script abrirá uma janela do Chrome, permitirá que você faça a autenticação no WhatsApp Web escaneando o código QR e, em seguida, enviará as mensagens conforme configurado no arquivo `main.py`.

## Exemplo de uso em main.py

```
if __name__ == "__main__":
    bot = WhatsAppBot()
    bot.send_message_to_new_users(["111111111111"], "Oi, bem-vindo!")
    bot.send_messages(["111111111111"], "Olá!")
    bot.search_contact("111111111111")
    print(bot.get_all_messages())
    print(bot.get_last_message())
```

## Contribuição

Contribuições são bem-vindas! Se você encontrar um bug ou tiver uma melhoria, sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter detalhes.
