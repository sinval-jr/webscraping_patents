import sys
import os
try:
    import importlib.metadata
    # Tenta obter a versão da biblioteca que está REALMENTE carregada
    version = importlib.metadata.version('google-cloud-bigquery')
except Exception:
    version = "ERRO: Biblioteca 'google-cloud-bigquery' NÃO ENCONTRADA."

print("\n" + "="*50)
print("--- DIAGNÓSTICO DE AMBIENTE ---")

print(f"\n1. Executável Python em uso:")
print(f"   {sys.executable}")

print(f"\n2. Versão da 'google-cloud-bigquery' carregada:")
print(f"   {version}")

# Verificação crucial: O script está rodando de dentro do .venv?
is_in_venv = ".venv" in sys.executable
print(f"\n3. Está rodando do .venv?")
print(f"   {is_in_venv}")

if not is_in_venv:
    print("\n   >>> ALERTA: Você NÃO está executando o Python do seu ambiente virtual!")

print("="*50 + "\n")