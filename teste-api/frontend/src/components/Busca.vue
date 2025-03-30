<template>
  <div class="container">
    <h1>Busca de Operadoras</h1>
    <form @submit.prevent="buscar" class="search-form">
      <div class="form-group">
        <label for="nomeSocial">Nome Social:</label>
        <input id="nomeSocial" type="text" v-model="nomeSocial" placeholder="Digite o nome social" />
      </div>
      <div class="form-group">
        <label for="cidade">Cidade:</label>
        <input id="cidade" type="text" v-model="cidade" placeholder="Digite a cidade" />
      </div>
      <div class="form-group">
        <label for="uf">UF:</label>
        <select id="uf" v-model="uf">
          <option value="">Selecione um UF</option>
          <option v-for="estado in ufs" :key="estado" :value="estado">{{ estado }}</option>
        </select>
      </div>
      <button type="submit">Buscar</button>
    </form>

    <div v-if="resultado.length" class="results">
      <h2>Resultados:</h2>
      <div v-for="item in resultado" :key="item.Registro_ANS" class="result-card">
        <div class="result-row">
          <p><strong>Registro ANS:</strong> {{ item.Registro_ANS }}</p>
          <p><strong>CNPJ:</strong> {{ item.CNPJ }}</p>
          <p><strong>Razão Social:</strong> {{ item.Razao_Social }}</p>
        </div>
        <div class="result-row">
          <p><strong>Nome Fantasia:</strong> {{ item.Nome_Fantasia }}</p>
          <p><strong>Modalidade:</strong> {{ item.Modalidade }}</p>
          <p><strong>CEP:</strong> {{ item.CEP }}</p>
        </div>
        <div class="result-row">
          <p><strong>Endereço:</strong> {{ item.Logradouro }}, {{ item.Numero }} <span v-if="item.Complemento"> - {{ item.Complemento }}</span></p>
          <p><strong>Bairro:</strong> {{ item.Bairro }}</p>
          <p><strong>Cidade:</strong> {{ item.Cidade }} - {{ item.UF }}</p>
        </div>
        <div class="result-row">
          <p><strong>Telefone:</strong> ({{ item.DDD }}) {{ item.Telefone }}</p>
          <p><strong>Representante:</strong> {{ item.Representante }}</p>
          <p><strong>Cargo:</strong> {{ item.Cargo_Representante }}</p>
        </div>
      </div>
    </div>
    
    <div v-else-if="buscou" class="no-results">
      <p>Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  name: 'BuscaOperadoras',
  setup() {
    const nomeSocial = ref('');
    const cidade = ref('');
    const uf = ref('');
    const resultado = ref([]);
    const buscou = ref(false);
    const ufs = ref(['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']);

    const buscar = async () => {
      try {
        const params = {};
        if (nomeSocial.value) params.query = nomeSocial.value;
        if (cidade.value) params.cidade = cidade.value;
        if (uf.value) params.uf = uf.value;
        const response = await axios.get('http://127.0.0.1:8000/buscar', { params });
        resultado.value = response.data;
        buscou.value = true;
      } catch (error) {
        console.error("Erro ao buscar:", error);
      }
    };

    return { nomeSocial, cidade, uf, resultado, ufs, buscar, buscou };
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

.container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  font-family: 'Poppins', sans-serif;
}

.search-form {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 20px;
  /* Alinhar os itens na base (ou centro) */
  align-items: flex-end; 
}

.form-group {
  display: flex;
  flex-direction: column;
}

input, select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
  color: #777;
  background: #f8f9fa;
  transition: border-color 0.3s;
}

input:focus, select:focus {
  border-color: #5A9;
  outline: none;
}

option {
  font-size: 16px;
  background: white;
  color: #333;
}

button {
  background-color: #5A9;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  border-radius: 5px;
  /* Remover margin para evitar desalinhamento */
  margin: 0; 
}

.results {
  margin-top: 20px;
}

.result-card {
  background: #eef5f9;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  margin-bottom: 15px;
}

.result-row {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-bottom: 10px;
  color: #555;
}

.no-results {
  text-align: center;
  margin-top: 20px;
  font-size: 18px;
  color: #777;
}
</style>
