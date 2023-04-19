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

    async GetUrlBaseRuntimeConfig(){
      // Nem sempre está disponivel no server por isso usarei try e catch
      try {
        const config = useRuntimeConfig()

        return config.public.apiBase

      } catch (error) {
        
        console.log('RuntimeConfig ainda não está disponivel')
        return "http://127.0.0.1:8000/api/"
      }
    
    },

    async GetUserData(){

      let bearer = await this.GetToken()
  
      let url = await this.GetUrlBaseRuntimeConfig()

      const response = await $fetch(`${url}user/`,{
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
      let url = this.GetUrlBaseRuntimeConfig()

      let form = {
          nome: nome.value,
          email: email.value,
          foto: foto.value,
          password:password.value
      } 
     
      const response = await $fetch(`${url}user/`,{
        method:'PUT',
        headers:{'Content-Type':'application/json',
        'Authorization': bearer,
        },
        body:form
       });

    }

  }

})