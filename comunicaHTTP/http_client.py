import requests
import os
import threading

operacoes = {
    1: 'soma',
    2: 'subtracao',
    3: 'multiplicacao',
    4: 'divisao'
}

if __name__ == "__main__":
    print(f"Sou o processo client, id: {os.getpid()}, thread: {threading.current_thread().ident}")
    
    def solicitar_valores():
        valor1 = input("Digite o primeiro valor: ")
        valor2 = input("Digite o segundo valor: ")
        return valor1, valor2
    
    def solicitar_operacao():
        operacao = input("""Escolha a operação: 
            1 - Soma
            2 - Subtração
            3 - Multiplicação
            4 - Divisão
            """)
        
        operacao = int(operacao)
        if operacao in operacoes:
            return operacoes[operacao]
        else:
            print("Escolha uma operação na lista.")
            return 'Erro'
        
    def chamar_endpoint(valor1, valor2, operacao):
        url = f"http://127.0.0.1:8080/{operacao}?p1={valor1}&p2={valor2}"
        headers = {'Content-Type': 'application/json'}
        print(url)
        response = requests.post(url, headers=headers)
        print("Resposta da API:")
        print(response.text.encode('utf8').decode())
        
    p1, p2 = solicitar_valores()
    operacao = solicitar_operacao()

    if operacao != 'Erro':
        chamar_endpoint(p1, p2, operacao)
