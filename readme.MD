# Monitor de Uso de Memória com Alerta de SMS

Este script em Python monitora o uso de memória do sistema e envia um alerta via SMS usando Twilio quando o uso de memória ultrapassa um limite predefinido.

## Instalação

1. Clone o repositório ou baixe o código-fonte.
2. Certifique-se de ter Python instalado no seu sistema. Se não estiver instalado, [baixe e instale](https://www.python.org/downloads/).
3. Instale as dependências executando o seguinte comando no terminal:

    ```
    pip install -r requirements.txt
    ```

## Configuração

Antes de executar o script, é necessário configurar suas credenciais do Twilio e os números de telefone apropriados no arquivo `.env`.

1. Crie um arquivo `.env` na mesma pasta do script.
2. Adicione as seguintes linhas ao arquivo `.env` e substitua os valores com suas próprias credenciais e números de telefone:

    ```
    TWILIO_ACCOUNT_SID=seu_account_sid
    TWILIO_AUTH_TOKEN=seu_auth_token
    TWILIO_PHONE_NUMBER=seu_numero_twilio
    RECIPIENT_PHONE_NUMBER=seu_numero_de_destino
    ```

Se você não possui uma conta Twilio, você precisa criar uma. Você pode se inscrever [aqui](https://www.twilio.com/try-twilio).

## Uso

Para iniciar o monitoramento do uso de memória, execute o script:
`python monitor_memory.py`

O script irá monitorar continuamente o uso de memória. Quando o uso de memória ultrapassar 50%, um alerta será enviado para o número de telefone especificado.

## Aviso

Este script deve ser executado em segundo plano para que possa monitorar continuamente o uso de memória. Certifique-se de que está sendo executado em um ambiente adequado.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma [issue](https://github.com/Solvezera/memory_monitor/issues) ou enviar um [pull request](https://github.com/Solvezera/memory_monitor/pulls).

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
