# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;

valor = float("digite valor da compra")
desconto = float("digite o valor do % desconto")

desconto = (valor * desconto)
resultado = valor - desconto

print(f"""
       
       valor de desconto:{desconto}
       valor final: {resultado}
       
       
       """)