import { defineStore } from 'pinia'

export const useUserStore = defineStore('User', {
  state: () => {
    return {
      access:'',
      refresh:'',
      nome:'',
      email:'',
      foto:'',
      password:'',
    }
  },

  actions:{
    async GetToken(){

      this.access = useCookie('access')
      this.refresh = useCookie('refresh')

      let bearer = 'Bearer ' + this.access;

      return bearer
    },

    async GetUserData(){

      let bearer = await this.GetToken()
  
      // Url base do back-end
      const config = useRuntimeConfig()
      
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
      this.password = user.password
      
    },

    async PutUserData(nome,email,foto,password){

      let bearer = await this.GetToken()
  
      // Url base do back-end
      const config = useRuntimeConfig()

      let form = {
          nome: nome.value,
          email: email.value,
          foto: foto,
          password:password.value
      } 
     
      const response = await $fetch(`${config.apiBase}user/`,{
        method:'PUT',
        headers:{'Content-Type':'application/json',
        'Authorization': bearer,
        },
        body:form
       });

    }

  }

})