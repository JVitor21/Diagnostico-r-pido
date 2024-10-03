def diagnostico (idade, sexo, sintomas):
    if not idade or not sexo or not sintomas:
        return "Por favor, forneça idade, sexo e sintomas"

    #exemplo de diagnostico com base em alguns sintomas
    if "febre" in sintomas and "tosse" in sintomas and idade >= 30:
        return "possivel diagnostico: gripe ou infecção respiaratoria. Consulte um medico para uma avaliação mais segura!"
    elif "dor de cabeça" in sintomas and "nausea" in sintomas:
        return "possivel doagnostico: enxaqueca. Consulte um medico para uma avaliação mais segura!"
    elif "dor no peito" in sintomas and sexo == "masculino" and idade > 40:
        return "Atenção: possivel risco de problema cardiaco. Consulte um medico para uma avaliação mais segura!"
    else:
        return "Os sintomas fornecidos não são suficientes para um diagnostico claro. Recomendamos uma consulta medica!"

#exemplo de dados 
idade = 40
sexo = "masculino"
sintomas = ["febre", "tosse"]

resultado = diagnostico(idade, sexo, sintomas)
print(resultado)