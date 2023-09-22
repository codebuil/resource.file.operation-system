import os

def create_resource_files(file_list):
    # Nome do arquivo .raw
    raw_file = "combined.raw"

    # Abre o arquivo .raw para escrever em modo binário
    with open(raw_file, "wb") as raw_output:
        resource_address = 0x60000

        for file_name in file_list:
            file_name=file_name.replace("\n","")
            file_name=file_name.replace("\r","")
            print(file_name)
            # Abre o arquivo de entrada e lê seu conteúdo
            with open(file_name, "rb") as input_file:
                file_content = input_file.read()

            # Escreve o conteúdo binário no arquivo .raw
            raw_output.write(file_content)

            # Cria um nome de variável a partir do nome do arquivo
            variable_name = os.path.splitext(os.path.basename(file_name))[0]

            # Escreve informações sobre a variável no arquivo .c
            with open("output.c", "a") as c_output:
                c_output.write(f"extern const char {variable_name}[];\n")
                c_output.write(f"const char {variable_name}[] = (const char *)(0x{resource_address:08X});\n\n")

            # Atualiza o endereço do recurso
            resource_address += len(file_content)

file_list =[]
print("\033c\033[44;37m\n")
input_file = input("Informe o nome do arquivo de entrada: ")
# Abra o arquivo de entrada e os arquivos de saída
with open(input_file, "r") as input_file:
    for line in input_file:
        file_list =file_list + [line]

# Lista de arquivos a serem processados

create_resource_files(file_list)
print("Arquivos .raw e .c foram criados com sucesso!")

