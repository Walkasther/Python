from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'sje23#ED$fsds'


def conectar():
    return mysql.connector.connect(
        host='localhost',
        database='urna_eletronica',
        user='root',
        password=''
    )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registrar_candidato', methods=['POST'])
def registrar_candidato():
    nome = request.form['nome']
    numero = request.form['numero']
    tipo_candidato = request.form['tipo_candidato']

    # Conexão com o banco de dados
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        # Verificar se já existe um candidato com o mesmo número e tipo_candidato
        query_verificar = """
            SELECT COUNT(*) 
            FROM candidatos 
            WHERE numero = %s AND tipo_candidato = %s
        """
        cursor.execute(query_verificar, (numero, tipo_candidato))
        resultado = cursor.fetchone()

        if resultado[0] > 0:
            # Se o número já existe para o tipo_candidato, retorna erro
            flash("Erro: Já existe um candidato com esse número e tipo de candidato.", "error")
            return redirect(url_for('index'))

        # Inserir o candidato no banco de dados
        query_inserir = """
            INSERT INTO candidatos (nome, numero, tipo_candidato) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(query_inserir, (nome, numero, tipo_candidato))
        conexao.commit()

        # Mensagem de sucesso
        flash("Candidato registrado com sucesso!", "success")

    except mysql.connector.Error as err:
        print(f"Erro ao registrar candidato: {err}")
        flash("Erro no servidor. Tente novamente mais tarde.", "error")

    finally:
        cursor.close()
        conexao.close()

    # Redirecionar para a página inicial após sucesso
    return redirect(url_for('index'))


@app.route('/obter_tipo_eleicao', methods=['GET'])
def obter_tipo_eleicao():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    try:
        # Simulação: Obter o tipo de eleição da tabela de configurações ou estado
        cursor.execute("SELECT tipo_eleicao FROM configuracao LIMIT 1")
        resultado = cursor.fetchone()
        if resultado:
            return jsonify({"tipoEleicao": resultado['tipo_eleicao']})
        else:
            return jsonify({"tipoEleicao": None})  # Caso não haja configuração
    finally:
        cursor.close()
        conexao.close()



@app.route('/votar', methods=['GET', 'POST'])
def votar():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM candidatos")
    candidatos = cursor.fetchall()
    cursor.execute("SELECT tipo from tipo_eleicao WHERE id= 1")
    tipo = cursor.fetchone
    cursor.close()
    conexao.close()

    if request.method == 'POST':
        titulo_eleitor = request.form['titulo_eleitor']
        votos = request.form['id_candidato']
        numero = request.form['numero']
        cursor.execute("SELECT id FROM candidatos where numero = %s",(numero,))

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM eleitores WHERE titulo_eleitor = %s", (titulo_eleitor,))
        eleitor = cursor.fetchone()

        if eleitor:
            mensagem = "Este eleitor já votou."
        else:
            cursor.execute("INSERT INTO eleitores (titulo_eleitor) VALUES (%s)", (titulo_eleitor,))
            cursor.execute("UPDATE candidatos SET votos = votos + 1 WHERE id = %s", (votos,))
            conexao.commit()
            mensagem = "Voto registrado com sucesso."
            print(votos)


        cursor.close()
        conexao.close()
        return render_template('votar.html', candidatos=candidatos, mensagem=mensagem)

    return render_template('votar.html', candidatos=candidatos)


@app.route('/resultados')
def resultados():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, votos FROM candidatos ORDER BY votos DESC")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('resultados.html', resultados=resultados)


@app.route("/verificar_ou_inserir", methods=["POST"])
def verificar_ou_inserir():
    data = request.json
    tipo_eleicao = data.get("tipo_eleicao")

    try:
        conn = conectar()
        cursor = conn.cursor()

        # Verificar se já existe um tipo registrado
        cursor.execute("SELECT tipo FROM tipo_eleicao WHERE tipo IS NOT NULL LIMIT 1")
        resultado = cursor.fetchone()
        print(resultado)



        if resultado:
            tipo_atual = resultado[0]
            return jsonify({"status": "exists", "tipo_eleicao": tipo_atual, "message": "Tipo de eleição já definido."})

        # Se não houver tipo definido e for fornecido um novo, atualiza no banco
        if tipo_eleicao:
            cursor.execute("DELETE FROM candidatos")
            cursor.execute("UPDATE tipo_eleicao SET tipo = %s WHERE id = 1", (tipo_eleicao,))
            conn.commit()
            return jsonify({"status": "success", "message": "Tipo de eleição registrado com sucesso."})

        return jsonify({"status": "not_exists", "message": "Nenhum tipo de eleição definido."})

    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)})

    finally:
        cursor.close()
        conn.close()



@app.route("/apagar_dados", methods=["POST"])
def apagar_dados():
    data = request.json
    tipo_eleicao = data.get("tipo_eleicao")

    # Nome da tabela a ser apagada (ou condição para deletar)
    tabela = "candidatos"

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM candidatos')
        dados = cursor.fetchall()

        # Apagar os dados
        if tipo_eleicao == "presidente":

            cursor.execute(f"DELETE FROM {tabela} WHERE tipo_candidato = 'presidente'")
        elif tipo_eleicao == "prefeito":

            cursor.execute(f"DELETE FROM {tabela} WHERE tipo_candidato IN ('prefeito', 'vereador')")

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"status": "success", "message": "Dados apagados com sucesso!"})

    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": str(err)})






if __name__ == '__main__':
    app.run(debug=True)
