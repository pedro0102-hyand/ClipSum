# 📝 ClipSum - Resumo Inteligente da Área de Transferência

ClipSum é uma aplicação web que monitora automaticamente a área de transferência do seu computador e gera resumos inteligentes dos textos copiados usando inteligência artificial.

## 🚀 Funcionalidades

- **Monitoramento automático** da área de transferência
- **Resumos inteligentes** gerados com modelo T5 da Hugging Face
- **Interface web moderna** e responsiva
- **Atualização em tempo real** (a cada 3 segundos)
- **Limpeza automática** de caracteres especiais e referências
- **Filtro inteligente** (apenas textos com mais de 8 palavras)

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **IA**: Transformers (Hugging Face) - Modelo T5-small
- **Frontend**: HTML, CSS, JavaScript
- **Monitoramento**: pyperclip para área de transferência
- **Threading**: Para processamento em background


## 📁 Estrutura do Projeto

```
clipsum/
├── app.py              # Aplicação Flask principal
├── templates/
│   └── index.html      # Interface web
├── static/
│   ├── style.css       # Estilos da interface
│   └── script.js       # JavaScript para atualização
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Este arquivo
```

## ⚙️ Configurações

### Personalização do Modelo

O projeto usa o modelo `t5-small` por padrão. Para usar um modelo diferente, modifique as linhas no `app.py`:

```python
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")
```

### Ajuste de Parâmetros

- **Intervalo de monitoramento**: Modificar `time.sleep(2)` em `clipboard_monitor()`
- **Tamanho mínimo do texto**: Alterar `len(current.split()) > 8`
- **Tamanho do resumo**: Ajustar `max_length=100` em `summarize_text()`

## 🔧 Funcionalidades Técnicas

### Limpeza de Texto
A função `limpar_texto()` remove:
- Referências numéricas (ex: [1], [2])
- Caracteres especiais desnecessários
- Mantém acentos e pontuação básica

### Geração de Resumos
- Usa o modelo T5 com prompt "summarize: "
- Parâmetros otimizados para resumos concisos
- Beam search para melhor qualidade

### Monitoramento
- Thread separada para não bloquear a interface
- Verificação a cada 2 segundos
- Tratamento de erros robusto

## 🚨 Requisitos do Sistema

- **RAM**: Mínimo 2GB (modelo T5-small)
- **Espaço**: ~500MB para dependências
- **Internet**: Necessário para download inicial do modelo

## 📝 Notas Importantes

- O modelo será baixado automaticamente na primeira execução
- Os resumos são gerados em inglês (característica do modelo T5-small)
- A aplicação roda em modo debug por padrão
- Funciona melhor com textos em português e inglês


## 🔗 Links Úteis

- [Documentação do Flask](https://flask.palletsprojects.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Modelo T5](https://huggingface.co/t5-small)

