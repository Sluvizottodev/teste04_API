# 🔍 Sistema de Busca de Operadoras de Saúde

**API Python/Flask + Frontend Vue.js 3**

---

## 📌 Visão Geral
Sistema completo para consulta de operadoras de saúde com:
- Backend em Python com busca em CSV
- Frontend moderno em Vue.js 3
- Integração via API REST

---

## 🛠️ Tecnologias Utilizadas

### Backend
| Tecnologia       | Função                |
|------------------|-----------------------|
| Python 3.11      | Linguagem principal   |
| Flask            | Framework web         |
| Pandas           | Processamento de CSV  |
| Flask-CORS       | Habilitar CORS        |

### Frontend
| Tecnologia       | Função                |
|------------------|-----------------------|
| Vue.js 3         | Framework frontend    |
| Pinia            | Gerenciamento de estado |
| Vue Router       | Navegação SPA         |
| Axios            | Chamadas HTTP         |

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.11+
- Node.js 18+
- Git (opcional)

### Passo a Passo

# Configurar Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```
# Configurar Frontend
```bash
cd ../frontend
npm install
npm run dev
```
# Estrutura de Arquivos
```
.
├── backend/
│   ├── app.py             # Servidor Flask
│   ├── models/            # Lógica de dados
│   ├── services/          # Regras de negócio
│   └── operadoras.csv     # Dataset ANS
│
└── frontend/
    ├── src/
    │   ├── stores/        # Gerenciamento de estado
    │   ├── views/         # Página
    │   └── components/    # Componentes UI
    └── package.json       # Dependências
```

#Endpoints da API
GET /buscar
Parâmetros:
termo: String para busca

Exemplo de chamada:
```
curl "http://localhost:5000/buscar?termo=ampla"
//Resposta esperada:
[
  {
    "Registro_ANS": "12345",
    "Razão_Social": "AMPLA SAÚDE LTDA",
    "CNPJ": "00.000.000/0001-00"
  }
]
```

