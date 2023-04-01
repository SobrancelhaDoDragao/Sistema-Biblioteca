import { defineStore } from 'pinia'

export const useUserStore = defineStore('User', {
  state: () => {
    return {
      access:'',
      refresh:'',
      nome:'',
      email:'',
      foto:'',
    }
  },

  actions:{
    async GetUserData(){
      // Url base do back-end
      const config = useRuntimeConfig()

      this.access = useCookie('access')
      this.refresh = useCookie('refresh')

      var bearer = 'Bearer ' + this.access;

      const response = await $fetch(`${config.apiBase}user/`,{
          method:'GET',
          headers:{'Content-Type':'application/json',
          'Authorization': bearer,
          },
      });

      const user = response

      this.nome = user.nome
      this.email = user.email
      this.foto = user.foto
    }
  }

})