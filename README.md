# Z80 Assembler em Python 3

Este projeto é um assembler para a arquitetura **Z80**, desenvolvido em **Python 3**, com foco em simplicidade, legibilidade e extensibilidade. Ele permite traduzir código assembly Z80 em código de máquina, sendo ideal tanto para aprendizado quanto para uso em projetos retrocomputacionais, emuladores e sistemas embarcados.

## Funcionalidades

* Suporte às principais instruções do conjunto Z80
* Parser simples e modular, fácil de entender e modificar
* Geração de código binário 
* Tratamento de rótulos (labels) e endereçamento simbólico

## Objetivo

O objetivo deste projeto é fornecer uma ferramenta acessível para entusiastas de sistemas clássicos e desenvolvedores interessados em baixo nível, ao mesmo tempo em que serve como base educacional para compreensão de como assemblers funcionam internamente.

## Tecnologias Utilizadas

* Python 3.x
* Estruturas de dados padrão (listas, dicionários)

## Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/AlbertWolf99/Z80-Assembler
   cd Z80-Assembler
   ```

2. Execute o assembler:

   ```bash
   python3 asm.py test.s test.bin
   ```

3. O arquivo de saída em binário será gerado automaticamente.

## Licença

Este projeto está licenciado sob a licença MIT.
