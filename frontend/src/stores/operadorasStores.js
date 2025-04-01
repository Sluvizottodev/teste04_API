import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useOperadorasStore = defineStore('operadoras', () => {
  const resultados = ref([])
  const carregando = ref(false)

  async function buscar(termo) {
    carregando.value = true
    try {
        const response = await fetch(`/api/buscar?termo=${termo}`)
      resultados.value = await response.json()
    } catch (error) {
      console.error("Erro na busca:", error)
    } finally {
      carregando.value = false
    }
  }

  return { resultados, carregando, buscar }
})