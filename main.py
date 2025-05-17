from datetime import date
import json
from faker import Faker
from typing import Dict, List

import 

faker = Faker('pt-br')

# Mapeamento dos tipos customizados para funções do faker
TIPOS_SUPORTADOS = {
    "user_name": faker.user_name,
    "person_name": faker.name(),
    "company_name": faker.company(),
    "email": faker.email,
    "company_email": faker.company_email,
    "age": lambda: faker.random_int(min=18, max=80),
    "bio": faker.text,
    "city": faker.city,
    "country": faker.country,
    "guid": faker.uuid4,
    "address": faker.address,
    "phone": faker.phone_number,
    "cpf": faker.cpf(),
    "cnpj": faker.cnpj()
}

def gerar_dados(schema: Dict[str, str], quantidade: int) -> List[Dict[str, str]]:
    resultado = []
    for _ in range(quantidade):
        item = {}
        for campo, tipo in schema.items():
            gerador = TIPOS_SUPORTADOS.get(tipo)
            if gerador:
                item[campo] = gerador()
            elif type(tipo) == int:
                item[campo] = faker.rd_number
            elif type(tipo) == str:
                item[campo] = faker.text
            elif type(tipo) == date:
                item[campo] = faker.date_this_century
            elif type(tipo) == float:
                item[campo] = faker.pydecimal(left_digits=4, right_digits=2, positive=True)
            else:
                item[campo] = f"<unsupported: {tipo}>"
        resultado.append(item)
    return resultado

if __name__ == "__main__":
    print("Inciando:")
    # Define a "interface"
    schema = {
        "userName": "user_name",
        "email": "email",
        "age": "age",
        "bio": "bio",
        "city": "city",
        "country": "country"
    }
print('erro')
    quantidade = 5  # Número de registros
    dados = gerar_dados(schema, quantidade)

    # Mostra como JSON
    print(json.dumps(dados, indent=2, ensure_ascii=False))