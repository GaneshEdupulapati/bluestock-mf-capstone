# Web Application Data Flow Architecture

## Data Flow

```text
┌──────────────────┐
│      USER        │
│  User Action     │
└────────┬─────────┘
         │
         │ HTTP Request
         ▼
┌──────────────────┐
│    FRONTEND      │
│ Web Application  │
└────────┬─────────┘
         │
         │ API Request
         ▼
┌──────────────────┐
│   BACKEND / API  │
│ Business Logic   │
└────────┬─────────┘
         │
         │ Authentication
         │ & Authorization
         ▼
┌──────────────────┐
│    DATABASE      │
│ Customer /       │
│ Transaction Data │
└────────┬─────────┘
         │
         │ Extract
         ▼
┌──────────────────┐
│   DATA PIPELINE  │
│ ETL / ELT        │
│ Cleaning &       │
│ Transformation   │
└────────┬─────────┘
         │
         │ Processed Data
         ▼
┌──────────────────┐
│    ANALYTICS     │
│ SQL / Python /   │
│ Statistical      │
│ Analysis         │
└────────┬─────────┘
         │
         │ KPIs / Insights
         ▼
┌──────────────────┐
│    DASHBOARD     │
│ Power BI /       │
│ Tableau          │
└──────────────────┘