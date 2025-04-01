<template>
    <div>
      <input 
        v-model="termo" 
        @keyup.enter="handleBusca" 
        placeholder="Digite o nome da operadora..."
      />
      <button @click="handleBusca" :disabled="carregando">
        {{ carregando ? 'Buscando...' : 'Buscar' }}
      </button>
      
      <ul v-if="resultados.length">
        <li v-for="op in resultados" :key="op.Registro_ANS">
          {{ op.Razão_Social }} (CNPJ: {{ op.CNPJ }})
        </li>
      </ul>
      <p v-else-if="!carregando">Nenhum resultado encontrado.</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useOperadorasStore } from '@/stores/operadorasStore'
  
  const termo = ref('')
  const store = useOperadorasStore()
  const { resultados, carregando, buscar } = store
  
  const handleBusca = () => {
    if (termo.value.trim()) buscar(termo.value)
  }
  </script>