# 📈 Temperaturas nos próximos dias
Eu utilizei Python para criar este Web Scraping com as bibliotecas Pandas, Matplotlib, e Selenium. Ele exibe e plota um gráfico com as 3 temperaturas dos próximos 3 dias, contendo as máximas e as mínimas. 
O site utilizado para web Scraping:
🔗 https://www.climatempo.com.br/

---

## ✅ Requisitos

- Python **3.13**
- `pandas`
- `matplotlib`
- `selenium`

---

## 🧰 Instalação das dependências

> As instruções abaixo funcionam tanto para **Windows** quanto para **Linux**.

### 1. Crie um ambiente virtual (opcional, mas recomendado)

#### Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

#### Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Instale as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install pandas matplotlib selenium
```

---

## ▶️ Como executar o script

Após instalar as dependências, execute:

### No Windows:

```powershell
python webScraping.py
```

### No Linux:

```bash
python3 webScraping.py
```

---

## 🧪 Funcionamento do script

Quando você roda o script, um menu interativo será exibido:

```text
Menu:
1 - Ver o clima dos próximos 3 dias
2 - Ver Gráfico do clima
3 - Sair
Escolha uma opção:
```

### Opções disponíveis:

- **1 - Ver o clima dos próximos 3 dias**  
  Exibe no terminal o clima em formato de tabela dos próximos 3 dias.

- **2 - Ver Gráfico do clima**  
  Gera e exibe um gráfico de barras com as temperaturas.

- **3 - Sair**  
  Encerra o programa.

---
